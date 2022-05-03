import React, { useEffect, useState } from "react";
import Plot from 'react-plotly.js';
import TableDatePicker from './DatePicker.js'

export default function FundInfo() {

    const [data, setData] = useState()
    const [isLoading, setIsLoading] = useState(true)
    const [start, setStart] = useState(0)
    const [end, setEnd] = useState(100)


    useEffect(() => {
        fetch("/money/pastHoldings", 
        {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'start': start,
                'end': end
            })
        })
        .then(res => res.json())
        .then( data => {

            setData({
                x: data.times,
                y: data.values,
                type: 'scatter'
            })
            setIsLoading(false)
        })

    }, [start, end]) 



    return (<>
        {!isLoading? (<>
            <h1 >Fund History</h1>
            <h2>View values over a time period</h2>
            <Plot data={[data]} 
                style={{
                    display: "block", width: "100%", margin: "0 auto", listStylePosition: "relative"
                    }} />
            
        </>): "Loading" }
        <TableDatePicker setStart={setStart} setEnd={setEnd}/>
            <br></br>
    </>)
}