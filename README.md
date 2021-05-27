# Todo-App-Web
## Criar listas de tarefas para organizar o seu dia ou semana de forma simples e rápida
### Escrito em python com:
- Flask 
- Flask_SQLAlchemy
- Flask_Login
- Flask_Migrate
- Bulma Framework Css 
*****
### Modo de Uso:
em primeiro lugar instale as dependências usando o pip 
```
   pip install flask
   pip install flask_login
   pip install flask_migrate
   pip install flask_sqlalchemy
```
o Flask precisa ser informado sobre como importá-lo, definindo a FLASK_APP variável de ambiente:
1. Linux:
``` export=FLASK_APP=run ```

2. ```flask db init ``` criar o repositório de migração:
3. ``` flask db migrante ``` Migração caso você queria mudar algo na base de dados 
4. ```flask db upgrade```
5. ```flask run```
