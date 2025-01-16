from empresa import Empresa
from empleado import Empleado

empresa_1 = Empresa("Prisma")

empresa_1.contratar_empleado("Matias","IT")
empresa_1.contratar_empleado("Lucas","IT")
empresa_1.contratar_empleado("Juan","IT")
empresa_1.contratar_empleado("Marcos","SEGURIDAD")
empresa_1.contratar_empleado("Marta","SEGURIDAD")
empresa_1.contratar_empleado("Benja","SEGURIDAD")

print ("Total de empleados :", Empleado.obtener_total_empleados())
print ("Numero de empleados en depto :",empresa_1.obtener_numero_empleados_por_departamento("SEGURIDAD"))
print (empresa_1.obtener_total_empleados())
