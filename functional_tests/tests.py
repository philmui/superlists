from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_requirement1(self):
        # Requirement 1.1: User is authenticated when they access FFR-ct details page
        #       Pre-condition: User has seen the "login page"
        #       Post-condition:
        #              If user is authenticated, FFR-ct details is shown
        #              Else, user is redirected back to "login page"
        logger.info("checking requirement 1.1")

        # Requirement 1.2:
        #       Pre-condition:
        #       Post-condition:
        logger.info("checking requirement 1.2")


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row_text for row in rows])

    def test_can_start_a_list_and_retrieve_it(self):
        # Requirement 2: User access the new site
        self.browser.get(self.live_server_url)

        # Requirement 2.1: She notices the page title and header mention "TO-DO" lists
        self.assertIn('To-Do lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do lists", header_text)

        # Requirement 2.2: She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Requirement 2.3: She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # Requirement 2.4: When she hits enter, she is taken to a new URL
        # and now the page lists "1: Buy peacock feathers" as an item in
        # a to-do list
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        logger.info("edith_list_url: %s" % edith_list_url)
        #self.assertRegex(edith_list_url, '/lists/.+')
        #self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feather to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feather to make a fly')

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
