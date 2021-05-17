import React from 'react';
import './style.scss'
import HeaderD from './components/Header/index.js';
import BodyD from './components/Body/index.js';
  

  const TableD = () => {
        return (
           <div className="mainContainer">
              
              <table>
                  <HeaderD />
                  <BodyD />
              </table>
           </div>
        )
     }
  
  export default TableD