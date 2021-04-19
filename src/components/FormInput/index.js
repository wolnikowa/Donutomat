import React, { useCallback } from 'react';
import { useFormikContext, useField } from 'formik';
import './style.scss';
import PropTypes from 'prop-types';

const FormInput = (props) => {
    const { id, name, type } = props;

    const { setFieldValue } = useFormikContext();
    const [ field ] = useField(props);

    const onChange = useCallback((ev) =>  setFieldValue(field.name, ev.target.value), [field.name]);

    return (
        <input
            id={id || name}
            name={name}
            type={type}
            onChange={onChange}
            value={field.value}
            className='formInput' >
        </input>
    )
}

// jeśli dodaję isRequired dla type i value, wyrzuca mi błąd w konsoli. Dlaczego?
FormInput.propTypes = {
    id: PropTypes.string,
    name: PropTypes.string.isRequired,
    type: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.date
    ]),
}

export default FormInput
