import React, { useCallback } from 'react';
import { Formik, Form } from 'formik';
import './main.scss';
import donut from './../../assets/donut-2.png';
import FormInput from '../FormInput';
import Button from '../Button';
import "react-datepicker/dist/react-datepicker.css";
import DatePickerField from '../DatePickerField';
import onSubmit from '../../Pages/Add'

const initialValues = {
    donutorName: 'Add donutor name',
    donutDate: '12/01/2021',
};

const DonutForm = ({onSubmit}) => {
    // onSubmit({document.getElementById("").value})
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
                    <div >
                        <DatePickerField name="donutDate" className="datepicker" />
                    </div>
                    <Button type="submit"> Add new donutor </ Button>
                </Form>
            </Formik>
        </div>
    )
}

export default DonutForm
