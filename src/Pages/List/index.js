import React, { useEffect, useState } from 'react';
import Table from '../../components/Table';
import MarkAsDone from '../../components/MarkAsDone';
import axios from 'axios';
import datatypes from '../../components/Table/datatypes';


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
        label: 'Date of adding',
        type: datatypes.date
    },
    {
        name: 'datedonut',
        label: 'Donuts date',
        type: datatypes.date
    },
    {
        name: 'donutiondone',
        label: 'Is it done?',
        accessor: (row) => <MarkAsDone data={row} />
    }
];

const List = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const result = await axios(
                '/api/donutors',
            );
            setData(result.data);
        }
        fetchData();
    }, []);
    return (
        <Table data={data} columns={columnsDef} />
    )
}

export default List
