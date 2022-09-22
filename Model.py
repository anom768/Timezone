from Domain import Users

class UserRegistrationRequest() :
    username = None
    password = None
    passwordVerify = None

class UserRegistrationResponse() :
    user:Users