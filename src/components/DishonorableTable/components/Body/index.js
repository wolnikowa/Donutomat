import React from 'react';

const donutors = [
    {
     id: '1',
     name:'Julia Bessman',
     addedby: 'Ryszard Jakielski',
     dateadd: '20-03-2021',
     datedonut: '21-03-2021',
     lateness: '5'
    },
    {
        id: '2',
        name:'Alicja Kempa',
        addedby: 'Ryszard Jakielski',
        dateadd: '20-03-2021',
        datedonut: '21-03-2021',
        lateness: '2'
    },
    {
        id: '3',
        name:'Wiktoria Wolnik',
        addedby:'Ryszard Jakielski',
        dateadd:'20-03-2021',
        datedonut: '21-03-2021',
        lateness: '36'
    }
  ]



const BodyD = () => {
    return (

<tbody>
                    {
                      donutors.map((donutors, index) => {
                          const { id,name,addedby, dateadd,  datedonut, lateness } = donutors 
                          return (
                           
                              <tr key={id} className>
                            
                                <td>{name}</td>
                                <td>{addedby}</td>
                                <td>{dateadd}</td>
                                <td>{datedonut}</td>
                                <td>{lateness}</td>
                               </tr>
                          
                      )}
                      )}
                 </tbody>
    )}


    export default BodyD