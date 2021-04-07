import React from 'react';

import './body.scss';


const Body = ({data, columns}) => {
    return (

<tbody>
      
      {
        data.map((dataItem, index) => (
                
          <tr key={dataItem.id} className>
          {
              columns.map((column) => (
              <td>{dataItem[column.name]}</td>
                         
        ))
          }
                      
          </tr>   
                          
        ))
      }
</tbody>
    )}

    export default Body