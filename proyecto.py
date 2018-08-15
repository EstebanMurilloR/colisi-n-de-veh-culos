datos={"cédula0":"208090159", "nombre0":"Esteban Murillo", "fecha de nacimiento0":"14/09/2000", "edad0":"17" ,"sexo0":"Masculino","residencia0":"San Carlos","Tipo de usuario0": "Admin", "Contraseña0":"Admin"}

def menuInicio():
    print()
    registro = input("está registrado?(si o no): ")
    if registro == "si" or registro == "Si" or registro=="SI":
        login()
    else:
        register()

def register():# sirve para registrar los usuarios
    largo=len(datos)
    nume=largo/9

    for i in range(int(nume),1000):
        print()
        print("Registrese")
        print()
        num=str(i)
        cedula=input("ingrese su número de cédula con ceros y sin espacios, si ingresa una x para: ")
        if cedula!="x":
            nombre=input("ingrese su nombre completo: ")
            fechaNacimiento=input("ingrese su fecha de nacimiento(día/mes/año): ")
            edad=int(input("ingrese su edad: "))
            if edad<=18:
                sexo=input("Ingrese su sexo(Masculino o Femenino): ")
                recidencia=input("ingrese su cantón de residencia, una vez ingrese al sistema vaya al apartado de provincias y agreguelo: ")
                tipoUsuario=input("ingrese su tipo de usurio(ciudadano, oficial u oficina del juzgado): ")
                password=input("ingrese una contraseña: ")

                datos["cédula"+num] = cedula
                datos["nombre"+num] = nombre
                datos["fecha de nacimiento"+num]=fechaNacimiento
                datos["edad"+num] = edad
                datos["sexo"+num] = sexo
                datos["lugar de residencia"+num] = recidencia
                datos["tipo de usuario"+num] = tipoUsuario
                datos["contraseña"+num] = password

                menuInicio()

            else:
                print("usted es menor de edad, no puede ecceder a la plataforma")
                exit()
        else:
            menuInicio()

print(datos)

def login():#el inicio de sesión

    try:
        print()
        cedula=input("ingrese su cédula con ceros y sin espacios: ")
        pasword=input("ingrese su contraseña: ")
        dd=list(datos.keys())[list(datos.values()).index(pasword)]
        jj=list(datos.keys())[list(datos.values()).index(cedula)]
        try:
            if cedula==datos.get(dd) and pasword== datos.get(jj):
                validacion(dd)
        except:
            print("intente de nuevo, por favor, sus datos no son correctos")
            login()
    except:
        print("Inte de nuevo, por favor, sus datos no son correctos")
        login()

def validacion(dd):#aqui se valida el tipo de usuario
    dd=dd
    hh = 0
    for i in dd:
        hh = i
        usuario = "tipo de usuario" + str(hh)
        if usuario == "ciudadano" or usuario == "Cuidadano":
            uu = persona()
            uu.ciudadano()
        elif usuario=="oficial" or usuario=="Oficial":
            uu=persona()
            uu.oficial()

def provincias():#CRUD de provincias
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
        menu()
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
        menu()
    class nuevoCanton(verprovincias):
        print("Escoja una provincia")
        print(verprovincias)
        menu()
    menu()

