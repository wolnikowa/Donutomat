const bodyParser = require("body-parser");

let donutorsList = [
  {
    id: 1,
    name:'Julia Bessman',
    addedby: 'Ryszard Jakielski',
    dateadd: '20-03-2021',
    datedonut: '27-03-2021'
   },
   {
       id: 2,
       name:'Alicja Kempa',
       addedby: 'Ryszard Jakielski',
       dateadd: '06-06-2021',
       datedonut: '13-06-2021'
   },
   {
       id: 3,
       name:'Wiktoria Wolnik',
       addedby:'Ryszard Jakielski',
       dateadd:'04-06-2021',
       datedonut: '11-06-2021'
   },
   {
    id: 4,
    name:'Łukasz Drzewiecki',
    addedby:'Ryszard Jakielski',
    dateadd:'08-04-2021',
    datedonut: '15-04-2021'
}
]


const api = (app, server, compiler) => {
  app.use(bodyParser.urlencoded({ extended: true }));
  app.use(bodyParser.json());

  app.post('/api/donutors', (req, res) => {
    const maxId = donutorsList.reduce((highest, current) => current.id > highest ? current.id : highest, 0);
    donutorsList = [...donutorsList, {...req.body, id: maxId + 1}];
    res.json(donutorsList);
  });

  app.put('/api/donutors/:id', (req, res) => {
    const { params: { id }, body } = req;

    if(!id || !body) {
      return donutorsList;
    }

    const index = donutorsList.findIndex((donutor) => donutor.id === id);

    if (index > -1) {
      donutorsList[index] = {
        ...body,
        id
      }
    }

    res.json(donutorsList);
  });

  app.get('/api/donutors', (req, res) => {
    res.json(donutorsList);
  });
}

module.exports = {
  api
}
