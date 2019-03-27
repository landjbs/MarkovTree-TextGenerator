from importer import process_text_folder
from classes import Node

sample = process_text_folder("sample_texts")
tree = Node(sample[0:10], sample[10])
tree.search_add(sample[1:11], sample[11])
tree.search_add(sample[1:11], sample[11])
tree.search_add(sample[1:11], sample[12])


print(len(sample))
