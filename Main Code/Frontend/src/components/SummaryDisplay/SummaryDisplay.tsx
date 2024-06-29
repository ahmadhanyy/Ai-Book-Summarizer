import React from 'react';
import './SummaryDisplay.scss';

interface SummaryDisplayProps {
  summary: string;
}

const SummaryDisplay: React.FC<SummaryDisplayProps> = ({ summary }) => {
  return (
    <div className="summary-display">
      <h2>Generated Summary</h2>
      <p dangerouslySetInnerHTML={{ __html: summary }} />
    </div>
  );
};

export default SummaryDisplay;