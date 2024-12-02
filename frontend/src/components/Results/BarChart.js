import React from 'react';
import PropTypes from 'prop-types';

const BarChart = ({ data }) => {
    if (!data || data.length === 0) {
        return <p>No data available for the bar chart.</p>;
    }

    return (
        <div className="bar-chart-container">
            <h4>Bar Chart</h4>
            <img
                src={data.imageUrl}
                alt="Bar Chart"
                className="chart-image"
                style={{ maxWidth: '100%' }}
            />
            <p className="chart-description">{data.description}</p>
        </div>
    );
};

BarChart.propTypes = {
    data: PropTypes.shape({
        imageUrl: PropTypes.string.isRequired,
        description: PropTypes.string,
    }),
};

BarChart.defaultProps = {
    data: {
        description: '',
    },
};

export default BarChart;
