def calculate_bill_and_tip(bill, tip_percentage):
    tip = bill * tip_percentage/100.0
    total = bill + tip
    info = []
    info.append(total)
    info.append(tip)
    return info