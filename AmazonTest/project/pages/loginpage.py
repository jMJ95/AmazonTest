"""RegistroPage """
import sys, os, time
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from project.locators.locators import Locators
from project.helpers import Helpers


class RegistroPage(Helpers):
    """Esta es la clase que contiene los elementos de la pagina de equipos de homepage"""

    def __init__(self, driver, test_name):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.test_name = test_name
        self.registro_btn = Locators.registro_btn
        self.input_in_reg = Locators.input_registro
        
    def click_registro_btn(self):
        """
        clickea el botón crea una cuenta de amazon.
        """
        registro_btn = self.driver.find_element(by=self.registro_btn[0], value=self.registro_btn[1])
        registro_btn.click()
        self.driver.save_screenshot('./evidencias/' + self.test_name + '/registro_btn_' +
        self.getdatetime() + '.png')

    def write_in_input_registro(self, nombre: str, correo: str, ctr: str):
        """
        llenar los datos de registro.
        """
        nombre = self.driver.find_element(by=self.input_in_reg[0], value=self.input_in_reg[1]%(nombre)) 
        correo = self.driver.find_element(by=self.input_in_reg[0], value=self.input_in_reg[1]%(correo))
        ctr = self.driver.find_element(by=self.input_in_reg[0], value=self.input_in_reg[1]%(ctr))