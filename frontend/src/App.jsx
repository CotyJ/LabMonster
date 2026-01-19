import axios from 'axios';
import './App.css';

const host = "http://localhost:8000"
const baseRoute = "/push-button";

import ACTIONS from './actions';

function App() {
  const pushButton = (dataJSON) => {
    axios.post(`${host}${baseRoute}`, dataJSON)
      .then( res => {
        console.log(res.data);
      })
      .catch( err => console.log(err.message));
  }

  return (
    <div className='container'>
      <div className="buttons">

        {Object.entries(ACTIONS).map(([name, inputs]) => (
          <div key={name} className='row m-2'>
            <button onClick={() => pushButton(inputs)}>{name}</button>
          </div>
        ))}

      </div>
    </div>
  )
}

export default App
