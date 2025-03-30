import subprocess  # Module to run external processes
import threading  # Module to handle threading and timers

# Path to the song file
# Update this path to the location of your song file
song_path = "/home/aazir/Desktop/CVproject/asrna.mp3"

# Function to launch VLC after a specified delay
def play_song(delay=5):
    """
    Plays the song using VLC media player after a delay.

    Parameters:
    - delay: Time in seconds to wait before playing the song (default is 5 seconds).
    """
    # Create a timer that waits for the delay and then launches VLC with the song
    timer = threading.Timer(delay, lambda: subprocess.Popen(["vlc", song_path]))
    timer.start()  # Start the timer

# If the script is run directly, play the song
if __name__ == "__main__":
    play_song()  # Call the play_song function with the default delay