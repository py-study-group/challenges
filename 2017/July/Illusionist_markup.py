import re

''' Sample text I was using in "sample.txt" to test the file input ----

[b][01-01-2017 12:30:22][::] [red]Error:[::] This is a quick error.
[b][02-01-2017 11:28:33][::] [green]Update completed.[::]
[b][03-01-2017 22:01:13][::] [yellow:b]Warning, disk space running out.[::]

'''

def colorize(string):
    '''
    Takes a string, subs any markup for ansi escape codes and returns it.
    Markup format has [] with markup inside it before the string to colorize
    and a [::] afterwards to reset the terminal.
    Example: [b:u:red]This is underlined, bolded and red text.[::]
    '''

    # dictionary of ansi escape codes
    formatting = {
        'b': '\033[1m',
        'u': '\033[4m',
        'reverse': '\033[7m',
        'black': '\033[30m',
        'red': '\033[31m',
        'yellow': '\033[33m',
        'magenta': '\033[35m',
        'blue': '\033[34m',
        'green': '\033[32m'
    }

    # reset ansi escape code
    reset = '\u001b[0m'


    # markup_outer gets the whole markup section e.g [b:green]
    # markup_inner gets the string from the markup e.g b:green

    markup_outer = re.compile(r'\[(\w+\:?)+\]')
    markup_inner = re.compile(r'(?<=\[)(\w+\:?)+')


    # iterates through the matches of markup
    for x in markup_outer.finditer(string):
        # grabs the inner of the markup from the above match
        y = markup_inner.search(x.group())

        # take the markup as keys, use them to get values and create string from it
        final_string = ''.join(str(formatting.get(word, word)) for word in re.split('\:', y.group() ))
        string = re.sub('\[(\w+\:?)+\]', final_string, string, 1)
        # replace any end codes with the reset code
        string = re.sub('\[\:\:\]', reset, string)

    return string


def test_unit():
    '''
    Some tests that show off some of the combos of the markup codes.
    '''

    print(colorize('[red]This is a quick error![::]'))
    print(colorize('[red:b]This is a bold error![::]'))
    print(colorize('[yellow]Warning Mode.[::]'))
    print(colorize('[green:u]Everything is now fine.[::]'))


def file_color(path):
    '''
    Takes a file, reads it into a string, and prints a colorized version to stdout
    '''

    try:
        f = open(path, 'r')
        file_content = f.read()
        print(colorize(file_content))
        f.close()

    except IOError:
        print(colorize('[b:red]That file cannot be found. Please correct filename.[::]'))
        return

file_color('./sample.txt')
