#
#    Para la siguiente prueba de demostración de conocimientos tenga en cuenta aplicar los siguientes elementos o conceptos:
#    
#    ·        Unit testing a las diferentes funciones o clases creadas.  
#   ·        Aplicar por lo menos un patrón de diseño.
#    ·        Utilizar programación orientada a objetos. 
#    ·        Tener presente el principio de responsabilidad única y resto de principios S.O.L.I.D.
#    ·        Establecer una correcta estructura de carpetas y código.
#    
#    Por favor aplicar, en lo posible, Cada uno de los elementos descritos anteriormente, pues son características indispensables en el perfil y serán muy tenidas en cuenta.
#    La prueba en cuestión es la siguiente: 
#   
#    ·        Desarrolle una clase que cumpla con las siguientes funciones para crear, modificar, eliminar, listar el modelo. (Para el proceso de guardado puede usar archivos locales con Pickle o JSON)
#    ·        Generar UI vía interfaz de comandos para usar las diferentes funciones. 
#    
#    El modelo para la clase es un usuario con datos simples como:
#    ·        Nombres
#    ·        Apellidos
#    ·        Edad
#    ·        Email
#   
#    Una vez finalizado el ejercicio por favor responda las siguientes preguntas:
#    1.      ¿Ha trabajado con frameworks como: Fast API, Flask o Tornado?
#    2.      ¿Ha trabajado con bases de datos Relacionales - y no Relacionales?
#    3.      ¿Ha trabajado con librerías de inteligencia artificial? 
#    4.      ¿Ha trabajado con frameworks de front end como VueJS o Angular JS?
#    5.      ¿Ha trabajado con conexiones en tiempo real? (Websockets) 
#    6.      ¿Cuánto tiempo o años de experiencia tiene con Python?
#

# Instalar Virtuaenviroment
    - pip install virtualenv

# Correr virtuaenv
    - Set-ExecutionPolicy Unrestricted -Scope Process [Si no permite activar el venv en Windows]
    - venv\Scripts\activate

# Probar unittest:
    * python -m unittest test.test_userdao
        - Agregar el prefijo src al from de los imports dentro d UserDao

    * python -m unittest test.test_user_validator