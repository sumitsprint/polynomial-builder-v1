import Desmos from 'desmos'
import { useEffect, useRef } from 'react';

export default function Graph({polynomial}){
    const calculatorRef = useRef(null);
    const desmosRef = useRef(null);


    useEffect(() => {
      desmosRef.current =  Desmos.GraphingCalculator(calculatorRef.current);
      return () => {
        desmosRef.current.destroy();
      };


    }, []);
    
    useEffect(() => {
    if (!desmosRef.current) return;

    desmosRef.current.setExpression({
        id: "poly",
        latex: polynomial
    });
}, [polynomial]);

    

    return(
        <div
        ref={calculatorRef}
        style={{ 
            width: "600px",
            height: "400px", 
            marginTop: "20px"
             }}
      />

    )

}