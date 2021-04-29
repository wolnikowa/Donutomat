import React from 'react';
import Header from './components/header/Header';
import Nav from './components/nav/Nav';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import DonutForm from './components/DonutForm';
import List from './Pages/List'


const App = () => (
    <Router >
        <div>
            <Header />
            <Nav />
            <Switch>
                <Route exact path="/">
                    <List />
                </Route>
                <Route path="/Form">
                    <DonutForm />
                </Route>
            </Switch>
        </div>
    </Router>
)

export default App
