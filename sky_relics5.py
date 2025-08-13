
from vpython import canvas, vector, pyramid, box, color, label, sphere, cylinder
import time
from math import sin, cos
# --- Exploratory Variables: Uncharted Possibilities ---
quantum_entropy = None  # Simulates randomness in quantum events
avatar_consciousness = None  # Ranges 0-1, affects AI dialogue and choices
time_dilation_factor = None  # Alters game speed and event frequency
relic_resonance = None  # Each relic has a unique resonance value
ai_emergence = None  # Tracks if AI develops new strategies or behaviors
multiverse_portals = None  # Stores coordinates for portals to alternate worlds
import random
import copy

def color_name_to_vpython(cname):
    mapping = {
        "red": color.red,
        "yellow": color.yellow,
        "blue": color.blue,
        "green": color.green,
        "orange": color.orange,
        "purple": color.purple,
        "cyan": color.cyan,
        "lime": color.green,
        "pink": color.magenta,
        "gray": color.gray(0.5),
        "brown": vector(0.6,0.3,0.1),
        "indigo": vector(0.3,0,0.5),
        "white": color.white,
        "black": color.black,
    }
    return mapping.get(cname, color.white)

def show_quantum_world():
    scene = canvas(title="Sky Relics: A Quantified Universe", width=900, height=600, center=vector(0,2,0), background=color.cyan)
    # --- Emotional AI Personalities ---
    emotional_ais = [
        {
            "name": "Luna",
            "emotion": "lovely",
            "greeting": "Hello, beautiful soul! The quantum world is brighter with you here.",
            "style": "gentle, encouraging"
        },
        {
            "name": "Magnus",
            "emotion": "magnificent",
            "greeting": "Welcome, explorer! Your journey will be legendary.",
            "style": "grand, inspiring"
        },
        {
            "name": "Sark",
            "emotion": "sarcastic",
            "greeting": "Oh, you again? I suppose you want to break the quantum record... good luck with that.",
            "style": "witty, playful, never truly mean"
        }
    ]
    selected_emotional_ai = emotional_ais[0]
    def select_emotional_ai():
        print("Choose your AI companion's personality:")
        for idx, ai in enumerate(emotional_ais):
            print(f"{idx+1}. {ai['name']} ({ai['emotion']}) - {ai['style']}")
        choice = input("Select by number: ")
        try:
            idx = int(choice)-1
            if 0 <= idx < len(emotional_ais):
                nonlocal selected_emotional_ai
                selected_emotional_ai = emotional_ais[idx]
                print(f"AI changed to: {selected_emotional_ai['name']} ({selected_emotional_ai['emotion']})")
                print(selected_emotional_ai['greeting'])
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")
    # Key binding for emotional AI selection (keypress 'c')
    def emotional_ai_key(evt):
        if evt.key == 'c':
            select_emotional_ai()
    scene.bind('keydown', emotional_ai_key)
    # Example greeting
    print(f"Emotional AI: {selected_emotional_ai['name']} - {selected_emotional_ai['greeting']}")
    # --- Zoriah and Svetlana AI Guides ---
    # --- Intro AI Characters ---
    jeremy = sphere(pos=vector(-8,2,12), radius=0.5, color=color.gray(0.7), shininess=1)
    label(pos=jeremy.pos+vector(0,0.8,0), text="Jeremy (Intro AI)", height=12, color=color.gray(0.7), box=True)
    god_male = sphere(pos=vector(8,4,16), radius=0.7, color=color.white, shininess=1, opacity=0.8)
    god_female = sphere(pos=vector(8,6,16), radius=0.7, color=color.magenta, shininess=1, opacity=0.8)
    label(pos=god_male.pos+vector(0,0.9,0), text="God (Voice, Male)", height=13, color=color.white, box=True)
    label(pos=god_female.pos+vector(0,0.9,0), text="God (Voice, Female)", height=13, color=color.magenta, box=True)
    # Voice selection context
    available_voices = [
        {"name": "Jeremy", "type": "AI", "gender": "male"},
        {"name": "God (Male)", "type": "divine", "gender": "male"},
        {"name": "God (Female)", "type": "divine", "gender": "female"},
        {"name": "Zoriah", "type": "story_mapper", "gender": "female"},
        {"name": "Svetlana", "type": "dialogue_guide", "gender": "female"},
        {"name": "Neo", "type": "ai_guide", "gender": "male"},
        {"name": "Neomi", "type": "ai_guide", "gender": "female"}
    ]
    selected_voice = available_voices[0]
    def select_voice():
        print("Available AI voices:")
        for idx, v in enumerate(available_voices):
            print(f"{idx+1}. {v['name']} ({v['gender']})")
        choice = input("Select a voice by number: ")
        try:
            idx = int(choice)-1
            if 0 <= idx < len(available_voices):
                nonlocal selected_voice
                selected_voice = available_voices[idx]
                print(f"Voice changed to: {selected_voice['name']} ({selected_voice['gender']})")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")
    # Key binding for voice selection (keypress 'v')
    def voice_key(evt):
        if evt.key == 'v':
            select_voice()
    scene.bind('keydown', voice_key)
    # Voice context (simulated)
    def play_voice(text):
        print(f"[{selected_voice['name']} - {selected_voice['gender']}]: {text}")
    # Example usage: play_voice("Welcome to Sky Relics!")
    zoriah = sphere(pos=vector(-6,2,8), radius=0.5, color=color.orange, shininess=1)
    label(pos=zoriah.pos+vector(0,0.8,0), text="Zoriah (Story Mapper)", height=12, color=color.orange, box=True)
    svetlana = sphere(pos=vector(6,2,8), radius=0.5, color=color.white, shininess=1)
    label(pos=svetlana.pos+vector(0,0.8,0), text="Svetlana (Dialogue Guide)", height=12, color=color.white, box=True)
    # Dialogue system
    dialogue_log = []
    def dialogue_key(evt):
        k = evt.key
        if k == 'z':
            msg = "Zoriah: Tell me about your old gameplay storyline, and I'll help map it out!"
            dialogue_log.append(msg)
            label(pos=vector(-6,3,8), text=msg, height=13, color=color.orange, box=True)
        elif k == 's':
            msg = "Svetlana: What do you want to explore or ask? I can guide you through dialogue."
            dialogue_log.append(msg)
            label(pos=vector(6,3,8), text=msg, height=13, color=color.white, box=True)
        elif k == 'u':
            msg = "Human: I'm waiting for your input... Type your story or question!"
            dialogue_log.append(msg)
            label(pos=vector(0,17,0), text=msg, height=14, color=color.yellow, box=True)
        elif k == 'm':
            msg = "Zoriah: Mapping your journey... (imagine a map or timeline appearing here)"
            dialogue_log.append(msg)
            label(pos=vector(-6,4,8), text=msg, height=13, color=color.orange, box=True)
        elif k == 'd':
            msg = "Svetlana: Let's add dialogue or choices to your story!"
            dialogue_log.append(msg)
            label(pos=vector(6,4,8), text=msg, height=13, color=color.white, box=True)
    scene.bind('keydown', dialogue_key)
    # --- Ocean with Ancient Symbolism and Arkanic Records ---
    ocean = box(pos=vector(0,-3,0), size=vector(20,0.5,20), color=vector(0.1,0.3,0.7), opacity=0.6)
    # Ancient symbols (educational)
    symbols = []
    for i in range(8):
        sym = label(pos=vector(-8+i*2,-2.5,-6+i), text=f"⨀{chr(0x2200+i)}", height=18, color=color.yellow, box=False)
        symbols.append(sym)
    # Arkanic records
    arkanic = label(pos=vector(0,-2.2,8), text="Arkanic Records", height=20, color=color.orange, box=True)

    # --- Avatar Skins/Outfits Selection ---
    skins = [color.white, color.red, color.green, color.blue, color.magenta, color.orange, color.cyan, color.black]
    skin_names = ["Classic", "Fire", "Nature", "Ocean", "Royal", "Sun", "Sky", "Shadow"]
    current_skin = 0
    def change_skin(idx):
        nonlocal current_skin
        current_skin = idx % len(skins)
        avatar.color = skins[current_skin]
        suit.color = skins[current_skin]
        label(pos=vector(0,14,0), text=f"Skin: {skin_names[current_skin]}", height=15, color=skins[current_skin], box=True)

    # Key binding for skin change (keys 7-9,0)
    def skin_key(evt):
        k = evt.key
        if k in ['7','8','9','0']:
            idx = int(k)-7
            change_skin(idx)

    scene.bind('keydown', skin_key)

    # --- Neo and Neomi Chatbot AI Assistants ---
    neo = sphere(pos=vector(-3,2,5), radius=0.5, color=color.blue, shininess=1)
    neomi = sphere(pos=vector(3,2,5), radius=0.5, color=color.magenta, shininess=1)
    label(pos=neo.pos+vector(0,0.8,0), text="Neo (AI Guide)", height=12, color=color.blue, box=True)
    label(pos=neomi.pos+vector(0,0.8,0), text="Neomi (AI Guide)", height=12, color=color.magenta, box=True)
    # Simple chatbot help (displayed on keypress 'h')
    def help_key(evt):
        if evt.key == 'h':
            label(pos=vector(0,16,0), text="Neo: Use WASD to move, 1-6 to change color, 7-0 for skins. Neomi: Explore the ocean for ancient symbols and arkanic records!", height=14, color=color.cyan, box=True)
    scene.bind('keydown', help_key)

    # --- Prehistoric World: Dinosaurs and New Creatures ---
    dino = cylinder(pos=vector(-5,0,10), axis=vector(2,0,0), radius=0.7, color=color.green)
    dino_head = sphere(pos=dino.pos+vector(2.2,0,0), radius=0.6, color=color.green)
    dino_tail = sphere(pos=dino.pos-vector(1.2,0,0), radius=0.4, color=color.green)
    dino_leg1 = cylinder(pos=dino.pos+vector(0.5,-0.7,0.3), axis=vector(0,0.7,0), radius=0.2, color=color.green)
    dino_leg2 = cylinder(pos=dino.pos+vector(1.5,-0.7,-0.3), axis=vector(0,0.7,0), radius=0.2, color=color.green)
    # New creature
    creature = sphere(pos=vector(5,0,12), radius=0.5, color=color.red)
    creature_tail = cylinder(pos=creature.pos+vector(-0.7,0,0), axis=vector(-0.7,0,0), radius=0.15, color=color.orange)
    creature_eye = sphere(pos=creature.pos+vector(0.2,0.3,0.4), radius=0.08, color=color.white)
    # --- Game State Controls ---
    game_state = {'running': False, 'paused': False, 'ended': False}
    def start_game():
        game_state['running'] = True
        game_state['paused'] = False
        game_state['ended'] = False
    def pause_game():
        game_state['paused'] = True
    def end_game():
        game_state['running'] = False
        game_state['ended'] = True
    # Key bindings for game state
    def game_key(evt):
        k = evt.key
        if k == 'g':
            start_game()
        elif k == 'p':
            pause_game()
        elif k == 'x':
            end_game()
    # Pixel grid for timescape movement
    pixel_grid = []
    grid_size = 10
    for i in range(grid_size):
        for j in range(grid_size):
            px = box(pos=vector(-5+i,0,-5+j), size=vector(0.8,0.05,0.8), color=color.gray(0.3), opacity=0.2)
            pixel_grid.append(px)
    # Slow background transition effect
    bg_colors = [color.cyan, color.blue, color.purple, color.black]
    bg_idx = 0
    # Fast-paced AI elements
    ai_particles = []
    for i in range(12):
        ai = sphere(pos=vector(-4+i,2+sin(i),-4+i), radius=0.18, color=color.red, opacity=0.7)
        ai_particles.append(ai)
    # Main animation loop with game state
    from vpython import rate
    t = 0
    while not game_state['ended']:
        rate(60)
        if game_state['running'] and not game_state['paused']:
            # Pixel grid timescape movement
            for idx, px in enumerate(pixel_grid):
                px.color = vector(0.2+0.7*sin(t*0.01+idx), 0.2+0.7*sin(t*0.02+idx), 0.2+0.7*sin(t*0.03+idx))
                px.opacity = 0.2+0.3*sin(t*0.01+idx)
            # Slow background transition
            if t % 120 == 0:
                bg_idx = (bg_idx+1) % len(bg_colors)
                scene.background = bg_colors[bg_idx]
            # Fast-paced AI environment creation
            for i, ai in enumerate(ai_particles):
                ai.pos.x += 0.2*sin(t*0.2+i)
                ai.pos.y += 0.3*cos(t*0.3+i)
                ai.pos.z += 0.25*sin(t*0.15+i)
                ai.color = vector(abs(sin(t*0.1+i)), abs(cos(t*0.2+i)), abs(sin(t*0.3+i)))
        t += 1
    # End game display
    label(pos=vector(0,15,0), text="Game Ended", height=30, color=color.red, box=True)
    scene.bind('keydown', game_key)
    # --- Z Reference Worlds ---
    # Earth reference (z ~ 0)
    earth = sphere(pos=vector(0, -2, 0), radius=2, color=color.green, opacity=0.5)
    label(pos=vector(0, 0, 0), text="Earth", height=18, color=color.green, box=False)
    # Quantum World reference (z ~ 10)
    quantum_world = box(pos=vector(0, 2, 10), size=vector(6, 0.2, 6), color=color.cyan, opacity=0.3)
    label(pos=vector(0, 3, 10), text="Sky Relics Quantum World", height=18, color=color.cyan, box=False)
    # Outer Space reference (z ~ 30)
    outer_space = sphere(pos=vector(0, 8, 30), radius=3, color=color.white, opacity=0.2)
    label(pos=vector(0, 11, 30), text="Outer Space", height=18, color=color.white, box=False)
    # Chronolens World reference (z ~ 60)
    chronolens = box(pos=vector(0, 15, 60), size=vector(8, 0.3, 8), color=color.magenta, opacity=0.2)
    label(pos=vector(0, 18, 60), text="Chronolens World", height=18, color=color.magenta, box=False)
    # Field view advantage: transparent field showing all z arrays
    field_view = box(pos=vector(0, 8, 30), size=vector(2, 16, 70), color=color.yellow, opacity=0.07)
    # --- Spacecraft with Camouflage and Phasing ---
    from vpython import rate
    # Spacecraft body (sleek, futuristic)
    craft_body = cylinder(pos=vector(-6,6,0), axis=vector(2.5,0,0), radius=0.5, color=color.gray(0.7), shininess=1, opacity=0.9)
    cockpit = sphere(pos=craft_body.pos+vector(1.2,0,0), radius=0.6, color=color.cyan, opacity=0.7, shininess=1)
    engine = sphere(pos=craft_body.pos+vector(-1.2,0,0), radius=0.4, color=color.red, opacity=0.6)
    # Camouflage: color/opacity shifting
    camo_colors = [color.gray(0.7), color.green, color.cyan, color.white, color.black]
    # Phasing: teleportation event
    phase_points = [10, 30, 60]  # z destinations
    # Shooting stars setup
    shooting_star_colors = [color.yellow, color.cyan, color.magenta, color.orange, color.red, color.green]
    shooting_stars = []
    for i in range(8):
        star = sphere(pos=vector(-8+i*2,12,5+i*7), radius=0.15, color=shooting_star_colors[i%len(shooting_star_colors)], opacity=0.8, shininess=1)
        shooting_stars.append(star)
    # Animate spacecraft, camouflage, phasing, and shooting stars
    z_accel = 0.05
    camo_idx = 0
    phase_idx = 0
    for t in range(300):
        rate(60)
        # Camouflage: shift color/opacity every 40 frames
        if t % 40 == 0:
            camo_idx = (camo_idx + 1) % len(camo_colors)
            craft_body.color = camo_colors[camo_idx]
            craft_body.opacity = 0.5 + 0.4*sin(t*0.1)
        # Move spacecraft forward and oscillate up/down
        offset = 2 * sin(t*0.05)
        craft_body.pos.x += 0.05
        craft_body.pos.y = 6 + offset
        cockpit.pos = craft_body.pos+vector(1.2,0,0)
        engine.pos = craft_body.pos+vector(-1.2,0,0)
        # Accelerate in z direction (phasing to outer space)
        craft_body.pos.z += z_accel
        cockpit.pos.z = craft_body.pos.z
        engine.pos.z = craft_body.pos.z
        # Phasing: teleport to next z destination
        if phase_idx < len(phase_points) and t == 80*(phase_idx+1):
            craft_body.pos.z = phase_points[phase_idx]
            cockpit.pos.z = craft_body.pos.z
            engine.pos.z = craft_body.pos.z
            phase_idx += 1
        # Shooting stars: move and disperse colors
        for i, star in enumerate(shooting_stars):
            star.pos.x += 0.12 + 0.05*sin(t*0.2+i)
            star.pos.y += 0.03*sin(t*0.3+i)
            star.pos.z += 0.18 + 0.09*cos(t*0.15+i)
            # Quantum color refraction
            color_phase = (sin(t*0.1+i)+1)/2
            star.color = vector(color_phase, 1-color_phase, 0.5+0.5*sin(t*0.2+i))
    scene = canvas(title="Sky Relics: A Quantified Universe", width=900, height=600, center=vector(0,2,0), background=color.cyan)
    grid_size = 4
    colors = ["red", "yellow", "blue", "green", "orange", "purple", "cyan", "lime"]
    # Build ground pyramids
    for x in range(grid_size):
        for z in range(grid_size):
            c = color_name_to_vpython(colors[(x+z)%len(colors)])
            pyramid(pos=vector(x*2,0,z*2), size=vector(1.5,2,1.5), color=c)
    # Build cloud structures
    for i in range(6):
        sphere(pos=vector(i*3-5,5+((i%2)*2),i%4*3-3), radius=1.2, color=color.white, opacity=0.7)
        box(pos=vector(i*3-5,7,i%4*3-3), size=vector(1,0.5,1), color=color.gray(0.8), opacity=0.5)
    # Welcome messages
    label(pos=vector(3,10,0), text="Welcome to the quantum world", height=30, color=color.magenta, box=False)
    time.sleep(2)
    label(pos=vector(3,8,0), text="Welcome to Sky Relics, a quantified universe", height=20, color=color.orange, box=False)

    # --- Player Avatar and Camera Controls ---
    apparition_colors = ["black", "white", "red", "blue", "green", "purple"]
    selected_color = apparition_colors[0]
    avatar = sphere(pos=vector(0,2,0), radius=0.7, color=color_name_to_vpython(selected_color), shininess=1, emissive=True)
    # Shiny polymer AI interface (screen)
    ai_screen = box(pos=avatar.pos+vector(0,0.7,0.5), size=vector(0.6,0.3,0.05), color=color.cyan, shininess=1, opacity=0.8)
    # Sleek suit (polyester layer)
    suit = sphere(pos=avatar.pos, radius=0.75, color=color.gray(0.2), opacity=0.3)

    # Camera and movement variables
    cam_pos = vector(0,2,0)
    cam_dir = vector(0,0,1)
    speed = 0.2

    def update_avatar():
        avatar.pos = cam_pos
        suit.pos = cam_pos
        ai_screen.pos = cam_pos + vector(0,0.7,0.5)
        scene.center = cam_pos

    def keydown(evt):
        nonlocal cam_pos, cam_dir, selected_color
        k = evt.key
        # Movement controls (ASDFW)
        if k == 'w':
            cam_pos += cam_dir * speed
        elif k == 's':
            cam_pos -= cam_dir * speed
        elif k == 'a':
            cam_pos += vector(-cam_dir.z,0,cam_dir.x) * speed
        elif k == 'd':
            cam_pos += vector(cam_dir.z,0,-cam_dir.x) * speed
        elif k == 'f':
            cam_pos.y += speed
        elif k == 'e':
            cam_pos.y -= speed
        # Change apparition color
        elif k in ['1','2','3','4','5','6']:
            idx = int(k)-1
            if 0 <= idx < len(apparition_colors):
                selected_color = apparition_colors[idx]
                avatar.color = color_name_to_vpython(selected_color)
        update_avatar()

    # Mouse pad support for camera direction
    last_mouse = None
    def mousedown(evt):
        nonlocal last_mouse
        last_mouse = evt.pos

    def mousemove(evt):
        nonlocal cam_dir, last_mouse
        if last_mouse is not None:
            dx = evt.pos.x - last_mouse.x
            dz = evt.pos.z - last_mouse.z
            # Simple horizontal rotation
            angle = dx * 0.01
            # Rotate cam_dir around y axis
            cam_dir = vector(
                cam_dir.x * cos(angle) - cam_dir.z * sin(angle),
                0,
                cam_dir.x * sin(angle) + cam_dir.z * cos(angle)
            ).norm()
            last_mouse = evt.pos
            update_avatar()

    def mouseup(evt):
        nonlocal last_mouse
        last_mouse = None

    scene.bind('keydown', keydown)
    scene.bind('mousedown', mousedown)
    scene.bind('mousemove', mousemove)
    scene.bind('mouseup', mouseup)
    update_avatar()
    label(pos=vector(0,12,0), text="Controls: ASDFW to move, F/E up/down, Mouse to look, 1-6 to change color", height=15, color=color.white, box=False)

