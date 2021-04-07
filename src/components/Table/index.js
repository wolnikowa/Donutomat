
import React from 'react';
import './table.scss';
import Header from './components/Header/index.js';
import Body from './components/Body/index.js';
  

  const Table = () => {
        return (
           <div>
              
              <table>
              <Header />
              <Body array = "[
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
  ]" />
              </table>
           </div>
        )
     }
  
  export default Table