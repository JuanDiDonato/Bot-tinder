# -*- coding: utf-8 -*-

# This get all elements html

# Time
import time

# Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Boton cookies
COOKIES_XPATH = '//*[@id="s-138260025"]/div/div[2]/div/div/div[1]/button'
# Boton login
LOGIN_XPATH = '//*[@id="s-138260025"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'
# Login con cel
CEL_XPATH = '//*[@id="s-1866641101"]/div/div/div[1]/div/div[3]/span/div[3]/button'
# Input para ingresar num. cel
CEL_INPUT_XPATH = '//*[@id="s-1866641101"]/div/div/div[1]/div[2]/div/input'
# Numero de cel
CEL_NUMBER = 'phone number'
# Inputs codigo sms
INP1_XPATH = '//*[@id="s-1866641101"]/div/div/div[1]/div[3]/input[1]'
INP2_XPATH = '//*[@id="s-1866641101"]/div/div/div[1]/div[3]/input[2]'
INP3_XPATH = '//*[@id="s-1866641101"]/div/div/div[1]/div[3]/input[3]'
INP4_XPATH = '//*[@id="s-1866641101"]/div/div/div[1]/div[3]/input[4]'
INP5_XPATH = '//*[@id="s-1866641101"]/div/div/div[1]/div[3]/input[5]'
INP6_XPATH = '//*[@id="s-1866641101"]/div/div/div[1]/div[3]/input[6]'
# Inputs codigo email
INP7_XPATH = '//*[@id="s-1866641101"]/div/div/div[1]/div[3]/input[1]' 
INP8_XPATH = '//*[@id="s-1866641101"]/div/div/div[1]/div[3]/input[2]'
INP9_XPATH = '//*[@id="s-1866641101"]/div/div/div[1]/div[3]/input[3]'
INP10_XPATH = '//*[@id="s-1866641101"]/div/div/div[1]/div[3]/input[4]'
INP11_XPATH = '//*[@id="s-1866641101"]/div/div/div[1]/div[3]/input[5]'
INP12_XPATH = '//*[@id="s-1866641101"]/div/div/div[1]/div[3]/input[6]'
# Boton de acceso a la ubicacion
LOCATION_XPATH = '//*[@id="s-1866641101"]/div/div/div/div/div[3]/button[1]'
# Boton para rechazar notificaciones
NOTIFICATIONS_XPATH = '//*[@id="s-1866641101"]/div/div/div/div/div[3]/button[2]'
# Boton like
LIKE_XPATH = '//*[@id="s-138260025"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button'
SHORTCUT_XPATH = '//*[@id="s-1866641101"]/div/div/div[2]/button[2]'

class ElementsHtml():

    def __init__(self):
        self.driver = webdriver.Chrome()  # Driver de Chrome
        self.driver.get('https://tinder.com/')  # Obtiene la url de Tinder
        self.step = None

    def get_cookies_btn(self):
        cookies_btn = self.driver.find_element(By.XPATH,COOKIES_XPATH)
        return cookies_btn

    def get_login_btn(self):
        return self.driver.find_element(By.XPATH,LOGIN_XPATH)
    
    def get_cel_btn(self):
        return self.driver.find_element(By.XPATH,CEL_XPATH)

    def get_cel_input(self):
        return self.driver.find_element(By.XPATH,CEL_INPUT_XPATH)

    def send_keys_to_cel_input(self):
        cel_input = self.get_cel_input()
        cel_input.send_keys(CEL_NUMBER, Keys.ENTER)
        return 'Numero celular cargado, rebice su telefono.'

    # Carga el codigo sms recibido
    def InsertCode(self,code):
        
        if self.step == 'sms':
            # Ingreso el codigo sms
            for i, caracter in enumerate(code):  # Enumerate crea una tupla de datos, primero el indice y luego el valor
                if i==0:
                    self.input1.send_keys(caracter)
                if i==1:
                    self.input2.send_keys(caracter)
                if i==2:
                    self.input3.send_keys(caracter)
                if i==3:
                    self.input4.send_keys(caracter)
                if i==4:
                    self.input5.send_keys(caracter)
                if i==5:
                    self.input6.send_keys(caracter,Keys.ENTER)
        else:
            # Ingreso el codigo email
            for i, caracter in enumerate(code): 
                if i==0:
                    self.input7.send_keys(caracter)
                if i==1:
                    self.input8.send_keys(caracter)
                if i==2:
                    self.input9.send_keys(caracter)
                if i==3:
                    self.input10.send_keys(caracter)
                if i==4:
                    self.input11.send_keys(caracter)
                if i==5:
                    self.input12.send_keys(caracter,Keys.ENTER)
    
    def get_sms_verification_inputs(self, sms_code):

        # Obtengo los input para ingresar el codigo sms
        self.input1 = self.driver.find_element(By.XPATH,INP1_XPATH)
        self.input2 = self.driver.find_element(By.XPATH,INP2_XPATH)
        self.input3 = self.driver.find_element(By.XPATH,INP3_XPATH)
        self.input4 = self.driver.find_element(By.XPATH,INP4_XPATH)
        self.input5 = self.driver.find_element(By.XPATH,INP5_XPATH)
        self.input6 = self.driver.find_element(By.XPATH,INP6_XPATH)

        # Cargo los datos
        self.InsertCode(sms_code)


    def get_email_verification_inputs(self,email_code):
        
        # Obtengo los input para ingresar el codigo de email
        self.input7 = self.driver.find_element(By.XPATH,INP7_XPATH)
        self.input8 = self.driver.find_element(By.XPATH,INP8_XPATH)
        self.input9 = self.driver.find_element(By.XPATH,INP9_XPATH)
        self.input10 = self.driver.find_element(By.XPATH,INP10_XPATH)
        self.input11 = self.driver.find_element(By.XPATH,INP11_XPATH)
        self.input12 = self.driver.find_element(By.XPATH,INP12_XPATH)

        self.InsertCode(email_code)
    
    def get_location_btn(self):
        return self.driver.find_element(By.XPATH,LOCATION_XPATH)

    def get_deny_notifications_btn(self): 
        return self.driver.find_element(By.XPATH,NOTIFICATIONS_XPATH)
    
    def get_like_btn(self):
        return self.driver.find_element(By.XPATH,LIKE_XPATH)

    def get_deny_shortcut_btn(self):
        return self.driver.find_element(By.XPATH,SHORTCUT_XPATH)

    # Like a los perfiles
    def like(self):

        time.sleep(3)
        like_btn = self.get_like_btn()
        
        while True:
            try:
                like_btn.click()
                time.sleep(2,5)
            except:
                self.deny_shortcut()

    def deny_shortcut(self):
        try:
            deny_shortcut_btn = self.get_deny_shortcut_btn()
            deny_shortcut_btn.click()
            self.like()
        except:
            print('No hay mas likes disponibles')
            