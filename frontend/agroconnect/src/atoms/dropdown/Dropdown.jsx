import React from 'react'
import"./Dropdown.css"
import Select from '@mui/material/Select';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';

const Dropdown = ({data,setSelectedFarmer}) => {
  console.log('from dropdown',data)
  return (

    <div style={{ display: 'flex', justifyContent: 'flex-end', paddingLeft: '170px',paddingRight:'10px'}} >
      <Box sx={{borderBottom:0}}>
     
      <FormControl fullWidth>
      <InputLabel id="demo-simple-select-label">Select Farmer Company</InputLabel>
        <Select 
        sx={{fontWeight:"regular",border:"0", height:"53px",width:"703px",backgroundColor:'#BACD9B',fontFamily: 'Inter',fontSize:30, '&:before': {borderBottom: 'none'} }}
        labelId="demo-simple-select-label"
        id="demo-simple-select"
        
        onChange={(e) => {
          const selectedId = e.target.value;
          setSelectedFarmer(selectedId);  // Update the selected ID here
          field.onChange(e);  // Ensures the react-hook-form's value is updated
        }}
        label="Select Farmer Company"
        >
          {
          data.map((options)=>(
          <MenuItem key={options.id} value={options.id}>
            {options.name}
          </MenuItem>
        ))} 
        </Select>
        </FormControl>
        </Box>
    </div>
  )
}
export default Dropdown