"""self - ссылка на текущий объект"""


class Auth:
    is_authed: bool = False

    def login(self):
        self.is_authed = True

# # С точки зрения кода он будет валидным, но не по стандарту
#     def logout(me):
#         """Выход"""
#         me.is_authed = False


auth_service = Auth()
auth_service.login()
# auth_service.logout()
# Auth.login(auth_service)
print(auth_service.is_authed)
