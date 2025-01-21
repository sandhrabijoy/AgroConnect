import React from 'react';
import './Button.css'; 

const Button = (props) => {
  return (
    <div>
      <button className={props.className}onClick={props.handleChange}>{props.text}</button>
    </div>
  );
};

export default Button;
