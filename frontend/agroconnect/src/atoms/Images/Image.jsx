import React from 'react';
import './Image.css';
import leftimage from '../../images/leftimage.jpg';
import rightimage from '../../images/rightimage.jpg';
import Descr from '../descr/Descr';

const Image = (props) => {
  return (
    <div className={props.className}>
      <img src={leftimage} alt="left image" className="left-image" />
      <Descr />
      <img src={rightimage} alt="right image" className="right-image" />
    </div>
  );
};

export default Image;
