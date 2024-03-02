import React from 'react';
import { Link } from 'react-router-dom';



const Logout = () =>{
    return (
        <div>
            <p className="mt-3 text-center">You logged out successfully..
            <Link to="/login">Click here</Link> to login again </p>

        </div>
    )
}

export default Logout;