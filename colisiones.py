from math import sqrt

def detectar_colision(rec_1,rec_2):
    """detecta si hay colision entre dos rectangulos

    Args:
        rec_1 (_type_): _description_
        rec_2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    distacia = distancia_centros_rec(rec_1,rec_2)

    radio1 = calcular_radio_rectangulo(rec_1)
    radio2 = calcular_radio_rectangulo(rec_2)

    return distacia <= (radio1 + radio2) #hubo colision

def distancia_entre_puntos(punto_1,punto_2):
    """cula la distancia entre dos puntos

    Args:
        punto_1 : punto 1 a calcular
        punto_2 : punto 2 a calcular

    Returns:
        None
    """
    x1 , y1 = punto_1
    x2 ,y2 = punto_2

    return sqrt((y1 - y2) ** 2 + (x1 - x2) ** 2)

def distancia_centros_rec(rec_1,rec_2):
    return distancia_entre_puntos(rec_1.center,rec_2.center)

def calcular_radio_rectangulo(rect):
    """calcula el randio de un rectangulo

    Args:
        rect : rectangulo a calcularle el radio

    Returns:
        None
    """
    return rect.width //2 

