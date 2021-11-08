link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestClass:

    def test_button_is_present(self, browser):
        # Открываем ссылку
        browser.get(link)
        # Проверяем присутствует ли кнопка на странице
        button = browser.find_element_by_css_selector('button.btn-add-to-basket').is_enabled()
        assert button, 'Button is missing on the page.'

