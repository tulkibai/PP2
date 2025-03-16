import os
import pygame
import keyboard

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()
        self.music_folder = music_folder
        self.playlist = self.load_music_files()
        self.current_index = 0
        self.is_playing = False

    def load_music_files(self):
        files = [f for f in os.listdir(self.music_folder) if f.endswith('.mp3')]
        files.sort()
        if not files:
            print("No MP3 files found in the folder:", self.music_folder)
        return files

    def play(self):
        if not self.playlist:
            return
        file_path = os.path.join(self.music_folder, self.playlist[self.current_index])
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        self.is_playing = True
        print("Playing:", self.playlist[self.current_index])

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        print("Stopped playback.")

    def next(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def previous(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

def main():
    music_folder = "music"
    player = MusicPlayer(music_folder)
    keyboard.add_hotkey('p', player.play)
    keyboard.add_hotkey('s', player.stop)
    keyboard.add_hotkey('n', player.next)
    keyboard.add_hotkey('b', player.previous)
    print("Music player controls:")
    print("Press 'p' to Play, 's' to Stop, 'n' for Next, 'b' for Previous")
    print("Press 'q' to Quit.")
    keyboard.wait('q')
    print("Exiting Music Player.")

if __name__ == '__main__':
    main()
