import pygame


class MusicTrack:
    def __init__(self, name, artist, genre, duration, file_link):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.duration = duration
        self.file_link = file_link


class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)

    def remove_track(self, track):
        self.tracks.remove(track)

    def list_tracks(self):
        for track in self.tracks:
            print(f"{track.name} by {track.artist} ({track.duration} min)")


class User:
    def __init__(self, name):
        self.name = name
        self.playlists = {}

    def create_playlist(self, name):
        playlist = Playlist(name)
        self.playlists[name] = playlist

    def remove_playlist(self, name):
        del self.playlists[name]

    def find_playlist(self, name):
        return self.playlists.get(name)

    def find_track(self, name):
        for playlist in self.playlists.values():
            for track in playlist.tracks:
                if track.name == name:
                    return track

    def list_playlists(self):
        for playlist in self.playlists.values():
            print(playlist.name)

    def play_track(self, track):
        pygame.mixer.init()
        pygame.mixer.music.load(track.file_link)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

class MusicPlayer:
    def __init__(self, user):
        self.user = user
        self.current_track = None

    def display_playlists(self):
        print("Your playlists:")
        for playlist in self.user.playlists.values():
            print(f"- {playlist.name}")
        print()

    def select_playlist(self):
        self.display_playlists()
        playlist_name = input("Select a playlist: ")
        playlist = self.user.find_playlist(playlist_name)
        if playlist:
            return playlist
        else:
            print("Playlist not found.")
            return None

    def display_tracks(self, playlist):
        print(f"Tracks in {playlist.name}:")
        for track in playlist.tracks:
            print(f"- {track.name} by {track.artist}")
        print()

    def select_track(self, playlist):
        self.display_tracks(playlist)
        track_name = input("Select a track: ")
        track = self.user.find_track(track_name)
        if track:
            self.current_track = track
            print(f"Now playing {track.name} by {track.artist}.")

        else:
            print("Track not found.")

    def play(self):
        if self.current_track:
            print(f"Playing {self.current_track.name}...")
            user.play_track(self.current_track)
        else:
            print("No track selected.")

user = User("Alice")
user.create_playlist("My Playlist")
user.create_playlist("Party Mix")
user.playlists["My Playlist"].add_track(MusicTrack("Down At McDonaldz", "Electric Six", "Rock", 3.5, "Electric_Six_-_Down_At_McDonaldz_(musmore.com) (1).mp3"))
user.playlists["My Playlist"].add_track(MusicTrack("RU Mine", "Arctic Monkeys", "Rock", 4.2, "Arctic_Monkeys_-_R_U_Mine_(musmore.com).mp3"))
user.playlists["Party Mix"].add_track(MusicTrack("Ruby", "Kaiser Chiefs", "Rock", 5.1, "Kaiser_Chiefs_-_Ruby_(musmore.com).mp3"))

player = MusicPlayer(user)
playlist = player.select_playlist()
if playlist:
    player.select_track(playlist)
    player.play()
