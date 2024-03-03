// components/DealAllocatorForm.tsx
'use client'

import React, { SetStateAction, Dispatch } from 'react'
import Investors from './Investor'
import { Investor } from './../lib/definitions'

interface DealAllocatorFormProps {
  onSubmit: (formData: any) => void;
  investorData: Investor[];
  setInvestorData: Dispatch<SetStateAction<Investor[]>>;
}

const DealAllocatorForm: React.FC<DealAllocatorFormProps> = ({ onSubmit, investorData, setInvestorData }) => {
  return (
    <form className="pt-8" onSubmit={onSubmit}>
      <label htmlFor="allocation" className="block text-sm font-medium leading-6 pt-6 text-gray-300">Total Allocation</label>
      <div className="relative mt-2 rounded-md shadow-sm">
        <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
          <span className="text-gray-500 sm:text-sm">$</span>
        </div>
        <input
          type="number"
          name="allocation_amount"
          id="allocation"
          className="block w-full rounded-md border-0 py-1.5 pl-7 pr-7 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
          placeholder="0.00"
        />
      </div>
      <Investors investorData={investorData} setInvestorData={setInvestorData} />
      <button
        type="submit"
        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 mt-6"
      >
        Submit
      </button>
    </form>
  )
}

export default DealAllocatorForm
