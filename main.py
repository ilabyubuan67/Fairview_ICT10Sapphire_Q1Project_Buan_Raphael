from pyscript import display, document

# receipt generator (from skills test)
def order(e):
    # prices (php)
    kakeudon_presyo = 140
    curryudon_presyo = 270
    beefudon_presyo = 235


    subtotal = (
        (kakeudon_presyo * 140) + (curryudon_presyo * 270) + (beefudon_presyo * 235)
    )


    vat = subtotal * 0.12

    # total
    total = subtotal + vat

   
    document.getElementById("subtotal").innerText = f"₱{subtotal}"
    document.getElementById("vat").innerText = f"₱{vat}"
    document.getElementById("total").innerText = f"₱{total}"



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

    display("SKU: ", SKU_name, target="div_id")