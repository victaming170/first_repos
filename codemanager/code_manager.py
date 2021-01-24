'''
Gather files to local Github_Repository.
'''
import json
from pathlib import Path
import code_manager_func as fct

print(35*'=')
print('==== This is The Code Manager. ====')
print(35*'=')

# filenotes initialize
filenotes = {
    "central_list": [],
    "central_root": "D:/WorkspaceMX/Mithub/",
    "local_list": [],
    "local_root": "D:/WorkspaceMX/Python_PJ/"
}

while True:
    choose0 = fct.option_button(0, 1, 'Exit', 'Update to central', 'Download to local', 'Browse existing file_couple',\
        'New file_couple', 'Change root directory')

    if choose0 == 0:
        break
    else:
        # ------------------- load .json---------------------
        try:
            with open('filenotes.json', 'r') as fj:
                filenotes = json.load(fj)
                # print(filenotes)
                local_root = filenotes["local_root"]
                central_root = filenotes["central_root"]
                local_list = filenotes["local_list"]
                central_list = filenotes["central_list"]
            # print(local_root, local_list)
            # print(central_root, central_list)
        except FileNotFoundError:
            print('FATAL ERROR: JSON BROKEN, CREATE NEW ONE.')
        notes_n = len(central_list)
        variation = False
        # -------------------- update file_couples --------------------
        if choose0 == 1 or choose0 == 2:
            for n in range(notes_n):
                local_path = local_root + local_list[n]
                central_path = central_root + central_list[n]
                if not fct.file_cmp_text(local_path, central_path):
                    if choose0 == 1:
                        fct.copy_file_text(local_path, central_path)
                        print(f'{local_path} ==>> {central_path}')
                    else:
                        fct.copy_file_text(central_path, local_path)
                        print(f'{central_path} ==>> {local_path}')
                    variation = True
                else:
                    print(f'{local_path} == {central_path}')
        # --------------- show current file_couples ------------------
        elif choose0 == 3:
            print(f'Root dir: {local_root} <==> {central_root}')
            for n in range(notes_n):
                print(f'{local_list[n]} <==> {central_list[n]}')
        # -------------- change root directory -------------------
        elif choose0 == 5:
            # source root
            change_sp_r = input(f'Source dir(enter to pass): {local_root} --> ')
            if not change_sp_r:
                change_sp = local_root
            else:
                change_sp = ((repr(change_sp_r))[1:-1]).replace('\\', '/')
            print(change_sp)
            change_sp_P = Path(change_sp)
            if change_sp_P.is_dir():
                local_root = change_sp
                if change_sp[-1] != '/':
                    change_sp = change_sp + '/'
                print(local_root)
            else:
                print(f'Directory {change_sp} is not exist.')
            # destination root
            change_dp_r = input(f'Destination dir(enter to pass): {central_root} --> ')
            if not change_dp_r:
                change_dp = central_root
            else:
                change_dp = ((repr(change_dp_r)).replace('\\', '/'))[1:-1]
            change_dp_P = Path(change_dp)
            if change_dp_P.is_dir():
                if change_dp[-1] != '/':
                    change_dp = change_dp + '/'
                central_root = change_dp
                print(central_root)
            else:
                print(f'Directory {change_dp} is not exist.')
            variation = True
        # ---------------- create new file_couple --------------------
        elif choose0 == 4:
            choose1 = fct.option_button(1, 2, 'Cancel', 'Auto Update', 'User Define')
            variation = True
            if choose1 == 1:
                print('Under construction.')
                variation = False
            elif choose1 == 2:
                # get source
                while True:
                    set_local = ((repr(input(f'Source: {local_root}'))).replace('\\', '/'))[1:-1]
                    set_local_path = local_root + set_local
                    if Path(set_local_path).is_file():
                        break
                    else:
                        print(f'Can not find {set_local}')
                # get destination
                set_central = ((repr(input(f'Destination: {central_root}'))).replace('\\', '/'))[1:-1]
                set_central_path = central_root + set_central
                if not Path(set_central_path).is_file():
                    with open(set_central_path, 'w') as fcreate:
                        print(f'Can not find {set_central}, create empty destination.')
                # append to list
                local_list.append(set_local)
                central_list.append(set_central)
            else:
                variation = False
    # ----------------- dump .json --------------------
    if variation:
        filenotes["local_root"] = local_root
        filenotes["central_root"] = central_root
        filenotes["local_list"] = local_list
        filenotes["central_list"] = central_list
        with open('filenotes.json', 'w') as fj:
            json.dump(filenotes, fj, indent=4, sort_keys=True)
    print(16*'-', '\n')


# end = input('\n==== END ====\nEnter anything to exit...')
