import React from 'react'
import "./Image.css"
import leftimage from "../../images/leftimage.svg"
import rightimage from "../../images/rightimage.svg"
const Image = (props) => {
  return (
    <div className={props.className}>
        <div className={props.className}>
        <img src={leftimage} alt ="left image"/>
        <img src={rightimage} alt ="right image"/>
        </div>
    </div>
  )
}
export default Image