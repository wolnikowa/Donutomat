import React, { useCallback } from 'react';
import { Formik, Form } from 'formik';
import './main.scss';
import donut from './../../assets/donut-2.png';
import FormInput from '../FormInput';
import Button from '../Button';
import DatePicker from "react-datepicker"
import "react-datepicker/dist/react-datepicker.css";
import DatePickerField from '../DatePickerField';

const initialValues = {
    donutorName: 'Add donutor name',
    donutDate: '12/01/2021',
};

const DonutForm = () => {
    const onSubmit = useCallback((values) => {
        console.log(JSON.stringify(values, null, 2));
    }, []);

    return (
        <div className="formContainer">
            <header>
                <p>Add a new donutor</p> <img src={donut} />
            </header>
            <Formik
                initialValues={initialValues}
                onSubmit={onSubmit}
            >
                <Form className="insideForm">
                    <label htmlFor="donutorName">Name</label>
                    <FormInput
                        name="donutorName"
                        type="text"
                    />

                    <label htmlFor="donutDate">Date</label>
                    <div className="datepicker">
                        <DatePickerField name="donutDate" />
                    </div>
                    <Button type="submit"> Add new donutor </ Button>
                </Form>
            </Formik>
        </div>
    )
}

export default DonutForm
