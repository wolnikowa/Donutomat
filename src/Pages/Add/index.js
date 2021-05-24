import React, { useCallback } from 'react';
import { useHistory } from 'react-router-dom';
import DonutForm from '../../components/DonutForm';
import axios from 'axios'
const Add = () => {
    let history = useHistory();
    const onSubmit = useCallback((form) => {
        let a = new Date(form.donutDate)
        axios.post('/api/donutors', {
            id: form.id,
            name: form.donutorName,
            dateadd: new Date().toISOString(),
            datedonut: a.toISOString(),
            addedby: "Ryszard Jakielski"
        }
        )
            .then(() => history.push("/"))
            .catch((err) => console.log(new Error(err)))
    }, []);

    return (
        <DonutForm onSubmit={onSubmit} />
    )
}

export default Add