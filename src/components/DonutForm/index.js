import React, { useState } from 'react';
import { useFormik } from 'formik';
import './main.scss';
import donut from './../../assets/donut-2.png';
import FormInput from '../FormInput';
import Button from '../Button';
import DatePicker from "react-datepicker"
import "react-datepicker/dist/react-datepicker.css";

const MyContainer = ({ className, children }) => {
    return (
        <div style={{ background: "#216ba5", color: "#fff" }}>
            <CalendarContainer className={className}>
                <div style={{ position: "relative" }}>{children}</div>
            </CalendarContainer>
        </div>
    );
};

const DonutForm = () => {
    const form = useFormik({
        initialValues: {
            donutorName: 'Add donutor name',
            donutDate: '12/01/2021',
        },
        onSubmit: values => {
            console.log(JSON.stringify(values, null, 2));
        },
    });

    const [startDate, setStartDate] = useState(new Date());


    return (
        <div className="formContainer">
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
                <div className="datepicker">
                    <DatePicker
                        selected={startDate}
                        onChange={form.handleChange}
                        CalendarContainer={MyContainer}
                        value={form.values.donutDate}
                    />
                </div>
                <Button type="submit"> Add new donutor </ Button>
            </form>
        </div>
    )
}

export default DonutForm