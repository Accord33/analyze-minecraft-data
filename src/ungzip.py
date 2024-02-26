import gzip
import shutil
import os

files = [i for i in os.listdir("../logs") if i.split(".")[-1] == "gz"]

# 解答
def ungzip(files):
    for i in files:
        source_file = i
        target_file = i[:-3]

        with gzip.open("../logs/"+source_file, mode="rb") as gzip_file:
            with open("../logs/"+target_file, mode="wb") as decompressed_file:
                shutil.copyfileobj(gzip_file, decompressed_file)
        print(source_file)

# 削除
def delete_gz(files):
    for i in files:
        os.remove("../logs/"+i)

if __name__ == "__main__":
    ungzip(files)
    delete_gz(files)