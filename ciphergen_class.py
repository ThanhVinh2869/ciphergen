import string, random

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Settings:
    def __init__(self):
        self._uppercase = True
        self._lowercase = True
        self._number = True
        self._special = True

        self._len = 5
        self._min_number = 1
        self._min_special = 1

    def generate(self):
        unshuffled = ''
        c = ''
         
        # add min amount of number 
        if self.number:
            c += string.digits
            for i in range(self.min_number):
                unshuffled += random.choice(string.digits)

        # add min amount of special characters
        if self.special:
            c += string.punctuation
            for i in range(self.min_special):
                unshuffled += random.choice(string.punctuation)
    
        # add the rest
        if self.uppercase:
            c += string.ascii_uppercase
            
        if self.lowercase:
            c += string.ascii_lowercase

        for i in range(self.len - len(unshuffled)):
            unshuffled += random.choice(c)
        
        shuffled = list(unshuffled)
        random.shuffle(shuffled)
        return ''.join(shuffled)

    def check_settings(self, attr, value):
        current = {
            'upp': self._uppercase,
            'low': self._lowercase,
            'dig': self._number,
            'spe': self._special
        }
        current[attr] = value
        if not any(current.values()):
            raise ValueError('Cannot set all attributes to False')

    # _uppercase getter & setter
    @property
    def uppercase(self):
        return self._uppercase

    @uppercase.setter
    def uppercase(self, input):
        if not input:
            self.check_settings('upp', input)
        if isinstance(input, bool):
            self._uppercase = input
        else:
            raise TypeError

    # _lowercase getter & setter
    @property
    def lowercase(self):
        return self._lowercase

    @lowercase.setter
    def lowercase(self, input):
        if not input:
            self.check_settings('low', input)
        if isinstance(input, bool):
            self._lowercase = input
        else:
            raise TypeError
        
    # _number getter & setter
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, input):
        if not input:
            self.check_settings('dig', input)
        if isinstance(input, bool):
            self._number = input
        else:
            raise TypeError

    # _special getter & setter
    @property
    def special(self):
        return self._special

    @special.setter
    def special(self, input):
        if not input:
            self.check_settings('spe', input)
        if isinstance(input, bool):
            self._special = input
        else:
            raise TypeError
        
    # _len getter & setter
    @property
    def len(self):
        return self._len

    @len.setter
    def len(self, n):
        try:
            n = int(n)
        except:
            raise TypeError('Password length must be an integer')
        
        if n < 5 or n > 128:
            raise ValueError('Password length must be from 5 to 128')
        elif n < self.min_number + self.min_special + 3:
            raise ValueError(f'Input length below minimum values ({self._min_number + self._min_special + 3})')
        else:
            self._len = n

    # _min_number getter & setter
    @property
    def min_number(self):
        return self._min_number

    @min_number.setter
    def min_number(self, n):
        if self._number == False:
            raise AttributeError('Numbers are disabled')
        try:
            num = int(n)
        except:
            raise TypeError('Minimum value must be an integer')
        
        if num >= 1 and num <= 9:
            self._min_number = num
        else: 
            raise ValueError('Minimum value must be from 1 to 9')
        
        if self._min_number + self._min_special > self.len - 3:
            self.len = self._min_number + self._min_special + 3

    # _min_special getter & setter
    @property
    def min_special(self):
        return self._min_special

    @min_special.setter
    def min_special(self, n):
        if self._special == False:
            raise AttributeError('Special characters are disabled')
        try:
            num = int(n)
        except:
            raise TypeError('Minimum value must be an integer')
        
        if num >= 1 and num <= 9:
            self._min_special = num
        else:
            raise ValueError('Minimum value must be from 0 to 9')
        
        if self._min_number + self._min_special > self.len - 3:
            self.len = self._min_number + self._min_special + 3