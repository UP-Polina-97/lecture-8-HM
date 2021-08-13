import json
def compile_files(files_list):
    data = {}
    for file in files_list:
        with open(file, encoding="utf-8") as f:
            file_data = f.readlines()
            data[len(file_data)] = (file, "".join(file_data))
            di = data.items()
            so = sorted(di)
    data1 = dict(so)
    #print(data1)


    with open("result_data.txt", "w", encoding="utf-8") as new_file:
        for key, value in data1.items():
            new_file.write(str(value[0]))
            new_file.write(("\n"))
            new_file.write(str(key))
            new_file.write(("\n"))
            new_file.write(str(value[1]))
            new_file.write(("\n"))

files = ["1.txt", "2.txt", "3.txt"]
compile_files(files)







