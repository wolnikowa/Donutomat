import React from 'react';
import './style.scss';
import PropTypes from 'prop-types';

const FormInput = ({ id, name, type, onChange, value }) => (

    <input
        id={id || name}
        name={name}
        type={type}
        onChange={onChange}
        value={value}
        className='formInput' >
    </input>
)
// jeśli dodaję isRequired dla type i value, wyrzuca mi błąd w konsoli. Dlaczego? 
FormInput.propTypes = {
    id: PropTypes.string,
    name: PropTypes.string.isRequired,
    type: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.date
    ]),
    onChange: PropTypes.func,
    value: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.date
    ]),
}

export default FormInput


