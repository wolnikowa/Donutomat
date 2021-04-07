import React from 'react';
import PropTypes from 'prop-types';
import './style.scss'

const Button = ({ text, type, onClick }) => (

    <button
        type={type}
        onClick={onClick}
        className='formButton'>
        {text}
    </button>
);

Button.propTypes = {
    type: PropTypes.string,
    text: PropTypes.string.isRequired,
    onClick: PropTypes.func
}
export default Button