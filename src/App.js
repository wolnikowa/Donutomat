import React from 'react';
import Header from './components/header/Header';
import Nav from './components/nav/Nav';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import DonutForm from './components/DonutForm';
import Table from './components/Table';
import MarkAsDone from './components/MarkAsDone';

const data = [
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
]


const App = () => (
    <Router >
        <div>
            <Header />
            <Nav />
            <Switch>
                <Route exact path="/">
                    <Table data={data} columns={columnsDef} />
                </Route>
                <Route path="/Form">
                    <DonutForm />
                </Route>
            </Switch>
        </div>
    </Router>
)

export default App
