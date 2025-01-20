import React from 'react'
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';

import "./BottomNav.css"

const Navigation = (Navigationbar) => {
    return (
      <div >Navigation</div>
    )
  }

export default function Navigationbar(){
    return(
        <Box className ="bottom-nav" >
            <AppBar position="static" width ="100%" >
                <Toolbar sx={{backgroundColor: "#2A4704"}}>
                         
                </Toolbar>
            </AppBar>
        </Box>
    );
}