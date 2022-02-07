from selenium.webdriver import Chrome
from Pages.Data import Login, Filter, SeeCart, Checkout, Final
import time

browser = Chrome()
inicio = Login(browser)
inicio.signin()

# --- Para melhor visualização das landing pages:
time.sleep(3)

ordenar = Filter(browser)
ordenar.filtro()

time.sleep(3)

ordenar.addcarrinho()

time.sleep(3)

carrinho = SeeCart(browser)
carrinho.cart()

time.sleep(3)

confirma = Checkout(browser)
confirma.info()

time.sleep(3)

saida = Final(browser)
saida.complete()


print('Compras realizadas com sucesso!')

