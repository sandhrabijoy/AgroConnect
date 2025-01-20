import React from 'react'
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '../button/Button';
import Heading from '../Heading/Heading';
import SmallHead from '../SmallHead/SmallHead';
import "./Navigation.css";
const pages = ['HOME', 'CONTACT'];

const Navigation = (Navigationbar) => {
  return (
    <div className=''>Navigation</div>
  )
}
export default function Navigationbar(){
    return(
        <Box >
            <AppBar position="static" >
                <Toolbar sx={{flexGrow:1, backgroundColor: "#2A4704"}}>
                    
                        
                        <Typography variant="h6" component="div" style={{lineHeight:"50px"}}>
                            <Heading className="small-heading"/>
                            <SmallHead className="s-heading"/>
                        </Typography>
                        <div className='home-contact'> 
                            <Button className='home-button' text="HOME"></Button> 
                            <Button className='home-button' text="CONTACT"></Button>
                        </div>                    

                    
                </Toolbar>
            </AppBar>
        </Box>
    );
}