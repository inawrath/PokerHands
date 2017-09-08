# Instalación y ejecución del proyecto

Para la utilización del proyecto utilice Python 3.4.

En ubuntu hay que instalar Pip para poder utilizar los requerimientos

```sh
sudo apt-get install python3-pip
```

Luego se debe ingresar a la carpeta del proyecto, a la altura donde esta `manage.py` y debemos instalar los requerimientos del proyecto

```sh
sudo pip3 install -r .requirements
```

Por ultimo, se debe echar a correr el servidor con el siguiente comando.

```sh
sudo python3 manage.py runserver 0.0.0.0:80
```

Si el puerto 80 esta utilizado, cambiar por otro, no hay problemas con ello.