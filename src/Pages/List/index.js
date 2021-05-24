import React, { useEffect, useState } from 'react';
import Table from '../../components/Table';
import MarkAsDone from '../../components/MarkAsDone';
import axios from 'axios';

/*const data = [
    {
        id: '1',
        name: 'Julia Bessman',
        addedby: 'Ryszard Jakielski',
        dateadd: '20-03-2021',
        datedonut: '21-03-2021'
    },
    {
        id: '2',
        name: 'Alicja Kempa',
        addedby: 'Ryszard Jakielski',
        dateadd: '20-03-2021',
        datedonut: '21-03-2021'
    },
    {
        id: '3',
        name: 'Wiktoria Wolnik',
        addedby: 'Ryszard Jakielski',
        dateadd: '20-03-2021',
        datedonut: '21-03-2021'
    }
]
*/

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
    },
    {
        name: 'donutiondone',
        label: 'Is it done?',
        accessor: (row) => <MarkAsDone data={row} />
    }
];

const List = () => {
    const[data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const result = await axios(
                '/api/donutors',
            );
            setData(result.data);
        }
        fetchData();
    });
    return (
        <Table data={data} columns={columnsDef} />
    )
}

export default List
