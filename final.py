def get_final_line(filename):
    final_line = ''
    with open(filename) as infile:
        for current_line in infile:
            final_line = current_line
    return final_line

print(get_final_line('/etc/passwd'))
