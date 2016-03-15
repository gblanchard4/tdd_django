from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.asserIn('To-Do', header_text)

        # I am invited to enter a todo item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # I type "Buy peacock feathers"
        inputbox.send_keys('Buy peacock feathers')

        # When I hit enter the page updates with "Buy peacock feathers" on a todo list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peackock feathers' for row in rows)
        )

        # There is another box inviting me to enter another item on a list
        # I type "Tie a fly with peacock feathers"
        self.fail('Finish the test!')

        # The page updates again, now shows both items

        # I wonder if the site would remember my list. I see it has generated a unique
        # URL for me with an explination

        # I visit the URL and my list is still There

if __name__ == '__main__':
    unittest.main(warnings='ignore')
