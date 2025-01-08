# Documentação Inicial

Este guia fornece instruções para configurar um ambiente virtual Python, instalar Django e outras dependências, e iniciar um novo projeto Django.

1. **Criar um ambiente virtual**:
    - Utilize o comando `python3 -m venv venv` para criar um novo ambiente virtual chamado `venv`.

2. **Ativar o ambiente virtual**:
    - No Linux ou macOS, use `source venv/bin/activate` para ativar o ambiente virtual.

3. **Instalar dependências**:
    - Instale Django e outras bibliotecas necessárias com `pip install django djangorestframework celery redis`.

4. **Iniciar um novo projeto Django**:
    - Use `django-admin startproject project .` para criar um novo projeto Django no diretório atual.

5. **Executar o servidor de desenvolvimento**:
    - Inicie o servidor de desenvolvimento Django com `python manage.py runserver`.

Siga estas etapas para configurar e iniciar seu projeto Django com sucesso.
python3 -m venv venv

source venv/bin/activate

pip install django
pip install django djangorestframework celery redis

django-admin startproject project .

python manage.py runserver