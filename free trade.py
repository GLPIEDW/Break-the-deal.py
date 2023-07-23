class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Player:
    def __init__(self, name, coins=100):
        self.name = name
        self.coins = coins
        self.inventory = {}

    def add_item(self, item, quantity):
        if item.name in self.inventory:
            self.inventory[item.name] += quantity
        else:
            self.inventory[item.name] = quantity

    def remove_item(self, item, quantity):
        if item.name in self.inventory:
            if self.inventory[item.name] >= quantity:
                self.inventory[item.name] -= quantity
                return True
            else:
                return False
        else:
            return False

def show_inventory(player):
    print("你的物品清单：")
    for item_name, quantity in player.inventory.items():
        print(f"{item_name} x{quantity}")

def show_shop_items(shop):
    print("商店物品清单：")
    for item in shop:
        print(f"{item.name} - 价格: {item.price}")

def trade(player, shop):
    while True:
        print("\n1. 查看你的物品清单")
        print("2. 查看商店物品清单")
        print("3. 购买物品")
        print("4. 卖出物品")
        print("5. 退出交易")
        choice = int(input("请输入你的选择（1/2/3/4/5）: "))

        if choice == 1:
            show_inventory(player)
        elif choice == 2:
            show_shop_items(shop)
        elif choice == 3:
            print("可购买的物品：")
            for idx, item in enumerate(shop, start=1):
                print(f"{idx}. {item.name} - 价格: {item.price}")
            buy_choice = int(input("请输入你要购买的物品序号："))
            if 1 <= buy_choice <= len(shop):
                item_to_buy = shop[buy_choice - 1]
                if player.coins >= item_to_buy.price:
                    player.add_item(item_to_buy, 1)
                    player.coins -= item_to_buy.price
                    print(f"购买了 {item_to_buy.name}，花费了 {item_to_buy.price} 金币。")
                else:
                    print("金币不足，无法购买物品。")
            else:
                print("无效的选择。")
        elif choice == 4:
            if len(player.inventory) == 0:
                print("你的物品清单为空，无物品可卖。")
            else:
                print("你的物品清单：")
                for idx, item_name in enumerate(player.inventory.keys(), start=1):
                    print(f"{idx}. {item_name}")
                sell_choice = int(input("请输入你要卖出的物品序号："))
                if 1 <= sell_choice <= len(player.inventory):
                    item_to_sell = list(player.inventory.keys())[sell_choice - 1]
                    sell_price = shop[item_to_sell].price // 2
                    if player.remove_item(shop[item_to_sell], 1):
                        player.coins += sell_price
                        print(f"卖出了 {item_to_sell}，获得了 {sell_price} 金币。")
                    else:
                        print("你没有这个物品，无法卖出。")
                else:
                    print("无效的选择。")
        elif choice == 5:
            print("交易结束。")
            break
        else:
            print("无效的选择，请重新输入。")

if __name__ == "__main__":
    player_name = input("请输入你的角色名字：")
    player = Player(player_name)
    item1 = Item("草药", 10)
    item2 = Item("剑", 50)
    item3 = Item("魔法书", 100)
    shop_items = [item1, item2, item3]

    print(f"欢迎 {player_name} 来到商店，你有 {player.coins} 金币。")
    trade(player, shop_items)
