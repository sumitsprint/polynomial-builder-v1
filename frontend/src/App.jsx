import { useState} from 'react'


import { polynomialString, polynomialLatex } from './utils/polynomial';
import CoordinateTable from './CoordinateTable';
import PolynomialDisplay from './PolynomialDisplay';
import Graph from './Graph';
import './App.css'


export default function App() {
  const [coordinates, setCoordinates] = useState([{x: "", y: ""},
    {x: "", y: ""},
    {x: "", y: ""},
    {x: "", y: ""},
    {x: "", y: ""}
    ]);

    
    
    const [polyLatex, setPolyLatex] = useState("");
    const [error, setError] = useState("");
    const[poly, setPoly] = useState("");
    
    
    

    // /**/
    //  */
    const handleAnalyse = async () => {
        try {
          setError("");
          

        const response = await fetch('http://127.0.0.1:8000/analyse', {method: 'POST', 
          headers: {'content-type': 'application/JSON'},
          body: JSON.stringify(coordinates)
        });
        
        const data = await response.json();
        if(!response.ok) {
          throw new Error(data.detail);
        }

        const poly = polynomialString(data.coeffs);
        const latex = polynomialLatex(data.coeffs)


        
        setPolyLatex(latex);
        setPoly(poly)

        
      } catch (error) {
        setError(error.message);
      }

       }

    



  return (
    
      <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100vh', fontSize: '2rem', fontWeight: 'bold'}}>
        Polynomial Builder V1

      <CoordinateTable coordinates={coordinates} 
      setCoordinates={setCoordinates}/>
      {/* all recieves an event object */}
      
       <button style={{marginBottom: "20px", marginTop: "20px"}} 
       onClick = {handleAnalyse}>
        Analyse
        </button>
       
       <PolynomialDisplay error={error} polyLatex={polyLatex}/>
       
      <Graph polynomial={poly} />
    
        </div>
    
  )
}

 
