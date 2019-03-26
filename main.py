import time
from importer import process_text_folder

# time import of sample_text folder
start = time.time()

sample = process_text_folder("sample_texts")

end = time.time()

print(end - start)
print(len(sample))
