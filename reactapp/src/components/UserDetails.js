import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";

function UserDetails() {
    const { id } = useParams(); 
    const [user, setUser] = useState(null);

    useEffect(() => {
        fetch(`http://localhost:8000/api/user_info/${id}`)
            .then((response) => response.json())
            .then((data) => {console.log(data); setUser(data);})
            .catch((error) => console.error("Error fetching user:", error));
    }, [id]);

    if (!user) return <p>Loading...</p>;

    return (
        <div>
            <h1>{user.username}</h1>
            <p><b>Email:</b> {user.email}</p>
            <p><b>Bio:</b> {user.bio}</p>
            <p><b>Interests:</b> {Array(user.interests).join(", ")}</p>
            <p><b>Skills:</b> {Array(user.skills).join(", ")}</p>
            <p><b>Type:</b> {user.user_type}</p>
            <Link to="/users">Back to Users</Link>
        </div>
    );
}

export default UserDetails;