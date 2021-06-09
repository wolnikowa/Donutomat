import React, { Component } from "react";
import Calendar from 'react-calendar';
import './style.scss'
 
const MyDonuts=()=>{
  
    return( <div className='calendar'> 
    <Calendar
        mode="month"
      /> </div>)
  }
export default MyDonuts;