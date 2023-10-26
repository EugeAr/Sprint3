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
        driver.find_element(By.ID, registro.txt_email_id).send_keys('eugetmarbelo@gmail.com')
        driver.find_element(By.ID, registro.txt_password_id).send_keys('Arbelo123.')
        ingresar = driver.find_element(By.XPATH, registro.btn_ingresar_xpath)
        ingresar.click()
        time.sleep(2)
        #Validacion de la pantalla "Mi Cuenta"
        titulo_pag = driver.title
        self.assertEqual("Mi Cuenta", titulo_pag, "La pantalla no es la que corresponde")
        
    def test_1076(self):
        driver = self.driver
        driver.get('https://bensimon.com.ar/customer/account/login/')
        time.sleep(3) 
        pop_up = driver.find_element(By.ID, registro.btn_popup_id)
        pop_up.click()
        time.sleep(2)
        driver.find_element(By.ID, registro.txt_email_id).send_keys('eugetmarbelo@gmail.com')
        driver.find_element(By.ID, registro.txt_password_id).send_keys('Arbelo123.')
        ingresar = driver.find_element(By.XPATH, registro.btn_ingresar_xpath)
        ingresar.click()
        time.sleep(2)
        buscador = driver.find_element(By.XPATH, busqueda.dpd_search_xpath).send_keys('llaveros')
        Lupa_buscador = driver.find_element(By.XPATH, busqueda.btn_search_xpath)
        Lupa_buscador.click()
        titulo_pag = driver.title
        self.assertEqual(busqueda.txt_busqueda, titulo_pag, "No coincide con la búsqueda efectuada")
        time.sleep(3)
    
    def test_1086(self):
        driver = self.driver
        driver.get('https://bensimon.com.ar/customer/account/login/')
        time.sleep(3) 
        pop_up = driver.find_element(By.ID, registro.btn_popup_id)
        pop_up.click()
        time.sleep(2)
        driver.find_element(By.ID, registro.txt_email_id).send_keys('eugetmarbelo@gmail.com')
        driver.find_element(By.ID, registro.txt_password_id).send_keys('Arbelo123.')
        ingresar = driver.find_element(By.XPATH, registro.btn_ingresar_xpath)
        ingresar.click()
        time.sleep(2)
        buscador = driver.find_element(By.XPATH, busqueda.dpd_search_xpath).send_keys('llaveros')
        Lupa_buscador = driver.find_element(By.XPATH, busqueda.btn_search_xpath)
        Lupa_buscador.click()
        titulo_pag = driver.title
        self.assertEqual(busqueda.txt_busqueda, titulo_pag, "No coincide con la búsqueda efectuada")
        time.sleep(3)
        llavero = driver.find_element(By.LINK_TEXT, busqueda.txt_busqueda_link_text).click()
        time.sleep(3)       
        talle = driver.find_element(By.ID, producto1_carrito.btn_talle_id).click()
        time.sleep(3)
        boton_comprar = driver.find_element(By.ID, producto1_carrito.btn_comprar_id)
        boton_comprar.click()
        wait = WebDriverWait(driver, 10)
        mensaje_esperado = producto1_carrito.txt_compra
        leyenda_compra = wait.until(EC.presence_of_element_located((By.XPATH, producto1_carrito.txt_compra_xpath ))).text
        self.assertEqual(mensaje_esperado, leyenda_compra, "El mensaje de compra no coincide")
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
