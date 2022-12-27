import pyxel



class app():

    def __init__(self):


        self.mario_x = 0
        self.mario_y = 151
        self.jump_counter = 5
        self.is_jump = False
        self.floor = [(80,150), (100,150),(120,150)]
        pyxel.init(200,200)
        pyxel.load("my_resource.pyxres")
        self.far_cloud = [(-10, 1), (30, 30), (90, 40)]
        pyxel.run(self.update, self.draw)
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.mairo()



    def draw(self):
        pyxel.cls(12)# ЗАдаем цвет фона

        pyxel.blt(0,180,0,0,180,200,20)# нижние блоки
        pyxel.blt(0, 167, 0, 0,184, 200, 17)# нижние блоки 2

        offset = (pyxel.frame_count // 8) % 160     # Анимация облаков
        for i in range(2):
            for x, y in self.far_cloud:
                pyxel.blt(x + i * 160 - offset,y, 0, 64, 138, 38, 35, 35) # отрисовка облаков
        pyxel.blt(self.mario_x, self.mario_y, 0, 0, 240, 15, 20)# наш марио

        self.level = [                  #Отрисовка уровня согласно данному списку
            "          ",
            "          ",
            "          ",
            "          ",
            "          ",
            "          ",
            "          ",
            "          ",
            "      -   "]

        one = t = 0  # координаты
        self.block =[]
        for row in self.level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    # создаем блок, заливаем его цветом и рисеум его
                    pyxel.blt(one, t, 0, 0, 200, 20, 15, 15)


                    print(self.block)
                    self.block.append(one)
                    self.block.append(t)
                    print(self.block)



                one += 20  # блоки платформы ставятся на ширине блоков
            t += 20  # то же самое и с высотой
            one = 0

        for i in self.block  :                  # Попытка сделать физику рисунка
            if i == self.mario_x + 15:
                self.mario_x = self.mario_x-1
                if self.is_jump == True:
                    self.mario_x = self.mario_x + 1
                    if i == self.mario_x+15:
                        self.mario_y -= 15 //2

            if self.mario_x + 15 ==  self.block[0] + 25:
                self.mario_y+=15//2
                break
        self.g = pyxel.tilemap(0).pget(120,160)
        print(self.g)


    def mairo(self):             # Функция движения марио
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.mario_x += 1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.mario_x -= 1
        if pyxel.btn(pyxel.KEY_UP):
            self.is_jump = True
        if self.is_jump is True:
            if self.jump_counter >= -5:
                if self.jump_counter < 0:
                    self.mario_y += (self.jump_counter ** 2) // 2
                else:
                    self.mario_y -= (self.jump_counter ** 2) // 2
                self.jump_counter -= 1
            else:
                self.is_jump = False
                self.jump_counter = 5



app()