#!/bin/bash
# api_test_functions.sh - Helper functions for testing Collabify API

# Function to get auth token and store it
get-token() {
  if [[ -z "$1" || -z "$2" ]]; then
    echo "Usage: get-token <username> <password>"
    return 1
  fi
  
  local username="$1"
  local password="$2"
  
  # Make the login request and extract the tokens
  local response=$(curl -s -X POST http://localhost:8000/api/login/ \
    -H "Content-Type: application/json" \
    -d "{\"username\":\"$username\", \"password\":\"$password\"}")
  
  # Extract and store tokens
  export ACCESS_TOKEN=$(echo "$response" | grep -o '"access":"[^"]*' | cut -d'"' -f4)
  export REFRESH_TOKEN=$(echo "$response" | grep -o '"refresh":"[^"]*' | cut -d'"' -f4)
  
  if [[ -z "$ACCESS_TOKEN" ]]; then
    echo "Failed to get token. Response: $response"
    return 1
  fi
  
  echo "Tokens saved to ACCESS_TOKEN and REFRESH_TOKEN environment variables"
  echo "Access token: $ACCESS_TOKEN"
}

# Function to make authenticated API calls
auth-curl() {
  if [[ -z "$ACCESS_TOKEN" ]]; then
    echo "No access token found. Use get-token first."
    return 1
  fi
  
    # Check if jq is installed
  if command -v jq &> /dev/null; then
    # Use jq for pretty output if available
    curl -s -H "Authorization: Bearer $ACCESS_TOKEN" "$@" | jq
  else
    # Fallback to regular curl if jq isn't available
    curl -H "Authorization: Bearer $ACCESS_TOKEN" "$@"
  fi
}

# Create a post
create-post() {
  if [[ -z "$1" || -z "$2" ]]; then
    echo "Usage: create-post <title> <description> [genre] [looking_for]"
    return 1
  fi
  
  local title="$1"
  local description="$2"
  local genre="${3:-}"
  local looking_for="${4:-}"
  
  local data="{\"title\":\"$title\",\"description\":\"$description\""
  
  if [[ -n "$genre" ]]; then
    data="$data,\"genre\":\"$genre\""
  fi
  
  if [[ -n "$looking_for" ]]; then
    data="$data,\"looking_for\":\"$looking_for\""
  fi
  
  data="$data}"
  
  auth-curl -X POST http://localhost:8000/api/posts/ \
    -H "Content-Type: application/json" \
    -d "$data"
}

# Like a post
like-post() {
  if [[ -z "$1" ]]; then
    echo "Usage: like-post <post_id>"
    return 1
  fi
  
  auth-curl -X POST http://localhost:8000/api/posts/$1/like/
}

# Add a comment
add-comment() {
  if [[ -z "$1" || -z "$2" ]]; then
    echo "Usage: add-comment <post_id> <comment_text>"
    return 1
  fi
  
  local post_id="$1"
  local comment="$2"
  
  auth-curl -X POST http://localhost:8000/api/posts/$post_id/comments/ \
    -H "Content-Type: application/json" \
    -d "{\"content\":\"$comment\"}"
}

# Get all posts
get-posts() {
  auth-curl -X GET http://localhost:8000/api/posts/
}

# Get specific post
get-post() {
  if [[ -z "$1" ]]; then
    echo "Usage: get-post <post_id>"
    return 1
  fi
  
  auth-curl -X GET http://localhost:8000/api/posts/$1/
}

CURRENT_USER=$(whoami)

# Helper message
echo "Welcome ${CURRENT_USER}!"
echo "Collabify API testing functions loaded."
echo "Usage:"
echo "  get-token <username> <password> - Get and store auth token"
echo "  create-post <title> <description> [genre] [looking_for] - Create a new post"
echo "  get-posts - Get all posts"
echo "  get-post <id> - Get a specific post"
echo "  like-post <id> - Like a post"
echo "  add-comment <post_id> <comment> - Add a comment to a post"
