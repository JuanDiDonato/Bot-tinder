# -*- coding: utf-8 -*-

# Time
import time

# Elements HTML
from src.elements_html import ElementsHtml

# Script
class TinderBot(ElementsHtml):

    # Acepta las cookies de la pagina para evitar problemas
    def AcceptCookies(self):
        time.sleep(3)
        cookies_btn = self.get_cookies_btn()
        cookies_btn.click()

    # Login en Tinder
    def Login(self):

        print('[+] Iniciando proceso de login')

        # Obtiene el boton login y hace click
        time.sleep(3)
        login_btn = self.get_login_btn()
        login_btn.click()
        
        # Obtiene el boton para loguear con el num de cel y hace click
        time.sleep(3)
        cel_btn = self.get_cel_btn()
        cel_btn.click()

    # Ingresa el num cel 
    def Authentication(self):

        time.sleep(10)
        print(self.send_keys_to_cel_input())  # Ingresa numero de telefono

    # Obtiene los input para la carga del sms
    def ConfirmSmsCode(self):

        self.step = 'sms'
        # Codigo sms
        sms_code = input('Ingrese su codigo sms: ')
        self.get_sms_verification_inputs(sms_code)

    # Obtiene los input para la carga del email
    def ConfirmEmailCode(self):

        time.sleep(3)
        self.step = 'email'
        # Codigo email
        email_code = input('Ingrese su codigo email: ')
        self.get_email_verification_inputs(email_code)

    # Da acceso a la ubicacion
    def AllowLocation(self):
        
        time.sleep(3)
        location_btn = self.get_location_btn()
        location_btn.click()

    # Rechaza las notificaciones
    def DenyNotifications(self):

        time.sleep(3)
        deny_notifications_btn = self.get_deny_notifications_btn()
        deny_notifications_btn.click()

    # Like a los perfiles
    def Like(self):

        time.sleep(3)
        like_btn = self.get_like_btn()
        
        while True:
            try:
                like_btn.click()
                time.sleep(3)
            except:
                self.deny_shortcut()


    # Inicia el script
    def Start(self):
        self.AcceptCookies()
        self.Login()
        self.Authentication()
        self.ConfirmSmsCode()
        self.ConfirmEmailCode()
        self.AllowLocation()
        self.DenyNotifications()
        self.Like()


bot = TinderBot()
bot.Start()


