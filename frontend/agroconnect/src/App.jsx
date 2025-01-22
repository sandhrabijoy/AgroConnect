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
  const[selectedFarmer,setSelectedFarmer]=useState(null);
  const[cultivators,setCultivators]=useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Selected Farmer ID:", selectedFarmer);
    console.log("Cultivators Data:", cultivators);
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

  
  // (() => {
  //   if (selectedFarmer) {
  //     axios
  //       .get(`http://127.0.0.1:8000/cultivators/by_company/${selectedFarmer}`)
  //       .then((response) => {
  //         setCultivators(response.data);
  //       })
  //       .catch((error) => {
  //         console.error("Error fetching cultivators:", error);
  //       });
  //   }
  // }, [selectedFarmer]);

  async function handleOnclick() {
    try {
      const result = await fetch(`http://127.0.0.1:8000/cultivator/by_company/${selectedFarmer}`);
      
      if (!result.ok) {
        throw new Error("No output");
      }
      
      const data = await result.json(); 
      console.log(data); 
      
      const newdata = data; 
      console.log(newdata); 
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  }
  return (
    <div className="App">
      <Navigation />
      <Image />
      <Heading className="big-heading" />
      <SmallHead className="b-heading" />
      <div className="bar">
        <Dropdown 
        data={farmerOptions}
        setSelectedFarmer={setSelectedFarmer}
    
         />
        <Button className="button-style" text="SUBMIT" Onclick={handleOnclick}  />
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
