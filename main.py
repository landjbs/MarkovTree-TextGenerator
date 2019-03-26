import time
from importer import process_text_folder

# timing stuff
start = time.time()

sample = process_text_folder("sample_texts")

end = time.time()

print(len(sample))
print(end - start)
