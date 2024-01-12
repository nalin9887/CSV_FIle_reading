import pandas
data=pandas.read_csv("004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
fur_color=data["Primary Fur Color"]
grey=0
cinnamon=0
nan=0
Black=0
list=fur_color.tolist()
for color in list:
    if color=="Gray":
        grey+=1
    elif color=="Cinnamon":
        cinnamon+=1
    elif color=="Black":
        Black+=1
    else:
        nan+=1

print(f"num of grey squirral is :{grey} \nnum of cinnamon squirral is :{cinnamon} \nnum of black squirral is :{Black} \nnum of nan squirral is :{nan} \n")
fur_color.to_csv("color_data.csv")
