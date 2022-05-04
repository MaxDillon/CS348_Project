import React, { useState } from "react";

import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import './Date.css'
export default function TableDatePicker(props) {
    const [startDate, setStartDate] = useState(new Date());
    const [endDate, setEndDate] = useState(new Date());

    console.log( Date.parse(startDate)/1000, Date.parse(endDate)/1000)

    function handleSubmit() {
        props.setStart(Date.parse(startDate)/1000)
        props.setEnd(Date.parse(endDate)/1000)
    }
   
    return (
      <div>
          <h4>Start date:</h4>
        <DatePicker
          selected={startDate}
          selectsStart
          startDate={startDate}
          endDate={endDate}
          onChange={date => setStartDate(date)}
        />
        <br></br>
        <br></br>
        <h4>End date:</h4>

        <DatePicker
          selected={endDate}
          selectsEnd
          startDate={startDate}
          endDate={endDate}
          minDate={startDate}
          onChange={date => setEndDate(date)}
        />
        <br></br>
        <br></br>
        <button onClick={handleSubmit}>Apply</button>
      </div>
    );
   }