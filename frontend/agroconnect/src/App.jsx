import React, { useState, useEffect } from 'react';
import './App.css';
import Heading from './atoms/Heading/Heading';
import Dropdown from './atoms/dropdown/Dropdown';
import SmallHead from './atoms/SmallHead/SmallHead';
import Button from './atoms/button/Button';
import Image from './atoms/Images/Image';
import Navigation from './atoms/Navigation/Navigation';
import BasicTable from './atoms/Table/Table';
import BottomNav from './atoms/BottomNav/BottomNav';
import axios from 'axios';

function App() {
  const [farmerOptions, setFarmerOptions] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Button clicked");
  };

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/farmer/")
      .then((response) => {
        console.log(response)
        console.log(response.data);
        setFarmerOptions(response.data);
        console.log(farmerOptions)
      })
      .catch((error) => {
        console.error("There was an error!", error);
      });
  }, []); 

  useEffect(() => {
    console.log(farmerOptions); 
  }, [farmerOptions]);

  return (
    <div className="App">
      <Navigation />
      <Image />
      <Heading className="big-heading" />
      <SmallHead className="b-heading" />
      <div className="bar">
        <Dropdown data={farmerOptions} />
        <Button className="button-style" text="SUBMIT" onClick={handleSubmit} />
      </div>
      <div className="table-size">
        <center>
          <BasicTable />
        </center>
      </div>
      <BottomNav />
    </div>
  );
}

export default App;
