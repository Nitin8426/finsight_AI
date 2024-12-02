import React from 'react';
import PropTypes from 'prop-types';

const PieChart = ({ data }) => {
    if (!data || data.length === 0) {
        return <p>No data available for the pie chart.</p>;
    }

    return (
        <div className="pie-chart-container">
            <h4>Pie Chart</h4>
            <img
                src={data.imageUrl}
                alt="Pie Chart"
                className="chart-image"
                style={{ maxWidth: '100%' }}
            />
            <p className="chart-description">{data.description}</p>
        </div>
    );
};

PieChart.propTypes = {
    data: PropTypes.shape({
        imageUrl: PropTypes.string.isRequired,
        description: PropTypes.string,
    }),
};

PieChart.defaultProps = {
    data: {
        description: '',
    },
};

export default PieChart;
