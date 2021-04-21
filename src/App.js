import React from 'react';
import Header from './components/header/Header';
import Nav from './components/nav/Nav';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import DonutForm from './components/DonutForm';
import Table from './components/Table';



    

const App = () => (
    <Router >
        <div>
            <Header />
            <Nav />
            <Switch>
                <Route exact path="/">
                    <Table />
                </Route>
                <Route path="/Form">
                    <div className='mainContainer'>
                        <DonutForm />
                    </div>
                </Route>
            </Switch>
        </div>
    </Router>
)

export default App
