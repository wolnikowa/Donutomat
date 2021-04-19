import React from 'react';
import './body.scss';
import Rows from '/Users/admin/Documents/GitHub/Donutomat/src/components/Table/components/Rows/index.js'
import Cell from '/Users/admin/Documents/GitHub/Donutomat/src/components/Table/components/Cell/index.js'

const Body = ({data}) => {
    return (

<tbody className = "tbody">
      
      {
        data.map((dataItem, index) => (
          
         <Rows /> 
         <Cell />
                   
        ))
     
      }
     
</tbody>

    )}

    export default Body
