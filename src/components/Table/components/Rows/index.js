
import React from 'react';
import './style.scss';

const Rows = (props, dataItem) => {
    return (

    <tr key={dataItem.id} className="rows">   
    {props.Children}
    </tr>   
    );
}
       
export default Rows

