from ciphergen_class import Settings, color
import sys, pyfiglet

def main():
    password = Settings()
    print(execute(password, '.help'))
    while True:
        result = execute(password, input().lower())
        if result:
            print(result)

def check_arg(command):
    values = command.split(' ')
    if len(values) == 1:
        raise ValueError('Missing 1 additional argument')
    else:
        return values[1]
        
def execute(object, command):
    command = command.strip()
    # CUSTOMIZATION
    if command.startswith('.len'):
        try:
            arg = check_arg(command)
            return format_complete(exe_len(object, arg))

        except Exception as e:
            return format_error(str(e))
            
    elif command.startswith('.ena'):
        try:
            arg = check_arg(command)
            return format_green(exe_enable(object, arg))

        except Exception as e:
            return format_error(str(e))

    elif command.startswith('.dis'):
        try:
            arg = check_arg(command)
            return format_red(exe_disable(object, arg))

        except Exception as e:
            return format_error(str(e))

    elif command.startswith('.num'):
        try:
            arg = check_arg(command)
            return format_complete(exe_number(object, arg))

        except Exception as e:
            return format_error(str(e))

    elif command.startswith('.spe'):
        try:
            arg = check_arg(command)
            return format_complete(exe_special(object, arg))

        except Exception as e:
            return format_error(str(e))
    
    # UTILITY
    elif command.startswith('.set'):
        return exe_settings(object)
    
    elif command.startswith('.res'):
        try:
            return format_complete(exe_reset(object))

        except ValueError as e:
            return format_error(str(e))

        except Exception as e:
            return format_yellow(str(e))

    elif command.startswith('.gen'):
        try:
            if ' ' not in command:
                arg = 1
            else:
                arg = check_arg(command)
            return format_complete(exe_generate(object, arg))
        except ValueError as e:
            return format_error(str(e))
        
    elif command.startswith('.hel'):
        return exe_help()

    elif command.startswith('.exit'):
        sys.exit(format_complete('Thank you for using CipherGen!'))
    
    # UNKNOWN
    elif not command:
        return None
    
    else:
        return format_error('Invalid command')

def exe_len(object, arg):
    object.len = arg
    return f'Password length set to {arg}'

def exe_enable(object, arg):
    if 'up' in arg:
        object.uppercase = True
        return 'Enabled uppercase characters'
    elif 'low' in arg:
        object.lowercase = True
        return 'Enabled lowercase characters'
    elif 'num' in arg:
        object.number = True
        return 'Enabled numbers'
    elif 'spe' in arg:
        object.special = True
        return 'Enabled special characters'
    else:
        raise Exception(f'Argument is invalid')
    
def exe_disable(object, arg):
    if 'up' in arg:
        object.uppercase = False
        return 'Disabled uppercase characters'
    elif 'low' in arg:
        object.lowercase = False
        return 'Disabled lowercase characters'
    elif 'num' in arg:
        object.number = False
        return 'Disabled numbers'
    elif 'spe' in arg:
        object.special = False
        return 'Disabled special characters'
    else:
        raise Exception(f'Argument is invalid')

def exe_number(object, arg):
        old_len = object.len
        object.min_number = arg
        result = f'Minimum amount of numbers is set to {object.min_number}'
        
        if old_len != object.len:
            result += f'\n{color.END}{color.YELLOW}Current minimum values exceed password length. New length set to {object.len}{color.END}'
        
        return result

def exe_special(object, arg):
            old_len = object.len
            object.min_special = arg
            result = f'Minimum amount of special characters is set to {object.min_special}'
            
            if old_len != object.len:
                result += f'\n{color.END}{color.YELLOW}Current minimum values exceed password length. New length is set to {object.len}{color.END}'

            return result

def exe_settings(object):
    nl = '\n' # Python doesn't allow backslash in f-string expression
    settings = f'''
{color.BOLD}CURRENT SETTINGS{color.END}
-------------------------------------
Password length: {color.CYAN}{object.len}{color.END}
Include uppercase (A-Z): {color.GREEN if object.uppercase == True else color.RED}{object.uppercase}{color.END}
Include lowercase (a-z): {color.GREEN if object.lowercase == True else color.RED}{object.lowercase}{color.END}
Include numbers (0-9): {color.GREEN if object.number == True else color.RED}{object.number}{color.END}{f'{nl}Minimum numbers: {object.min_number}' if object.number == True else ''}
Include special: {color.GREEN if object.special == True else color.RED}{object.special}{color.END}{f'{nl}Minimum special: {object.min_special}' if object.special == True else''}\n'''

    return settings

def exe_reset(object):
    ans = input(format_green('Would you like to reset all settings? (y/n) ')).lower()
    if ans in ('y', 'ye', 'yes'):
        object.uppercase = True
        object.lowercase = True
        object.number = True
        object.special = True
        object.min_number = 1
        object.min_special = 1
        object.len = 5
        return 'Default settings restored'
    
    elif ans in ('n', 'no'):
        raise Exception(format_yellow('Settings unchanged'))
    
    else:
        raise ValueError('Invalid command')

def exe_generate(obj, arg):
    try:
        n = int(arg)
    except:
        raise ValueError('Argument must be an integer')
    
    if n < 1 or n > 10:
        raise ValueError('Can only generate 1 to 10 passwords at once')
    
    result = list()
    for i in range(n):
        result.append(obj.generate())
        
    return '\n'.join(result)

def exe_help():
    title = pyfiglet.figlet_format("CipherGen", font="kban")
    
    return f'''
{color.BOLD}{title}CUSTOMIZATION{color.END}
-------------------------------------
{color.BOLD}.length{color.END} [int] -> Set password length
{color.BOLD}.enable/disable{color.END} [upper/lower/number/special] -> Enable/disable the corresponding type of character
{color.BOLD}.number{color.END} [int] -> Set the minimum amount of numbers
{color.BOLD}.special{color.END} [int] -> Set the minimum amount of special characters

{color.BOLD}UTILITY{color.END}
-------------------------------------
{color.BOLD}.settings{color.END} -> See current settings
{color.BOLD}.reset{color.END} -> Reset settings to default
{color.BOLD}.generate{color.END} -> Generate a random password with current settings
{color.BOLD}.help{color.END} -> Display available commands
{color.BOLD}.exit{color.END} -> Exit application
'''

def format_green(text):
    return f'{color.GREEN}{text}{color.END}\n'

def format_red(text):
    return f'{color.RED}{text}{color.END}\n'

def format_yellow(text):
    return f'{color.YELLOW}{text}{color.END}\n'

def format_complete(text):
    return f'{color.BOLD}{color.GREEN}{text}{color.END}\n'

def format_error(text):
    return f'{color.BOLD}{color.RED}{text}{color.END}\n'

if __name__ == '__main__':
    main()