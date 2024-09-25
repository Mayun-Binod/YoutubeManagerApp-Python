import json

def load_data():
    try:
        with open ("youtube.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_data_helper(videos):
    with open ("youtube.txt","w") as file:
        json.dump(videos,file)
def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos = load_data()  #load_data() is typically a function name used to indicate that the function is responsible for loading or retrieving some form of data, usually from a file, database, or an API.
    while True:
        print("\nYoutube Manager | Choose an option")
        print("1. List all Youtube videos")
        print("2. Add a Youtube Video")
        print("3. Update a Youtube Video details")
        print("4. Delete a Youtube Video")
        print("5. Exit/Quit the App")
        
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Sorry, invalid choice...")
if __name__=="__main__":
    main()

