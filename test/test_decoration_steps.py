import allure
from selene import by, be
from selene.support.shared import browser


def test_decoration_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("76")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys(repo)
    browser.element(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем таб issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие ишью с номером {number}")
def should_see_issue_with_number(number):
    browser.element(by.partial_text("#" + number)).should(be.visible)