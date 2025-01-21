import React,{ useState,useEffect } from 'react';
import './App.css';
import Heading from './atoms/Heading/Heading';
import Dropdown from './atoms/dropdown/Dropdown';
import SmallHead from './atoms/SmallHead/SmallHead'
import Button from './atoms/button/Button';
import Image from './atoms/Images/Image'
import Navigation from './atoms/Navigation/Navigation'
import BasicTable from'./atoms/Table/Table'
import BottomNav from './atoms/BottomNav/BottomNav'
import axios from "axios";


function App() {
  const [lotOptions,setLotOptions] = useState([]);
  useEffect(()=>{
    axios
    .get("http://localhost:8000/farmercompany/")
    .then((response)=>{
      console.log(response.data.data);
      setLotOptions(response.data.data)
    })
  })
  const handleSubmit =(e)=>{
    e.preventDefault();
    console.log("ButtonClicked");
  }


  return (
    <>
     
          <div className="App">
          <Navigation />
          <Image/>
          <Heading className="big-heading"></Heading>
          <SmallHead className= "b-heading"/>         
          <div className='bar'>
            <Dropdown/>
            <Button  className="button-style" text="SUBMIT" handleChange={handleSubmit}/></div>
          <div className='table-size'><center>
          <BasicTable/>
          </center>
        </div>
       <BottomNav/>

       
    </div>
    </>
  );
}

export default App;

