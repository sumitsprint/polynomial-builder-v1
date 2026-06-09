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
    {x: "", y: ""}
    ]);

    const [result, setResult] = useState("");
    const [polyString, setPolyString] = useState("");
    const [coeffs, setCoeffs] = useState(null);

    function polynomialString(coeffs) {
      if (!coeffs || coeffs.length === 0) return "";

      let deg = coeffs.length - 1;
      let terms = [];
      coeffs.forEach((coeff, i) => {
        if (coeff === 0) return;
        let power = deg - i;
        let term = "";

        if (power === 0) {
          term = ` ${coeff} `;
        }
        else if (power === 1) {
          term = ` ${coeff}x `;
        }
        else {
 
        term = ` ${coeff}x^${power} `;
        
      }
      terms.push(term);
      })
      return terms.join(' + ');
    }
  
    
    
    



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
          {coordinates.map((point, index) => (
            <tr key = {index}>
              <td>
            <input
            value = {point.x}
            onChange = {(e) => {const updated = [...coordinates];
              updated[index].x = e.target.value;
              setCoordinates(updated);
            }}
            />
              </td>
              <td>
                <input
                value = {point.y}
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
      
       <button onClick = {async () => {
        const response = await fetch('http://127.0.0.1:8000/analyse', {method: 'POST', 
          headers: {'content-type': 'application/JSON'},
          body: JSON.stringify(coordinates)
        });
        const data = await response.json();
        console.log(data.coeffs);
        setCoeffs(data.coeffs);
        
        setPolyString(polynomialString(data.coeffs));
        

       }}>Analyse</button>
       <div>
         {polyString && <p>Polynomial: {polyString}</p>}

       </div>
       
       
    

        
     
      

      

      </div>
    
  )
}

export default App
