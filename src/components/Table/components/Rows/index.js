import React from 'react';
import './style.scss';
import Cell from '../Cell'
import datatypes from '../../datatypes';
import { FormattedDate } from 'react-intl';

// const Rows = ({ dataItem, columns }) => {
//     return (
//         <tr className="rows">
//             {
//                 columns.map((column) => (
//                     <Cell key={column.name}>
//                         {column.accessor ? column.accessor(dataItem) : dataItem[column.name]}
//                     </Cell>
//                 ))
//             }
//         </tr>
//     );
// }

const Rows = ({ dataItem, columns, a }) => {
    return (

        <tr className="rows">
            {
                columns.map((column) => (
                    (column.type === datatypes.date) ?
                        (<Cell key={column.name}>
                            {(column.name === 'dateadd') ?
                                <FormattedDate values={new Date()} year='numeric' month='numeric' day='numeric' /> :
                                <FormattedDate values={new Date(a)} year='numeric' month='numeric' day='numeric' />}

                        </Cell>) : (
                            <Cell key={column.name}>
                                {column.accessor ? column.accessor(dataItem) : dataItem[column.name]}
                            </Cell>
                        )

                ))
            }

        </tr>
    );
}


export default Rows
