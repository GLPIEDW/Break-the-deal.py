import random

# 定义玩家属性
player = {
    "name": "维京勇士",
    "health": 100,
    "gold": 0,
    "weapons": []
}

# 定义游戏中可能遇到的事件和场景
events = [
    "你遇到了一群敌人，你选择战斗。",
    "你发现了一个宝箱，里面有金币。",
    "你来到了一个维京村庄，村民们欢迎你。",
    "你遭遇了一场暴风雨，失去了一些健康。",
    "你购买了一把新武器。",
    "你在森林中迷路了，消耗了一些时间。"
]

def game_over():
    print("\n游戏结束，维京勇士的历险之旅结束了。")
    print(f"最终状态：")
    print(f"健康：{player['health']}")
    print(f"金币：{player['gold']}")
    print(f"武器：{', '.join(player['weapons'])}")

def main():
    print("欢迎来到维京镇历险记游戏！")
    print("你是一位勇敢的维京勇士，准备踏上一段充满挑战的冒险之旅。")

    while player["health"] > 0:
        print("\n选择一个行动：")
        print("1. 探索附近的区域")
        print("2. 购买武器")
        print("3. 查看状态")
        print("4. 退出游戏")

        choice = input("请输入选项的数字：")

        if choice == "1":
            event = random.choice(events)
            print(event)
            if "金币" in event:
                player["gold"] += random.randint(10, 30)
            elif "健康" in event:
                player["health"] -= random.randint(10, 20)
            elif "武器" in event:
                weapon = random.choice(["剑", "斧头", "长矛"])
                player["weapons"].append(weapon)
        elif choice == "2":
            if player["gold"] >= 50:
                player["gold"] -= 50
                weapon = random.choice(["剑", "斧头", "长矛"])
                player["weapons"].append(weapon)
                print(f"你购买了一把{weapon}！")
            else:
                print("金币不足，无法购买武器。")
        elif choice == "3":
            print(f"\n状态：")
            print(f"健康：{player['health']}")
            print(f"金币：{player['gold']}")
            print(f"武器：{', '.join(player['weapons'])}")
        elif choice == "4":
            game_over()
            break
        else:
            print("无效的选项，请重新选择。")

if __name__ == "__main__":
    main()
