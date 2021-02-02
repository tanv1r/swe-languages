def calculate_bill_and_tip(bill, tip_percentage):
    tip = round(bill * tip_percentage/100.0, 2)
    total = round(bill + tip, 2)
    info = []
    info.append(total)
    info.append(tip)
    return info