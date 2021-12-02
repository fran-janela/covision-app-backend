<div align="center">
<h1>
  <strong>Lab 1 - Backend</strong>
</h1>
  
## Autor: 
  
<table>
  <tr>
    <td align="center"><a href="https://github.com/fran-janela"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/21694400?v=4" width="100px;" alt=""/><br /><sub><b>Francisco Pinheiro Janela</b></sub></a><br /><a href="https://github.com/fran-janela" title="Francisco Pinheiro Janela"></a></td>
    </tr>
</table>
  
## Docker:
  
<p>

```bash
    # Iniciar o Docker
    $ docker-compose up db

    # Fazer as migrações necessárias
    $ docker-compose exec web python manage.py makemigrations
    $ docker-compose exec web python manage.py migrate

    # Criar um superusuário para a aplicação:
    $ docker-compose exec web python manage.py createsuperuser
```

</p>
</div>

<div align="right">
  Insper Jr
</div>
