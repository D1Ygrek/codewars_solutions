import random

class BefungeResolver():
    x = None
    y = None
    matrix = None
    buffer = None
    output = None
    direction = None
    is_running = None
    string_mode = None

    def change_direction(self,dir):
        self.direction = dir

    def add_digit(self, digit):
        self.buffer.append(digit)
    
    def empty(self, nth):
        pass

    def stop(self, stop_symbol):
        self.is_running = False

    def output(self, pop_out_symbol):
        self.output+=str(self.buffer.pop())    
       
    def a_b(self, action):
        a = int(self.buffer.pop())
        b = int(self.buffer.pop())
        if action == '+':
            self.buffer.append(a+b)
        elif action == '-':
            self.buffer.append(b-a)
        elif action == '*':
            self.buffer.append(a*b)
        elif action == '/':
            if a == 0:
                self.buffer.append(0)
            else:
                self.buffer.append(b//a)
        elif action == '%':
            if a == 0:
                self.buffer.append(0)
            else:
                self.buffer.append(a%b)
        elif action == '`':
            if b>a:
                self.buffer.append(1)
            else:
                self.buffer.append(0)

    def log_not(self, action):
        if self.buffer.pop() == 0:
            self.buffer.append(1)
        else:
            self.buffer.append(0)

    def random_dir(self, rand_symbol):
        dirs = ['v', '>', '<', '^']
        self.direction = dirs[random.randint(0, 3)]

    def pop_dir(self, dir_symbol):
        if dir_symbol == '_':
            if int(self.buffer.pop()) == 0:
                self.direction = '>'
            else:
                self.direction = '<'
        elif dir_symbol == '|':
            if int(self.buffer.pop()) == 0:
                self.direction = 'v'
            else:
                self.direction = '^'

    def activate_string_mode(self, act_symbol):
        self.string_mode = True
    
    def duplicate(self, dup_symbol):
        if len(self.buffer) == 0:
            self.buffer.append(0)
        else:
            self.buffer.append(self.buffer[-1])
    
    def swap(self, change_symbol):
        first = self.buffer.pop()
        second = 0
        if len(self.buffer) != 0:
            second = self.buffer.pop()
        self.buffer.append(first)
        self.buffer.append(second)

    def pop_value(self, pop_symbol):
        self.buffer.pop()
    
    def output_ascii(self, pop_out_symbol):
        self.output+=chr(self.buffer.pop())

    def trampline(self, tr_symbol):
        self.move()

    def put(self, put_symbol):
        y = int(self.buffer.pop())
        x = int(self.buffer.pop())
        v = int(self.buffer.pop())
        list_to_change = list(self.matrix[y])
        list_to_change[x] = chr(v)
        self.matrix[y] = ''.join(list_to_change)
    
    def get(self, get_symbol):
        y = int(self.buffer.pop())
        x = int(self.buffer.pop())
        self.buffer.append(ord(self.matrix[y][x].encode('ascii')))

    op_codes = {
        'v':change_direction,
        '>':change_direction,
        '<':change_direction,
        '^':change_direction,
        '0':add_digit,
        '1':add_digit,
        '2':add_digit,
        '3':add_digit,
        '4':add_digit,
        '5':add_digit,
        '6':add_digit,
        '7':add_digit,
        '8':add_digit,
        '9':add_digit,
        ' ':empty,
        '@':stop,
        '.':output,
        '+':a_b,
        '-':a_b,
        '/':a_b,
        '*':a_b,
        '%':a_b,
        '!':log_not,
        '`':a_b,
        '?':random_dir,
        '_':pop_dir,
        '|':pop_dir,
        '"':activate_string_mode,
        ':':duplicate,
        "\\":swap,
        '$':pop_value,
        ',':output_ascii,
        '#':trampline,
        'p': put,
        'g': get

    }

    def __init__(self):
        pass
    
    def read_command(self, command):
        self.op_codes[command](self,command)

    def move(self):
        if self.direction == 'v':
            self.y+=1
        elif self.direction == '>':
            self.x+=1
        elif self.direction == '<':
            self.x-=1
        elif self.direction == '^':
            self.y-=1

    def parse_string_mode(self, val):
        if val == '"':
            self.string_mode = False
        else:
            self.buffer.append(ord(val.encode('ascii')))

    def interpretator(self,matrix):
        self.x = 0
        self.y = 0
        self.matrix = matrix
        self.buffer = []
        self.output = ''
        self.direction = '>'
        self.is_running = True
        self.string_mode = False
        while self.is_running:
            print(self.buffer)
            print(self.matrix[self.y][self.x])
            if not self.string_mode:
                self.read_command(self.matrix[self.y][self.x])
            else:
                self.parse_string_mode(self.matrix[self.y][self.x])
            if self.is_running:
                self.move()
        print(self.output)

def matrix_generator(befunge_string):
    response = befunge_string.split('\n')
    return response

def interpret(code):
    output = ""
    compiler = BefungeResolver()
    output = compiler.interpretator(matrix_generator(code))
    return output


#interpret('>9#7v>.v\nv456<  :\n>321 ^ _@')
#interpret('>                          v\n@,,,,,,,,,,,,"Hello World!"<')
#interpret('62*1+v>01p001>+v>\:02p\:02gv\n     0       ^             <\n     .         :p\n     "         .1\n        v 0," "<0\n     "  >1g12-+:|\n     ,          @\n     >^')
interpret('08>:1-:v v *_$.@\n  ^    _$>\:^\n08>:1-:v v *_$.@\n  ^    _$>\:^')