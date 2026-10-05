
from datetime import datetime


class Vehiculo:
    """Clase base que representa un vehículo general de la flota."""

    _contador_vehiculos = 0 

    def __init__(self, marca: str, modelo: str, año: int, precio_base: float):
        """Inicializa las propiedades del vehículo y actualiza el contador de clase."""
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio_base = precio_base
        self._encendido = False  
        self._disponible = True  

        Vehiculo._contador_vehiculos += 1
        print(f"🚗 Vehículo registrado: {self.marca} {self.modelo} ({self.año})")

    def __del__(self):
        """Destructor que decrementa el contador de clase al dar de baja el vehículo."""
        Vehiculo._contador_vehiculos -= 1
        print(f"🗑️ {self.marca} {self.modelo} ha sido dado de baja.")
    @property
    def encendido(self) -> bool:
        """Devuelve el estado del motor (solo lectura)."""
        return self._encendido

    @property
    def disponible(self) -> bool:
        """Devuelve la disponibilidad del vehículo para alquilar (solo lectura)."""
        return self._disponible
    def encender(self):
        """Enciende el motor si está apagado."""
        if not self._encendido:
            self._encendido = True
            print(f"🔑 {self.marca} {self.modelo}: Motor encendido.")
        else:
            print(f"⚠️ {self.marca} {self.modelo}: El motor ya está encendido.")

    def apagar(self):
        """Apaga el motor si está encendido."""
        if self._encendido:
            self._encendido = False
            print(f"🔒 {self.marca} {self.modelo}: Motor apagado.")
        else:
            print(f"⚠️ {self.marca} {self.modelo}: El motor ya está apagado.")

    def calcular_alquiler(self, tiempo: float) -> float:
        """Método base para calcular costo de alquiler. Se redefinirá en las clases derivadas."""
        return self.precio_base * tiempo

    def mostrar_info(self):
        """Muestra la información general del vehículo."""
        estado_motor = "Encendido" if self._encendido else "Apagado"
        disponibilidad = "Disponible" if self._disponible else "Alquilado"
        print(
            f"Marca: {self.marca} | Modelo: {self.modelo} | Año: {self.año} | "
            f"Precio Base: ${self.precio_base:.2f} | Motor: {estado_motor} | Estado: {disponibilidad}"
        )

    def alquilar(self):
        """Marca el vehículo como no disponible si está disponible."""
        if not self._disponible:
            raise ValueError(f"El vehículo {self.marca} {self.modelo} ya está alquilado.")
        self._disponible = False
        print(f"🔑 {self.marca} {self.modelo} ha sido alquilado exitosamente.")

    def devolver(self):
        """Marca el vehículo como disponible si estaba alquilado."""
        if self._disponible:
            raise ValueError(f"El vehículo {self.marca} {self.modelo} no está alquilado actualmente.")
        self._disponible = True
        print(f"✅ {self.marca} {self.modelo} ha sido devuelto y está disponible.")
    @classmethod
    def total_vehiculos(cls) -> int:
        """Devuelve la cantidad total de vehículos activos en la flota."""
        return cls._contador_vehiculos

    @classmethod
    def crear_desde_diccionario(cls, datos: dict):
        """Crea una instancia de Vehiculo a partir de un diccionario de datos."""
        return cls(
            marca=datos["marca"],
            modelo=datos["modelo"],
            año=int(datos["año"]),
            precio_base=float(datos["precio_base"]),
        )

    @staticmethod
    def validar_año(año: int) -> bool:
        """Verifica que el año sea válido (mayor a 1900 y menor o igual al actual)."""
        año_actual = datetime.now().year
        return 1900 < año <= año_actual

    @staticmethod
    def validar_precio(precio: float) -> bool:
        """Verifica que el precio sea un número estrictamente positivo."""
        return precio > 0


class Coche(Vehiculo):
    """Clase derivada que representa un coche en la flota."""

    def __init__(self, marca: str, modelo: str, año: int, precio_base: float, num_puertas: int):
        """Inicializa el coche extendiendo el constructor de Vehiculo."""
        super().__init__(marca, modelo, año, precio_base)
        self.num_puertas = num_puertas

    def calcular_alquiler(self, dias: float) -> float:
        """Redefine el cálculo de alquiler cobrando por día con recargo por puertas."""
        return (self.precio_base * dias) + (self.num_puertas * 10)

    def mostrar_info(self):
        """Extiende el método de la clase base añadiendo el número de puertas."""
        super().mostrar_info()
        print(f" Puertas: {self.num_puertas}")

    def abrir_maletero(self):
        """Método específico de Coche."""
        print(f"🧳 {self.marca} {self.modelo}: Maletero abierto.")


class Moto(Vehiculo):
    """Clase derivada que representa una moto en la flota."""

    def __init__(self, marca: str, modelo: str, año: int, precio_base: float, cilindrada: int):
        """Inicializa la moto extendiendo el constructor de Vehiculo."""
        super().__init__(marca, modelo, año, precio_base)
        self.cilindrada = cilindrada

    def calcular_alquiler(self, horas: float) -> float:
        """Redefine el cálculo de alquiler cobrando por hora con recargo por cilindrada."""
        return (self.precio_base * horas) + (self.cilindrada * 0.5)

    def mostrar_info(self):
        """Extiende el método de la clase base añadiendo la cilindrada."""
        super().mostrar_info()
        print(f" Cilindrada: {self.cilindrada} cc")

    def hacer_caballito(self):
        """Método específico de Moto."""
        print(f"🏍️ {self.marca} {self.modelo}: ¡Haciendo caballito!")
