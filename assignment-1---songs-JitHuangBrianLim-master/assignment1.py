"""
Replace the contents of this module docstring with your own details
Name: Jit Huang Brian Lim
Date started: 12/08/2022
GitHub URL:
"""

FILENAME = 'songs.csv'
NEGATIVE = '-\\'

def main():
    """..."""
    songs_file = open('songs.csv', 'r')
    file_data = songs_file.read()
    file_data = file_data.strip()
    file_data_songs = file_data.split('\n')
    file_data_parts = file_data.split(',')
    append_file = open('songs.csv', 'a')

    number_of_songs = len(file_data_songs)

    print(repr(file_data))
    print("Songs to Learn 1.0 - by Jit Huang Brian Lim")
    print("L - List new Songs", "\nA - Add new song", "\nC - Complete a song", "\nQ - Quit")
    menu_choice = input().lower()

    unlearnt_count = 0
    learnt_count = 0
    new_song_list = []

    while menu_choice != 'q':
        if menu_choice == 'l':
            list_songs(learnt_count, unlearnt_count)
            print("L - List new Songs", "\nA - Add new song", "\nC - Complete a song", "\nQ - Quit")
            menu_choice = input().lower()

        elif menu_choice == 'a':
            add_songs(new_song_list, append_file)
            # append_file.write()
            print(new_song_list)
            print("L - List new Songs", "\nA - Add new song", "\nC - Complete a song", "\nQ - Quit")
            menu_choice = input().lower()

        elif menu_choice == 'c':
            learn_song = input("Enter the number of a song to mark as learned")
            while not learn_song.isdigit():
                if learn_song[0] in NEGATIVE:
                    print("Number must be >= 0")
                else:
                    print("Invalid Input; enter a valid number")
                learn_song = input("Year: ")

            learn_song = int(learn_song)
            while learn_song > number_of_songs:
                print("Invalid song number")
                learn_song = input()

            learn_song = int(learn_song)
            if file_data_songs[learn_song][-1] == 'l':
                print(f"You have already learned {file_data[learn_song]}")
            # elif file_data_songs[learn_song][-1] == 'u':
            #     print(file_data_songs[learn_song])
            # print(f"{file_data_songs[0]} by {file_data_songs[1]} learned")

            print("{} by {} learned".format(*file_data_parts))

            print("L - List new Songs", "\nA - Add new song", "\nC - Complete a song", "\nQ - Quit")
            menu_choice = input().lower()




    print(f"{len(songs_file.readlines())} songs saved to {FILENAME} \nHave a nice day :)")



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

def add_songs(new_song_list, append_file):
    new_song_data = []

    new_song_title = input("Title: ")
    while len(new_song_title) <= 0:
        print("Input cannot be blank")
        new_song_title = input("Title: ")
    new_song_data.append(new_song_title)

    new_artist = input("Artist: ")
    while len(new_artist) <= 0:
        print("Input cannot be blank")
        new_artist = input("Artist: ")
    new_song_data.append(new_artist)

    new_year = input("Year: ")
    while not new_year.isdigit():
        if new_year[0] in NEGATIVE:
            print("Number must be >= 0")
        else:
            print("Invalid Input; enter a valid number")
        new_year = input("Year: ")
    new_year = int(new_year)

    new_song_data.append(new_year)
    new_song_data.append('u')
    print("{} by {} ({}) added to song list".format(*new_song_data))
    # print(new_song_data)
    # print(repr(new_song_data))

    new_song_list.append(new_song_data)

    new_song = "{},{},{},{}".format(*new_song_data)

    append_file.write(new_song)
    # print(new_song_list)
    # print(new_song_list[0])
    return

if __name__ == '__main__':
    main()