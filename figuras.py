class Figuras:

    def cuadrado(self, lado):
        try:
            lado = float(lado)
            return lado * lado
        except Exception:
            return 'dato incorrecto'
