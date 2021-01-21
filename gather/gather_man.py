'''
Gather files to local Github_Repository.
'''
import json
from pathlib import Path
import gather_functions as fct

print('==== This is The GatherMan. ====')

while True:
    choose0 = fct.option_button(0, 1, 'Exit', 'Update', 'Browse existing file_couple',\
        'New file_couple', 'Change root directory')

    if choose0 == 0:
        break
    else:
        # -------------------load .json---------------------
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
            print('FATAL ERROR: JSON BROKEN, QUIT.')
            break
        notes_n = len(dst_list)
        variation = False
        # -------------------- update file_couples ---------------------
        if choose0 == 1:
            for n in range(notes_n):
                src_name = fct.get_filename_from_path(src_list[n])
                dst_name = fct.get_filename_from_path(dst_list[n])
                if src_name == dst_name:
                    src_path = src_root_dir + src_list[n]
                    dst_path = dst_root_dir + dst_list[n]
                    if not fct.file_cmp_text(src_path, dst_path):
                        fct.copy_file_text(src_path, dst_path)
                        print(f'{dst_name} = {src_path} ==> {dst_path}')
                    else:
                        print(f'{dst_name} \t= Remains')
                else:
                    print(f'{src_name} doesn\'t match {dst_name}')
            variation = True
        # --------------- show current file_couples ------------------
        elif choose0 == 2:
            print(f'Root dir: {src_root_dir} ==> {dst_root_dir}')
            for n in range(notes_n):
                print(f'{src_list[n]} ==> {dst_list[n]}')
        # -------------- change root directory -------------------
        elif choose0 == 4:
            # source root
            change_sp_r = input(f'Source dir(enter to pass): {src_root_dir} --> ')
            if not change_sp_r:
                change_sp = src_root_dir
            else:
                change_sp = ((repr(change_sp_r))[1:-1]).replace('\\', '/')
            print(change_sp)
            change_sp_P = Path(change_sp)
            if change_sp_P.is_dir():
                src_root_dir = change_sp
                if change_sp[-1] != '/':
                    change_sp = change_sp + '/'
                print(src_root_dir)
            else:
                print(f'Directory {change_sp} is not exist.')
            # destination root
            change_dp_r = input(f'Destination dir(enter to pass): {dst_root_dir} --> ')
            if not change_dp_r:
                change_dp = dst_root_dir
            else:
                change_dp = ((repr(change_dp_r)).replace('\\', '/'))[1:-1]
            change_dp_P = Path(change_dp)
            if change_dp_P.is_dir():
                if change_dp[-1] != '/':
                    change_dp = change_dp + '/'
                dst_root_dir = change_dp
                print(dst_root_dir)
            else:
                print(f'Directory {change_dp} is not exist.')
            variation = True
        # ---------------- create new file_couple --------------------
        elif choose0 == 3:
            choose1 = fct.option_button(1, 2, 'Cancel', 'Auto Update', 'User Define')
            variation = True
            if choose1 == 1:
                print('Under construction.')
                variation = False
            elif choose1 == 2:
                # get source
                while True:
                    set_src = ((repr(input(f'Source: {src_root_dir}'))).replace('\\', '/'))[1:-1]
                    set_src_path = src_root_dir + set_src
                    if Path(set_src_path).is_file():
                        break
                    else:
                        print(f'Can not find {set_src}')
                # get destination
                set_dst = ((repr(input(f'Destination: {dst_root_dir}'))).replace('\\', '/'))[1:-1]
                set_dst_path = dst_root_dir + set_dst
                if not Path(set_dst_path).is_file():
                    with open(set_dst_path, 'w') as fcreate:
                        print(f'Can not find {set_dst}, create empty destination.')
                # append to list
                src_list.append(set_src)
                dst_list.append(set_dst)
            else:
                variation = False
    # ----------------- dump .json --------------------
    if variation:
        filenotes["src_root_dir"] = src_root_dir
        filenotes["dst_root_dir"] = dst_root_dir
        filenotes["src_list"] = src_list
        filenotes["dst_list"] = dst_list
        with open('filenotes.json', 'w') as fj:
            json.dump(filenotes, fj, indent=4, sort_keys=True)
    print(16*'-', '\n')


# end = input('\n==== END ====\nEnter anything to exit...')
