import React, { useEffect, useState } from "react";
import Plot from 'react-plotly.js';
import { DateTime } from "luxon";

/*
TODO:
[] Figure out cors
[] 
*/

export default () => {

    const companyName = "uber"

    const [isLoading, setIsLoading] = useState(true)
    const [data, setData] = useState()

    useEffect(() => {
        (async () => {
            const response = await fetch("/buySell/?company=" + companyName)
            const parsedResponse = await response.json()
            // parsedResponse: {data: {time_fetched:int, trading_price:str}[], error: str}

            const dates = parsedResponse.data.map(row => row.time_fetched).map(ts => {
                return DateTime
                    .fromSeconds(ts).setZone("America/New_York")
                    .toFormat("kkkk-LL-dd HH:mm:ss")
                // https://moment.github.io/luxon/#/formatting?id=table-of-tokens
                // https://plotly.com/javascript/time-series/
            })

            const prices = parsedResponse.data.map(row => row.trading_price)

            // console.log(date_data)
            setData(() => ([{
                x: dates,
                y: prices,
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
                    <h1>{companyName.toUpperCase()}</h1>
                    <h2>Trading price: {data[0].y[data[0].y.length - 1]}</h2>
                    <Plot data={data} />
                </>
                )
                : "Loading"
        }
    </div>
}