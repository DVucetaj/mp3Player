from tkinter import *
from tkinter import filedialog
import pygame

root = Tk()
root.title('Audio File Player')
root.geometry('650x400')

# Initialize Pygame Mixer
pygame.mixer.init()

# Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/',
                                      title='Choose a song',
                                      filetypes=(('mp3 Files', '*.mp3'), ))
    # Strip location and mp3 file extension from name
    #song = song.replace('/Users/donatvucetaj/code/mp3Player/audio/', '')
    #song = song.replace('.mp', '')
    song_box.insert(END, song)

# Play Selected song
def play():
    song = song_box.get(ACTIVE)
    #song = (f'/Users/donatvucetaj/code/mp3Player/audio/{song}.mp3')
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
# Stop playing current song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

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
play_button_img = PhotoImage(file='gui/play50.png')
pause_button_img = PhotoImage(file='gui/pause50.png')
stop_button_img = PhotoImage(file='gui/stop50.png')

# Create player control frames
controls_frame = Frame(root)
controls_frame.pack()

# Create player control buttons
back_button = Button(controls_frame,
                     image=back_button_img,
                     borderwidth=0)
forward_button = Button(controls_frame,
                        image=forward_button_img,
                        borderwidth=0)
play_button = Button(controls_frame,
                     image=play_button_img,
                     borderwidth=0,
                     command=play)
pause_button = Button(controls_frame,
                      image=pause_button_img,
                      borderwidth=0)
stop_button = Button(controls_frame,
                     image=stop_button_img,
                     borderwidth=0,
                     command=stop)

# Create player control buttons Grid
back_button.grid(row=0, column=0)
forward_button.grid(row=0, column=3)
play_button.grid(row=0, column=2)
pause_button.grid(row=0, column=1)
stop_button.grid(row=0, column=4)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add one song to playist", command=add_song)

root.mainloop()