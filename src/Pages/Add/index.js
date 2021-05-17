import React,{useCallback} from 'react';
import DonutForm from '../../components/DonutForm';
const axios=require('axios')
const Add = () => {
    const onSubmit = useCallback((form) => {
        axios.post('/api/donutors',{
            id:form.id,
            name:form.donutorName,
            dateadd:new Date(form.donutDate).toISOString(),
            datedonut:new Date(new Date(form.donutDate).getDate()+7).toISOString(), //?
            addedby: "Ryszard Jakielski"
        }
        ).then((response)=> console.log(response))
        .then(()=>window.location.replace("/"))
        .catch((err)=>console.log(new Error(err)))
    }, []);

    return (
        <DonutForm onSubmit={onSubmit} />
    )
}

export default Add