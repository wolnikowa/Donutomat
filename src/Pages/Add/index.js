import React,{useCallback} from 'react';
import { useHistory } from 'react-router-dom';
import DonutForm from '../../components/DonutForm';
import axios from 'axios'
const Add = () => {
    let history = useHistory();
    const onSubmit = useCallback((form) => {
        let a=new Date(form.donutDate)
        a.setDate(a.getDate()+7)
        axios.post('/api/donutors',{
            id:form.id,
            name:form.donutorName,
            dateadd:new Date(form.donutDate).toISOString(),
            datedonut:a.toISOString(),
            addedby: "Ryszard Jakielski"
        }
        )
        .then((val)=>console.log(val.data))
        .then(()=>history.push("/"))
        .catch((err)=>console.log(new Error(err)))
    }, []);

    return (
        <DonutForm onSubmit={onSubmit} />
    )
}

export default Add