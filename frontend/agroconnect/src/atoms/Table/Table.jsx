import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

function createData(id, Name, active) {
  return { id, Name, active };
}

const rows = [
  createData(1,'ABC','Active'),
  createData(2 , 'XYZ','Non-Active'),
  createData(3, 'PQR', 'Active'),
];

export default function BasicTable({cultivators}) {
  console.log(cultivators)
  
    // Extract the map logic into a variable
    const tableRows = cultivators[0]?.map((cultivator) => (
      <TableRow key={cultivator.id}>
        <TableCell component="th" scope="row">
          {cultivator.id}
        </TableCell>
        <TableCell align="right">{cultivator.name}</TableCell>
        <TableCell align="right">{cultivator.active ? 'Active' : 'Inactive'}</TableCell>
      </TableRow>
    ));
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell className='heading' sx={{color:"rgb(42, 71, 4)" , fontWeight:"bold", fontSize:"30px"} }>ID </TableCell>
            <TableCell align="right"  className='heading' sx={{color:"rgb(42, 71, 4)" , fontWeight:"bold", fontSize:"30px"} }>NAME</TableCell>
            <TableCell align="right" className='heading'sx={{color:"rgb(42, 71, 4)" , fontWeight:"bold", fontSize:"30px"} }>ACTIVE&nbsp;</TableCell>
        
          </TableRow>
        </TableHead>
        <TableBody>
          {/* {rows.map((row) => (
            <TableRow className='heading' sx={{ fontWeight:"bold"} }
              key={row.companyid}>
             
              <TableCell component="th" scope="row"className='heading'  sx={{ fontWeight:"",fontSize:"20px"} }>
                {row.id}
              </TableCell>
              <TableCell align="right"  className='heading'  sx={{ fontWeight:"", fontSize:"20px"} }>{row.Name}</TableCell>
              <TableCell align="right" className='heading'  sx={{ fontWeight:"", fontSize:"20px"} }>{row.active}</TableCell>
            
            </TableRow>
          ))} */}
          {tableRows}
        </TableBody>
      </Table>
    </TableContainer>
  );
}