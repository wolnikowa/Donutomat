import React, { useCallback } from 'react';
import './style.scss'


const MarkAsDone = (props) => {

    const onClick = useCallback((props) => {
        console.log(JSON.stringify(props, null, 2));
    }, []);


    return (
        <button
            {...props}
            onClick={onClick}
            className='doneButton'>
            Done
        </button>
    )
};


// const Button = ({ text, type, onClick }) => (

//     <button
//         type={type}
//         onClick={onClick}
//         className='formButton'>
//         {text}
//     </button>
// );

export default MarkAsDone