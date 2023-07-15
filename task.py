# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
#
# * При переименовании в конце имени добавляется порядковый номер.
#
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
#
# * принимать в качестве аргумента расширение конечного файла.


import os


def files_rename(dir_path: str, new_name: str = '', count: int = 3,# путь к директории, имя и кол.
                 in_extension: str = 'txt',                        # входящее расширение
                 out_extension: str = 'txt',                       # исходящее
                 slice_name: tuple = (0, 0)):                      # срез
    if not os.path.isdir(dir_path):
        return False                                               # если нет файла в этой директории False
    files_list = os.listdir(dir_path)
    files_count = 1
    for current_file in files_list:
        current_file_name, cur_ext = current_file.split('.')
        if cur_ext == in_extension:
            new_file = ''
            if slice_name:
                new_file += f'{current_file_name[slice_name[0]:slice_name[1]]}'
            if new_name:
                new_file += f'{new_name}'
            new_file += f'_{files_count:0>{count}}.{out_extension}'
            os.rename(os.path.join(dir_path, current_file),
                      os.path.join(dir_path, new_file))
            files_count += 1
    return f'"old_name[{slice_name[0]}:{slice_name[1]}]{new_name}_{"X" * int(f"{count}")}.{out_extension}"'


print(files_rename('begin', new_name='finish', count=5, in_extension='txt',
                   out_extension='doc', slice_name=(5, 30)))