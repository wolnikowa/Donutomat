
import React from 'react';
import './table.scss';
import Header from './components/Header';
import Body from './components/Body';

const Table = ({ data, columns }) => {
   return (
      <div>
         <table className="table">
            <Header columns={columns} />
            <Body data={data} columns={columns} />
         </table>
      </div>
   )
}

export default Table