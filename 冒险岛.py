import random

class Player:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.hp = 100

    def attack(self):
        return random.randint(5, 15) * self.level

class Monster:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = 30 * level

    def attack(self):
        return random.randint(3, 10) * self.level

def main():
    print("欢迎来到《冒险岛探险》！")
    player_name = input("请输入您的角色名：")
    character_class = input("请选择您的角色职业（战士/法师/弓箭手）：")
    player = Player(player_name, character_class)

    print(f"\n欢迎您，{player.name}！您是一名{player.character_class}，现在开始您的冒险之旅。")

    while player.hp > 0:
        print("\n1. 探索冒险岛")
        print("2. 查看角色状态")
        print("3. 退出游戏")
        choice = input("请选择操作（输入数字）：")

        if choice == "1":
            monster_name = random.choice(["史莱姆", "野猪", "僵尸"])
            monster_level = player.level
            monster = Monster(monster_name, monster_level)

            print(f"您遇到了一只{monster.name}（等级：{monster.level}）！")
            while player.hp > 0 and monster.hp > 0:
                player_damage = player.attack()
                monster_damage = monster.attack()

                print(f"\n您对{monster.name}造成了{player_damage}点伤害！")
                monster.hp -= player_damage
                if monster.hp <= 0:
                    print(f"您击败了{monster.name}，获得了经验和奖励！")
                    player.level += 1
                    player.hp = min(player.hp + 20, 100)
                    break

                print(f"{monster.name}对您造成了{monster_damage}点伤害！")
                player.hp -= monster_damage
                if player.hp <= 0:
                    print("您被击败了，游戏结束。")
                    break

        elif choice == "2":
            print(f"\n角色名：{player.name}")
            print(f"职业：{player.character_class}")
            print(f"等级：{player.level}")
            print(f"生命值：{player.hp}")

        elif choice == "3":
            print(f"感谢您的游玩，《冒险岛探险》期待您的下次冒险！")
            break

if __name__ == "__main__":
    main()
