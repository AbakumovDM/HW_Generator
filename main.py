import hashlib

def my_gen(file_path):
  with open(file_path, 'rb') as file:
    for line in file:
      yield hashlib.md5(line).hexdigest()

for item in my_gen('text_for_hash.txt'):
  print(item)

