import os

def walk_target_files(root_path:str='.', condition:str=''):
    '''
    root_path:str,default $PWD;
    condition: the characters in files you want to find.
    '''
    out_li = []
    walk_tool = os.walk(root_path)
    for root,dirs,files in walk_tool:
        for file in files:
            if condition in file:
                out_li.append((root, file))
    return out_li

if __name__ == '__main__':
    walk_target_files()
    pass