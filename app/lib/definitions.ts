export type InvestorAllocation = {
    name: string,
    investment: string
}

export type Deal = {
    deal: InvestorAllocation[]
}

export type Investor = {
    name: string,
    requested_amount: string,
    average_amount: string
}

export const defaultDeal: Deal = { deal: [{name: '', investment: ''}] }

