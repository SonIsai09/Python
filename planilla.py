class Planilla:
    def __init__(self, codEmpleado, Nombre, Apellido, Cargo, Correo, Direccion, Salario):
        self.codEmpleado = codEmpleado
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Cargo = Cargo
        self.Correo = Correo
        self.Direccion = Direccion
        self.Salario = Salario

    def toDBCollection(self):  
        return{
            'codEmpleado': self.codEmpleado,
            'Nombre': self.Nombre,
            'Apellido': self.Apellido,
            'Cargo': self.Cargo,
            'Correo': self.Correo,
            'Direccion': self.Direccion,
            'Salario': self.Salario
        }