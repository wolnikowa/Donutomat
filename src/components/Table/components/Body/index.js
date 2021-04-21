import React from 'react';
<<<<<<< HEAD

const donutors = [
    {
     id: '1',
     name:'Julia Bessman',
     addedby: 'Ryszard Jakielski',
     dateadd: '20-03-2021',
     datedonut: '21-03-2021'
    },
    {
        id: '2',
        name:'Alicja Kempa',
        addedby: 'Ryszard Jakielski',
        dateadd: '20-03-2021',
        datedonut: '21-03-2021'
    },
    {
        id: '3',
        name:'Wiktoria Wolnik',
        addedby:'Ryszard Jakielski',
        dateadd:'20-03-2021',
        datedonut: '21-03-2021'
    }
  ]



const Body = () => {
    return (

<tbody>
                    {
                      donutors.map((donutors, index) => {
                          const { id,name,addedby, dateadd,  datedonut } = donutors 
                          return (
                           
                              <tr key={id} className>
                            
                                <td>{name}</td>
                                <td>{addedby}</td>
                                <td>{dateadd}</td>
                                <td>{datedonut}</td>
                               </tr>
                          
                      )}
                      )}
                 </tbody>
    )}


    export default Body
=======
import './body.scss';
import Rows from '/Users/admin/Documents/GitHub/Donutomat/src/components/Table/components/Rows/index.js'
import Cell from '/Users/admin/Documents/GitHub/Donutomat/src/components/Table/components/Cell/index.js'

const Body = ({data}) => {
    return (

<tbody className = "tbody">
      
      {
        data.map((dataItem, index) => (
          
         <Rows /> 
         <Cell />
                   
        ))
     
      }
     
</tbody>

    )}

    export default Body
>>>>>>> parent of 949bc23 (Rows/Cell)
