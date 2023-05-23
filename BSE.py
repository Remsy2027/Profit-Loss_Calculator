import tkinter as tk
from bsedata.bse import BSE

b = BSE()

# Stocks With Their Company Code
stocks = {
    "TATA_POWER": {
        "code": "500400",
        "price": 205,
        "quantity": 40
    },
    "TATA_MOTORS": {
        "code": "500570",
        "price": 524,
        "quantity": 15
    },
    "TATA_CONSULTANCY_SERVICES": {
        "code": "532540",
        "price": 3244,
        "quantity": 12
    },
    "Sona_BLW_Precision_Forgings": {
        "code": "543300",
        "price": 540,
        "quantity": 15
    },
    "HDFC_Bank": {
        "code": "500180",
        "price": 1648,
        "quantity": 19
    },
    "Aether_Industries": {
        "code": "543534",
        "price": 915,
        "quantity": 11
    },
    "Clean_Science_and_Technology": {
        "code": "543318",
        "price": 1495,
        "quantity": 6
    },
    "DYNEMIC_PRODUCTS": {
        "code": "532707",
        "price": 323,
        "quantity": 91
    },
    "Laxmi_Organic_Industries": {
        "code": "543277",
        "price": 275,
        "quantity": 75
    }
}

# Calculate the current invested amount
for stock, details in stocks.items():
    code = details["code"]
    quantity = details["quantity"]
    quote = b.getQuote(code)
    current_price = float(quote["currentValue"])
    invested_amount = current_price * quantity
    details["invested_amount"] = invested_amount

# Create the main window
window = tk.Tk()
window.title("Stock Information")

# Create labels for each stock
stock_labels = {}
row = 0
for stock, details in stocks.items():
    label = tk.Label(window, text=stock, font=("Arial", 12))
    label.grid(row=row, column=0, padx=10, pady=5)

    purchase_price = details["price"]
    current_price = float(quote["currentValue"])
    quantity = details["quantity"]
    invested_amount = details["invested_amount"]

    if current_price > purchase_price:
        profit = int((current_price - purchase_price) * quantity * 1.5)
        color = "green"
        status = f"Profit is {profit}"
    elif current_price == purchase_price:
        color = "black"
        status = "No Profit No Loss"
    else:
        loss = int((purchase_price - current_price) * quantity)
        color = "red"
        status = f"Loss is {loss}"

    value_label = tk.Label(window, text=status, font=("Arial", 12), fg=color)
    value_label.grid(row=row, column=1, padx=10, pady=5)

    stock_labels[stock] = value_label
    row += 1

# Calculate the total invested amount
total_invested_amount = sum(details["invested_amount"] for details in stocks.values())

# Start the Tkinter event loop
window.mainloop()
