class vocab_node:
    def __init__(self):
        self.val = 0
        self.letter = ''
        self.id = []
        self.children = [None]*26

def build_vocab(vocab, root_ls):
    ref_ls = root_ls
    for id, word in enumerate(vocab):
        root_ls = ref_ls
        for ind, ch in enumerate(word):
            print([root_ls[x].letter for x in range(26)])
            root = root_ls[ord(ch) - 97]
            root.letter = ch
            root.id.append(id)
            print([root_ls[x].letter for x in range(26)], '\n')
            if ind==len(word)-1:
                root.val = 1
            else:
                if not all(root.children):
                    root.children = [vocab_node() for x in range(26)]
                root_ls = root.children
        print('\n\n')

vocab = ['ship', 'shop', 'shape', 'stop', 'hello', 'hellen', 'man', 'mango', 'manic']
prefix = 'man'
root_list = [vocab_node() for x in range(26)]
build_vocab(vocab, root_list)

# print([root_list[18].children[x].id for x in range(26)])
# print(root_list[18].children[7].letter)
# print([root_list[18].children[7].children[x].letter for x in range(26)])

def traverse_prefix(prefix, root_ls):
    for ind, ch in enumerate(prefix):
        if ind == len(prefix)-1:
            return root_ls[ord(ch)-97].id
        root_ls = root_ls[ord(ch)-97].children
        # print([root_ls[x].letter for x in range(26)])

print([vocab[x] for x in traverse_prefix(prefix, root_list)])
