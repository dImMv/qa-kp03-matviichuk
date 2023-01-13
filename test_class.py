from types import NoneType
from classes.directory import Directory
from classes.binary import BinaryFile
from classes.log_text import LogTextFile
from classes.buffer import BufferFile

class TestClass:
    parent_dir = Directory('parent_dir', 10)
    inner_dir = Directory('inner_dir', 3, parent_dir)

    def test_dir(self):
        max_elems = 10
        dir = Directory('dir', max_elems)
        assert dir.DIR_MAX_ELEMS == max_elems
        assert dir.count_elems == 0
        assert type(dir.parent) is NoneType
        assert type(dir.list_elems()) is str
        dir.changeOrder(self.parent_dir)
        assert dir.parent == self.parent_dir
        del dir
        assert 'dir' not in locals()
    
    def test_binary_file(self):
        file = BinaryFile(self.parent_dir, 'test1', 'file info')
        assert 'info' in file.get()
        file.changeOrder(self.inner_dir)
        assert file.parent == self.inner_dir
        file.changeOrder(self.inner_dir)
        assert file.parent == self.inner_dir
        del file
        assert 'file' not in locals()

    def test_buf_file(self):
        max_size = 10
        file = BufferFile(self.parent_dir, max_size, 'test1')
        assert file.MAX_BUF_FILE_SIZE == max_size
        file.changeOrder(self.inner_dir)
        assert file.parent == self.inner_dir
        del file
        assert 'file'not in locals()

    def test_log_file(self):
        file = LogTextFile(self.parent_dir, 'test1', 'file info')
        file.append_line('new line')
        assert 'line' in file.get()
        assert '\n' in file.get()
        file.changeOrder(self.inner_dir)
        assert file.parent == self.inner_dir
        del file
        assert 'file' not in locals()

   