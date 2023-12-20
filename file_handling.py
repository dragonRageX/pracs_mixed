file1_write = open("./pracs/file1.txt", "w")
for i in range(10):
    word = input("Enter a number: ")
    file1_write.write(word)
    file1_write.write("\n")
file1_write.close()

file1_read = open("./pracs/file1.txt", "r")
print(file1_read)
List = list()
for line in file1_read:
    List.append(int(line))
file1_read.close()
print(List)
List.sort()
print(List)

file2_write = open("./pracs/file2.txt", "w")
for i in range(len(List)):
    file2_write.write(str(List[i]))
    file2_write.write("\n")
file2_write.close()