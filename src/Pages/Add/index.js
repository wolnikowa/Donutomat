import React,{useCallback} from 'react';
import { useHistory } from 'react-router-dom';
import DonutForm from '../../components/DonutForm';
import axios from 'axios'
const Add = () => {
    let history = useHistory();
    const onSubmit = useCallback((form) => {
        axios.post('/api/donutors',{
            id:form.id,
            name:form.donutorName,
            dateadd:new Date(form.donutDate).toISOString(),
            datedonut:new Date(new Date(form.donutDate).getDate()+7).toISOString(), //?
            addedby: "Ryszard Jakielski"
        }
        )
        .then(()=>history.push("/"))
        .catch((err)=>console.log(new Error(err)))
    }, []);

    return (
        <DonutForm onSubmit={onSubmit} />
    )
}

export default Add