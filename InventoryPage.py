"""from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    def add_to_cart_btn(self, item_name):
        return f"#add-to-cart-{item_name.lower().replace(" ","-")}"
    def item_price(self, item_name):
        return f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//div[@class='inventory_item_price']"
    def add_item_to_cart(self, item_name):
        self.page.click(self.add_to_cart_btn(item_name))

    def get_item_price(self, item_name):
        return self.page.locator(self.item_price(item_name)).inner_test()
    def get_inventory_count(self):
        return self.page.locator(".inventory_item").count()
"""
from playwright.sync_api import Page

class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart_icon = ".shopping_cart_link"
        self.success_badge = ".shopping_cart_badge"

    def add_item_to_cart(self, item_name: str):
        formatted = item_name.lower().replace(" ", "-")
        self.page.click(f"#add-to-cart-{formatted}")

    def open_cart(self):
        self.page.click(self.cart_icon)

    def get_cart_count(self):
        return self.page.locator(self.success_badge).inner_text()
