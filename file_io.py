from time import time 
import os

number_of_small_files = 10000
number_of_large_files = 1000
number_of_huge_files = 3

small_file_size_in_bytes = 2 * 1024 # 2kb
large_file_size_in_bytes = 25 * 1024 * 1024 # 25mb
huge_file_size_in_bytes = 1 * 1024 * 1024 * 1024 # 5gb


def create_files(number_of_files=1, file_size=1024, prefix=""):
    files = []
    for i in range(number_of_files):
        file_name = prefix + "_file_{}".format(i)
        with open(file_name, "w") as f:
            for _ in range(file_size):
                f.write("x")
        files.append(file_name)
    return files

def read_files(files):
    for file in files:
        with open(file, "r") as f:
            f.read()

def write_performance_result(small_results, large_results, huge_results):
    write_line = lambda f, line: f.write(line + "\n")
    with open("file_io_results.txt", "w") as f:
        write_line(f, "Small Files Creation Time: {}".format(small_results[0]))
        write_line(f, "Small Files Read Time: {}".format(small_results[1]))
        write_line(f, "Large Files Creation Time: {}".format(large_results[0]))
        write_line(f, "Large Files Read Time: {}".format(large_results[1]))
        write_line(f, "Huge Files Creation Time: {}".format(huge_results[0]))
        write_line(f, "Huge Files Read Time: {}".format(huge_results[1]))



if __name__ == "__main__":
    start = time()
    small_files = create_files(number_of_files=number_of_small_files, file_size=small_file_size_in_bytes, prefix="small")
    end = time()
    small_creation = end - start
    start = time()
    sorted_files = read_files(small_files)
    end = time()
    small_read = end - start

    start = time()
    large_files = create_files(number_of_files=number_of_large_files, file_size=large_file_size_in_bytes, prefix="large")
    end = time()
    large_creation = end - start
    start = time()
    read_files(large_files)
    end = time()    
    large_read = end - start

    start = time()
    huge_files = create_files(number_of_files=number_of_huge_files, file_size=huge_file_size_in_bytes, prefix="huge")
    end = time()
    huge_creation = end - start
    start = time()
    read_files(huge_files)
    end = time()
    huge_read = end - start

    write_performance_result((small_creation, small_read), (large_creation, large_read), (huge_creation, huge_read))
    os.system("rm small* large* huge*")