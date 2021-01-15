
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
        print('>Creat ', end='')
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


def get_filename_from_path(path_):
    try:
        x_index = path_.rfind('/')
    except AttributeError:
        print('Error.')
    if x_index == -1:
        return path_
    else:
        return path_[x_index+1:]

