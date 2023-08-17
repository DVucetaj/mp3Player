from tkinter import *
from tkinter import filedialog
import pygame

song_global = None
root = Tk()
root.title('Audio File Player')
root.geometry('650x400')

# Initialize Pygame Mixer
pygame.mixer.init()

# Modify global song variable
def modify_song(song):
    global song_global
    song_global = song
    
# Add Song Function
def add_song():
    global song_global

    new_song = filedialog.askopenfilename(
        initialdir='audio/',
        title='Choose a song',
        filetypes=(('mp3 Files', '*.mp3'),)
    )

    if new_song:
        modify_song(new_song)
        song_box.insert(END, song_global)

    
# Checks if music is playing
def is_busy():
    return pygame.mixer.music.get_busy()

# Checks if Global is active
def is_active():
    return song_box.get(ACTIVE) == song_global

# Checks if Active song matches Global song
def is_active():
    return song_box.get(ACTIVE) == song_global

# Play Selected song
def play():
    global song_global

    active_song = song_box.get(ACTIVE)

    if is_active():
        if is_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    else:
        song_global = active_song  # Update the global song
        pygame.mixer.music.load(song_global)
        pygame.mixer.music.play(loops=0, fade_ms=-1)

    
# Stop playing current song
def stop():
    pygame.mixer.music.stop()
    song_global = None
    song_box.selection_clear(ACTIVE)

# Play last song
def back():
    pass

# Play next song
def forward():
    pass


# Create Playlist Box
song_box = Listbox(root,
                   bg='white',
                   fg='green',
                   width=60,
                   selectbackground='gray',
                   selectforeground='black')
song_box.pack(pady=20)

# Create player control button images
back_button_img = PhotoImage(file='gui/reverse50.png')
forward_button_img = PhotoImage(file='gui/forward50.png')
playpause_button_img = PhotoImage(file='gui/playpause50.png')
stop_button_img = PhotoImage(file='gui/stop50.png')

# Create player control frames
controls_frame = Frame(root)
controls_frame.pack()

# Create player control buttons
back_button = Button(controls_frame,
                     image=back_button_img,
                     borderwidth=0,
                     command=back)

forward_button = Button(controls_frame,
                        image=forward_button_img,
                        borderwidth=0,
                        command=forward)

play_button = Button(controls_frame,
                     image=playpause_button_img,
                     borderwidth=0,
                     command=play)

stop_button = Button(controls_frame,
                     image=stop_button_img,
                     borderwidth=0,
                     command=stop)

# Create player control buttons Grid
back_button.grid(row=0, column=0)
forward_button.grid(row=0, column=2)
play_button.grid(row=0, column=1)
stop_button.grid(row=0, column=3)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add a song", command=add_song)

root.mainloop()