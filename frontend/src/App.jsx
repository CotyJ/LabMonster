import { useEffect, useState } from 'react'
import axios from 'axios';
import './App.css';

const host = "http://localhost:8000"
const baseRoute = "/push-button";

const fakeData = {
  actions: [
    {startFrame: 1, button: "back", holdFor: 30},
    {startFrame: 32, button: "forward", holdFor: 1},
    {startFrame: 33, button: "back", holdFor: 1},
    {startFrame: 34, button: "forward", holdFor: 1},
    {startFrame: 35, button: "X", holdFor: 1},
]}

function App() {
  // const [data, setData] = useState({});
  const pushButton = (dataJSON) => {
    axios.post(`${host}${baseRoute}`, dataJSON)
      .then( res => {
        console.log(res.data);
        // setData(res.data);
      })
      .catch( err => console.log(err.message));
  }

  // useEffect(() => {}, [data])


  return (
    <>
      <div>
        <button onClick={() => pushButton(fakeData)}>Send</button>
      </div>
    </>
  )
}

export default App
