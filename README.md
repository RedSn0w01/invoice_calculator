# from invoice_calculator import calculate_invoice

HT = 250
invoice_details = ttc_calculate(HT)
for key, value in invoice_details.items():
    print(f"{key} : {value:.2f} DH")
