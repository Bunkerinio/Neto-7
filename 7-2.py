# Code

def text_line_counter(file_name, type="r"):
    line_counter = 0
    with open(file_name, type) as f:
        for line in f:
            line_counter += 1
    txt_line_number_match[file_name] = line_counter


def txt_files_sorting():
    line_number = 0
    line_list = []
    for k, v in txt_line_number_match.items():
        line_list.append(v)
    sorted_line_list = sorted(line_list)
    for number in range(len(line_list)):
        for k, v in txt_line_number_match.items():
            if k not in sorted_txt and v == sorted_line_list[number]:
                sorted_txt.append(k)


txt_line_number_match = {}
sorted_txt = []
# Ввести имена файлов как аргумент функции text_line_counter
text_line_counter("1.txt")
text_line_counter("2.txt")
text_line_counter("3.txt")

txt_files_sorting()

for file in sorted_txt:
    with open(file, "r") as f:
        data = f.read()
        file_to_write = open("Summary.txt", "a")
        file_to_write.write(file + "\n" + str(txt_line_number_match[file]) + "\n" + data + "\n")
file_to_write.close()

# Code testing
# print(txt_line_number_match)
# print(sorted_txt)
