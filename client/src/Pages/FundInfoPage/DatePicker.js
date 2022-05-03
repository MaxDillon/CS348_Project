import React, { useState } from "react";

import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import './Date.css'
export default function TableDatePicker() {
    const [startDate, setStartDate] = useState(new Date());
    const [endDate, setEndDate] = useState(new Date());

    console.log(Date.parse(startDate), Date.parse(endDate))
   
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
      </div>
    );
   }