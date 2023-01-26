# Algoritmos 🧩💻 

Consiste em seis desafios propostos pela [Trybe]() para resolução e otimização dos algoritmos, aplicando os conceitos de recursividade e iteratividade; complexidade de tempo e espaço; aplicação de algoritmos de busca e ordenação não nativos do Python e realizações de testes.

* Solucionado com a utilizando da linguagem Python

<details>
  <summary><strong>Descrição das soluções criadas:</strong></summary><br />

| Função | Descrição | Localização |
|---|---|---|
| `simple_report` | Classe  | `` |


<br />
</details>

<details>
  <summary><strong>Descrição do teste criado:</strong></summary><br />
 
| Teste | Descrição | Localização |
|---|---|---|
| `test_product` | Implement | `` |


<br />
</details>

### Estrutura do Projeto

```
.
├── challenges
│   ├──🔹 challenge_anagrams.py
│   ├──🔸 challenge_encrypt_message.py
│   ├──🔹 challenge_find_the_duplicate.py
│   ├──🔹 challenge_palindromes_iterative.py
│   ├──🔹 challenge_palindromes_recursive.py
│   └──🔹 challenge_study_schedule.py
├── tests
│   ├── encrypt
│   │   ├──🔸 __init__.py
│   │   └──🔹 test_encrypt.py
│   ├──🔸 __init__.py
│   ├──🔸 complexities.py
│   └──🔸 geradores.py
├──🔸 dev-requirements.txt
├──🔸 pyproject.toml
├──🔸 README.md
├──🔸 requirements.txt
├──🔸 setup.cfg
└──🔸 setup.py

Legenda:
🔸 Arquivos desenvolvidos pela Trybe (não foram alterados).
🔹 Arquivos a serem alterados para realizar os requisitos.

```



### Instruções

- Para rodar a aplicação localmente e os testes, realize o clone do projeto e utilize os comandos a seguir:

```
Para instalar as dependências e iniciar as aplicações:
<-- na raiz do projeto -->
python3 -m venv .venv // para criar o ambiente virtual
source .venv/bin/activate // para ativar o ambiente virtual
python3 -m pip install -r dev-requirements.txt // instalação das dependências

Para gerar os relatórios via linha de comando:
<-- na raiz do projeto -->
pip install . // para instalar a dependência da linha de comando
inventory_report <argumento1> <argumento2>
--> <argumento1> = deve receber o caminho de um arquivo a ser importado
--> <argumento2> = formato do relatório (simples ou completo)
ou
python3 -m inventory_report.main <argumento1> <argumento2>

Para rodar todos os testes:
<-- na raiz do projeto -->
python3 -m pytest

Para rodar os testes individualmente:
<-- na raiz do projeto -->
python3 -m pytest -k test_cria_produto
python3 -m pytest -k test_relatorio_produto
python3 -m pytest -k test_decorar_relatorio

Para rodar os testes utilizando Docker:
<-- na raiz do projeto -->
docker-compose run --rm inventory pytest
```

