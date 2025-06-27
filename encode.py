import sys, locale

expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """

my_file = open('dummy', 'w')

for expression in expressions.split():
    try:
        if expression == 'locale.getpreferredencoding()':
            value = locale.getpreferredencoding()
        elif expression == 'type(my_file)':
            value = type(my_file)
        elif expression == 'my_file.encoding':
            value = getattr(my_file, 'encoding', None)
        elif expression == 'sys.stdout.isatty()':
            value = sys.stdout.isatty()
        elif expression == 'sys.stdout.encoding':
            value = sys.stdout.encoding
        elif expression == 'sys.stdin.isatty()':
            value = sys.stdin.isatty()
        elif expression == 'sys.stdin.encoding':
            value = sys.stdin.encoding
        elif expression == 'sys.stderr.isatty()':
            value = sys.stderr.isatty()
        elif expression == 'sys.stderr.encoding':
            value = sys.stderr.encoding
        elif expression == 'sys.getdefaultencoding()':
            value = sys.getdefaultencoding()
        elif expression == 'sys.getfilesystemencoding()':
            value = sys.getfilesystemencoding()
        else:
            value = 'N/A'
        print(f'{expression:>30} -> {value!r}')
    except Exception as e:
        print(f'{expression:>30} -> Error: {e}')