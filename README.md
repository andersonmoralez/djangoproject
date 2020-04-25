# Atividade seletiva

## Dependências:
* Todas as dependências do projeto podem ser instaladas via _txt (requirements.txt)_ através do comando: _"pip install -r requirements.txt"_<br>

* Caso seja solicitado, por algum motivo, crie um novo ambiente virtual na pasta raiz deste projeto.

* Caso seja solicitado, também por algum motivo, faça upgrade do pip através do comando: _"python -m pip install --upgrade pip"._
O projeto já possuí suas migrações no github, mas caso seja necessário, realize-as através do comando: _"python manage.py makemigration" e "python manage.py migrate"_



## URLs:
<b>GET</b> retorna todos os registros contidos no DB sqlite3 (nativo do django): http://127.0.0.1:8000/v1/records <br>
<b>GET</b> retorna um registro da database de acordo com o id fornecido: http://127.0.0.1:8000/v1/record/id <br>
<b>POST</b> insere um registro na database: http://127.0.0.1:8000/v1/records <br>
<b>PUT</b> altera qualquer dado no registro da database, de acordo com o id: http://127.0.0.1:8000/v1/record/id <br>
<b>DELETE</b> remove/deleta o registro na database de acordo com o id: http://127.0.0.1:8000/v1/record/id <br>
## Parte 1 Backend GET, POST, PUT e DELETE (Adicional): 

### GET database vazia: 
![get records](https://github.com/andersonmoralez/djangoproject/blob/master/backend/screenshot/get_user.PNG?raw=true)

### Populando database via POST:
> _perceba que nossa senha foi criptografada pós requisição_

![post records](https://github.com/andersonmoralez/djangoproject/blob/master/backend/screenshot/post.PNG?raw=true)


### GET database populada:
![get records database](https://github.com/andersonmoralez/djangoproject/blob/master/backend/screenshot/get_users.PNG?raw=true)

### Alterando dados via PUT:
> _Alteramos o sobrenome de “Jose Almeida” para “Jose Souza”, e o campo senha de “4321567” para “12345678”:_ 

![put records](https://github.com/andersonmoralez/djangoproject/blob/master/backend/screenshot/put_user.PNG?raw=true)

### Usamos GET passando o id na URL para confirmar a alteração:
![get record 3](https://github.com/andersonmoralez/djangoproject/blob/master/backend/screenshot/get_user_3.PNG?raw=true)

### DELETE (ADICIONAL) tomamos a liberdade para adicionar “delete”:
> _inserimos o id na URL para remover os dados desejados_

![delete record 2](https://github.com/andersonmoralez/djangoproject/blob/master/backend/screenshot/delete_user2.PNG?raw=true)

### TOKEN:
> _usamos autenticação via token no header das requisições:_

![token records](https://github.com/andersonmoralez/djangoproject/blob/master/backend/screenshot/token_records.PNG?raw=true)

### Pode ser consultada pela url (/v1/token): token_url
![url token](https://github.com/andersonmoralez/djangoproject/blob/master/backend/screenshot/token_url.PNG?raw=true)


## Frontend Parte 2:
O que esperavamos para o frontend: 3 páginas utilizando HTML, CSS Javascript e Bootstrap. Seguindo os requisitos da avaliação.

O que conseguimos entregar (infelizmente e/ou felizmente): 1 página ESTILIZADA (CSS/Bootstrap) e dinâmica contendo os registros GET da nossa base de dados:
> _nosso frontend não possuí autenticação por token, porém, TODOS os tipos de requisições funcionam!_

![frontend](https://github.com/andersonmoralez/djangoproject/blob/master/frontend/screenshot/registers_front.PNG?raw=true)

Se você é portador de algum dado utilizado aqui, como exemplo, e se sinta ofendido. Por favor nos comunique para que seja feita a remoção!
* Caso seja solicitado, por algum motivo, crie um novo ambiente virtual na pasta raiz deste projeto.

* Caso seja solicitado, também por algum motivo, faça upgrade do pip através do comando: _"python -m pip install --upgrade pip"._
O projeto já possuí suas migrações no github, mas caso seja necessário, realize-as através do comando: _"python manage.py makemigration" e "python manage.py migrate"_



## URLs:
<b>GET</b> retorna todos os registros contidos no DB sqlite3 (nativo do django): http://127.0.0.1:8000/v1/records <br>
<b>GET</b> retorna um registro da database de acordo com o id fornecido: http://127.0.0.1:8000/v1/record/id <br>
<b>POST</b> insere um registro na database: http://127.0.0.1:8000/v1/records <br>
<b>PUT</b> altera qualquer dado no registro da database, de acordo com o id: http://127.0.0.1:8000/v1/record/id <br>
<b>DELETE</b> remove/deleta o registro na database de acordo com o id: http://127.0.0.1:8000/v1/record/id <br>
## Parte 1 Backend GET, POST, PUT e DELETE (Adicional): 

### GET database vazia: 
![get records](https://github.com/andersonmoralez/djangoproject/blob/master/backend/screenshot/get_user.PNG?raw=true)

### Populando database via POST:
> _perceba que nossa senha foi criptografada pós requisição_

![post records](https://github.com/andersonmoralez/djangoproject/blob/master/backend/screenshot/post.PNG?raw=true)


### GET database populada:
![get records database](https://github.com/andersonmoralez/djangoproject/blob/master/backend/screenshot/get_users.PNG?raw=true)

### Alterando dados via PUT:
> _Alteramos o sobrenome de “Jose Almeida” para “Jose Souza”, e o campo senha de “4321567” para “12345678”:_ 

![put records](https://github.com/andersonmoralez/djangoproject/blob/master/backend/screenshot/put_user.PNG?raw=true)

### Usamos GET passando o id na URL para confirmar a alteração:
![get record 3](https://github.com/andersonmoralez/djangoproject/blob/master/backend/screenshot/get_user_3.PNG?raw=true)

### DELETE (ADICIONAL) tomamos a liberdade para adicionar “delete”:
> _inserimos o id na URL para remover os dados desejados_

![delete record 2](https://github.com/andersonmoralez/djangoproject/blob/master/backend/screenshot/delete_user2.PNG?raw=true)

### TOKEN:
> _usamos autenticação via token no header das requisições:_

![token records](https://github.com/andersonmoralez/djangoproject/blob/master/backend/screenshot/token_records.PNG?raw=true)

### Pode ser consultada pela url (/v1/token): token_url
![url token](https://github.com/andersonmoralez/djangoproject/blob/master/backend/screenshot/token_url.PNG?raw=true)


## Frontend Parte 2:
O que esperavamos para o frontend: 3 páginas utilizando HTML, CSS Javascript e Bootstrap. Seguindo os requisitos da avaliação.

O que conseguimos entregar (infelizmente e/ou felizmente): 1 página ESTILIZADA (CSS/Bootstrap) e dinâmica contendo os registros GET da nossa base de dados:
> _nosso frontend não possuí autenticação por token, porém, TODOS os tipos de requisições funcionam!_

![frontend](https://github.com/andersonmoralez/djangoproject/blob/master/frontend/screenshot/registers_front.PNG?raw=true)

Se você é portador de algum dado utilizado aqui, como exemplo, e se sinta ofendido. Por favor nos comunique para que seja feita a remoção!
