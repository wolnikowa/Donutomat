
import './header.scss';
import React from 'react';


const Header = ({ columns }) => {
    return (
        <thead className="thead">
            <tr>
                {
                    columns.map((column) => (
                        <th>{column.label}</th>
                    ))
                }
            </tr>
        </thead>
    )
}
export default Header