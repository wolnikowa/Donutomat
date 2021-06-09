import React, { useEffect, useState } from 'react';
import Table from '../../components/Table';
import axios from 'axios';

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
        name: 'lateness',
        label: 'Days of late',

    }
];
const TODAY=new Date();
const Dishonorable = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const result = await axios(
                '/api/donutors',
            );
            let dishonorableData=result.data.filter(x=>new Date(x.datedonut)<TODAY)
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