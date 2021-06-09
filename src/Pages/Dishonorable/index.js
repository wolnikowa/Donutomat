import React, { useEffect, useState } from 'react';
import Table from '../../components/Table';
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
        name: 'lateness',
        label: 'Days of late',

    }
];
const TODAY = new Date();
const Dishonorable = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const result = await axios(
                '/api/donutors',
            );
            let dishonorableData = result.data.filter(x => new Date(x.datedonut) < TODAY)
            setData(dishonorableData);
            console.log(dishonorableData)
        }
        fetchData();
    }, []);
    return (
        <Table data={data} columns={columnsDef} />
    )
}

export default Dishonorable