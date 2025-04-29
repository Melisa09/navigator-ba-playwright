import time
from playwright.sync_api import sync_playwright

def test_nb16_valid_search(page):
    page.goto("https://www.navigator.ba/#/categories")
    page.wait_for_load_state('load')
    textbox = page.get_by_role("textbox", name="Traži ulicu ili objekat")
    textbox.click()
    textbox.press("CapsLock")
    textbox.fill("H")
    textbox.press("CapsLock")
    textbox.fill("Hrasno")
    textbox.press("Enter")
    time.sleep(5)

def test_nb17_invalid_search(page):
    page.goto("https://www.navigator.ba/#/categories")
    page.wait_for_load_state('load')
    textbox = page.get_by_role("textbox", name="Traži ulicu ili objekat")
    textbox.click()
    textbox.fill("2333")
    textbox.press("Enter")
    time.sleep(5)
    print("There is no posssiblity for searching by numbers.")

def test_nb18_empty_search(page):
    page.goto("https://www.navigator.ba/#/categories")
    page.wait_for_load_state('load')
    page.get_by_role("textbox", name="Traži ulicu ili objekat").click()
    page.wait_for_timeout(2000)
    page.get_by_role("textbox", name="Traži ulicu ili objekat").press("Enter")
    page.wait_for_timeout(2000)

def test_nb19_special_characters_search(page):
    page.goto("https://www.navigator.ba/#/categories")
    page.wait_for_load_state('load')
    page.get_by_role("textbox", name="Traži ulicu ili objekat").click()
    page.get_by_role("textbox", name="Traži ulicu ili objekat").fill("Franz & Sophie")
    page.get_by_role("textbox", name="Traži ulicu ili objekat").press("Enter")
    time.sleep(5)

def test_nb20_autocomplete_suggestions(page):
    page.goto("https://www.navigator.ba/#/categories")
    page.wait_for_load_state('load')
    page.get_by_role("link", name="SARAJEVO").click()
    page.get_by_role("textbox", name="Traži ulicu ili objekat").click()
    page.get_by_role("textbox", name="Traži ulicu ili objekat").fill("trave")
    page.get_by_text("Hostel/Travel Agency \"Ljubič").click()
    page.wait_for_timeout(2000)

def test_nb21_case_insensitive_search(page):

    page.goto("https://www.navigator.ba/#/categories")
    page.wait_for_load_state('load')
    page.get_by_role("textbox", name="Traži ulicu ili objekat").click()
    page.get_by_role("textbox", name="Traži ulicu ili objekat").fill("hotel vip")
    page.get_by_role("textbox", name="Traži ulicu ili objekat").press("Enter")
    page.wait_for_timeout(2000)
    page.get_by_role("link", name="Hotel VIP Jaroslava Černija 3").click()
    page.wait_for_timeout(2000)

    page.get_by_role("textbox", name="Traži ulicu ili objekat").click()
    page.get_by_role("textbox", name="Traži ulicu ili objekat").fill("HOTEL VIP")
    page.get_by_role("textbox", name="Traži ulicu ili objekat").press("Enter")
    page.wait_for_timeout(2000)
    page.get_by_role("link", name="Hotel VIP Jaroslava Černija 3").click()
    page.wait_for_timeout(2000)

def run_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        test_nb16_valid_search(page)
        test_nb17_invalid_search(page)
        test_nb18_empty_search(page)
        test_nb19_special_characters_search(page)
        test_nb21_case_insensitive_search(page)
        test_nb20_autocomplete_suggestions(page)
      

        context.close()
        browser.close()

if __name__ == "__main__":
    run_tests()

