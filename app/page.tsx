// pages/index.tsx
"use client"

import React, {FormEvent, useState } from 'react'
import DealAllocatorForm from '@/app/components/DealAllocatorForm'
import DealResults from '@/app/components/DealResults'
import {Investor, Deal, defaultDeal } from '@/app/lib/definitions'

const HomePage: React.FC = () => {
  const [investorData, setInvestorData] = useState<Investor[]>([
    { name: '', requested_amount: '', average_amount: '' },
    { name: '', requested_amount: '', average_amount: '' }
  ]);
  const [deal, setDeal] = useState<Deal>(defaultDeal);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()

    const allocationInput = document.querySelector('#allocation') as HTMLInputElement;
    const allocation = allocationInput.value

    const dealRequest = {
      allocation_amount: allocation,
      investor_amounts: investorData
    }

    const response = await fetch('/api/prorate', {
      method: 'POST',
      body: JSON.stringify(dealRequest),
    })

    if (!response.ok) {
      setError(response.body ? response.body.toString() : 'An error occurred')
    } else {
      setError(null)
    }

    // Handle response if necessary
    const deal: Deal = await response.json()
    setDeal(deal)
  }

  return (
    <main className="flex min-h-screen flex-col grid grid-cols-3 items-left justify-between p-24">
      <div className="col-span-2 pr-6">
        <h1 className="text-2xl font-bold text-left">Deal Allocator</h1>
        <DealAllocatorForm onSubmit={handleSubmit} investorData={investorData} setInvestorData={setInvestorData} />
      </div>
      <div className="col-span-1 pl-12">
        <h1 className="text-2xl font-bold text-left">Deal Results</h1>
        <DealResults dealData={deal} error={error}/>
      </div>
    </main>
  )
}

export default HomePage
