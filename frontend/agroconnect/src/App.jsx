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
function App() {


  return (
    <>
      {/* <div>
        <a href="https://vite.dev" target="_blank" rel="noopener noreferrer">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank" rel="noopener noreferrer">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div> */}
          <div className="App">
          <Navigation />
          <Image/>
          {/* <Descr/> */}
          <Heading className="big-heading"></Heading>
          <SmallHead className= "b-heading"/>         
          <div className='bar'>
            <Dropdown/>
            <Button className="submit-button" text="SUBMIT"/>
          </div>
          <BasicTable/>
        </div>
       
      
    </>
  );
}

export default App;

