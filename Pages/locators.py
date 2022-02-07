from selenium.webdriver.common.by import By

class Locators():
    # --- Login
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login = (By.NAME, "login-button")

    #  --- Filtro e carrinho
    filter = (By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select/option[3]')
    onesie = (By.NAME, "add-to-cart-sauce-labs-onesie")
    tshirt = (By.NAME,"add-to-cart-test.allthethings()-t-shirt-(red)")

    # --- Checkout
    carrinho = (By.XPATH,'//*[@id="shopping_cart_container"]/a')
    checkout = (By.ID, "checkout")

    # --- Informações para checkout
    firstname = (By.ID, "first-name")
    lastname = (By.ID, "last-name")
    postalcode = (By.ID, "postal-code")

    # --- Finalização da compra
    continue_button = (By.ID, "continue")
    finish = (By.ID, "finish")
