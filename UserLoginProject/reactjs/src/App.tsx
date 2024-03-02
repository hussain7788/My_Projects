import React from 'react';
import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Login from './components/Login.tsx';
import AddCustomer from './components/AddCustomer.tsx';
import Logout from './components/Logout.tsx';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/login" Component={Login} />
        <Route path="/addCustomer" Component={AddCustomer} />
        <Route path="/logout" Component={Logout} />
        <Route path="*" element={<Navigate to="/login" />} />
      </Routes>
    </Router>
  );
};

export default App;
