import React, { useEffect, useState } from "react";
import Plot from 'react-plotly.js';
import { DateTime } from "luxon";

export default function FundInfo() {

    const companyID = "uber"

    const [isLoading, setIsLoading] = useState(false)
    const [data, setData] = useState()
    const [companyDetails, setCompanyDetails] = useState()

    const [value, setValue] = useState(0);

    /**
     * 
     * @param {int} value Number of stocks in transaction
     * @param {boolean} buy Is it a buy or a sell transaction
     */
    const onSubmitHandler = async (value, buy) => {
        const res = await fetch("/buySell/", {
            method: "POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ buy, "value": value })
        })
        const parsedResponse = await res.json()

        if (parsedResponse.ok == false) {
            alert(parsedResponse.error)
        }
        else {
            alert("Transaction successful")
            // return to previous page
        }
    }

    const sample = {
        data: {
          companyDetails: {
            company_name: "Uber Technologies Inc", 
            num_shares: 0
          }, 
          stockData: [{time: 1, fund: 12}, {time: 2, fund: 14}, {time: 3, fund: 25}]
        }, 
        "error": null
    }

    const times = sample.data.stockData.map(row => {return row.time});
    const fundVal = sample.data.stockData.map(row => {return row.fund});

   /* useEffect(() => {
        setData(() => ([{
            x: times,
            y: fundVal,
            type: 'scatter'
        }]))

    }, [])   */ 



    useEffect(() => {
        (async () => {
            const response = await fetch("/money/pastHoldings")
            .then(res => res.json())
            .then( data => {
                setData(data)
            })
            // parsedResponse: {data: {time_fetched:int, trading_price:str}[], error: str}

           /* const dates = parsedResponse.data.stockData.map(row => row.time_fetched).map(ts => {
                return DateTime
                    .fromSeconds(ts).setZone("America/New_York")
                    .toFormat("kkkk-LL-dd HH:mm:ss")
                // https://moment.github.io/luxon/#/formatting?id=table-of-tokens
                // https://plotly.com/javascript/time-series/
            })*/
            const times = data.times;

            const values = data.values;

            // console.log(date_data)
            setData(() => ([{
                x: times,
                y: values,
                type: 'scatter'
            }]))

            
            console.log(data)

            setIsLoading(false)
        })()
    }, []
    ) 


    return <div>
        {
            !isLoading
                ? (<>
                    <Plot data={data} style={{
                        display: "block", width: "80%", margin: "0 auto"
                    }} />
                    <div style={{
                        width: "80%",
                        display: "flex",
                        flexDirection: "row",
                        justifyContent: "space-evenly",
                        alignItems: "center",
                        margin: "0 auto"
                    }}>
                    </div>
                </>
                )
                : "Loading"
        }
    </div>
}