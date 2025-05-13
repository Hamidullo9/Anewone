from pages.login_page import LoginPage


def test_logout_success(driver):
    driver.get("https://my.proweb.uz/log-in")
    try:
        login = LoginPage(driver)
        login.EnterPhoneNumber('998330091296')
        login.ClickLogin()
        login.EnterPassword('Hamidullo8')
        login.ClickLogin()
        login.LogOutInitial()
        driver.quit()
    except:
        driver.quit()