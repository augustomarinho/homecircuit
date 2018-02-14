class Circuit:
    'Classe que representa um mapeamento eletrico'


    def __init__(self, title, short_description, gpio_port, gpio_mode, gpio_value):
        self.__title = title
        self.__short_description = short_description
        self.__gpio_port = gpio_port
        self.__gpio_mode = gpio_mode
        self.__gpio_value = gpio_value

    def __str__(self) -> str:
        return super().__str__()
