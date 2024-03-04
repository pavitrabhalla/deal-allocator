import React from 'react'
import { Deal, defaultDeal } from '../lib/definitions';

interface DealResultProps {
  dealData: Deal,
  error: string | null
}

const Results: React.FC<DealResultProps> = ({ dealData, error }) => {
  if (error) {
    return <div className="pt-12">Error: {error}</div>;
  }

  if (dealData == defaultDeal) {
    return <div className="pt-12">Waiting for inputs...</div>;
  }

  if (dealData.deal.length === 0) {
    return <div className="pt-12">No valid investors</div>;
  }

  return (
    <div className="pt-12">
      <table className="border-collapse border mt-4">
        <thead>
          <tr>
            <th className="border px-4 py-2">Name</th>
            <th className="border px-4 py-2">Allocated</th>
          </tr>
        </thead>
        <tbody>
          {dealData.deal.map((investorAllocation, index) => (
            <tr key={index}>
              <td className="border px-4 py-2">{investorAllocation.name}</td>
              <td className="border px-4 py-2">{investorAllocation.investment}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Results;
