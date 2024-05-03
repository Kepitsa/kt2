import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера и сервиса
service = ChromeService()
driver = webdriver.Chrome(service=service)

# Добавление товара в корзину
def add_to_cart():
    driver.get("https://demo-opencart.ru/index.php?route=product/product&product_id=43")
    buy_button = driver.find_element(By.ID, "button-cart")
    buy_button.click()
    time.sleep(5)
    buy_message = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")
    if "Apple Cinema 30 добавлен в корзину покупок!" in buy_message.text:
        print("Товар добавлен в корзину")
        cart_button = driver.find_element(By.CSS_SELECTOR, "#cart-total")
        cart_button.click()
        in_cart = driver.find_element(By.CSS_SELECTOR, "div.container div.row div.col-sm-3 div.btn-group.btn-block.open ul.dropdown-menu.pull-right li:nth-child(2) div:nth-child(1) p.text-right a:nth-child(1) > strong:nth-child(1)")
        in_cart.click()
        driver.get("https://demo-opencart.ru/index.php?route=checkout/cart")
        cross_button_cart = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.table-responsive table.table.table-bordered tr:nth-child(1) td.text-left:nth-child(4) div.input-group.btn-block span.input-group-btn > button.btn.btn-danger:nth-child(2)")
        cross_button_cart.click()
    time.sleep(1)

# Тестирование галереи изображений
def test_product_images():
    driver.get("https://demo-opencart.ru/index.php")
    search_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(2) div.product-thumb.transition div.image a:nth-child(1) > img.img-responsive")))
    search_icon.click()
    time.sleep(5)
    driver.get("https://demo-opencart.ru/index.php?route=product/product&product_id=43")
    search_image = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(1) div.col-sm-8 ul.thumbnails li:nth-child(1) a.thumbnail > img:nth-child(1)")))
    search_image.click()
    time.sleep(5)
    image_click = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body:nth-child(2) div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-image-holder.mfp-s-ready div.mfp-content:nth-child(1) div.mfp-figure figure:nth-child(2) > img.mfp-img:nth-child(1)")))
    image_click.click()
    next_image = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body:nth-child(2) div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-image-holder.mfp-s-ready > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close:nth-child(4)")))
    if search_image != next_image:
        search_cross = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-image-holder.mfp-s-ready div.mfp-figure > button.mfp-close:nth-child(1)")))
        time.sleep(1)
        search_cross.click()
        print("Изменилась")
    time.sleep(3)

# Проверка пустой категории
def check_empty_category():
    driver.get("https://demo-opencart.ru/index.php?route=checkout/cart")
    category_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) > a.dropdown-toggle")))
    category_button.click()
    category_button_choose = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) div.dropdown-menu div.dropdown-inner ul.list-unstyled li:nth-child(1) > a:nth-child(1)")))
    category_button_choose.click()
    time.sleep(1)
    driver.get("https://demo-opencart.ru/index.php?route=product/category&path=20_26")
    nothing_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body:nth-child(2) div.container:nth-child(4) div.row div.col-sm-9 > p:nth-child(2)")))
    if "Нет товаров." in nothing_message.text:
        print("Пройдено")
    time.sleep(1)

# Регистрация нового пользователя
def register_new_user():
    driver.get("https://demo-opencart.ru/index.php?route=account/register")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-firstname"))).send_keys("aboba")
    driver.find_element(By.CSS_SELECTOR, "#input-lastname").send_keys("aboba")
    driver.find_element(By.CSS_SELECTOR, "#input-email").send_keys("aboba@aboba.com")
    driver.find_element(By.CSS_SELECTOR, "#input-telephone").send_keys("46064")
    driver.find_element(By.CSS_SELECTOR, "#input-password").send_keys("aboba123")
    driver.find_element(By.CSS_SELECTOR, "#input-confirm").send_keys("aboba123")
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
    time.sleep(3)

# Поиск
def perform_search():
    driver.get("https://demo-opencart.ru/index.php")
    search_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "search")))
    search_input.send_keys("Canon EOS 5D")
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.btn-lg").click()
    time.sleep(2)

add_to_cart()
test_product_images()
check_empty_category()
register_new_user()
perform_search()

driver.quit()

