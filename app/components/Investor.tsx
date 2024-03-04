import React, { Dispatch, SetStateAction } from 'react'
import { Investor } from './../lib/definitions'

interface InvestorFormProps {
  investorData: Investor[]
  setInvestorData: Dispatch<SetStateAction<Investor[]>>
}

const Investors: React.FC<InvestorFormProps> = ({ investorData, setInvestorData }) => {
  const handleInputChange = (index: number, field: keyof Investor, value: string) => {
    const newInvestors = [...investorData]
    newInvestors[index][field] = value
    setInvestorData(newInvestors)
  };

  const handleAddInvestor = () => {
    const newInvestors = [...investorData, { name: '', requested_amount: '', average_amount: '' }];
    setInvestorData(newInvestors);
  };

  const handleRemoveInvestor = (index: number) => {
    const newInvestors = [...investorData];
    newInvestors.splice(index, 1); // Remove the investor at the specified index
    setInvestorData(newInvestors);
  };

  return (
    <div className="pt-10">
      <div className="mb-4">
        <div className="grid grid-cols-10 gap-2">
          <label className="block text-sm font-medium leading-6 pt-6 col-span-4">Investor Name</label>
          <label className="block text-sm font-medium leading-6 pt-6 col-span-2">Allocation Request</label>
          <label className="block text-sm font-medium leading-6 pt-6 col-span-2">Average Amount</label>
          <label className="block text-sm font-medium leading-6 pt-6 col-span-2"></label>
        </div>
      </div>
      {investorData.map((investor, index) => (
        <div key={index} className="mb-4">
          <div className="grid grid-cols-10 gap-2">
            <input
              type="text"
              placeholder="Name"
              value={investor.name}
              onChange={(e) => handleInputChange(index, 'name', e.target.value)}
              className="border border-gray-300 px-3 py-2 mr-2 col-span-4"
              required
            />
            <input
              type="number"
              placeholder="Requested"
              value={investor.requested_amount}
              onChange={(e) => handleInputChange(index, 'requested_amount', e.target.value)}
              className="border border-gray-300 px-3 py-2 mr-2 col-span-2"
              required
            />
            <input
              type="number"
              placeholder="Average"
              value={investor.average_amount}
              onChange={(e) => handleInputChange(index, 'average_amount', e.target.value)}
              className="border border-gray-300 px-3 py-2 mr-2 col-span-2"
              required
            />
            <button onClick={() => handleRemoveInvestor(index)} className="ml-2 p-2 col-span-1 rounded-full bg-red-500 text-white hover:bg-red-600 focus:outline-none focus:bg-red-600">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
          </div>
        </div>
      ))}
      <button onClick={handleAddInvestor} className="bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 rounded mt-4">
        Add Investor
      </button>
    </div>
  )
}

export default Investors
