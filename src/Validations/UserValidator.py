import validators
from Dao.UserDAO import UserDAO

class UserValidator():

    @staticmethod
    def validateData( user_dao, names, surnames, age, email, email_ignore = None):
        errors = []

        if len(names) < 3:
            errors.append('El nombre debe tener mas de 3 carácteres')

        if len(surnames) < 3:
            errors.append('El apellido debe tener mas de 3 carácteres')

        if age < 0:
            errors.append('La edad no puede ser menor que 0')

        if age > 120:
            errors.append('La edad no puede ser mayor que 120')

        if not validators.email(email):
            errors.append('El email no es valido')
        else:
            if (email and not email_ignore) or (email and email_ignore and email is not email_ignore) :
                user = user_dao.find(email)

                if user:
                    errors.append('El email ya se encuentra registrado para otro usuario')

        return errors