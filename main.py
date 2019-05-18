from importer import process_mutable, process_text
from classes_test import Node
import time

SAMPLE_NAME = "sample_texts/thegreatgatsby.txt"

sample, type = process_mutable(SAMPLE_NAME)

sample_length = len(sample)
print(f"Imported {sample_length} samples from {type}, {SAMPLE_NAME}")
n = 10
tree = Node(sample[0:n], sample[n])

for i in range(1,sample_length-(n+1)):
    print(f"|Loading: {round(i/sample_length, 2)}", end="\r")
    tree.search_add(sample[i:i+n], sample[i+n+1])
print("Loading complete!")

# print(sample[500:500+n], tree.nav(sample[500:500+n]))
gen_words = 500
gen_text = []

# user_seed = input("Seed:\n")

# if (set(process_text(user_seed))).issubset(set(sample)):
#     seed = process_text(user_seed)
# else:
#     raise ValueError("Usage: seed must be in sample")

seed = process_text("this")

for i in range(gen_words):
    next = False
    order = n
    while next == False:
        next = tree.nav(seed[-order:])
        order += -1
    seed.append(next)

textString = " ".join(seed)

print(f"GENERATED TEXT:\n{textString}\n")
