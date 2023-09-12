


driver.find_element_by_xpath("//a[text()='Movers and Shakers']").click()


class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self,driver):
        result = super().__call__(driver)
        if isinstance(result,WebElement):
            return result.is_enabled()



wait = WebDriverWait(webelement, timeout=10)