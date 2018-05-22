from .base import DictTransformer


class DSMTransformer(DictTransformer):
    FIELDS_MAPPING = {
        'Employee Internal ID': 'traveler_id',
        'Employee Name': 'traveler_name',
        'Org Unit 2 - Code': None,
        'Employee E-mail Address': 'traveler_email',
        'Spend Category Name': None,
        'Expense Type': 'expense_type',
        'Origin Destination City Pair': 'comment',
        'Vendor': 'vendor_name',
        'Transaction Date': 'transaction_datetime',
        'Expense Amount (reimbursement currency)': 'reimbursed_amount',
        'Reimbursement Currency': 'reimbursed_currency',
        'Expense Report ID': 'report_id',
        'Expense Report Name': 'report_name',
        'Expense Amount (transaction currency)': 'expensed_amount',
        'Transaction Currency': 'expensed_currency',
        'Approved Amount (rpt)': None,
        'Reporting Currency': None,
        'Approval Date': 'approved_datetime'
    }

    EXPENSE_TYPE_CONTAIN = {
        'Hotel': 'hotel',
        'Air': 'flight',
        'Car': 'car',
    }