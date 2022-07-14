from random import randrange
class Board:
    def __init__(self, height, width, number_of_mines):
        self.height = height
        self.width = width
        self.number_of_mines = number_of_mines
        self.number_of_safe_squares = width * height - number_of_mines
        self.board_values = []
        self.alive = True
        for i in range(self.height * self.width):
            square = {"status":1, "danger":0}
            
            self.board_values.append(square)
        squares = list(range(width * height))
        for i in range(number_of_mines):
            m = randrange(len(squares))
            n = squares[m]
            self.board_values[n]["danger"] = -1
            del squares[m]
            for j in self.adjacent(n):
                self.board_values[j]["danger"] += 1
                
            
            
            
            

    def __str__(self):
        ret = ""
        for i in range(self.width):
            ret += (str(i + 1) + " ")
        ret += "\n"
        for i in range(self.height * self.width):
            if i % self.width == 0 and i != 0:
                ret += "%d \n" % (i / self.width)
            status = self.board_values[i]["status"] 
            if self.alive and status == 1:
                ret += "# "
            elif self.alive and status == -1:
                ret += "F "
            else:
                danger = self.board_values[i]["danger"]
                if danger < 0:
                    ret += "X "
                else:
                    ret += str(danger) + " "
                
            
                
                
        ret += str(self.height)
        

        return ret

    def flag(self, x, y):
        index = self.width * y + x
        if self.board_values[index]["status"] > 0:
            if self.board_values[index]["danger"] < 0:
                self.number_of_mines -= 1

        elif self.board_values[index]["status"] < 0:
            if self.board_values[index]["danger"] < 0:
                self.number_of_mines += 1
            
            
        self.board_values[index]["status"] *= -1

    def dig(self, x, y):
        index = self.width * y + x
        status = self.board_values[index]["status"]
        self.board_values[index]["status"] = 0
        if self.board_values[index]["danger"] >= 0 and status:
            self.number_of_safe_squares -= 1
        
        if self.board_values[index]["danger"] < 0:
            self.alive = False
        elif self.board_values[index]["danger"] == 0:
            if status != 0:
                for i in self.adjacent(index):
                    x = i % self.width
                    y = i // self.width
                    self.dig(x, y)
                
            

    def adjacent(self, index):
        x = index % self.width
        y = index // self.width
        adj_squares = (
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1),
        (x - 1, y),
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1)
        )
        for square in adj_squares:
            i = self.width * square[1] + square[0]
            if i < 0:
                continue
            if i >= len(self.board_values):
                continue
            if square[0] < 0 or square[0] >= self.width:
                continue
            if self.board_values[i]["danger"] < 0:
                continue
            yield i

    def win(self):
        return self.number_of_mines <= 0 or self.number_of_safe_squares <= 0
            
            
            
            
            
            
            
            
            
        
        
        
            
            

    
    
    
