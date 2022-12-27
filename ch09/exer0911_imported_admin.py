from users import Admin

lista_privilegios = ['can delete post', 'can ban user', 'can add post']

admin_1 = Admin("Rubén", "García", 32, "Ibi", "Rugar", lista_privilegios)
admin_1.privileges.show_privileges()
