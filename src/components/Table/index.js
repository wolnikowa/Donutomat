
import React from 'react';
import './table.scss';
import Header from './components/Header/index.js';
import Body from './components/Body/index.js';
  

  const Table = () => {
        return (
           <div>
              
              <table>
              <Header />
              <Body />
              </table>
           </div>
        )
     }
  
  export default Table