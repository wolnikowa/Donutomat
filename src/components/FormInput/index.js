import React from 'react';
import './style.scss';


const FormInput = (props) => {

    return (
        <input
            id={props.id}
            name={props.name}
            type={props.type}
            onChange={props.onChange}
            value={props.value} >
        </input>
    )
}

export default FormInput