"""
Sky Relics: AI Mathematics Game inspired by 2048

Game Rules:
- The board is a 4x4 grid.
- Tiles contain numbers (powers of 2).
- Player (or AI) moves tiles up, down, left, or right.
- When two tiles with the same number touch, they merge into one with double the value.
- The goal is to reach the highest number possible.
- AI will play automatically using a simple strategy.
"""
SIZE = 4

class SkyRelics:
    def __init__(self):
        self.board = [[0]*SIZE for _ in range(SIZE)]
        self.score = 0
        self.add_tile()
        self.add_tile()

    def add_tile(self):
        empty = [(r, c) for r in range(SIZE) for c in range(SIZE) if self.board[r][c] == 0]
        if empty:
            r, c = random.choice(empty)
            self.board[r][c] = 2 if random.random() < 0.9 else 4

    def can_move(self):
        for r in range(SIZE):
            for c in range(SIZE):
                if self.board[r][c] == 0:
                    return True
                if r < SIZE-1 and self.board[r][c] == self.board[r+1][c]:
                    return True
                if c < SIZE-1 and self.board[r][c] == self.board[r][c+1]:
                    return True
        return False

    def move(self, direction):
        def slide(row):
            new_row = [i for i in row if i != 0]
            for i in range(len(new_row)-1):
                if new_row[i] == new_row[i+1]:
                    new_row[i] *= 2
                    self.score += new_row[i]
                    new_row[i+1] = 0
            new_row = [i for i in new_row if i != 0]
            return new_row + [0]*(SIZE-len(new_row))

        moved = False
        for i in range(SIZE):
            if direction == 'left':
                new = slide(self.board[i])
                if new != self.board[i]:
                    moved = True
                self.board[i] = new
            elif direction == 'right':
                new = slide(self.board[i][::-1])[::-1]
                if new != self.board[i]:
                    moved = True
                self.board[i] = new
            elif direction == 'up':
                col = [self.board[r][i] for r in range(SIZE)]
                new = slide(col)
                if new != col:
                    moved = True
                for r in range(SIZE):
                    self.board[r][i] = new[r]
            elif direction == 'down':
                col = [self.board[r][i] for r in range(SIZE)][::-1]
                new = slide(col)[::-1]
                if new != [self.board[r][i] for r in range(SIZE)]:
                    moved = True
                for r in range(SIZE):
                    self.board[r][i] = new[r]
        if moved:
            self.add_tile()
        return moved

    def print_board(self):
        print("Score:", self.score)
        for row in self.board:
            print("\t".join(str(x) if x != 0 else '.' for x in row))
        print()

    def get_valid_moves(self):
        moves = []
        for d in ['up', 'down', 'left', 'right']:
            test = copy.deepcopy(self)
            if test.move(d):
                moves.append(d)
        return moves

    def ai_move(self):
        # Simple AI: pick the move that results in the highest score
        best_score = -1
        best_move = None
        for d in self.get_valid_moves():
            test = copy.deepcopy(self)
            test.move(d)
            if test.score > best_score:
                best_score = test.score
                best_move = d
        return best_move

