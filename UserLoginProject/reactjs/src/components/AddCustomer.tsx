// src/components/AddCustomer.tsx
import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Button, Alert } from 'react-bootstrap';
import { ADD_CUSTOMER_URL, LOGOUT_URL } from '../backendinterface.ts';
import axios from "axios";


const AddCustomer = () => {
  const navigate = useNavigate();
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [dob, setDob] = useState('');
  const [phone, setPhone] = useState('');
  const [success, setSuccess] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);


  const isEmailValid = (email: string): boolean => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const isValid = emailRegex.test(email);
    const error = isValid ? true : false;
    return error

  };
  
  const validateFields = () => {
    if (firstName.trim() && lastName.trim() && 
    email.trim() && dob.trim() && phone.trim()){
      var output = { result: false, 
                     error: "" }

        if (!isEmailValid(email)) {
              output.error = "Please enter a valid email address"
              return output
          }
        if (!isValidPhoneNumber(phone)){
              output.error = "Please provide valid phone number"
              return output
        }
        return { result: true, error: null}
    }
    else{
        return { result: false, 
                 error: "Please fill in all details" };
    }
  }

  const isValidPhoneNumber = (value: string) => {
    if (((value.match(/^\+?[0-9]{10,}$/))) && 
            (value.length >= 5 && value.length <= 13)){
        return true
    }
    return false
}

  const clearForm = () => {
        setFirstName("");
        setLastName("");
        setDob("");
        setEmail("");
        setPhone("");
        
  };

  const handleAddCustomer = async () => {
    const output = validateFields()
    if (output.result && !output.error){
      try{
        let formData = new FormData
        formData.append('first_name', firstName)
        formData.append('last_name', lastName)
        formData.append('email', email)
        formData.append('dob', dob)
        formData.append('phone', phone)
        let authToken = localStorage.getItem('authToken')
        const headers = {
          'Content-Type': 'application/json',
          'Authorization': `Token ${authToken}`,
        };
        const response = await axios.post(ADD_CUSTOMER_URL, formData, {headers});
        setSuccess(`${response.data.message}`)
        clearForm();
      }catch(error){
        setError(`${error.response.data.error}`)
      }
    }else if (output.error){
      setError(output.error);
    }
  };

  const handleLogout = async () => {
    try{
      let authToken = localStorage.getItem('authToken')
      const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Token ${authToken}`,
      };
      const response = await axios.post(LOGOUT_URL, null, {headers});
      localStorage.removeItem('authToken');
      if (response.status === 200){
        navigate('/logout');
      }else{
        navigate('/login');
    }
    }catch(error){
      navigate('/login');
    }
  }
  const setAlert = () => {
    setError(null);
    setSuccess(null);
  }

  return (
    <div className="container d-flex justify-content-center align-items-center min-vh-100">
      <div className="card p-5" style={{ maxWidth: '400px', width: '100%' }}>
        <h3 className="text-center">Welcome</h3><br />
        <h2 className="text-center">Add Customer</h2>
        {error && <Alert variant="danger">{error}</Alert>}
        {success && <Alert variant="primary">{success}</Alert>}
        <div className="mb-3">
          <label htmlFor="firstName" className="form-label">
            First Name
          </label>
          <input
            type="text"
            className="form-control"
            id="firstName"
            placeholder="Enter first name"
            value={firstName}
            onChange={(e) => {
              setFirstName(e.target.value);
              setAlert();
            }}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="lastName" className="form-label">
            Last Name
          </label>
          <input
            type="text"
            className="form-control"
            id="lastName"
            placeholder="Enter last name"
            value={lastName}
            onChange={(e) => {
              setLastName(e.target.value);
              setAlert();
            }}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="email" className="form-label">
            Email
          </label>
          <input
            type="email"
            className="form-control"
            id="email"
            placeholder="Enter email"
            value={email}
            onChange={(e) => {
              setEmail(e.target.value);
              setAlert();
            }}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="dob" className="form-label">
            Date of Birth
          </label>
          <input
            type="date"
            className="form-control"
            id="dob"
            value={dob}
            onChange={(e) => {
              setDob(e.target.value);
              setAlert();
            }}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="phone" className="form-label">
            Phone
          </label>
          <input
            type="tel"
            className="form-control"
            id="phone"
            placeholder="Enter phone number"
            value={phone}
            onChange={(e) => {
              setPhone(e.target.value);
              setAlert();
            }}
          />
        </div>
        <Button variant="primary" onClick={handleAddCustomer} className="w-100">
          Add
        </Button>
        <Button variant="danger" onClick={handleLogout} className="mt-3" style={{ width: '80px' }}>
        Logout
        </Button>
      </div>
    </div>
  );
};

export default AddCustomer;
