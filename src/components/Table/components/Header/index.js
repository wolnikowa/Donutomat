import './header.scss';
import React from 'react';


const Header = ({columns}) => {
    return (

<thead>
              
{
    data.map((dataItem, index) => (
                
                           
        <tr>
        {
            columns.map((columns) => (
            <th>{dataItem[columns.label]}</th>             
        ))
        }
                      
        </tr>   
                          
        ))
}

</thead>

    )}
export default Header



