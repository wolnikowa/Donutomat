
const Body = (props) => {
    return (

<tbody>
                    {
                      data.map((props, index) => {
                
                          return (
                           
                              <tr key={id} className>
                            
                                <td>{props.name}</td>
                                <td>{props.addedby}</td>
                                <td>{props.dateadd}</td>
                                <td>{props.datedonut}</td>
                               </tr>
                          
                      )}
                      )}
                 </tbody>
    )}


    export default Body