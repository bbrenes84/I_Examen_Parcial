def calcular_descuento(precio):
    if precio > 500:
        descuento = precio * 0.10
        precio_descuento = precio - descuento
        return precio_descuento
    else:
        return precio
precio_original = 600
precio_descuento = calcular_descuento(precio_original)
print(f"el precio original {precio_original}")
print(f"el precio con descuento {precio_descuento}")
