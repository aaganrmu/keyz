ENTER = "ENTER"
DEFAULT_ALPHABET = "`1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,.~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?"
DEFAULT_PASSWORD_LENGTH = 64

class Password:
    def __init__(self, pad_filename='pad'):
        with open(pad_filename, 'r') as file:
            self.pad = file.readline()
        self.alphabet = DEFAULT_ALPHABET
        self.password_length = DEFAULT_PASSWORD_LENGTH
        self._reset_stream()

    def process(self, code, pressed):
        print(code)
        if not pressed:
            return
        if code is ENTER:
            password = self._generate()
            print(password)
            return
        self._stream += code
        print(self._stream)

    def _generate(self):
        i_str = 0
        i_pad = 0
        i_alf = 0
        password = ""
        for i in range(1,self.password_length):
            n_str = int(self._stream[i_str])
            n_pad = int(self.pad[i_pad])

            d_pad = (n_str + 2) ** (n_pad + 1)
            d_alp = (n_pad + 2) ** (n_str + 1)

            i_pad = (i_pad + d_pad) % len(self.pad)
            i_alp = (i_alp + d_alp) % len(self.alphabet)
            i_str = (i_str + 1) % len(self._stream)

            password += self.alphabet[i_alp]
        self._reset_stream()
        return password


    def _reset_stream(self):
        self._stream = ""