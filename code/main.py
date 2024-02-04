import pygame
import sys
import random

# Constants for the game
TILE_SIZE = 40
MAP_WIDTH, MAP_HEIGHT = 21, 21
SCREEN_WIDTH, SCREEN_HEIGHT = TILE_SIZE * MAP_WIDTH, TILE_SIZE * MAP_HEIGHT
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 200, 0)
GREY = (128, 128, 128)
PURPLE = (128, 0, 128)
BROWN = (165, 42, 42)
GREEN = (0, 128, 0)
LIME_GREEN = (50, 205, 50)
LIGHT_GREEN = (144, 238, 144)
LIGHT_YELLOW = (255, 255, 150)
LIGHT_BROWN = (181, 101, 29)

ORE_TYPES = {
    'Stone': {'color': (150, 150, 150), 'id': 0, 'durability': 2},
    'Iron': {'color': (184, 115, 51), 'id': 1, 'durability': 3},
    'Copper': {'color': (218, 165, 32), 'id': 2, 'durability': 3},
    'Tin': {'color': (192, 192, 192), 'id': 3, 'durability': 3},
    'Gold': {'color': (255, 215, 0), 'id': 4, 'durability': 4},
    'Silver': {'color': (192, 192, 192), 'id': 5, 'durability': 4},
    'Platinum': {'color': (229, 228, 226), 'id': 6, 'durability': 5},
    'Mithril': {'color': (0, 191, 255), 'id': 7, 'durability': 6},
    'Adamantine': {'color': (163, 163, 194), 'id': 8, 'durability': 7},
    'Crystal Quartz': {'color': (224, 255, 255), 'id': 9, 'durability': 5},
    'Gemstones': {'color': (255, 0, 0), 'id': 10, 'durability': 6},  # For all gemstones
    'Coal': {'color': (54, 69, 79), 'id': 11, 'durability': 2},
    'Obsidian': {'color': (47, 79, 79), 'id': 12, 'durability': 6}
}

# Probabilities for each ore type (in percent)
ORE_PROBABILITIES = {
    'Stone': 35,  # Most common
    'Iron': 20,
    'Coal': 15,  # Making coal more common
    'Copper': 10,
    'Tin': 5,
    'Gold': 4,
    'Silver': 3,
    'Platinum': 2,
    'Mithril': 2,
    'Adamantine': 1,
    'Crystal Quartz': 1,
    'Gemstones': 1,  # Rare gemstones
    'Obsidian': 1
}

# Ensure total probability is 100%
assert sum(ORE_PROBABILITIES.values()) == 100, "Total probability must be 100%"

resources = {
    # Ores
    'Stone': 0,
    'Iron': 0,
    'Coal': 0,
    'Copper': 0,
    'Tin': 0,
    'Gold': 0,
    'Silver': 0,
    'Platinum': 0,
    'Mithril': 0,
    'Adamantine': 0,
    'Crystal Quartz': 0,
    'Gemstones': 0,
    'Obsidian': 0,

    # Plants
    'Wheat': 0,
    'Berries': 0,
    'Herbs': 0,
    'Mushrooms': 0,
    'Carrots': 0,
    'Potatoes': 0,
    'Tomatoes': 0,
    'Corn': 0,
    'Cotton': 0,

    # Food
    'Bread': 0,
    'Raw Meat': 0,
    'Cooked Meat': 0,
    'Fish': 0,
    'Cooked Fish': 0,
    'Soup': 0,
    'Cooked Vegetables': 0,

    # Animal Resources
    'Leather': 0,
    'Wool': 0,
    'Eggs': 0,
    'Feathers': 0,
    'Bone': 0,
    'Scales': 0,

    # Weapons
    'Sword': 0,
    'Axe': 0,
    'Short Bow': 0,
    'Long Bow': 0,
    'Arrows': 0,
    'Dagger': 0,
    'Spear': 0,
    'Hammer': 0,
    'Mace': 0,
    
    # Armor
    'Leather Armor': 0,
    'Iron Armor': 0,
    'Platinum Armor': 0,
    'Shield': 0,

}

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Colony Game Tilemap')
clock = pygame.time.Clock()

class OreTile:
    def __init__(self, x, y, ore_type, num_speckles=10):
        self.x = x
        self.y = y
        self.ore_type = ore_type
        self.ore_id = ORE_TYPES[ore_type]['id']
        self.color = ORE_TYPES[ore_type]['color']
        self.hits_to_mine = ORE_TYPES[ore_type]['durability']
        if ore_type == 'Stone':
            self.speckles = []
        else:
            self.speckles = [(random.randint(self.x * TILE_SIZE, (self.x + 1) * TILE_SIZE),
                              random.randint(self.y * TILE_SIZE, (self.y + 1) * TILE_SIZE),
                              self.color) for _ in range(num_speckles)]

    def draw(self):
        # Draw the base tile
        base_rect = pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, GREY, base_rect)

        # Draw speckles
        for speckle_x, speckle_y, _ in self.speckles:
            pygame.draw.circle(screen, self.color, (speckle_x, speckle_y), 2)

class FarmTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.stage = 0  # Represents the growth stage (0: Soil, 1: Growing, 2: Ripe)
        self.color = LIGHT_BROWN  # Initial color for soil
        self.last_update_time = pygame.time.get_ticks()  # Get the initial time

    def update(self):
        current_time = pygame.time.get_ticks()  # Get the current time
        if current_time - self.last_update_time >= 5000:  # Check if 5 seconds have passed
            self.last_update_time = current_time  # Update the last update time
            # Update the growth stage
            if self.stage < 2:
                self.stage += 1
                self.color = LIGHT_GREEN if self.stage == 1 else LIGHT_YELLOW  # Update color based on stage

    def draw(self):
        # Draw the farm tile
        base_rect = pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, self.color, base_rect)
        # Add speckles for visual effect
        if self.stage > 0:
            for _ in range(10):  # Number of speckles
                speckle_x = random.randint(self.x * TILE_SIZE, (self.x + 1) * TILE_SIZE)
                speckle_y = random.randint(self.y * TILE_SIZE, (self.y + 1) * TILE_SIZE)
                pygame.draw.circle(screen, LIME_GREEN if self.stage == 1 else YELLOW, (speckle_x, speckle_y), 2)

def draw_resource_panel(screen, resources, x, y, width, height):
    # Draw the background of the panel
    panel_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, (100, 100, 100), panel_rect)  # Grey background

    # Display each resource and its amount
    font = pygame.font.SysFont(None, 24)
    line_counter = 0
    for resource, amount in resources.items():
        # Skip resources with a quantity of 0
        if amount == 0:
            continue

        text = font.render(f"{resource}: {amount}", True, WHITE)
        screen.blit(text, (x + 10, y + 10 + line_counter * 30))
        line_counter += 1

# NPCs
class NPC:
    def __init__(self, x, y, color, npc_type):
        self.x = x
        self.y = y
        self.color = color
        self.npc_type = npc_type

    def move(self, direction, ore_tiles):
        new_x, new_y = self.x, self.y

        if direction == 'up':
            new_y -= 1
        elif direction == 'down':
            new_y += 1
        elif direction == 'left':
            new_x -= 1
        elif direction == 'right':
            new_x += 1

        # Check if the new position is occupied by an ore tile
        if not any(tile.x == new_x and tile.y == new_y for tile in ore_tiles):
            self.x, self.y = new_x, new_y
    
    def is_leader_nearby(self, leader):
        # Calculate distance from the leader
        distance = max(abs(self.x - leader.x), abs(self.y - leader.y))
        return distance <= 5  # If the leader is within 5 tiles, return True

    def mine(self, ore_tiles, leader, click_pos):
        if self.npc_type != 'miner':
            return

        # Convert click position to tile coordinates
        click_x, click_y = click_pos[0] // TILE_SIZE, click_pos[1] // TILE_SIZE

        # Check if leader is nearby to increase mining speed
        leader_nearby = self.is_leader_nearby(leader)

        for tile in ore_tiles:
            if tile.x == click_x and tile.y == click_y and abs(tile.x - self.x) <= 1 and abs(tile.y - self.y) <= 1:
                hit_power = 2 if leader_nearby else 1
                tile.hits_to_mine -= hit_power
                if tile.hits_to_mine <= 0:
                    resources[tile.ore_type] += 1  # Update resources
                    print(f"Mined {tile.ore_type}, ID: {tile.ore_id}")
                    ore_tiles.remove(tile)  # Remove the mined tile
                break  # Stop after mining one tile

    def build(self):
        if self.npc_type == 'builder':
            # Implement building logic here
            pass

    def craft(self):
        if self.npc_type == 'crafter':
            # Implement crafting logic here
            pass

    def lead(self):
        if self.npc_type == 'leader':
            # Implement leadership logic here
            pass

    def farm(self, farm_tiles, click_pos, resources):
        if self.npc_type != 'farmer':
            return

        # Convert click position to tile coordinates
        click_x, click_y = click_pos[0] // TILE_SIZE, click_pos[1] // TILE_SIZE

        # Check if the farm tile is within range
        if abs(click_x - self.x) > 1 or abs(click_y - self.y) > 1:
            return

        # Check if there's already a farm tile here
        existing_tile = next((tile for tile in farm_tiles if tile.x == click_x and tile.y == click_y), None)

        # Check if there's an ore tile at the clicked position
        ore_tile = next((tile for tile in ore_tiles if tile.x == click_x and tile.y == click_y), None)
        if ore_tile:
            return

        if existing_tile:
            if existing_tile.stage == 2:  # Ripe for harvesting
                resources[existing_tile.crop_type] += 1  # Add crop to resources
                farm_tiles.remove(existing_tile)  # Remove the tile
        else:
            # Display menu for selecting what to plant
            print("Select a crop to plant:")
            for i, crop in enumerate(self.vegetables):
                print(f"{i + 1}. {crop}")

            # Get player's selection
            selection = int(input("Enter the number of the crop you want to plant: ")) - 1

            # Check if the selection is valid
            if selection < 0 or selection >= len(self.vegetables):
                print("Invalid selection.")
                return

            # Plant new farm tile with the selected crop
            farm_tiles.append(FarmTile(click_x, click_y, self.vegetables[selection]))
    
    def is_clicked(self, mouse_pos):
        # Check if the mouse click is within the NPC's tile
        rect = pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        return rect.collidepoint(mouse_pos)
    
    def draw(self):
        # Make the NPC a bit smaller than the tile
        padding = 10  # Increase padding to make the NPC smaller
        npc_rect = pygame.Rect(self.x * TILE_SIZE + padding, self.y * TILE_SIZE + padding, 
                               TILE_SIZE - 2 * padding, TILE_SIZE - 2 * padding)

        pygame.draw.rect(screen, self.color, npc_rect)

