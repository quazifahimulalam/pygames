import random
import pygame


class button():
    def __init__(self, x, y, pos , width , height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = pos
        
    def clicked(self , pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
        return False
    
class rpsgame():
    def __init__(self):
        pygame.init()  
        
        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("Rock Paper Scissors")
        
        self.bg = pygame.image.load("background.jpg")
        self.r_btn = pygame.image.load("r_button.png").convert_alpha()    
        self.p_btn = pygame.image.load("p_button.png").convert_alpha()  
        self.s_btn = pygame.image.load("s_button.png").convert_alpha()  
        
        self.chose_rock = pygame.image.load("rock.png").convert_alpha()  
        self.chose_paper = pygame.image.load("paper.png").convert_alpha()
        self.chose_scissors = pygame.image.load("scissors.png").convert_alpha()
        
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_btn, (20, 500))
        self.screen.blit(self.p_btn, (330, 500))
        self.screen.blit(self.s_btn, (640, 500))
        
        self.rock_btn = button(30, 520, (30,520), 300, 140)
        self.paper_btn = button(340, 520, (340,520), 300, 140)
        self.scissors_btn = button(640, 520, (640,520), 300, 140)
        
        self.font = pygame.font.Font("Splatch.ttf", 90)
        self.text = self.font.render(f" ", True , (255 , 255 , 255))
        
        self.pl_score = 0
        self.pc_score = 0 
        
    def  player(self):
        if self.rock_btn.clicked(30):
            self.p_option = "rock"
            self.screen.blit(self.chose_rock, (120, 200))
        elif self.paper_btn.clicked(340):
            self.p_option = "paper"
            self.screen.blit(self.chose_paper, (120, 200))
        else:
            self.scissors_btn.clicked(640)
            self.p_option = "scissors"
            self.screen.blit(self.chose_scissors, (120, 200))
            
        return self.p_option
    
    def computer(self):
        self.pc_random_choice = " "
        option = ["rock", "paper", "scissors"]
        pc_choice = random.choice(list(option))
        if pc_choice == "rock":
            self.pc_random_choice = "rock"
            pc_choice = self.chose_rock
        elif pc_choice == "paper":
            self.pc_random_choice = "paper"
            pc_choice = self.chose_paper
        else:
            self.pc_random_choice = "scissors"
            pc_choice = self.chose_scissors
        pc_option = self.screen.blit(pc_choice, (600, 200))
        return pc_option
    
    def pl_score_cache(self):
        self.pl_score = 0
        self.pc_score = 0
        
        pl = self.p_option
        pc = self.pc_random_choice
        
        if pl == "rock" and pc == "scissors" or pl == "paper" and pc == "scissors" or pl == "scissors" and pc == "rock":
            self.pc_score += 1
        elif pl == pc :
            pass
        else:
            self.pl_score += 1
            
        return self.pl_score
    
    def pc_score_cache(self):
        self.pl_score = 0
        self.pc_score = 0
        
        pl = self.p_option
        pc = self.pc_random_choice
        
        if pl == "rock" and pc == "scissors" or pl == "paper" and pc == "scissors" or pl == "scissors" and pc == "rock":
            self.pc_score += 1
        elif pl == pc :
            pass
        else:
            self.pl_score += 1
            
        return self.pc_score