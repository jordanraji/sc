class StoreManager:
    def __init__(self) -> None:
        self.products: dict[int, str] = {}
        self.prices: dict[int, float] = {}
        self.stock: dict[int, int] = {}

    def get_available_id(self) -> int:
        if not self.products:
            return 1
        return max(self.products.keys()) + 1

    def add_product(self, product: str, price: float, stock: int) -> None:
        id = self.get_available_id()
        self.products[id] = product
        self.prices[id] = price
        self.stock[id] = stock

    def delete_product(self, id: int) -> None:
        del self.products[id]
        del self.prices[id]
        del self.stock[id]

    def update_product(self, id: int, product: str, price: float, stock: int) -> None:
        self.products[id] = product
        self.prices[id] = price
        self.stock[id] = stock

    def print_list(self) -> None:
        print("==========================================")
        print("Lista de productos")
        print("==========================================")
        for id in self.products:
            print(
                f"{id:<5}\t{self.products[id]:<15}\t{self.prices[id]:<10.2f}\t{self.stock[id]:<10}"
            )
        print("==========================================")

    def add_stock(self, id: int, quantity: int) -> None:
        self.stock[id] += quantity

    def sell_product(self, id: int, quantity: int = 1) -> None:
        self.stock[id] -= quantity


def store_cli(store: StoreManager) -> None:
    while True:
        store.print_list()
        print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
        print("Elija opción: ")
        option = input()
        if option == "1":
            product = input("Ingrese nombre del producto: ")
            price = float(input("Ingrese precio del producto: "))
            stock = int(input("Ingrese stock del producto: "))
            store.add_product(product, price, stock)
        elif option == "2":
            id = int(input("Ingrese ID del producto: "))
            store.delete_product(id)
        elif option == "3":
            id = int(input("Ingrese ID del producto: "))
            product = input("Ingrese nombre del producto: ")
            price = float(input("Ingrese precio del producto: "))
            stock = int(input("Ingrese stock del producto: "))
            store.update_product(id, product, price, stock)
        elif option == "4":
            break
        else:
            print("Opción inválida")


def main() -> None:
    store = StoreManager()
    store.add_product("Pantalones", 200.0, 50)
    store.add_product("Camisas", 120.0, 50)
    store.add_product("Corbatas", 50.0, 50)
    store.add_product("Casacas", 350.0, 50)

    store_cli(store)


if __name__ == "__main__":
    main()