npcs = [
    NPC(10, 10, PURPLE, 'leader'),
    NPC(11, 10, YELLOW, 'builder'),  
    NPC(10, 11, GREY, 'miner'),      
    NPC(9, 10, BROWN, 'crafter'),
    NPC(10, 9, GREEN, 'farmer') 
    # NPC(x, y, COLOR, 'npc_type')  # Add more NPCs here
    # NPC(x, y, LIGHT_GREEN, 'cook'),
    # NPC(x, y, LIME_GREEN, 'scout'),
    # NPC(x, y, LIGHT_YELLOW, 'warrior'),
    # NPC(x, y, LIGHT_BROWN, 'shaman'),
    # NPC(x, y, GOLD, 'merchant'),
    # NPC(x, y, SILVER, 'scholar'),
    # NPC(x, y, PLATINUM, 'nurturer'),
    # NPC(x, y, MITHRIL, 'forager'),
    # NPC(x, y, ADAMANTINE, 'diplomat'),
    # NPC(x, y, CRYSTAL_QUARTZ, 'entertainer')
]

def choose_ore_type():
    rand_num = random.randint(1, 100)
    cumulative_probability = 0
    for ore_type, probability in ORE_PROBABILITIES.items():
        cumulative_probability += probability
        if rand_num <= cumulative_probability:
            return ore_type
    return 'Stone'  # Fallback, in case the probabilities don't sum up to 100

# Defining Tiles
ore_tiles = []
farm_tiles = []

for x in range(MAP_WIDTH):
    for y in range(MAP_HEIGHT):
        if 9 <= x <= 11 and 9 <= y <= 11:  # Skip the specific area
            continue
        ore_type = choose_ore_type()
        ore_tiles.append(OreTile(x, y, ore_type))

def draw_npc(npc):
    inner_rect = pygame.Rect(npc.x * TILE_SIZE + 5, npc.y * TILE_SIZE + 5, TILE_SIZE - 10, TILE_SIZE - 10)
    outer_rect = pygame.Rect(npc.x * TILE_SIZE, npc.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, RED, outer_rect)
    pygame.draw.rect(screen, npc.color, inner_rect)

def draw_grid():
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

def game_loop():
    selected_npc = 0  # Index of the currently selected NPC

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                # Left-click to select NPC
                if event.button == 1:
                    for i, npc in enumerate(npcs):
                        if npc.is_clicked(mouse_pos):
                            selected_npc = i
                            break

                # Right-click to mine, if the selected NPC is a miner
                elif event.button == 3 and npcs[selected_npc].npc_type == 'miner':
                    # Find the leader NPC
                    leader = next((npc for npc in npcs if npc.npc_type == 'leader'), None)

                    # Perform mining action, passing the leader NPC and mouse position
                    npcs[selected_npc].mine(ore_tiles, leader, mouse_pos)

                elif event.button == 3 and npcs[selected_npc].npc_type == 'farmer':
                    mouse_pos = event.pos
                    npcs[selected_npc].farm(farm_tiles, mouse_pos, resources)

            # Handling key presses for movement
            if event.type == pygame.KEYDOWN:
                # Cycle through NPCs with the spacebar
                if event.key == pygame.K_SPACE:
                    selected_npc = (selected_npc + 1) % len(npcs)

                # Determine the direction for the movement
                direction = None
                if event.key == pygame.K_w:
                    direction = 'up'
                elif event.key == pygame.K_s:
                    direction = 'down'
                elif event.key == pygame.K_a:
                    direction = 'left'
                elif event.key == pygame.K_d:
                    direction = 'right'

                # Move the selected NPC, if a direction is set
                if direction:
                    npcs[selected_npc].move(direction, ore_tiles)

        screen.fill(BLACK)
        draw_grid()
        for tile in farm_tiles:
            tile.update()
            tile.draw()
        for npc in npcs:
            npc.draw()
        for tile in ore_tiles:
            tile.draw()

        draw_resource_panel(screen, resources, 10, 10, 200, 100)
        pygame.display.flip()
        clock.tick(FPS)




game_loop()
