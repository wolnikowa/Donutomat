import React, {useState} from 'react';
import { useFormik } from 'formik';
import './main.scss';
import donut from './../../assets/donut-2.png';
import FormInput from '../FormInput';
import DatePicker from "react-datepicker"
import "react-datepicker/dist/react-datepicker.css";

const DonutForm = () => {
    const form = useFormik({
        initialValues: {
            donutorName: 'Add donutor name',
            donutDate: '12/01/2021',
        },
        onSubmit: values => {
            // alert(JSON.stringify(values, null, 2));
        },
    });

    const [startDate, setStartDate] = useState(new Date());
    const MyContainer = ({ className, children }) => {
      return (
        <div style={{ background: "#216ba5", color: "#fff" }}>
          <CalendarContainer className={className}>
            <div style={{ position: "relative" }}>{children}</div>
          </CalendarContainer>
        </div>
      );
    };

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
                    <div className="datepicker">
                        <DatePicker
                            selected={startDate}
                            onChange={date => setStartDate(date)}
                            CalendarContainer={MyContainer}
                        />
                    </div>

                <button type="submit">Add a new donutor</button>
            </form>
        </div>
    )
}

export default DonutForm