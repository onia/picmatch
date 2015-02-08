#!/usr/bin/env python
from PIL import Image
import imagehash

ahash1 = imagehash.average_hash(Image.open('1.jpg'))
ahash2 = imagehash.average_hash(Image.open('2.jpg'))

phash1 = imagehash.phash(Image.open('1.jpg'))
phash2 = imagehash.phash(Image.open('2.jpg'))

dhash1 = imagehash.dhash(Image.open('1.jpg'))
dhash2 = imagehash.dhash(Image.open('2.jpg'))

print(ahash1,ahash2,phash1,phash2)
print(ahash2-ahash1,phash1-phash2,dhash1-dhash2)