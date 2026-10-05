def order(e):
    BeefUdon_price = 240
    CurryUdon_price = 290
    KakeUdon_price = 125

    ordered_beefudon = float(document.getElementById("beefudon").checked)
    ordered_curryudon = float(document.getElementById("curryudon").checked)
    ordered_kakeudon = float(document.getElementById("kakeudon").checked)

    subtotal = ((ordered_beefudon * BeefUdon_price) + (ordered_curryudon * CurryUdon_price) + (ordered_kakeudon * KakeUdon_price))

    vat = subtotal * 0.12

    total = subtotal + vat

    document.getElementById("subtotal").innerText = f"₱{subtotal:.2f}"
    document.getElementById("vat").innerText = f"₱{vat:.2f}"
    document.getElementById("total").innerText = f"₱{total:.2f}"


def generate_sku(e):
    document.getElementById("div_id").innerHTML = " "

    category_var = document.getElementById("category").value
    productname_var = document.getElementById("pname").value
    stock_qty = document.getElementById("qty").value

    SKU_name = (
        category_var[:3].upper()
        + "-"
        + productname_var[:4].upper()
        + "-"
        + str(stock_qty)
    )
    display("SKU: " + SKU_name, target="div_id")