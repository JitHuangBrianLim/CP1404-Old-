"""
Replace the contents of this module docstring with your own details
Name: Jit Huang Brian Lim
Date started: 12/08/2022
GitHub URL:
"""

FILENAME = 'songs.csv'

def main():
    """..."""
    songs_file = open('songs.csv', 'r')
    print("Songs to Learn 1.0 - by Jit Huang Brian Lim")
    print("L - List new Songs", "\nA - Add new song", "\nC - Complete a song", "\nQ - Quit")
    menu_choice = input().lower()

    unlearnt_count = 0
    learnt_count = 0

    if menu_choice == 'l':
        list_songs(learnt_count, unlearnt_count)


    songs_file.close()

def list_songs(learnt_count, unlearnt_count):
    songs_list = []

    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        data_parts = line.split(',')
        songs_list.append(data_parts)
    input_file.close()
    for songs_data in songs_list:

        if songs_data[3] == 'u':
            unlearnt_count += 1
            print(songs_list.index(songs_data), ".", " * ", end=' ', sep='')
        elif songs_data[3] == 'l':
            learnt_count += 1
            print(songs_list.index(songs_data), ".   ", end=' ', sep='')

        print("{:30} - {:25} {:4}".format(*songs_data))

    print(f"{learnt_count} songs learned, {unlearnt_count} songs still to learn")
    return

if __name__ == '__main__':
    main()