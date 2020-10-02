"""
2 вариант.
Получить на вход два файла с предложениями в формате CONLL. 
В памяти сформировать деревья предложений, 
вывести деревья предложений в консоль, используя пробелы для форматных отступов. 
Определить, является ли второе дерево поддеревом первого.

NB:
В чате написали, что вопрос омонимии деревьев решается на усмотрение студента.
Мне кажется, что дерево_1 (родитель: А; потомки: Б, В) != дерево_2 (родитель: А; потомки: В, Б)
Например,  дереву_1 соответствует предложение "она упала и заплакала",
а дереву_2 – предложение "она заплакала и упала". С семантической точки зрения предложения не омонимичны,
хотя 'упала' и 'заплакала' соседи и у них общий предок. 
И больше всего будет заметна разница предложений, если мы захотим по дереву восстановить предложение, 
как мы делали на одной из лекций.
"""


def tree_of_sentence(filename):
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        words = [l.split() for l in lines]

        tokens = [w[2] for w in words]
        nodes = [('root', [])]
        nodes.extend([(t, []) for t in tokens])

        for num, word in enumerate(words):
            nodes[int(word[6])][1].append(nodes[num+1])
        return nodes[0]


def print_tree(node, shift=0):
    print(' ' * shift, node[0])
    for child in node[1]:
        print_tree(child, shift+2)


def convert_tree(tree):
    res = tree[0]
    for elem in tree[1]:
        res += convert_tree(elem)
    return res


def is_subtree_in_tree(tree, subtree):
    return convert_tree(subtree) in convert_tree(tree)


if __name__ == '__main__':
    tree1 = tree_of_sentence('tree1.txt')
    tree2 = tree_of_sentence('tree2ns.txt')

    print('The first tree:')
    print_tree(tree1)

    print(f'\nThe second tree:')
    print_tree(tree2)

    print(f'\nIs the second tree is a subtree for the first one: {is_subtree_in_tree(tree1, tree2)}.')
