from importer import process_text, read_file, process_text_folder
from classes_test import Node



# sample = process_text_folder("sample_texts")
sample = process_text(read_file("sample_texts/prideandprejudice.txt"))
sample_length = len(sample)
print(sample_length)
n = 10
tree = Node(sample[0:n], sample[n])

for i in range(1,sample_length-(n+1)):
    if i%10000 == 0:
        print(f"{i} | {sample_length}")
    tree.search_add(sample[i:i+n], sample[i+n+1])

# print(sample[500:500+n], tree.nav(sample[500:500+n]))
gen_words = 100
gen_text = []

user_seed = input("Seed:\n")

if (set(process_text(user_seed))).issubset(set(sample)):
    seed = process_text(user_seed)
else:
    raise ValueError("Usage: seed must be in sample")

for i in range(gen_words):
    next = False
    order = n
    while next == False:
        next = tree.nav(seed[-order:])
        order += -1
    seed.append(next)

print(" ".join(seed))
