import { useState, useEffect, useRef } from 'react'
import Desmos from 'desmos'



import './App.css'

function App() {
  const [coordinates, setCoordinates] = useState([{x: "", y: ""},
    {x: "", y: ""},
    {x: "", y: ""},
    {x: "", y: ""},
    {x: "", y: ""}
    ]);

    
    const [polyString, setPolyString] = useState("");
    

    function polynomialString(coeffs) {
      if (!coeffs || coeffs.length === 0) return "";

      let deg = coeffs.length - 1;
      let terms = [];
      coeffs.forEach((coeff, i) => {
        if (coeff === 0) return;
        let power = deg - i;

        let absoluteCoeff = Math.abs(coeff);

        let term = "";

        if (power === 0) {
          term = ` ${absoluteCoeff} `;
        }
        else if (power === 1) {
          term = ` ${absoluteCoeff}x `;
        }
        else {
 
        term = ` ${absoluteCoeff}x^${power} `;
        
      }
      // what does it do 
        if (absoluteCoeff === 1 && power > 0) {
          term = term.replace("1", "");
        }
        if (coeff < 0) {
          term = " - " + term;
        }
        else if (terms.length > 0) {
          term = " + " + term;
        }
      terms.push(term);
      })
      if (terms.length === 0) return "0"; // this is for 0 p(x)
      
      return terms.join(" ");
    }

    const calculatorRef = useRef(null);

    useEffect(() => {
      const calculator = Desmos.GraphingCalculator(calculatorRef.current);
      return () => {
        calculator.destroy();
      };


    }, []);
    



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
      {/* all recieves an event object */}
      
       <button onClick = {async () => {
        const response = await fetch('http://127.0.0.1:8000/analyse', {method: 'POST', 
          headers: {'content-type': 'application/JSON'},
          body: JSON.stringify(coordinates)
        });
        const data = await response.json();
        console.log(data.coeffs);
        
        
        setPolyString(polynomialString(data.coeffs));
        

       }}>Analyse</button>
       <div>
         {polyString && <p>P(x) = {polyString}</p>}

       </div>
       <>
      <div
        ref={calculatorRef}
        style={{ width: "600px", height: "400px" }}
      />
    </>
        </div>
    
  )
}

export default App
