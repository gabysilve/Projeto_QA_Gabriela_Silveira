from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages import locators
from Pages import webdata


class Basecode():
    # para toda vez que um objeto novo for criado
    def __init__(self, driver):
        self.driver = driver

    #Clicar de acordo com o locator
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    #Digitar texto nos campos
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

class Login(Basecode):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(webdata.WebData.url_inicio)
        self.driver.maximize_window()

    def signin(self):
        self.enter_text(locators.Locators.username, webdata.WebData.username)
        self.enter_text(locators.Locators.password, webdata.WebData.password)
        self.click(locators.Locators.login)

class Filter(Basecode):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(webdata.WebData.url_display)

    def filtro(self):
        self.click(locators.Locators.filter)


    def addcarrinho(self):
        self.click(locators.Locators.onesie)
        self.click(locators.Locators.tshirt)

class SeeCart(Basecode):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(webdata.WebData.url_cart)

    def cart(self):
        self.click(locators.Locators.carrinho)
        self.click(locators.Locators.checkout)

class Checkout(Basecode):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(webdata.WebData.url_checkout_one)

    def info(self):
        self.enter_text(locators.Locators.firstname, webdata.WebData.firstname)
        self.enter_text(locators.Locators.lastname, webdata.WebData.lastname)
        self.enter_text(locators.Locators.postalcode, webdata.WebData.postalcode)
        self.click(locators.Locators.continue_button)

class Final(Basecode):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(webdata.WebData.url_checkout_two)

    def complete(self):
        self.click(locators.Locators.finish)


