'''
Gather files to local Github_Repository.
'''
import json
import gather_functions as fct

with open('filenotes.json', 'r') as fj:
    filenotes = json.load(fj)
    # print(filenotes)
    src_root_dir = filenotes["src_root_dir"]
    dst_root_dir = filenotes["dst_root_dir"]
    src_list = filenotes["src_list"]
    dst_list = filenotes["dst_list"]

# print(src_root_dir, src_list)
# print(dst_root_dir, dst_list)

notes_n = len(src_list)
for n in range(notes_n):
    src_name = fct.get_filename_from_path(src_list[n])
    dst_name = fct.get_filename_from_path(dst_list[n])
    if src_name == dst_name:
        src_path = src_root_dir + src_list[n]
        dst_path = dst_root_dir + dst_list[n]
        if not fct.file_cmp_text(src_path, dst_path):
            fct.copy_file_text(src_path, dst_path)
            print(f'{dst_name} = {src_path} --> {dst_path}')
        else:
            print(f'{dst_name} \t= Remains')
    else:
        print(f'{src_name} != {dst_name}')


# src = 'test_class.py'
# dst = 'test_class2.py'
# different = not fct.file_cmp_text(src, dst)
# if different:
#     fct.copy_file_text(src, dst)

# end = input('\n==== END ====\nEnter anything to exit...')
