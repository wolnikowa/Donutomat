import React from 'react';
import './nav.scss';
import donut from "./../../assets/donut-2.png";

class Nav extends React.Component{
    render(){
        return(
            <div className='nav'>
                <div className='user'>
                    <img src={donut}/>
                    <p>Julia Bessman</p>
                </div>
                <div className='tabs'>
                    <ul>
                        <li><a href="#">List of donutors</a></li>
                        <li><a href="#">Add a new donutor</a></li>
                        <li><a href="#">Report a dishonorable donutor</a></li>
                        <li><a href="#">List of dishonorable donutors</a></li>
                        <li><a href="#">My calendar</a></li>
                    </ul>
                </div>
            </div>
        )
    }
}
export default Nav