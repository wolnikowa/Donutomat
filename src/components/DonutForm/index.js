import React, {useState} from 'react';
import { useFormik } from 'formik';
import './main.scss';
import donut from "./../../assets/donut-2.png";
// import DatePicker from "react-horizontal-datepicker";
import DatePicker from "react-datepicker"
import "react-datepicker/src/stylesheets/datepicker.scss";
// import Calendar from 'react-input-calendar';



const DonutForm = () => {

    const form = useFormik({
        initialValues: {
            donutorName: 'Alicja Kempa',
            donutDate: '12/01/2021',
        },
        onSubmit: values => {
            // alert(JSON.stringify(values, null, 2));
        },
    });
    // const selectedDay = val => {
    //     console.log(val);
    // };
    
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
                <input
                    id="donutorName"
                    name="donutorName"
                    type="text"
                    onChange={form.handleChange}
                    value={form.values.donutorName}
                    className="firstInput" />

                <label htmlFor="donutDate" className="secondLabel">Date</label>
                {/* <input
                    id="donutDate"
                    name="donutDate"
                    type="date"
                    onChange={form.handleChange}
                    value={form.values.donutDate}
                    className="secondInput" /> */}

                <div className="datepicker">
                    <DatePicker
                        selected={startDate}
                        onChange={date => setStartDate(date)}
                        CalendarContainer={MyContainer}
                    />
                    {/* <DatePicker 
                        getSelectedDay={selectedDay}
                        labelFormat={"MMMM"}
                        color={"#FFD242"}          
                    /> */}
                    {/* <Calendar format='DD/MM/YYYY' date='4-12-2014' /> */}
                    
                </div>


                <button type="submit">Add a new donutor</button>
            </form>
        </div>
    )


}

export default DonutForm