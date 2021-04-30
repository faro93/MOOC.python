# code utf-8

class Fifo:
    def __init__(self):
        self.fifo = list()

    def incoming(self, value):
        self.fifo.append(value)

    def outgoing(self):
        try:
            return self.fifo.pop(0)
        except IndexError:
            return None

if __name__ == '__main__':
    f = Fifo()
    for i in (1, 2, 5, 4 , 8, 6 , 9, 7, 3):
        print(i)
        f.incoming(i)
    
    print(f'fifo = {f.fifo} avant la purge et contient {len(f.fifo)} éléments.')
    for i in range(len(f.fifo)):
        r = f.outgoing()
        print(f'fifo = {f.fifo} après la suppression de {r} et contient {len(f.fifo)} éléments.')
    
    print(f'fifo = {f.fifo} une fois purgée alors qu\'elle contient {len(f.fifo)} éléments.')
    r = f.outgoing()
    print(f'r = {r} alors que fifo contient {len(f.fifo)} éléments.')
