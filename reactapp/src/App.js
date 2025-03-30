import './App.css';
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./components/HomePage";
import UsersPage from "./components/UsersPage";
import UserDetails from "./components/UserDetails";


function App() {
  return (
      <Router>
          <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/users" element={<UsersPage />} />
              <Route path="/users/details/:id" element={<UserDetails />} />
          </Routes>
      </Router>
  );
}

export default App;