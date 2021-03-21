import React from 'react';
import './header.scss';
import jitLogo from "./../../assets/logoBiale.png";
import jitName from "./../../assets/name.png";


class Header extends React.Component{
    render(){
        return(
            <div className='header'>
                <div className='images'>
                    <img src={jitLogo} />
                    <div>
                        <span>D</span>
                        <span className='yellow'>o</span>
                        <span>nuts</span>
                    </div>
                </div>
            </div>
        )
    }
}
export default Header