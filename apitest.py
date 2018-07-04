import uinttest
import api

class Testapi(uinttest.TestCase):
	def test_timestamp(self):
		self.assertEqual(api.timestamp(2018070373523),2018070373523)


if __name__ == '__main__':
	
		