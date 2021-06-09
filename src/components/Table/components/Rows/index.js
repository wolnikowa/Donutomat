import React from 'react';
import './style.scss';
import Cell from '../Cell'
import datatypes from '../../datatypes';
import { FormattedDate } from 'react-intl';

const getValueComponent = (dataToDisplay, type) => {
    switch (type) {
        case datatypes.date:
            return <FormattedDate value={dataToDisplay} />
        default:
            return dataToDisplay;
    }
}

const Rows = ({ dataItem, columns, a }) => {
    return (

        <tr className="rows">
            {
                columns.map((column) => {
                    const valueToDisplay = column.accessor ? column.accessor(dataItem) : dataItem[column.name];

                    return (
                        <Cell key={column.name}>
                            {
                                getValueComponent(valueToDisplay, column.type)
                            }
                        </Cell>
                    )
                })
            }
        </tr>
    );

}
export default Rows
