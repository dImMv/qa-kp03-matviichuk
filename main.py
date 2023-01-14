from classes.directory import Directory
from classes.binary import BinaryFile
from classes.buffer import BufferFile
from classes.log_text import LogTextFile

main_dir = Directory('main_dir', 100)
sub_dir1 = Directory('sub_dir1', 10, main_dir)
sub_dir2 = Directory('sub_dir2', 5, sub_dir1)

bin_file1 = BinaryFile(sub_dir2, 'file1', 'text info')
bin_file2 = BinaryFile(main_dir, 'file2', 'another text info')

log_file1 = LogTextFile(sub_dir1, 'file3', 'first line')
log_file2 = LogTextFile(sub_dir2, 'file4', 'foo')
log_file1.append_line('second line')
print(log_file1.get())

buf_file1 = BufferFile(main_dir, 10, 'file5')
buf_file2 = BufferFile(sub_dir1, 20, 'file6')

buf_file2.changeOrder(sub_dir2)

print(main_dir.list_elems())