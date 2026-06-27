export default function CoordinateTable({coordinates, setCoordinates}){
    return (
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
    )
}