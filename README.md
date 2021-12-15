# GARFO - Gestão Automática de Restaurantes em Fluxo Operacional

O GARFO é um sistema de gestão de pedidos em restaurantes. Para sua utilização, o gerente do
restaurante cadastra o número de mesas e os pratos disponíveis. Os clientes podem
visualizar o cardápio e fazer seu pedido, selecionando os pratos. A cozinha recebe
uma lista dos pedidos e prepara os pratos. Os garçons recebem uma lista de pedidos
prontos com a identificação de mesa e entregam os pratos. No final da refeição, a
conta é gerada automaticamente pelo sistema e o garçom faz a cobrança na mesa.
Os pedidos podem ser feitos por clientes diferentes em uma mesma mesa, assim ao
final, a conta pode ser separada por indivíduo.

O GARFO foi desenvolvido usando o Django e está hospedado no [GitHub](https://github.com/Henrique-BO/GARFO).

Como acompanhamento, pode-se utilizar seu Dashboard, a [COLHER](https://github.com/Henrique-BO/COLHER).

## Utilização

Para abrir localmente o GARFO, execute

`python manage.py runserver`

> Obs.: Da primeira vez, é necessário aplicar as migrações com `python manage.py migrate`

O GARFO também está hospedado publicamente no Heroku em

https://sistema-garfo.herokuapp.com/