import pygame
import numpy as np
import math

class HexagonalGameOfLife:
    """Main class for Hexagonal Game of Life simulation"""
    
    def __init__(self, width=610, height=635, radius=15):
        # Initialize pygame
        pygame.init()
        
        # Game state variables
        self.running = False
        self.game_active = False
        
        # Screen dimensions and hexagon properties
        self.radius = radius
        self.width = width
        self.height = height
        self.instruction_height = 40                                # Height for instruction area
        self.game_height = height - self.instruction_height         # Actual game area height
        
        self.rows = math.floor(self.game_height / (1.5 * radius))
        self.columns = math.floor(width / (math.sqrt(3) * radius))
        self.tiltangle = math.pi
        
        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (128, 128, 128)
        self.DARK_GRAY = (64, 64, 64)
        
        # Screen setup - total height includes instruction area
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Hexagonal Game of Life")
        self.screen.fill(self.BLACK)
        
        # Font for instructions
        self.font = pygame.font.Font(None, 24)
        
        # Grid and tracking variables
        self.grid = np.zeros((self.rows, self.columns))
        self.generation = np.ones((self.rows, self.columns))
        self.previous = np.zeros((self.rows, self.columns))
        self.generation_count = 1
    
    def draw_polygon(self, color, num_sides, x, y, radius):
        """Drawing a single hexagon - your original function"""
        pts = []
        for i in range(0, num_sides):
            x = x + radius * math.cos(self.tiltangle / 2 + math.pi * 2 * i / num_sides)
            y = y + radius * math.sin(self.tiltangle / 2 + math.pi * 2 * i / num_sides)
            pts.append([x, y])
        pygame.draw.polygon(self.screen, color, pts)
    
    def draw_instruction_area(self):
        """Draw the instruction area at the bottom of the screen"""

        # Draw instruction background
        instruction_rect = pygame.Rect(0, self.game_height, self.width, self.instruction_height)
        pygame.draw.rect(self.screen, self.DARK_GRAY, instruction_rect)
        
        # Draw border line
        pygame.draw.line(self.screen, self.GRAY, (0, self.game_height), (self.width, self.game_height), 2)
        
        # Prepare instruction text based on game state
        if not self.game_active:
            instruction_text = "Click to draw cells | S: Start | E: Exit"
        else:
            instruction_text = f"Generation: {self.generation_count} | E: Exit"
        
        # Render and display instruction text
        text_surface = self.font.render(instruction_text, True, self.WHITE)
        text_rect = text_surface.get_rect(center=(self.width // 2, self.game_height + self.instruction_height // 2))
        self.screen.blit(text_surface, text_rect)
    


    def draw_grid(self):
        """Drawing grid in screen - your original function with instruction area"""

        # Clear only the game area, not the instruction area
        game_area_rect = pygame.Rect(0, 0, self.width, self.game_height)
        pygame.draw.rect(self.screen, self.BLACK, game_area_rect)
        
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                
                if (i % 2 == 0):  # For even rows
                    # If cell is alive
                    if self.grid[i][j] == 1:
                        self.draw_polygon(self.WHITE, 6,
                                        math.sqrt(3) * self.radius + self.radius * math.sqrt(3) * j,
                                        self.radius / 2 + 1.5 * self.radius * i, self.radius)
                    # If cell is dead
                    elif self.grid[i][j] == 0:
                        self.draw_polygon(self.BLACK, 6,
                                        math.sqrt(3) * self.radius + self.radius * math.sqrt(3) * j,
                                        self.radius / 2 + 1.5 * self.radius * i, self.radius)
                        
                else:  # For odd rows
                    # If cell is alive
                    if self.grid[i][j] == 1:
                        self.draw_polygon(self.WHITE, 6,
                                        self.radius * 1.5 * math.sqrt(3) + self.radius * math.sqrt(3) * j,
                                        1.5 * self.radius * i + self.radius / 2, self.radius)
                    # If cell is dead
                    elif self.grid[i][j] == 0:
                        self.draw_polygon(self.BLACK, 6,
                                        self.radius * 1.5 * math.sqrt(3) + self.radius * math.sqrt(3) * j,
                                        1.5 * self.radius * i + self.radius / 2, self.radius)
        
        # Draw instruction area
        self.draw_instruction_area()
        pygame.display.update()
    
    def count_neighbours(self, row, column):
        """Looking for neighbours - your original function"""

        count = 0
        # Define neighbor offsets for even and odd rows
        if row % 2 == 0:  # Even row
            neighbors = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]
        else:  # Odd row
            neighbors = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]
        
        for dr, dc in neighbors:
            new_row, new_col = row + dr, column + dc
            if 0 <= new_row < self.rows and 0 <= new_col < self.columns:
                count += self.grid[new_row][new_col]
        return count
    
    def update_grid(self):
        """Update grid - your original function"""

        new_grid = np.zeros((self.rows, self.columns))  # Making new local grid 
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                
                # When a particular cell is alive
                if self.grid[i][j] == 1:
                    if (self.count_neighbours(i, j) < 2 and self.previous[i][j] != 1):  # Dies because of under population denoted by 1
                        new_grid[i][j] = 0
                        self.generation[i][j] = 0
                        self.previous[i][j] = 1
                    elif (self.count_neighbours(i, j) > 3 and self.previous[i][j] != 2):  # Died because of over Population denoted by 2
                        new_grid[i][j] = 0
                        self.generation[i][j] = 0
                        self.previous[i][j] = 2
                    elif self.count_neighbours(i, j) == 2 or self.count_neighbours(i, j) == 3:
                        new_grid[i][j] = 1
                    else:
                        new_grid[i][j] = 1
                # When a particular cell is dead
                elif self.grid[i][j] == 0:
                    if self.count_neighbours(i, j) == 3:
                        new_grid[i][j] = 1
                        self.generation[i][j] = 0
                    elif self.generation[i][j] == 6:
                        new_grid[i][j] = 1
                        self.generation[i][j] = 0
        
        # Random dead cell becomes alive after every 4 population          
        if (self.generation_count % 4 == 1):
            attempts = 0
            while attempts < 1000:
                random_row = np.random.randint(0, self.rows)        # Random row
                random_column = np.random.randint(0, self.columns)  # Random column
                if self.grid[random_row][random_column] == 0:
                    new_grid[random_row][random_column] = 1
                    self.generation[random_row][random_column] = 0
                    break
                attempts += 1
        
        self.generation_count = self.generation_count + 1  
        self.generation = self.generation + 1    
        return new_grid  # Returning the local grid
    
    def mouse_input(self):
        """Mouse input - your original function with adjusted coordinates"""

        if pygame.mouse.get_pressed()[0] and not self.game_active:
            pos = pygame.mouse.get_pos()
            # Only process clicks in the game area, not instruction area
            if pos[1] < self.game_height:
                row = math.floor((pos[1] - self.radius / 2) / (1.5 * self.radius))
                column = math.floor(
                    (pos[0] - ((row % 2) * math.sqrt(3) * self.radius * 0.5)) /
                    (math.sqrt(3) * self.radius))
                if 0 <= row < self.rows and 0 <= column < self.columns:
                    if self.grid[row][column] == 0:
                        self.grid[row][column] = 1
    
    def check_all_white(self):
        """Check if all cells are white - your original function"""
        return np.all(self.grid == 1)
    
    def main(self):
        """Main function - your original function converted to method"""
        self.running = True
        self.game_active = False
        
        self.generation = np.ones((self.rows, self.columns))
        self.previous = np.zeros((self.rows, self.columns))
        self.generation_count = 1
        
        # Infinite Loop and exits until PyGame is Quit
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s and not self.game_active:
                        self.game_active = True
                    elif event.key == pygame.K_e:
                        self.running = False
            
            self.mouse_input()
            
            if self.game_active:
                pygame.image.save(self.screen, "Output\\output%d.png" % self.generation_count)  # Saving picture
                new_grid = self.update_grid()
                self.grid = new_grid  # Giving the value of local grid to the global grid
                pygame.time.wait(500)
                # Check if all cells are white
                if self.check_all_white():
                    print("All cells are alive! Simulation ending")
                    self.running = False
            
            self.draw_grid()

# Usage
if __name__ == "__main__":
    game = HexagonalGameOfLife()
    game.main()
    pygame.quit()
