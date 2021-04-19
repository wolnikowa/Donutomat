import React, { useCallback } from 'react';
import { useField, useFormikContext } from 'formik';
import DatePicker from 'react-datepicker';

const DatePickerField = ({ ...props }) => {
    const { setFieldValue } = useFormikContext();
    const [ field ] = useField(props);

    const onChange = useCallback((val) =>  setFieldValue(field.name, val), [field.name]);

    return (
        <DatePicker
            {...field}
            {...props}
            selected={(field.value && new Date(field.value)) || null}
            onChange={onChange}
        />
    );
};

export default DatePickerField
