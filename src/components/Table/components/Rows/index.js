
import React from 'react';
import './style.scss';
import Cell from '../Cell'

const Rows = ({dataItem, columns}) => {
    return (
        <tr className = "rows">
        {
            columns.map((column) => (
                <Cell key={column.name}>{dataItem[column.name]} </Cell>
                
            ))
        }
             
        </tr>
        );
        }
       
export default Rows

