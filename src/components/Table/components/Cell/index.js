import React from 'react';

const Cell = (props) => {
    return (

        <td> {props.children}</td>
    );
}

export default Cell