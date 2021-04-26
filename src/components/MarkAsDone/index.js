import React, { useCallback } from 'react';
import './style.scss'


const MarkAsDone = ({ data }) => {

    const onClick = useCallback(() => {
        console.log(data);
    }, [data]);


    return (
        <button
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