# -----------------------------------------------------------------------------------------------------
# ---------------------------------------- Principios SOLID -------------------------------------------
# -----------------------------------------------------------------------------------------------------

# Son 5 principios que nos ayudan a crear código más limpio, mantenible y fácil de escalar.

# -----------------------------------------------------------------------------------------------------

# Principio #5: D - Dependency Inversion Principle (DIP)

# Depende de abstracciones, no de clases concretas

'''
EJERCICIO :
    Explora eI "Principio SOLID de Inversión de Dependencias (Dependency Inversion
    Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento
    de forma correcta e incorrecta.
DIFICULTAD EXTRA (opcional) :
    Crea un sistema de notificaciones.
Requisitos :
    1. EI sistema puede enviar Email, PUSH y SMS (implementaciones específicas) .
    2. EI sistema de notificaciones no puede depender de las implementaciones específicas.
Instrucciones :
    1. Crea la interfaz o clase abstracta.
    2. Desarrolla las implementaciones específicas.
    3. Crea eI sistema de notificaciones usando eI DIP.
    4. Desarrolla un código que compruebe que se cumple eI principio.
'''

from abc import ABC, abstractmethod

class Notifier(ABC):

    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando email con texto: {message}")


class PUSHNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando PUSH con texto: {message}")


class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando SMS con texto: {message}")


class NotificationService:

    def __init__(self, notifier: Notifier) -> None:
        self.notifier = notifier

    def notify(self, message: str):
        self.notifier.send(message)


# service = NotificationService(EmailNotifier())
# service = NotificationService(PUSHNotifier())
service = NotificationService(SMSNotifier())
service.notify("¡Hola, notificador!")
