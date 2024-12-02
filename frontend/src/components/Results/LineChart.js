import React from 'react';
import PropTypes from 'prop-types';

const LineChart = ({ data }) => {
    if (!data || !data.imageUrl) {
        return <p>No data available for the line chart.</p>;
    }

    return (
        <div className="line-chart-container">
            <h4>Line Chart</h4>
            <img
                src={data.imageUrl}
                alt="Line Chart"
                className="chart-image"
                style={{ maxWidth: '100%' }}
            />
            {data.description && <p className="chart-description">{data.description}</p>}
        </div>
    );
};

LineChart.propTypes = {
    data: PropTypes.shape({
        imageUrl: PropTypes.string.isRequired,
        description: PropTypes.string,
    }),
};

LineChart.defaultProps = {
    data: {
        description: '',
    },
};

export default LineChart;
