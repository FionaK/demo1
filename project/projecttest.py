import unittest
import project

class TestProject(unittest.TestCase):

    def test_register(self):
        self.assertEqual(project.firstname('fiona'), 'fiona')
        self.assertEqual(project.lastname('owuor'), 'owuor')
        self.assertEqual(project.username('fk'), 'fk')
        self.assertEqual(project.email('fko@gmail.com'), 'fko@gmail.com')


    def test_login(self):
        self.assertEqual(project.username('fk'), 'fk')
        self.assertEqual(project.password(12345), 12345)    



if __name__ == '__main__':
    unittest.main()
