import os
import sys
import time


def borrar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperar_tecla():
    input("\n\t\t... Presiona Enter para continuar ...")

def validar_opcion(opcion, opciones_validas):
    return opcion.strip().lower() in [o.lower() for o in opciones_validas]

def escribir_lento(texto, delay=0.03):
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def generar_reporte_pdf(titulo, contenido, nombre_archivo):
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas

        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        width, height = letter

        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height - 50, str(titulo))

        c.setFont("Helvetica", 12)
        y = height - 80
        for linea in contenido:
            c.drawString(50, y, str(linea))
            y -= 18
            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = height - 50

        c.save()
        print(f"✅ Reporte PDF generado: {nombre_archivo}")
        return True
    except ImportError:
        print("❌ Debes instalar reportlab: pip install reportlab")
        return False
    except Exception as e:
        print(f"❌ Error al generar PDF: {e}")
        return False
        print(f"✅ Reporte PDF generado: {nombre_archivo}")
        return True
    except ImportError:
        print("❌ Debes instalar reportlab: pip install reportlab")
        return False
    except Exception as e:
        print(f"❌ Error al generar PDF: {e}")
        return False
