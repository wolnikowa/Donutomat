import React from 'react';
import './header.scss';
import jitLogo from "./../../assets/logoBiale.png";


class Header extends React.Component{
    render(){
        return(
            <div className='header'>
                <div className='images'>
                    <img src={jitLogo} />
                    <img src="" />
                </div>
            </div>
        )
    }
}
export default Header