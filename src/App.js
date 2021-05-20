import React from 'react';
import Header from './components/header/Header';
import Nav from './components/nav/Nav';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import List from './Pages/List';
import Dishonorable from './Pages/Dishonorable';
import 'core-js/stable';
import 'regenerator-runtime/runtime';
require("babel-core/register");
require("babel-polyfill");



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
                    <Add />
                </Route>
                <Route path="/Dishonorable-donutors">
                    <Dishonorable />
                </Route>
            </Switch>
        </div>
    </Router>
)

export default App
