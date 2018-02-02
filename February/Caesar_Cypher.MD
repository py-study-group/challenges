# Febuary Challenge

For this month, your challenge is to write a Caesar cipher encoder/decoder. For those not familiar with a Caeser cipher, it is one of the simplest and most widely known encryption techniques. It is a substitution cipher in which one letter is transposed by another. The replacement of a letter with another is based on the 'shift' of the cipher. For example if the shift was +1, 'a' would become 'b' and 'b' would become 'c' this continues all the way down the line until you get to the letter 'z' which becomes 'a'.  
Here is another example of a shift with +3 (the top line is the original and the bottom is the cipher results):
    
    ABCDEF...XYZ
    DEFGHI...ABC

## Brackets 🔱

**Beginner** 👶

Write two python scripts that can encode/decode input based on a fixed shift. - The amount and direction of the shift is up to you.
* Encode: Your encode script should ask the user for a sentence and then print the results of the encoded text.
* Decode: Your decode script should ask the user for a sentence and then print the results of the decoded text.

**Intermediate** 🛠️

Write one python script/function that can encode and decode text based on the supplied shift. The script should have the following arguments: 
  * `encode`/`decode` - Required. The action the script will take.
  * `shift` - Required. The amount of shift applied to encoding ord decoding the text.
  * `-f, --file` - Optional. The file to encode/decode
  * `-t, --text` - Optional. The text to encode/decode
  * If a `file` and `text` argument is not provided the script should ask the user for input.

The script should print the results to the screen.

**Advanced** 🤓

Write a python script that will take a file as input and 'guess' the correct shift to decode the text. The challenge will be to apply some sort of natural language processing to the decryption and based on the results determine the correct shift.

## Resources 📃

* [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
* [Asking the user for input](https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html)
* [Argument Parser](https://docs.python.org/3/library/argparse.html)
* [Natural Language Toolkit](http://www.nltk.org/)
