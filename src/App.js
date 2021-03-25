import React from 'react';
import Header from './components/header/Header';
import Nav from './components/nav/Nav';
import Main from './components/main/Main';
import { BrowserRouter as Router,Route,Switch} from 'react-router-dom';
import DonutForm from './components/DonutForm';
import Table from './components/Table';
import './components/main/main.scss'

const App = () => (
    <Router >
        <div>
            <Header />
            <Nav />
            {/* <Main />  */}
            <Switch>
                <Route path="/Home">
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
