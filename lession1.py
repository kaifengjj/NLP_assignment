
from matplotlib.pyplot import show
import random

grammar = """
sentence = adj noun verb adv noun2
adj = adj_single adj_single 的 | null
adj_single = 漂亮  | 蓝色 | 好看
adv = 安静地 | 静静
noun = 猫 | 女人 | 男人
verb = adv 看着 | adv 
noun2 = 桌子 | 皮球 
"""


def build_grammar(grammar_str):
    grammar_pattern={}
    for line in grammar_str.split('\n'):
        if len(line)==0 :
            continue
        statement,expression=line.split('=')
        #for e in expression.split('|'):
        #    grammar_pattern[statement.strip()]=e.strip()
        grammar_pattern[statement.strip()]=[e.split() for e in expression.split('|')]

    return grammar_pattern


def generate(grammar_pattern, target):
    if target not in grammar_pattern: return target
    expression=random.choice(grammar_pattern[target])
    tokens=[generate(grammar_pattern,e) for e in expression]
    return ''.join([t for t in tokens if t !='null'])



# simple solution
def adj():
    return random.choice('漂亮 | 蓝色| 好看'.split('|'))


def noun():
    return random.choice('猫 | 女人 | 男人'.split('|'))


def sentence():
    return ''.join([adj(),noun()])

# search base intelligence
# breadth search engine

graph = {
    'A':'B B B C',
    'B': 'A C',
    'C': 'A B D D E',
    'D': 'C',
    'E': 'C C F',
    'F': 'E'
}

for i in graph:
    graph[i]=set(graph[i].split())

seen=set()
need_visited=['A']
while need_visited:
    node=need_visited.pop(0)
    if node in seen :continue
   # print(format(node))
    need_visited += graph[node]
    seen.add(node)


# DEEP FIRST Search

graph_long = {
    '1': '2 7',
    '2': '1 3',
    '3': '2 4',
    '4': '3 5',
    '5': '6 10',
    '7': '8',
    '6': '5',
    '8': '9',
    '9': '10',
    '10': '5 11',
    '11': '12',
    '12': '11',
}

for i in graph_long:
    graph_long[i] = graph_long[i].split()


seen=set()
need_visited=['1']
while need_visited:
    node=need_visited.pop(0)
    if node in seen : continue
    #print(format(node))

    need_visited=graph_long[node]+need_visited
    seen.add(node)


def search(graph, concat_func):
    seen = set()
    need_visited = ['1']

    while need_visited:
        node = need_visited.pop(0)
        if node in seen: continue
        #print(format(node))
        seen.add(node)
        new_discoveried = graph[node]
        need_visited = concat_func(new_discoveried, need_visited)


def treat_new_discover_more_important(new_discoveried, need_visited):
    return new_discoveried + need_visited


def treat_already_discoveried_more_important(new_discoveried, need_visited):
    return need_visited + new_discoveried

from functools import partial


dfs=partial(search,concat_func=treat_new_discover_more_important)
dfs(graph_long)
#
bfs=partial(search,concat_func=treat_already_discoveried_more_important)
bfs(graph_long)


BJ = 'Beijing'
SZ = 'Shenzhen'
GZ = 'Guangzhou'
WH = 'Wuhan'
HLG = 'Heilongjiang'
NY = 'New York City'
CM = 'Chiangmai'
SG = 'Singapore'

air_route = {
    BJ: {SZ, GZ, WH, HLG, NY},
    GZ: {WH, BJ, CM, SG},
    SZ: {BJ, SG},
    WH: {BJ, GZ},
    HLG: {BJ},
    CM: {GZ},
    NY: {BJ}
}

# import networkx
#
#
#air_oute= networkx.Graph(air_route)
#
#networkkx.draw(air_route1, with_labels=True)
#
#


def search_desitination(graph, start, destination):
    pathes = [[start]]
    seen = set()
    choosen_pathes = []
    while pathes:
        path = pathes.pop(0)
        froniter = path[-1]
        if froniter in seen: continue
        # get new lines

        for city in graph[froniter]:
            new_path = path + [city]
            pathes.append(new_path)
            if city == destination: return new_path

        seen.add(city)
    return choosen_pathes


print(search_desitination(air_route,BJ,SZ))

