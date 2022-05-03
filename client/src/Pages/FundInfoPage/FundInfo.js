import React, { useEffect, useState } from "react";
import Plot from 'react-plotly.js';
import { DateTime } from "luxon";

export default function FundInfo() {

    const [data, setData] = useState()
    const [received, setReceived] = useState({times: [], values: []})
    const [isLoading, setIsLoading] = useState(true)
    const [times, setTimes] = useState([])
    const [values, setValues] = useState([])

    useEffect(() => {
        (async () => {
            const response = await fetch("/money/pastHoldings")
            .then(res => res.json())
            .then( data => {
                setReceived(data)
            })
            //console.log(received)

            const times = received.times;
            const values = received.values;
           
            setData(() => ([{
                x: times,
                y: values,
                type: 'scatter'
            }])) 

            setIsLoading(false)


        })()
    }, []
    ) 



    return <div>
        {
           !isLoading
           ? (<>
          <h1 >Fund History</h1>
          <h2>View values over a time period</h2>
                    <Plot data={data} 
                        style={{
                            display: "block", width: "100%", margin: "0 auto"
                         }} />
                    <div style={{
                        width: "100%",
                        display: "flex",
                        flexDirection: "row",
                        justifyContent: "space-evenly",
                        alignItems: "center",
                        margin: "0 auto"
                    }}>
                    </div>
            </>): "Loading"
                
        }
    </div>
}