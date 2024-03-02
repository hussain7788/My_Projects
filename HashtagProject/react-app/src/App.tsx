import logo from './logo.svg';
import './App.css';
import React from "react";
import axios, {AxiosResponse} from 'axios';
import DateComponent from './components/DateComponent.tsx';


function App() {
 
  return (
    <div className="App">
      <DateComponent />
    </div>
   
  );
}

export default App;
