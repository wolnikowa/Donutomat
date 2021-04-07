import React from 'react';
import DonutForm from '../DonutForm';
import Table from '../Table';
import './main.scss';


const data = [
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

const columnsDef = [
    {
        name: 'name',
        label: 'Name'
    },
    {
        name: 'addedby',
        label: 'Added by'
    },
    {
        name: 'dateadd',
        label: 'Date of adding'
    },
    {
        name: 'datedonut',
        label: 'Donuts date'
    }
]

const Main = () => (

   

    <div>
        <Table data ={data} columns={columnsDef} />
        <DonutForm />
        
    </div>
)

export default Main