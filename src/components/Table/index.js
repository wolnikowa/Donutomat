
import React from 'react';
import './table.scss';
import Header from './components/Header/index.js';
import Body from './components/Body/index.js';
  

  const Table = ({data, columns}) => {
        return (
           <div>
              <table>
              <Header columns={columns} />
              <Body data={data} columns={columns} />
              </table>
           </div>
        )
     }
  
  export default Table