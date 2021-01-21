
# compare 2 files
def file_cmp_text(file0_, file1_):
    try:
        f0 = open(file0_, 'r', encoding='utf-8')
    except FileNotFoundError:
        print(f'Can not find {file0_}')
        return True
    try:
        f1 = open(file1_, 'r', encoding='utf-8')
    except FileNotFoundError:
        f1 = open(file1_, 'w')
        print('[Create]', end='')
        f1 = open(file1_, 'r', encoding='utf-8')
    #  compare
    while True:
        line0 = f0.readline()
        line1 = f1.readline()
        if not line0 and not line1:
            # print('--> CMP-Identical.')
            f0.close()
            f1.close()
            return True
        if line1 != line0:
            # print('--> CMP-Different.')
            f0.close()
            f1.close()
            return False

# copy text file from file0 to file1
def copy_file_text(file_src_, file_dst_):
    f_src = open(file_src_, 'r', encoding='utf-8')
    f_dst = open(file_dst_, 'w', encoding='utf-8')
    while True:
        line = f_src.readline()
        if not line:
            # print('--> Copy-Done.')
            break
        f_dst.write(line)
    f_src.close()
    f_dst.close()


# strip filename from path(py style)
def get_filename_from_path(path_):
    try:
        x_index = path_.rfind('/')
    except AttributeError:
        print('Error.')
    if x_index == -1:
        return path_
    else:
        return path_[x_index+1:]


# show user options, get the choice of user
def option_button(layer_, default_, *options_):
    # show the option layer
    print(f'Option_{layer_}:')
    options_n = len(options_)
    # get default choice
    try:
        default_ = int(default_)
    except ValueError:
        default_ = 0
        print('[ERROR-options_button]Invalid default option, reset to 0.')
    else:
        if default_ >= options_n:
            default_ = 0
            print('[ERROR-options_button]Invalid default option, reset to 0.')
    # show options
    for n in range(options_n):
        if n != default_:
            print(f'({n}) {options_[n]}')
        else:
            print(f'[{n}] {options_[n]}')
    while True:
        button = input('>>>')
        if not button:
            button = default_
            break
        elif button in [str(n) for n in range(options_n)]:
            break
        else:
            print('Invalid option, try again pls.')
    return int(button)
