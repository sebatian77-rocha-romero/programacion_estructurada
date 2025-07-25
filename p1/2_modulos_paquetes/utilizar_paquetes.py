from paquete1 import modulos

print(modulos.saludar("Daniel Contreras Ruano"))

modulos.borrarPantalla()
nom,tel=modulos.solicitarDatos2()
print(f"\n\t :: agenda telefonica :: \n\t\tNombre: {nom}\n\t\ttelefono: {tel}")
modulos.espereTecla()