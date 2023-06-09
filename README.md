# Sistemas Moveis Distribuidos API
 Repositório criado para a publicação da ADO de Sistemas Móveis Distríbuidos.
## Participantes:
### Ivo Bueno, Lucas Matulis, Marcos Rosa e Thomas Ferreira - TADS - Turma B.
### Link Repositório Replit: https://replit.com/@MarcosRos4/SistemasMoveisDistribuidosAPI

## Instruções para a execução do projeto:
### Criando ambiente virtual em python

1: python (ou py) -m venv .venv

2: Abra o windows powershell e habilite a opção (caso a sua ainda não esteja habilitada):

 No powershell: 
  Set-ExecutionPolicy -Scope Current User -	ExecutionPolicy Remote Signed

 No terminal do vscode:
 .\venv\Scripts\Activate.ps1 


3. Instalar e iniciar o Django: 
pip install django djangorestframework


OBS: Todos os comandos a partir de agora chamaremos o arquivo manage.py:

4. Fazer as migrações necessárias do banco de dados:
	python manage.py makemigrations
	python manage.py migrate

5. Para iniciar o servidor:
	python manage.py run server

Para parar o servidor:
	^C (ctrl + c)
