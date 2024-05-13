from turtle import Turtle

WIN = 5

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 220)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(200, 220)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))
        
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
        
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
        
    def game_over(self):
        winner = ''
        if self.r_score == WIN:
            winner = "Right Paddle"
        elif self.l_score == WIN:
            winner = "Left Paddle" 
        self.goto(0, 0)
        self.write(f"GAME OVER {winner} wins!", False, align="center", font=("Courier", 20, "normal"))