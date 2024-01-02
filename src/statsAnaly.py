import json
import os
import pandas as pd

uuids = []
plan_users = pd.read_csv("../ex_datas/plan_users.csv")
    


# データの書き込み
with open("../output/playdata.csv", "w") as playdata:
    playdata.write("name,mined_block,move(m),playtime(s)\n")
    for i in plan_users.id:
        filename = "../stats/" + plan_users[plan_users.id == i].uuid.values[0] + ".json"


        with open(filename, "r") as f:
            # 掘ったブロック数
            data = json.load(f)
            print(plan_users[plan_users.id == i].name.values[0], end=" ")
            player_name = plan_users[plan_users.id == i].name.values[0]
            try:
                print("破壊したブロック数",sum(data["stats"]["minecraft:mined"].values()), end=" ")
                mined_block = sum(data["stats"]["minecraft:mined"].values())
            except:
                # もしデータがなかったらNaNで埋める
                mined_block = ""

            # 移動量
            move_cm = 0
            # 移動量のkey
            value = [
                "minecraft:crouch_one_cm",
                "minecraft:fly_one_cm",
                "minecraft:sprint_one_cm",
                "minecraft:swim_one_cm",
                "minecraft:walk_one_cm",
                "minecraft:walk_on_water_one_cm",
                "minecraft:walk_under_water_one_cm",
                "minecraft:boat_one_cm",
                "minecraft:aviate_one_cm",
                "minecraft:horse_one_cm",
                "minecraft:minecart_one_cm",
                "minecraft:pig_one_cm",
                "minecraft:strider_one_cm"
                ]
            for j in value:
                try:
                    move_cm += data["stats"]["minecraft:custom"][j]
                except:
                    pass
            # cm単位だけど10cmごとにカウントされているよう
            print("移動距離",move_cm//10,"m", end=" ")
            mive_m = move_cm//10

            # プレイ時間 なぜか20で割らないといけない。tick単位な気がする
            # ver1.16.5まではminecraft:play_one_minute
            playtime = data["stats"]["minecraft:custom"]["minecraft:play_time"]//20
            print("プレイ時間",playtime,"秒")

            # 書き込み
            playdata.write(player_name + "," + str(mined_block) + "," + str(mive_m) + "," + str(playtime) +"\n")
