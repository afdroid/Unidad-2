def utilidad_bruta(ventas_netas: float, costo_ventas: float) -> float:
    """Calcula la utilidad bruta, solicita ventas netas y costo de ventas. Retorna un flotante"""
    return ventas_netas - costo_ventas


def perdida_bruta(costo_ventaM: float, ventas_netas: float) -> float:
    """Calcula la perdida bruta, solicita costo de ventas y ventas netas. Retorna un flotante"""
    return costo_ventaM - ventas_netas