vehiculos = {}
evento={}
codigos=[]

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

            def menVehiculos(self):
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
                    print(vehiculos)
                elif desicion==4:
                    menuciudadano()

            def ingresarVehi(self):

                for i in range(0,1000):

                    self.cedula=int(input("Ingrese su cédula, si ingresa x cierra: "))

                    try:
                        if self.cedula!="x":
                            self.placa= input("ingrese la placa del vehículo: ")
                            self.ano=int(input("Ingrese el año del carro: "))
                            self.marca= input("ingrese la marca del vehículo: ")
                            self.color=input("Ingrese el color de su carro: ")
                            self. tipo=input("Su carro es moto, automóvil, bus o camión")
                            nom=list(datos.keys())[list(datos.values()).index(self.cedula)]
                            j=0
                            if len(vehiculos)==0:
                                j=0
                            elif len(vehiculos)>0:
                                j=len(vehiculos)/6

                            vehiculos["Cédula"+str(j)]=self.cedula
                            vehiculos["placa"+str(j)]=self.placa
                            vehiculos["Año"+str(j)]=self.ano
                            vehiculos["Marca"+str(j)]=self.marca
                            vehiculos["color"+str(j)]=self.color
                            vehiculos["tipo"+str(j)]=self.tipo
                    except:
                        break

                    dd=list(datos.keys())[list(datos.values()).index(self.cedula)]
                    hh="0"
                    for i in dd:
                        hh=i
                    datos["vehiculo"+str(hh)]=vehiculos



            def vervehiculo(self):

                placa=(input("Ingrese la placa del vehículo que desea ver: "))
                num=list(datos.keys())[list(datos.values()).index(placa)]
                for i in num:
                    num=i
                print("La cédula del dueño del carro es ",vehiculos["Cédula"+num])
                print("Placa ",vehiculos["placa"+num])
                print("Año",vehiculos["Año"+num])
                print()


            menVehiculos()




        class eventociudadano(persona):#CRUD evento ciudadano

            codigo = []

            import datetime
            from random import randint
            for i in range(0, 5):
                nume = randint(0, 6)
                codigo.append(nume)
            if codigo not in codigos:
                codigos.append(codigo)

            nombre=input("ingrese su nombre: ")
            nom=list(datos.keys())[list(datos.values()).index(nombre)]
            num=0
            for i in nom:
                num=i

            print("Desea saber si el lugar existe en la base de datos")
            desicion=input("si o no: ")
            if desicion=="si":
                provincias()

            lugar=input("Ingrese el lugar del accidente(Provincia/cantón): ")
            fecha = datetime
            placa=input("Ingrese la placa del vehículo:")
            try:
                if placa in datos:
                    estado="abierto"

                    multa=0
                    tipo=vehiculos.get("tipo"+str(num))
                    ano=vehiculos.get("Año"+str(num))
                    impuesto=0
                    impuesto2=0

                    if tipo=="moto"or tipo =="Moto":#este montón de if es para comprobar cuanto tiene que pagar de multa
                        impuesto=10000*0.15
                        if ano < 2000:
                            impuesto2 = 10000 * 0.10
                        multa=10000+impuesto+impuesto2
                    elif tipo=="Automóvil" or tipo=="automóvil":
                        impuesto=2500*0.30
                        if ano < 2000:
                            impuesto2 = 2500 * 0.10
                        multa=2500+impuesto+impuesto2
                    elif tipo=="Bus" or tipo=="bus":
                        impuesto=45000*0.45
                        if ano < 2000:
                            impuesto2 = 45000 * 0.10
                        multa=45000+impuesto+impuesto2
                    elif tipo =="Camión" or tipo=="camión":
                        impuesto =65000*0.70
                        if ano < 2000:
                            impuesto2 = 65000 * 0.10
                        multa=65000+impuesto+impuesto2
                    numero=0
                    if len(evento)>0:
                        numero=len(evento)/6
                    elif len(evento)==0:
                        numero=0

                    evento["código"+str(numero)]=codigo
                    evento["nombre de usuario"+str(numero)]=nombre
                    evento["lugar"+str(numero)]=lugar
                    evento["placa"+str(numero)]=placa
                    evento["estado"+str(numero)]=estado
                    evento["fecha"+str(numero)]=fecha

                    print("Código: ",codigo,", nombre del usuario: ", nombre, ", lugar del incidente: ",lugar, ", placa: ", placa, ", estado: ", estado, "fecha: ",fecha)

            except:
                print("Su placa no se encuentra registrada, vuelva a intentarlo")
                menuciudadano()

        menuciudadano()

    def oficial(self):
        print()
        print("A continuación se mostrarán todos los eventos registrados")
        print()
        nom=input("Ingrese su nombre: ")

        for i in range(0, len(evento)):
            j=i
            codigo=evento.get("código"+str(j))
            nombre=evento.get("nombre de usuario"+str(j))
            lugar=evento.get("lugar"+str(j))
            placa=evento.get("placa"+str(j))
            estad = evento["estado" + str(j)] = "Por aprobar"
            estado=evento.get("estado"+str(j))
            fecha=evento.get("fecha"+str(j))
            numparte=int(input("Ingrese el número de parte: "))
            evento["oficial"+str(j)]=nom
            print()
            import datetime
            ahora=datetime.datetime.now()
            compara=fecha+datetime.timedelta(0,30)
            if ahora>=compara:
                print("Evento"+str(j), ", codigo: ",codigo,", nombre de usuario: ",nombre,", lugar: ",lugar,", placa: ",placa, ", nobre del oficial: ", nom, ", número de parte: ", numparte, ", estado: ", estado, ", fecha: ", ahora)

    def juzgado(self):
        nom=input("Ingrese su nombre: ")
        print()
        print("Ahora se mostrarán todos los eventos ")
        for i in range(0, len(evento)):
            j = i
            nome= evento.get("oficial"+str(j))
            numreg = int(input("Ingrese el número de registro: "))
            codigo = evento.get("código" + str(j))
            nombre = evento.get("nombre de usuario" + str(j))
            lugar = evento.get("lugar" + str(j))
            placa = evento.get("placa" + str(j))
            estad = evento["estado" + str(j)] = "Completo"
            estado = evento.get("estado" + str(j))
            fecha = evento.get("fecha" + str(j))
            numparte = int(input("Ingrese el número de parte: "))
            print()
            import datetime
            ahora = datetime.datetime.now()
            print("Evento" + str(j), ", codigo: ", codigo, ", nombre de usuario: ", nombre, ", lugar: ", lugar,
                ", placa: ", placa, ", nobre del oficial: ", nome, ", número de parte: ", numparte,
                ", nombre oficina del juzgado: ", nom, ", número de registro: ", numreg ,", estado: ", estado, ", fecha: ", ahora)



menuInicio()