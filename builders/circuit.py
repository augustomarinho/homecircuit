import json

import yaml
import logging
from models.models import Circuit

class CircuitReader:
    'Classe responsavel por ler o arquivo homecircuit.yml e criar uma lista de circuitos'

    __logger = logging.getLogger(__name__)
    __circuits

    def __init__(self):
        try:
            stream = open('resources/homecircuit.yml', 'r')
            dictCircuits = list(yaml.load_all(stream))

            for dictCircuit in dictCircuits[0].get('circuits'):
                circuit = Circuit(title=dictCircuit['title'],
                                  short_description=dictCircuit['short-description'],
                                  gpio_mode=dictCircuit['gpio']['mode'],
                                  gpio_port=dictCircuit['gpio']['port'],
                                  gpio_value=dictCircuit['gpio']['value'])

            stream.close()
        except yaml.YAMLError as error:
            self.__logger.error('Erro ao ler arquivo yaml')
