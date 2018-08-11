datos={"cédula0":"208090159", "nombre0":"Esteban Murillo", "fecha de nacimiento0":"14/09/2000", "edad0":"17" ,"sexo0":"Masculino","residencia0":"San Carlos","Tipo de usuario0": "Admin", "Contraseña0":"Admin"}

def register():
    largo=len(datos)
    nume=largo/10

    for i in range(int(nume),1000):
        print("Registrese")
        print()
        num=str(i)
        cedula=input("ingrese su número de cédula, si ingresa una x para: ")
        if cedula!="x":
            nombre=input("ingrese su nombre completo: ")
            fechaNacimiento=input("ingrese su fecha de nacimiento(día/mes/año): ")
            edad=int(input("ingrese su edad: "))
            if edad<18:
                sexo=input("Ingrese su sexo(Masculino o Femenino): ")
                recidencia=input("ingrese su cantón de residencia, una vez ingrese al sistema vaya al apartado de provincias y agreguelo: ")
                tipoUsuario=input("ingrese su tipo de usurio(ciudadano, oficial u oficina): ")
                if tipoUsuario=="ciudadano" or tipoUsuario=="Ciudadano" or tipoUsuario=="oficial de tránsito" or tipoUsuario=="Oficial de tránsito"or tipoUsuario=="oficina del juzgado"or tipoUsuario=="Oficina del juzgado":
                    password=input("ingrese una contraseña: ")

                    datos["cédula"+num] = cedula
                    datos["nombre"+num] = nombre
                    datos["fecha de nacimiento"+num]=fechaNacimiento
                    datos["edad"+num] = edad
                    datos["sexo"+num] = sexo
                    datos["lugar de residencia"+num] = recidencia
                    datos["tipo de usuario"+num] = tipoUsuario
                    datos["contraseña"+num] = password

                login()

            else:
                print("usted es menor de edad, no puede ecceder a la plataforma")
                exit()

print(datos)

def login():
    registro=input("está registrado?(si o no): ")
    if registro=="si":
        cedula=input("ingrese su cédula: ")
        pasword=input("ingrese su contraseña: ")
        dd=list(datos.keys())[list(datos.values()).index(pasword)]
        jj=list(datos.keys())[list(datos.values()).index(cedula)]
        if dd in datos and jj in datos:
            hh=0
            for i in dd:
                hh=i

            usuario="tipo de usuario"+str(hh)
            if usuario == "ciudadano"or usuario=="Cuidadano":
                uu=persona()
                uu.ciudadano()

        else:
            print("Inte de nuevo, por favor")
            login()
    else:
        register()

def provincias():
    def menu():
        print()
        print("1. Ver las provincias y cantones")
        print("2. Ingresar una nueva provincia")
        print("3. Ingresar un nuevo cantón")
        print("4. Regresar al menú anterior")
        print()
        desicion=int(input("Ingrese su elección: "))
        if desicion==1:
            verprovincias()
        elif desicion==2:
            nuevaProvincia()
        elif desicion==3:
            nuevoCanton()

    class verprovincias():
        def __init__(self):
            self.alajuela=["Alajuela", "San Carlos", "Los Chiles"]
            self.heredia=["Heredia", "Flores"]
            self.sanJose=["San Pedro de Montes de Oca", "Desamparados"]

    class nuevaProvincia(verprovincias):
        prov=input("Ingrese el nombre de la provincia: ")
        provincias=[]
        provincia = []
        for u in range(0,10000):
            canton=input("Ingrese los cantones que desee, para parar ingrese una x: ")
            if canton=="x" or canton=="X":
                break
            else:
                provincia.append(canton)

    class nuevoCanton(verprovincias):
        print("Escoja una provincia")
        print(verprovincias)

class persona():
    def ciudadano(self):

        def menuciudadano():
            print("1. menú de vehículos")
            print("2. registrar accidente")
            print("3. salir")
            print()
            desicion=int(input("ingrese el numero de su elección: "))
            if desicion==1:
                crudVehiculos()
            elif desicion==2:
                eventociudadano()
            elif desicion==3:
                login()

        class crudVehiculos(persona):

            def __init__(self):
                self.vehiculos = []

            def ingresarVehi(self):

                for i in range(0,1000):
                    num=str(i)
                    cedula=int(input("Ingrese su cédula, si ingresa x cierra: "))
                    if cedula!="x":
                        placa= input("ingrese la placa del vehículo: ")
                        dic= {}
                        ano=int(input("Ingrese el año del carro: "))
                        marca= input("ingrese la marca del vehículo: ")
                        color=input("Ingrese el color de su carro: ")
                        tipo=input("Su carro es moto, automóvil, bus o camión")

                        if placa not in self.vehiculos:

                            dic["Cédula"+num]=cedula
                            dic["placa"+num]=placa
                            dic["Año"+num]=ano
                            dic["Marca"+num]=marca
                            dic["color"+num]=color
                            dic["tipo"+num]=tipo
                        self.vehiculos.append(dic)

                    else:
                        break

                    dd=list(datos.keys())[list(datos.values()).index(cedula)]
                    hh="0"
                    for i in dd:
                        hh=i
                    datos["vehiculo"+str(hh)]=self.vehiculos


            def vervehiculo(self):

                placa=int(input("Ingrese la placa del vehículo que desea ver: "))

                for i in self.vehiculos:
                    if placa in self.vehiculos:
                        resultado=self.vehiculos
                        print(placa,",", resultado )

            def menuVehiculos(self):
                print()
                print("1. ingresar un nuevo vehiculo")
                print("2. ver un vehiculo en especifico")
                print("3. ver todos los vehiculos")
                print("4. volver al menú principal")
                print()
                desicion=int(input("ingrese su desición: "))
                if desicion ==1:
                    self. ingresarVehi()
                elif desicion==2:
                    self. vervehiculo()
                elif desicion==3:
                    print(self.vehiculos)
                elif desicion==4:
                    menuciudadano()
            menuVehiculos()


        class eventociudadano(persona):
            from random import randint
            codigo=randint(0,6)
            nombre=input("ingrese su nombre: ")
            ff=list(datos.keys())[list(datos.values()).index(nombre)]


        menuciudadano()
login()