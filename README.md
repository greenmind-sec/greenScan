## Requisitos
> https://pypi.org/project/youtube-search-python/

### Instalando
```sh
pip install youtube-search-python
```

## Como usar
O greenScan é feito em Python, atualmente tem as opções:

- -m (Maximo de pesquisas)
- --search (O que deseja pesquisar)
- -t (Tipo de ação da ferramenta)

### Realizando uma busca
Em seguida pode executar o projeto da seguinte forma:
```sh
python greenScan.py -m 2 --search BMX -t search
```

## Usando Docker

### Gerando imagem
```sh
docker build -t "greenmind/greenscan:1" .
```
> Tamanho da imagem: 85.6MB

### Como usar ?
```sh
docker run -it --rm "greenmind/greenscan:1" -m 2 --search BMX -t search
```
