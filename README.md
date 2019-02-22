# Requisitos de Instalación Generales

* __Instalación de Python 3.6__

    * Esta instalación Python requerie el compilador __GCC__ en su sistema,
      use el siguiente comando para instalar los requisitos previos de __Python 3.6__ antes de instalarlo.

      ```sh
         $ yum install gcc openssl-devel bzip2-devel
         o
         $ sudo apt install gcc openssl-devel bzip2-devel
      ```

    * Descarga __Python 3.6__

      ```sh
         $ cd /usr/src
         $ wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
      ```

    * Ahora extrae el paquete descargado.

      ```sh
         $ tar xzf Python-3.6.5.tgz
         $ cd Python-3.6.5
         $ ./configure --enable-optimizations
         $ make altinstall
      ```

        > __NOTA:__ \
        \
        __make altinstall__ se usa para evitar reemplazar el archivo binario predeterminado de python __/usr/bin/python__

    * Verifique la versión de Python

      ```sh
         $ python3.6 -V
      ```

    * Luego de realizar la verificación de la version de __python3.6__ \
     procederemos a realizar la instalación de __pip__ ejecutando los siguientes comandos:


      ```sh
         $ yum install epel-release -y
         $ yum update -y
         $ yum install python-pip -y
          
         o 

         $ sudo apt install epel-release -y
         $ sudo apt update -y
         $ sudo apt install python-pip -y

      ```

* __Instalación de virtualenv y virtualenvwrapper (Python)__

    * __virtualenvwrapper__ debe instalarse en el mismo área global de paquetes de sitio donde virtualenv está instalado.
      Es posible que necesite privilegios administrativos para hacer eso. La forma más fácil de instalarlo es usar __pip__

      ```sh
         $ pip install virtualenv
         $ pip install virtualenvwrapper
      ```

       o:

      ```sh
         $ sudo pip install virtualenv
         $ sudo pip install virtualenvwrapper
      ```

      > __NOTA:__ \
      \
      __virtualenv__ te permite crear muchos entornos virtuales diferentes de Python.
      Solo debe instalar virtualenv y virtualenvwrapper en su instalación base de Python (es decir, NO mientras un virtualenv está activo)
      para que el mismo release sea compartido por todos los entornos de Python que dependan de él.


        * Agregar variables de entorno en bash profile
    
          ```sh
              export WORKON_HOME=~/virtualenvs
              source /usr/bin/virtualenvwrapper.sh
          ```
    
          > __NOTA:__ \
          \
           Verificar si el bash existe en la siguente ruta: \
           \
           `/usr/bin/virtualenvwrapper.sh`



* __Instalación de Git__

    * Utilice el siguiente comando para instalar __Git__.

      ```sh
         $ yum update -y
         $ yum install git -y
         
         o 

         $ sudo apt update -y
         $ sudo apt install git -y

      ```
* __Clonar repositorio__

    * Utilice el siguiente comando para clonar repositorio.

      ```sh
         $ git clone https://github.com/stevedch/fibonacci.git

      ```

* __Crear entorno virtual y activar entorno virtual__

    * Utilice el siguiente comando para crear un entorno virtual.

      ```sh
         $ virtualenv --python=/usr/bin/python2.7 ~/.virtualenvs/fibonacci
      ```

    * Después de haber creado el entorno virual deberá activar el entorno creado con el 
      siguiente comando.

      ```sh
         $ source /home/[user]/.virtualenvs/fibonacci/bin/activate
      ```

`

* __Instalar proyecto__

    * Después de haber instalado el proyecto deberá dirigirse al proyecto.

      ```sh
         $ cd /home/steve/Escritorio/fibonacci
      ```

    * Deberá instalar las librerías ejecutando el siguiente comando.

      ```sh
         $ pip install -r requirements.txt
      ```   ```

    * Deberá ejecutar el siguiente comando para levantar el servidor.

      ```sh
         $ python server.py
      ```

    * Acceda a la siguiente url.

      ```sh
         $ http://127.0.0.1:8080/
      ```




Dependencias
============

| Name | URL |
| ------ | ------ |
| Python 3.6.5 | [https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz] |
| virtualenv | [https://virtualenv.pypa.io/en/stable/installation/] |
| virtualenvwrapper | [https://virtualenvwrapper.readthedocs.io/en/latest/install.html] |