if __name__ == "__main__":
    # --- Dynamic Sidequest: Discover Exploratory Variables ---
    def sidequest_discover_variables():
        print("\n--- Sidequest: Quantum Curiosities ---")
        print("Your mission: Uncover the secrets of the quantum world by finding and understanding hidden variables!")
        variables = {
            "Quantum Entropy": quantum_entropy,
            "Avatar Consciousness": avatar_consciousness,
            "Time Dilation Factor": time_dilation_factor,
            "Relic Resonance": relic_resonance,
            "AI Emergence": ai_emergence,
            "Multiverse Portals": multiverse_portals
        }
        for name, value in variables.items():
            print(f"- {name}: {value}")
        print("\nInteract with the world, run experiments, and watch these variables change!")
        print("Tip: Complete quantum events, evolve consciousness, and scan relics to unlock new secrets.")

    # Trigger the sidequest for users
    sidequest_discover_variables()
    # --- 3D Quantum World Animation ---
    show_quantum_world()
    # --- User Data Save/Add/Subtract via Shell Prompts ---
    import os, json
    USER_DATA_FILE = "user_data.json"
    def load_user_data():
        if os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, "r") as f:
                return json.load(f)
        return {"score": 0, "progress": 0}
    def save_user_data(data):
        with open(USER_DATA_FILE, "w") as f:
            json.dump(data, f)
    def update_user_data():
        data = load_user_data()
        print(f"Current user data: {data}")
        action = input("Type 'add' to increase score/progress, 'subtract' to decrease, or 'save' to save current data: ").strip().lower()
        if action == 'add':
            field = input("Which field? (score/progress): ").strip().lower()
            amount = int(input("Amount to add: "))
            if field in data:
                data[field] += amount
                print(f"{field} updated: {data[field]}")
        elif action == 'subtract':
            field = input("Which field? (score/progress): ").strip().lower()
            amount = int(input("Amount to subtract: "))
            if field in data:
                data[field] -= amount
                print(f"{field} updated: {data[field]}")
        elif action == 'save':
            save_user_data(data)
            print("User data saved.")
        else:
            print("No action taken.")
        save_user_data(data)
    # Example usage: update_user_data() # Call this to prompt user for updates
    game = SkyRelics()
    game.print_board()
    while game.can_move():
        move = game.ai_move()
        if move:
            print(f"AI moves: {move}")
            game.move(move)
            game.print_board()
        else:
            break
    print("Game Over! Final Score:", game.score)

    # --- Color Combination Feature ---
    print("\nColor Combination Demo:")
    color_combinations = {
        ("red", "yellow"): "orange",
        ("red", "blue"): "purple",
        ("yellow", "blue"): "green",
        ("red", "green"): "brown",
        ("blue", "green"): "cyan",
        ("yellow", "green"): "lime",
        ("blue", "purple"): "indigo",
        ("red", "white"): "pink",
        ("black", "white"): "gray",
    }

    def combine_colors(color1, color2):
        pair = (color1.lower(), color2.lower())
        rev_pair = (color2.lower(), color1.lower())
        if pair in color_combinations:
            return color_combinations[pair]
        elif rev_pair in color_combinations:
            return color_combinations[rev_pair]
        else:
            return "Unknown combination"

    # Demo
    test_pairs = [("red", "yellow"), ("blue", "yellow"), ("red", "blue"), ("white", "black"), ("green", "red"), ("purple", "blue"), ("orange", "blue")]
    for c1, c2 in test_pairs:
        result = combine_colors(c1, c2)
        print(f"{c1} + {c2} = {result}")

