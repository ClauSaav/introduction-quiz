# introduction-quiz  
Repositorio de Quiz  

**Inistrucciones y Pasos**  
* Primero creamos un repositorio y lo clonamos: git clone `git clone https://github.com/ClauSaav/introduction-quiz`  
* Copiando y Editando el archivo con respuestas: `vim introduction_quiz.json`  
* Instalamos el entorno virtual: `virtualenv -p python3.6 env`  
* Activamos el entorno virtual: `source env/bin/activate`  
* Instalando librerias(requests): `pip install requests`  
* Entramos a Python y ejecutamos el archivo `send_answres.py`  
* Asegurandonos de tener el archivo `introduction_quiz.json` ya con los cambios correspondientes(respuestas)
* Revisamos que el servicio de elasticsearch esté dispopnible  
* En el navegador ponemos la siguiente URL `http://localhost:9200/beeva/clau/1?pretty`  
* Y podremos ver las preeguntas y respuestas
