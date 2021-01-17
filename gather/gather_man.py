'''
Gather files to local Github_Repository.
'''
import json
from pathlib import Path
import gather_functions as fct

print('==== This is GatherMan. ====')

while True:
    choose0 = fct.option_button(0, 1, 'Exit', 'Update', 'Browse existing file_couple',\
        'New file_couple', 'Change root directory')

    if choose0 == 0:
        break
    else:
        # load json
        try:
            with open('filenotes.json', 'r') as fj:
                filenotes = json.load(fj)
                # print(filenotes)
                src_root_dir = filenotes["src_root_dir"]
                dst_root_dir = filenotes["dst_root_dir"]
                src_list = filenotes["src_list"]
                dst_list = filenotes["dst_list"]
            # print(src_root_dir, src_list)
            # print(dst_root_dir, dst_list)
        except FileNotFoundError:
            print('JSON BROKEN')
            break
        notes_n = len(dst_list)
        if choose0 == 1:        # update
            for n in range(notes_n):
                src_name = fct.get_filename_from_path(src_list[n])
                dst_name = fct.get_filename_from_path(dst_list[n])
                if src_name == dst_name:
                    src_path = Path(src_root_dir + src_list[n])
                    dst_path = Path(dst_root_dir + dst_list[n])
                    if not fct.file_cmp_text(src_path, dst_path):
                        fct.copy_file_text(src_path, dst_path)
                        print(f'{dst_name} = {src_path} ==> {dst_path}')
                    else:
                        print(f'{dst_name} \t= Remains')
                else:
                    print(f'{src_name} doesn\'t match {dst_name}')
        elif choose0 == 2:      # show
            print(f'Root dir: {src_root_dir} ==> {dst_root_dir}')
            for n in range(notes_n):
                print(f'{src_list[n]} ==> {dst_list[n]}')
        elif choose0 == 4:      # change root directory
            change_sp = Path(input(f'Source dir: {src_root_dir} --> '))
            if change_sp.is_dir():
                src_root_dir = change_sp
            else:
                print(f'Directory {change_sp} is not exist.')
            change_dp = Path(input(f'Destination dir: {dst_root_dir} --> '))
            if change_dp.is_dir():
                dst_root_dir = change_dp
            else:
                print(f'Directory {change_dp} is not exist.')


    # refresh .json
    filenotes["src_root_dir"] = src_root_dir
    filenotes["dst_root_dir"] = dst_root_dir
    filenotes["src_list"] = src_list
    filenotes["dst_list"] = dst_list
    with open('filenotes.json', 'w') as fj:
        json.dump(filenotes, fj, indent=4, sort_keys=True)

# end = input('\n==== END ====\nEnter anything to exit...')
