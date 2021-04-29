import React from 'react';
import './nav.scss';
import donut from "./../../assets/donut-2.png";
import { Link } from 'react-router-dom';

class Nav extends React.Component {
    render() {
        return (
            <div className='nav'>
                <div className='user'>
                    <img src={donut} />
                    <p>Julia Bessman</p>
                </div>
                <div className='tabs'>
                    <ul>
                        <li><Link to={'/'}>List of donutors</Link></li>
                        <li><Link to={'/Form'}>Add a new donutor</Link></li>
                        <li><Link to={'/Dishonorable-donutors'}>List of dishonorable donutors </Link></li>
                        <li><a href="/">My calendar</a></li>
                    </ul>
                </div>
            </div>
        )
    }
}
export default Nav