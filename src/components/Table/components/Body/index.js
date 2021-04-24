import React from 'react';
import Rows from '../Rows'
import './body.scss';


const Body = ({ data, columns }) => (


    <tbody className="tbody">

        {
            data.map((dataItem, index) => (

                <Rows key={dataItem.id} dataItem={dataItem} columns={columns} />

            ))
        }

    </tbody>

)
export default Body