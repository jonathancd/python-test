from asyncio.windows_events import NULL
import os
from Dao.UserDAO import UserDAO
from Models.User import User
from Validations.UserValidator import UserValidator

class App():
    def __init__(self, resource_active = None):
        self._is_running = True
        self._resource_active = resource_active
        self._clear_screen()

    @property
    def is_running(self):
        return self._is_running

    @property
    def resources(self):
        return self._resources

    @property
    def resource_active(self):
        return self._resource_active

    @resource_active.setter
    def resource_active(self , resource_active):
        self._resource_active = resource_active
    
    @is_running.setter
    def is_running(self , is_running):
        self._is_running = is_running

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _handle_menu_keypress(self):
        resource_active = self.resource_active

        if resource_active is not None:
            if resource_active == 'users':
                self._handle_users_keypress()

    def _handle_users_keypress(self):
        key = input('Seleccione una opción: ')
        key = key.upper()

        if key == 'L':
            self._on_list_users()
        elif key == 'C':
            self._on_create_user()
        elif key == 'A':
            self._on_update_user()
        elif key == 'E':
            self._on_delete_user()
        elif key == 'S':
            self.is_running = False

    def _initialize_app(self):
        try:
            while (self.is_running):
                self._print_menu_main()
                self._handle_menu_keypress()
                
        except KeyboardInterrupt:
            pass

    def _on_list_users(self):
        user_dao = UserDAO()
        users = user_dao.index()

        for index, user in enumerate(users):
            print("{}- {} {} - Edad: {} - Email: {}".format((index + 1), user.names, user.surnames, user.age, user.email))

    def _on_create_user(self):
        try:
            while True:
                print('\nIngrese datos del usuario')
                names = input('Nombres: ')
                surnames = input('Apellidos: ')
                email = input('Email: ')

                while True:
                    try:
                        age = int(input('Edad: '))
                        break
                    except:
                        print("Ingresa una edad válida")
                
                user_dao = UserDAO()
                errors = UserValidator.validateData(user_dao, names, surnames, age, email)
                if len(errors) == 0:
                    user = User()
                    user.age = age
                    user.email = email
                    user.names = names
                    user.surnames = surnames
                    user_dao.store(user)
                    break
                else:
                    print("\nDatos incorrectos:")
                    for error in errors:
                        print(error)
        except BaseException as err:
            print(err)
            print('Ha ocurrido un error al tratar de crear el usuario')

    def _on_update_user(self):
        try:
            email_user = input('\nIngrese Email del usuario: ')
            user_dao = UserDAO()
            user = user_dao.find(email_user)

            if user:
                while True:
                    print('Ingrese nuevos datos del usuario')
                    names = input('Nombres: ')
                    surnames = input('Apellidos: ')
                    email = input('Email: ')

                    while True:
                        try:
                            age = int(input('Edad: '))
                            break
                        except:
                            print("Ingresa una edad válida")

                    errors = UserValidator.validateData(user_dao, names, surnames, age, email, email_user)

                    if len(errors) == 0:
                        user = User(age, email, names, surnames)
                        user_dao.update(user, email_user)
                        print('Usuario actualizado')
                        break
                    else:
                        print("\nDatos incorrectos:")
                        for error in errors:
                            print(error)
            else:
                print('Usuario no encontrado')
        except BaseException as err:
            print('Ha ocurrido un error al tratar de actualizar el usuario')
            raise

    def _on_delete_user(self):
        try:
            email = input('Ingrese Email del usuario: ')
            user_dao = UserDAO()
            deleted = user_dao.delete(email)
            if deleted:
                print('Usuario eliminado')
            else:
                print('Usuario no encontrado')
        except BaseException as err:
            print('Ha ocurrido un error al tratar de eliminar el usuario')
            raise

    def _print_menu_main(self):
        title = '## Bienvenido a gestion de usuarios ##'
        print("\n\n")
        print("#"*len(title))
        print(title)
        print("#"*len(title))
        
        resource_active = self.resource_active

        if resource_active is not None:
            if resource_active == 'users':
                self._print_submenu_users()

    def _print_submenu_users(self):
        print('*  [L] Listar usuarios     *')
        print('*  [C] Crear usuario       *')
        print('*  [A] Actualizar usuario  *')
        print('*  [E] Eliminar usuario    *')
        print('*  [S] Salir               *')
        print('*                          *')
        print('*'*10)

app = App('users')
app._initialize_app()