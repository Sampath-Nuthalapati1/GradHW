from tree_sitter import Language, Parser
from git import Repo
import git
import shutil
import os
import fnmatch
# if os.path.isdir("./GitRepo"):
#     os.chmod("./GitRepo", 0o777)
#     shutil.rmtree("./GitRepo")

# https://github.com/tree-sitter/py-tree-sitter.git
gitURL = input("Enter Git Repo Link: ")
gitRep = ".\\GitRepo"

prg_lang_type = input("Enter one file extension, only python javascript go ruby allowed: ").lower()
print(prg_lang_type)

if prg_lang_type == 'python':
    prg_extension = '.py'
if prg_lang_type == 'javascript':
    prg_extension = '.js'
if prg_lang_type == 'go':
    prg_extension = '.go'
if prg_lang_type == 'ruby':
    prg_extension = '.rb'


Repo.clone_from(gitURL, gitRep)
# print("cloned")


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

required_files = find('*'+prg_extension, gitRep)

# required_files = find('*.py', gitRep)
# required_files.extend(find('*.rb', gitRep))
# required_files.extend(find('*.go', gitRep))
# required_files.extend(find('*.js', gitRep))

print("required_files-----------------------------------------")

print(required_files)

Language.build_library(
  # Store the library in the `build` directory
  'build/my-languages.so',

  # Include one or more languages
  [
    'vendor/tree-sitter-go',
    'vendor/tree-sitter-javascript',
    'vendor/tree-sitter-python',
    'vendor/tree-sitter-ruby',
  ]
)

GO_LANGUAGE = Language('build/my-languages.so', 'go')
JS_LANGUAGE = Language('build/my-languages.so', 'javascript')
PY_LANGUAGE = Language('build/my-languages.so', 'python')
# RB_LANGUAGE = Language('build/my-languages.so', 'ruby')

if prg_lang_type == 'python':
    Lang = Language('build/my-languages.so', 'python')
if prg_lang_type == 'ruby':
    Lang = Language('build/my-languages.so', 'ruby')
if prg_lang_type == 'go':
    Lang = Language('build/my-languages.so', 'go')
if prg_lang_type == 'javascript':
    Lang = Language('build/my-languages.so', 'javascript')

parser = Parser()
parser.set_language(Lang)
#


text_file = open(required_files[0], "r")
data = text_file.read()
text_file.close()

tree = parser.parse(bytes(data, "utf-8"))
print("tree:")
print(tree)

root_node = tree.root_node

# function_node = root_node.children[0]

print("identifier?")
# print(root_node.children[0].type)
#
# children = root_node.children
print("entered for loop:")

li = []


def recur(childr):
    for child in childr.children:
        if child.type =='identifier':
            print(child)
            li.append(child)
            # li.append(child)
        recur(child)

recur(root_node)

print('li==================================================================================================================================================')

print(required_files[0])
with open(required_files[0], "r") as f:
    code_file = f.readlines()
    output1_list = []
    print("asjfljasl;f")
    print(code_file[0])
    print(code_file[1])
    print(code_file[2])
    print(code_file[3])
    for i in range(len(li)):

        line_number = li[i].start_point[0]
        start_index = li[i].start_point[1]
        end_index = li[i].end_point[1]


        name_identifier = code_file[line_number][start_index:end_index]

        output1_list.append('Identifier: '+str(name_identifier)+ '   line number: '+ str(line_number) +'   Start index: '+ str(start_index) + '    End index: ' + str(end_index))



    # open text file
    output1 = open("./Output1.txt", "w")
    # output2 = open("./Output1.txt", "w")
    output1.write('')
    # output1.write('Hello World!')
    # dictionary = {'item': 1, 'cursor': 5}
    for i in range(len(output1_list)):
        # identifier
        output1.write("%s : " % i)
        # location
        output1.write("%s \n" % output1_list[i])

    # close file
    output1.close()
    # output2.close()