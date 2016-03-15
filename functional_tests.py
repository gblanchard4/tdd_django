from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get('http://localhost:8000')

        # I notice the page title mentions todo lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # I am invited to enter a todo item

        # I type "Buy peacock feathers"

        # When I hit enter the page updates with "Buy peacock feathers" on a todo list

        # There is another box inviting me to enter another item on a list
        # I type "Tie a fly with peacock feathers"

        # The page updates again, now shows both items

        # I wonder if the site would remember my list. I see it has generated a unique
        # URL for me with an explination

        # I visit the URL and my list is still There

if __name__ == '__main__':
    unittest.main(warnings='ignore')
