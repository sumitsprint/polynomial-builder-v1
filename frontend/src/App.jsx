import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  const [coordinates, setCoordinates] = useState([{x: "", y: ""},
    {x: "", y: ""},
    {x: "", y: ""},
    {x: "", y: ""},
    ]);
  
    



  return (
    
      <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100vh', fontSize: '2rem', fontWeight: 'bold'}}>
        Polynomial Builder V1

      <table>
        <thead>
          <tr>
            <th>x</th>
            <th>y</th>
            </tr>
          </thead>
        <tbody>
          {coordinates.map((points, index) => (
            <tr key = {index}>
              <td>
            <input
            value = {points.x}
            onChange = {(e) => {const updated = [...coordinates];
              updated[index].x = e.target.value;
              setCoordinates(updated);
            }}
            />
              </td>
              <td>
                <input
                value = {points.y}
                onChange = {(e) => {const updated = [...coordinates];
                  updated[index].y = e.target.value;
                  setCoordinates(updated);
                }}
                
                />

              </td>

            </tr>


          ))}
        </tbody>
      </table>

      </div>
    
  )
}

export default App
