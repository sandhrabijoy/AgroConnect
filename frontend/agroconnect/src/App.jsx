import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';
import Heading from './atoms/Heading/Heading';
import Dropdown from './atoms/dropdown/Dropdown';
import SmallHead from './atoms/SmallHead/SmallHead'
import Button from './atoms/button/Button';
// import Descr from './atoms/descr/Descr'
import Image from './atoms/Images/Image'
import Navigation from './atoms/Navigation/Navigation'
import BasicTable from'./atoms/Table/Table'
import BottomNav from './atoms/BottomNav/BottomNav'

function App() {


  return (
    <>
     
          <div className="App">
          <Navigation />
          <Image/>
          <Heading className="big-heading"></Heading>
          <SmallHead className= "b-heading"/>         
          <div className='bar'>
            <Dropdown/>
            <Button className="submit-button" text="SUBMIT"/></div>
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

