from playwright.sync_api import sync_playwright

def test_navigator_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False = we can see browser
        page = browser.new_page()
        page.goto("https://www.navigator.ba")
        assert "Navigator" in page.title()
        print("Homepage loaded successfully and title verified!")
        browser.close()

if __name__ == "__main__":
    test_navigator_homepage()
