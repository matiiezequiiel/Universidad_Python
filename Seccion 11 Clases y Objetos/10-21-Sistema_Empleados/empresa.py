from empleado import Empleado
class Empresa:

    def __init__(self,nombre):
        self._nombre = nombre
        self.empleados = []
    
    def contratar_empleado(self,nombre,departamento):
        empleado = Empleado(nombre,departamento)
        self.empleados.append(empleado)
        
    def obtener_numero_empleados_por_departamento(self,departamento):
        contador_empleados = 0
        for empleado in self.empleados:
            if empleado.departamento == departamento:
                contador_empleados += 1
        return contador_empleados
    
    def obtener_total_empleados(self):
        print(f"\n Total de empleados de la empresa {self._nombre}")
        for empleado in self.empleados:
            print(f''' Empleado: {empleado.id}
            Nombre: {empleado.nombre}
            Departamento: {empleado.departamento}''')