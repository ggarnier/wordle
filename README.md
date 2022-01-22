# Wordle

Simple implementation of [Wordle](https://www.powerlanguage.co.uk/wordle/) game, for command-line playing.

To play it, you need a dictionary - a text file containing one word per line. Here are some examples:

- English: https://github.com/dwyl/english-words/blob/master/words_alpha.txt
- Portuguese (BR): https://raw.githubusercontent.com/pythonprobr/palavras/master/palavras.txt
- Portuguese (BR): http://200.17.137.109:8081/novobsi/Members/cicerog/disciplinas/introducao-a-programacao/arquivos-2016-1/algoritmos/Lista-de-Palavras.txt/view
- Portuguese (BR): https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt

After downloading a dictionary, play the game with `python -m wordle -d <path to dictionary file>`. Here's an example with a portuguese dictionary:

```shell
$ python3 -m wordle -d palavras.txt
Dictionary contains 7326 words

Guess #1
claro
_____

Guess #2
pinte
Word not in dictionary
gesto
_ox__

Guess #3
cisne
__x_o

Guess #4
festa
_ox__

Guess #5
museu
Correct! You're right after 5 guesses
```
