from importer import process_mutable
from classes_test import Node

SAMPLE_NAME = "sample_texts"

sample = process_mutable(SAMPLE_NAME)

sample_length = len(sample)
print(f"Loading {sample_length} samples from")
n = 10
tree = Node(sample[0:n], sample[n])

for i in range(1,sample_length-(n+1)):
    if i%20000 == 0:
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
