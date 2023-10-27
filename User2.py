from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Bensimon_Registro import *
import pytest

class sprint3_user2(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_1075(self):
        driver = self.driver
        driver.get('https://bensimon.com.ar/customer/account/login/')
        time.sleep(3)  
        pop_up = driver.find_element(By.ID, registro.btn_popup_id)
        pop_up.click()
        time.sleep(2)
        # Validación de visibilidad del textbox "Email"
        email_textbox = driver.find_element(By.ID, registro.txt_email_id)
        if email_textbox.is_displayed():
            print("El textbox -EMAIL- es visible")
        else:
            print("El textbox -EMAIL- no es visible")
        email_textbox.send_keys('eugetmarbelo@gmail.com')
        # Validación de visibilidad del textbox "contraseña"
        password_textbox = driver.find_element(By.ID, registro.txt_password_id)
        if password_textbox.is_displayed():
            print("El textbox -PASSWORD- es visible")
        else:
            print("El textbox -PASSWORD- no es visible")
        password_textbox.send_keys('Arbelo123.')
        #Validación de boton Ingresar
        boton_ingreso = driver.find_element(By.XPATH,'//*[@id="send2"]/span')
        if boton_ingreso.is_displayed():
            print("El botón -INGRESAR- es visible")
        else:
            print("El botón -INGRESAR- no es visible")
        ingresar = driver.find_element(By.XPATH, registro.btn_ingresar_xpath)
        ingresar.click()
        time.sleep(2)
        # Validación de visibilidad de la pantalla "Mi Cuenta"
        titulo_pag = driver.title
        self.assertEqual("Mi Cuenta", titulo_pag, "La pantalla no es la que corresponde")
        print("-SE MUESTRA PANTALLA MI CUENTA CORRECTAMENTE-")

    def test_1076(self):
        driver = self.driver
        driver.get('https://bensimon.com.ar/customer/account/login/')
        time.sleep(3) 
        pop_up = driver.find_element(By.ID, registro.btn_popup_id)
        pop_up.click()
        time.sleep(2)
        driver.find_element(By.ID, registro.txt_email_id).send_keys('eugetmarbelo@gmail.com')
        driver.find_element(By.ID, registro.txt_password_id).send_keys('Arbelo123.')
        boton_ingreso = driver.find_element(By.XPATH,'//*[@id="send2"]/span').click()
        time.sleep(2)
        #Validar visibilidad de la barra de búsqueda
        buscador = driver.find_element(By.XPATH, busqueda.dpd_search_xpath)
        if buscador.is_displayed():
            print("La barra de búsqueda es visible")
        else:
            print("La barra de búsqueda NO es visible")
        buscador.send_keys('llaveros')
        #Validar visibilidad del botón lupa
        lupa_buscador = driver.find_element(By.XPATH, busqueda.btn_search_xpath)
        if buscador.is_displayed():
            print("La Lupita es visible")
        else:
            print("La Lupita NO es visible")
        lupa_buscador.click()
        time.sleep(6)
        titulo_pag = driver.title
        self.assertEqual(busqueda.txt_busqueda, titulo_pag, "No coincide con la búsqueda efectuada")
        print("La pagina muestra variedad de llaveros")
        time.sleep(3)
        
    def test_1081(self):
        driver = self.driver
        driver.get('https://bensimon.com.ar/customer/account/login/')
        time.sleep(3) 
        pop_up = driver.find_element(By.ID, registro.btn_popup_id)
        pop_up.click()
        time.sleep(2)
        driver.find_element(By.ID, registro.txt_email_id).send_keys('eugetmarbelo@gmail.com')
        driver.find_element(By.ID, registro.txt_password_id).send_keys('Arbelo123.')
        boton_ingreso = driver.find_element(By.XPATH,'//*[@id="send2"]/span').click()
        time.sleep(2)
        buscador = driver.find_element(By.XPATH, busqueda.dpd_search_xpath).send_keys('llaveros')
        lupa_buscador = driver.find_element(By.XPATH, busqueda.btn_search_xpath)
        lupa_buscador.click()
        time.sleep(3)
        llavero = driver.find_element(By.LINK_TEXT, busqueda.txt_busqueda_link_text).click()
        time.sleep(3)       
        talle = driver.find_element(By.ID, producto1_carrito.btn_talle_id).click()
        time.sleep(3)
        #Validar visibilidad del botón comprar
        boton_comprar = driver.find_element(By.ID, producto1_carrito.btn_comprar_id)
        if boton_comprar.is_displayed():
            print("Botón comprar es visible")
        else:
            print("Botón comprar NO es visible")
        boton_comprar.click()
        wait = WebDriverWait(driver, 10)
        mensaje_esperado = producto1_carrito.txt_compra
        #Validacion de mensaje de carrito
        leyenda_compra = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="maincontent"]/div/div/div[1]/div[2]/div[2]/div/div/div')))
        if leyenda_compra.is_displayed():
            print("Agregaste LLAVERO PVC B NEGRO a tu carrito de compras")
        else:
            print("El producto no se agrego correctamente")
        carrito= driver.find_element(By.XPATH, producto1_carrito.btn_carrito_xpath)
        carrito.click()
        time.sleep(3)
        titulo_producto = wait.until(EC.presence_of_element_located((By.XPATH, producto1_carrito.txt_producto_carrito_xpath ))).text
        self.assertEqual(busqueda.txt_busqueda_link_text, titulo_producto, "El producto en carrito no coincide")
        ver_detalles = driver.find_element(By.XPATH, producto1_carrito.dpd_detalles_xpath ).click()
        time.sleep(3)


    def tearDown(self):
        self.driver.close()
 
if __name__ == '__main__':
    unittest.main()
