import React, { useEffect, useState } from "react";
import Plot from 'react-plotly.js';
import { DateTime } from "luxon";

/*
TODO:
[] Figure out cors
[] 
*/

export default () => {
    const [isLoading, setIsLoading] = useState(true)
    const [data, setData] = useState()

    useEffect(async () => {
        // const response = await fetch("/buySell")
        // const parsedResponse = await response.json()
        const parsedResponse = {
            "data": [
                {
                    "time_fetched": 1651072489,
                    "trading_price": "$30.64"
                },
                {
                    "time_fetched": 1651072551,
                    "trading_price": "$30.74"
                },
                {
                    "time_fetched": 1651072612,
                    "trading_price": "$30.78"
                },
                {
                    "time_fetched": 1651072674,
                    "trading_price": "$30.71"
                },
                {
                    "time_fetched": 1651072735,
                    "trading_price": "$30.78"
                },
                {
                    "time_fetched": 1651072796,
                    "trading_price": "$30.75"
                },
                {
                    "time_fetched": 1651072858,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651072926,
                    "trading_price": "$30.66"
                },
                {
                    "time_fetched": 1651072987,
                    "trading_price": "$30.72"
                },
                {
                    "time_fetched": 1651089907,
                    "trading_price": "$30.69"
                },
                {
                    "time_fetched": 1651093725,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651093786,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651093879,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651093941,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651093996,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651094057,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651094119,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651094180,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651094241,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651094303,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651094365,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651094426,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651094487,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651094549,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651094610,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651094671,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651094733,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651094794,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651094856,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651094917,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651094979,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095013,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095075,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095136,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095197,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095259,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095306,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095367,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095429,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095490,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095553,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095615,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095677,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095739,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095801,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095863,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095924,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651095986,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651096048,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651096110,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651096172,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651096233,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651096295,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651096356,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651096417,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651096478,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651096540,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651096601,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651096662,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651096724,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651096785,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651103891,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651103952,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651104013,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651104075,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651104136,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651104198,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651104259,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651104320,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651104382,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651104443,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651104504,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651104565,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651104627,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651104689,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651104750,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651104811,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651104872,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651104961,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651105022,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651105084,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651105145,
                    "trading_price": "$30.68"
                },
                {
                    "time_fetched": 1651105206,
                    "trading_price": "$30.68"
                }
            ],
            "error": null
        }

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
    }, []
    )

    /*
    var data = [
        {
            x: ['2013-10-04 22:23:00', '2013-11-04 22:23:00', '2013-12-04 22:23:00'],
            y: [1, 3, 6],
            type: 'scatter'
        }
    ];
    */

    return <div>
        {
            !isLoading
                ? <Plot data={data} />
                : "Loading"
        }
    </div>
}