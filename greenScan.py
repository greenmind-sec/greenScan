#!/usr/python
import argparse
from youtubesearchpython import SearchVideos

# Funções
def search_videos(search,max):
    max = int(max)
    for param in search:
        print("Buscando por",param)
        search = SearchVideos(param, offset = 1, mode = "json", max_results = max)
        print(search.result())

parser = argparse.ArgumentParser(description = 'GreenMind Security Scan.')
parser.add_argument('-m', action = 'store', default=20, dest = 'max', required = False,help = 'insert max for search')
parser.add_argument('--search', dest = 'search', action='append')
parser.parse_args('--search 1 --search 2'.split())
parser.add_argument('-t', action = 'store', dest = 'type', required = True,help = 'insert type.')


arguments = parser.parse_args()
search = arguments.search
max = arguments.max
type = arguments.type
if type == "search":
    search_videos(search,max)
else:
    print("Erro!")
