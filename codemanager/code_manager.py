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
    choose0 = fct.option_button('What do you want to do?', 1, 
        'Exit', 
        'Update to central', 
        'Download to local',
        'Browse or delete existing file_couple', 
        'New file_couple', 
        'Change root directory'
        )

    if choose0 == 0:
        break
    else:
        # ------------------- load .json---------------------
        try:
            with open('filenotes.json', 'r') as fj:
                filenotes = json.load(fj)
        except FileNotFoundError:
            print('FATAL ERROR: JSON BROKEN, CREATE NEW ONE.')
        finally:
            local_root = filenotes["local_root"]
            central_root = filenotes["central_root"]
            local_list = filenotes["local_list"]
            central_list = filenotes["central_list"]
            # print(local_root, local_list)
            # print(central_root, central_list)
        notes_n = len(central_list)
        stationary = True
        # -------------------- update file_couples --------------------
        if choose0 == 1 or choose0 == 2:
            for n in range(notes_n):
                local_path = local_root + local_list[n]
                central_path = central_root + central_list[n]
                if not fct.text_cmp(local_path, central_path):
                    if choose0 == 1:
                        fct.text_copy(local_path, central_path)
                        print(f'{local_path} ==>> {central_path}')
                    else:
                        fct.text_copy(central_path, local_path)
                        print(f'{central_path} ==>> {local_path}')
                    stationary = False
                else:
                    print(f'{local_path} == {central_path}')
        # --------------- show current file_couples ------------------
        elif choose0 == 3:
            print(f'Root dir: {local_root} <==> {central_root}')
            for n in range(notes_n):
                print(f'{local_list[n]} <==> {central_list[n]}')
            choose1 = fct.option_button('Then', 0, 'Return', 'Delete one')
            if choose1 == 1:
                del_index = input('Press the index of the file_couple you want delete.')
                if del_index in [str(i) for i in range(notes_n)]:
                    del_index = int(del_index)
                    del local_list[del_index]
                    del central_list[del_index]
                    stationary = False
                else:
                    print(f"Index{del_index} doesn't exist.")
        # ---------------- create new file_couple --------------------
        elif choose0 == 4:
            choose1 = fct.option_button('Create new file_couple:', 1, 'Cancel', 'User Define', 'Auto Update')
            stationary = False
            if choose1 == 2:
                print('Under construction.')
                stationary = True
            elif choose1 == 1:
                # get local
                while True:
                    set_local = ((repr(input(f'Local: {local_root}'))).replace('\\', '/'))[1:-1]
                    set_local_path = local_root + set_local
                    if Path(set_local_path).is_file():
                        break
                    else:
                        print(f'Can not find {set_local}')
                # get central
                set_central = ((repr(input(f'Central: {central_root}'))).replace('\\', '/'))[1:-1]
                set_central_path = central_root + set_central
                if not Path(set_central_path).is_file():
                    with open(set_central_path, 'w') as fcreate:
                        print(f'Can not find {set_central}, create empty file.')
                # append to list
                local_list.append(set_local)
                central_list.append(set_central)
            else:
                stationary = True
        # -------------- change root directory -------------------
        elif choose0 == 5:
            print('WARNNING! Change root directory may invalidate previous file_couples.')
            # local root
            nx_local_root = input(f'Local dir(enter to pass): {local_root} --> ')
            if not nx_local_root:
                nx_local_root = local_root
            else:
                nx_local_root = ((repr(nx_local_root))[1:-1]).replace('\\', '/')
            nx_local_root_P = Path(nx_local_root)
            if nx_local_root_P.is_dir():
                if nx_local_root[-1] != '/':
                    nx_local_root = nx_local_root + '/'
                local_root = nx_local_root
                # print('New local_root:', local_root)
            else:
                print(f'Directory {nx_local_root} is not exist.')
            # central root
            nx_central_root = input(f'Central dir(enter to pass): {central_root} --> ')
            if not nx_central_root:
                nx_central_root = central_root
            else:
                nx_central_root = ((repr(nx_central_root)).replace('\\', '/'))[1:-1]
            nx_central_root_P = Path(nx_central_root)
            if nx_central_root_P.is_dir():
                if nx_central_root[-1] != '/':
                    nx_central_root = nx_central_root + '/'
                central_root = nx_central_root
                # print('New central_root:', central_root)
            else:
                print(f'Directory {nx_central_root} is not exist.')
            stationary = False
    # ----------------- dump .json --------------------
    if not stationary:
        filenotes["local_root"] = local_root
        filenotes["central_root"] = central_root
        filenotes["local_list"] = local_list
        filenotes["central_list"] = central_list
        with open('filenotes.json', 'w') as fj:
            json.dump(filenotes, fj, indent=4, sort_keys=True)
    print(16*'-', '\n')

print(8*'-', 'by Victaming')
# end = input('\n==== END ====\nEnter anything to exit...')
