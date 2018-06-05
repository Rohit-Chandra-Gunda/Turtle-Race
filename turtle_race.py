"""
    Copyright 2018 Gunda Rohit Chandra

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import turtle as tu
from random import randint
import random

tu.penup()
tu.goto(-140, 140)

for step in range(15):
    tu.write(step)
    tu.right(90)
    tu.forward(10)
    tu.pendown()
    tu.forward(150)
    tu.penup()
    tu.backward(160)
    tu.left(90)
    tu.forward(20)

players = []
locations = [-160, -160]
player1 = tu.Turtle()
player1.color('red')
player1.shape('arrow')
player1.pu()
player1.goto(-160, 90)
player1.pendown()
player2 = tu.Turtle()
player2.color('blue')
player2.shape('arrow')
player2.pu()
player2.goto(-160, 60)
player2.pendown()

players.append(player1)
players.append(player2)

over = False
winner = 0

random.seed()
while any(location < 150 for location in locations):
    for index in range(len(players)):
        if locations[index] < 150:
            temp = randint(1, 5)
            locations[index] += temp
            players[index].fd(temp)
            if locations[index] >= 150 and not over:
                over = True
                winner = index + 1

print("The winner is player " + str(winner) + "! Congratulations")
