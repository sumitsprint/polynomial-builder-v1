export function polynomialString(coeffs) {
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

    

  