import React, { useEffect, useState } from "react";
import Plot from 'react-plotly.js';
import { DateTime } from "luxon";
import { useParams } from "react-router-dom";
// import { useHistory } from "react-router-history"
/*
TODO:
[*] Figure out cors 
*/

/**
     * 
     * @param {int} value Number of stocks in transaction
     * @param {boolean} buy Is it a buy or a sell transaction
     */
const onSubmitHandler = async (value, buy, company) => {
    const res = await fetch("/buySell/", {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ buy, "value": value, company })
    })
    const parsedResponse = await res.json()

    if (parsedResponse.error != null || parsedResponse.data == null) {
        alert(parsedResponse.error)
    }
    else {
        alert("Transaction successful")
        // return to previous page
    }
}

export default () => {

    const { companyID } = useParams()

    const [isLoading, setIsLoading] = useState(true)
    const [data, setData] = useState()
    const [companyDetails, setCompanyDetails] = useState()

    const [value, setValue] = useState(0);


    useEffect(() => {
        (async () => {
            const response = await fetch("/buySell/?company=" + companyID)
            const parsedResponse = await response.json()
            // parsedResponse: {data: {time_fetched:int, trading_price:str}[], error: str}

            const dates = parsedResponse.data.stockData.map(row => row.time_fetched).map(ts => {

                return DateTime
                    .fromSeconds(parseInt(ts)).setZone("America/New_York")
                    .toFormat("kkkk-LL-dd HH:mm:ss")
                // https://moment.github.io/luxon/#/formatting?id=table-of-tokens
                // https://plotly.com/javascript/time-series/
            })

            const prices = parsedResponse.data.stockData.map(row => row.trading_price)

            // console.log(date_data)
            setData(() => ([{
                x: dates,
                y: prices,
                type: 'scatter'
            }]))

            setCompanyDetails(
                parsedResponse.data.companyDetails
            )

            console.log(parsedResponse)

            setIsLoading(false)
        })()
    }, []
    )


    return <div>
        {
            !isLoading
                ? (<>
                    <h1>{companyDetails.company_name} - {companyID.toUpperCase()}</h1>
                    <h2>Trading price: {companyDetails.currentTradingPrice}</h2>
                    <h2>Current holdings: {companyDetails.num_shares}</h2>
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
                        <h2>Transaction Volume: </h2>
                        <input value={value} onChange={e => setValue(e.target.value)} type={"number"} />
                        <button onClick={() => {
                            onSubmitHandler(value, true, companyID)
                        }}>Buy</button>
                        <button onClick={() => {
                            onSubmitHandler(value, false, companyID)
                        }}>Sell</button>
                    </div>
                </>
                )
                : "Loading"
        }
    </div>
}