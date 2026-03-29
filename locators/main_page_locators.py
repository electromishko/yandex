from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, '/account')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__') and contains(@href, '/')]")
    FEED_LINK = (By.XPATH, "//a[contains(@href, '/feed')]")
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/a")
    INGREDIENT = (By.XPATH, "//a[contains(@href, '/ingredient/')]//h2[text()='Флюоресцентная булка R2-D3']/parent::a")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")
    CLOSE_MODAL = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    BUN_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__')]//span[text()='Булки']/parent::div")
    SAUCE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__')]//span[text()='Соусы']/parent::div")
    FILLING_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__')]//span[text()='Начинки']/parent::div")

class ConstructorPageLocators:

    BUN = (By.XPATH, "//a[contains(@href, '/ingredient/')]//p[text()='Флюоресцентная булка R2-D3']/parent::a")
    SAUCE = (By.XPATH, "//a[contains(@href, '/ingredient/')]//h2[contains(text(), 'Соус')]/parent::a")
    FILLING = (By.XPATH, "//a[contains(@href, '/ingredient/')]//h2[contains(text(), 'Мясо')]/parent::a")
    BURGERS_PAGE = (By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients__')]")
    BASKET = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket__')]")
    COUNTER_0 = (By.XPATH, "//a[contains(@href, '/ingredient/')]//p[text()='0']")
    COUNTER_2 = (By.XPATH, "//a[contains(@href, '/ingredient/')]//p[text()='2']")
    MODAL_INGREDIENT = (By.XPATH, "//div[contains(@class, 'Modal_modal__content__')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__')]")
