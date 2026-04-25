from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        # Selector para todos los contenedores de productos
        self.inventory_items = page.locator(".inventory_item")
        # Selectores internos (se usan dentro de cada item)
        self.item_name = ".inventory_item_name"
        self.item_desc = ".inventory_item_desc"
        self.item_price = ".inventory_item_price"
