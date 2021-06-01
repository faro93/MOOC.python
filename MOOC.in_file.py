#coding utf-8

def comptage(in_filename, out_filename):
    with open (in_filename, 'r', encoding='utf-8') as fin:
        linenum = 0
        words = 0
        chars = 0
        lines_out = list()
        for line in fin:
            linenum += 1
            words = len(line.split())
            chars = len(line)
            lines_out.append(f'{linenum}:{words}:{chars}:{line}')

    with open(out_filename, 'w', encoding='utf-8') as fout:
        for line in lines_out:
            fout.write(line)
        fout.close()

if __name__ == '__main__':
    comptage('MOOC.in_file.txt', 'MOOC.out_file.txt')