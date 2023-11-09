
# Desafio Técnico Netflix


## Rodando localmente

Clone o projeto

```bash
git clone https://github.com/natanbravo/desafio-tecnico-netflix.git
cd desafio-tecnico-netflix
```
Crie seu ambiente virtual

```bash
python3 -m venv venv
```

Instale as dependências

```bash
pip install -r requirements.txt
```



# Descrição do desafio


Given a string 's' consisting od small English letters, find and return the first instance of a non-repeating
character in it. If there is no such character, return '_'

Example: 

   . For (s = "abacabad"), the output should be (solution(s) = 'c').
    There are no '2' non-repeating characters in the strig: 'c' and 'd'. Return (c) since it appears in the string first.

   . For (s = "abacabaabacaba"), the output should be (solution(s) = '_').
    There are no characters in this string that do not repeat.