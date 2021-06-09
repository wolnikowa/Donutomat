import React from 'react';
import Header from './components/header/Header';
import Nav from './components/nav/Nav';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import List from './Pages/List';
import Dishonorable from './Pages/Dishonorable';
import Add from './Pages/Add';
import MyDonuts from './Pages/Scheduler';
import 'react-calendar/dist/Calendar.css';




const App = () => {
    return (
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
                    <Route path="/Calendar">
                    <MyDonuts />
                    </Route>

                     </Switch>
        </div>
    </Router>
)
}
export default App
