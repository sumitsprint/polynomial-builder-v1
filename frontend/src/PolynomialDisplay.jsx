import katex from "katex";
import "katex/dist/katex.min.css";

export default function PolynomialDisplay({error, polyLatex}){
    return (
        <>
        {
  error && (
    <p
      style={{
        color: "red",
        fontSize: "18px",
        marginTop: "10px"
      }}
    >
      {error}
    </p>
  )
}
       <div style={{marginBottom: "20px", marginTop: "20px"}}>
         {polyLatex && (
          <div
            dangerouslySetInnerHTML={{
              __html: katex.renderToString(
                `y=${polyLatex}`,
                {
                  throwOnError: false
                }
              )
            }}
          />
          )}

       </div>
       </>
    )
}