import React from "react";
import {useState, useLayoutEffect} from 'react'
import { useNavigate } from 'react-router-dom';
import './Edit.css'
export default function Field(props) {
    const[details, setDetails] = useState(props);
    const [isEditing, setEditing] = useState(false);

function handleSubmit(e) {
    e.preventDefault();
    setEditing(false);
  }
const view = ( <div className={"stackIt"}>
    <p>{props.details[0]}</p> 
    <p>{props.details[1]}</p> 
    <p><button className={"button"} onClick={() => setEditing(true)}>Click</button></p>
    </div>
);

const editing = (
        <div className={"stackIt"}>

<p>{props.details[0]}</p>
    <input></input>
<p><button className={"button"} onClick={() => setEditing(false)}>Save</button></p>
</div>
);

return <div>{isEditing ? editing : view}</div>;

}