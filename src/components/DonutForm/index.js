import React from 'react';
import { useFormik } from 'formik';
import './main.scss';
import donut from './../../assets/donut-2.png';
import FormInput from '../FormInput';

const DonutForm = () => {
    const form = useFormik({
        initialValues: {
            donutorName: 'Add donutor name',
            donutDate: '12/01/2021',
        },
        onSubmit: values => {
            alert(JSON.stringify(values, null, 2));
        },
    });

    return (
        <div className="formCointainer">
            <header>
                <p>Add a new donutor</p> <img src={donut} />
            </header>
            <form onSubmit={form.handleSubmit} className="insideForm">
                <label htmlFor="donutorName" className="firstLabel">Name</label>
                <FormInput
                    name="donutorName"
                    type="text"
                    onChange={form.handleChange}
                    value={form.values.donutorName} />

                <label htmlFor="donutDate" className="secondLabel">Date</label>
                <FormInput
                    name="donutDate"
                    type="date"
                    onChange={form.handleChange}
                    value={form.values.donutDate} />
                <button type="submit">Add a new donutor</button>
            </form>
        </div>
    )
}

export default DonutForm