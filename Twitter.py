import json
import os

from Post import Post

class Twitter:
    def __init__(self, login_JSON, post_JSON, logins, user_posts, current_user):
        self.login_JSON = login_JSON
        self.post_JSON = post_JSON
        self.logins = logins
        self.user_posts = user_posts
        self.current_user = current_user

        # Create file with an empty dictionary if missing or empty
        for path in (self.login_JSON, self.post_JSON):
            if not os.path.exists(path) or os.path.getsize(path) == 0:
                with open(path, "w") as f:
                    json.dump({}, f)

        # Create posts file with an empty dictionary if missing or empty
        if not os.path.exists(self.post_JSON) or os.path.getsize(self.post_JSON) == 0:
            with open(self.post_JSON, "w") as f:
                json.dump({}, f)

    # Scans the logins JSON file to see if the username already has an account
    # If the username isn't registered it creates a new account by adding the username/password to the JSON
    def create_account(self, name, password):
        with open(self.login_JSON, "r") as f:
            logins = json.load(f)

        # Check if username already exists
        if name in logins:
            return False

        # Add the new username and password
        logins[name] = password

        # Write the updated dictionary back to the JSON file
        with open(self.login_JSON, "w") as f:
            json.dump(logins, f, indent=4)

        self.current_user = name
        return True

    # Verifies if the user-inputted username and password is correct
    def login(self, name, password):
    # Check if the user has a name, password exists
        with open(self.login_JSON, "r") as f:
            data = json.load(f)
        # Check if username/password entry exists in file and if so, does the username/password match password inputted
        if name in data and data[name] == password:
            self.current_user = name
            return True
        # In any other case, if the password does not exist or wrong password
        return False 

    # Make post
    def create_post(self):
        # If they want to make post then don't quit
        answer = input("Do you want to create a post? (y/n): ").strip().lower()

        if answer == "n":
            return None

        # Handle weird input
        if answer != "y":
            print("Respond with (y/n).")
            return None

        # Get input for the post and create
        title = input("Post title: ")
        caption = input("Post caption: ")
        message = input("Post message: ")

        new_post = Post(self.current_user, title, caption, message)

        # Handles the fact that when we first create the Twitter object user posts is set to None
        if self.user_posts is None:
            self.user_posts = []

        self.user_posts.append(new_post)

        print("Post created successfully!")
        return new_post

    # Saves the post into the post_JSON file 
    def save_post(self, post):
        # Load the existing posts from the post_JSON file
        try:
            with open(self.post_JSON, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {}

        # Find out who the author of this post we want to save
        user = post.author

        # Check if the user already has a prexisting entry in the dictionary
        # If not create a empty list within the dictionary for the user to store its post
        if user not in data:
            data[user] = []

        # Flatten the Post to a dict and add it
        data[user].append(post.to_dict())

        # Write the whole dict back into the file
        with open(self.post_JSON, "w") as f:
            json.dump(data, f)

        return True

    # Print all posts that are not by the current user
    def display_feed(self):
        print()
        print("Here is your feed:")
        print()

        # Go through posts.json
        with open(self.post_JSON, "r") as f:
            data = json.load(f)

        # Go through each user's posts
        for user in data:
            # Skip the current user's posts
            if user != self.current_user:
                for post in data[user]:
                    print("Username:", post["author"])
                    print("Title:", post["title"])
                    print("Caption:", post["caption"])
                    print("Message:", post["message"])
                    print()

if __name__ == "__main__":
    t = Twitter("logins.json", "posts.json", None, None, None)

    while True:
        # Isolate try/except to validate (y/n) input using raise ValueError
        # Because it was hard to figure out JSON errors otherwise
        try:
            isAccountMade = input("Do you have an account? (y/n): ").strip().lower()
            
            if isAccountMade not in ["y", "n"]:
                raise ValueError("Must enter 'y' or 'n'")
                
        except ValueError:
            print("Respond with (y/n).\n")
            continue

        # Act based on input
        # Must validate username/password
        if isAccountMade == "y":
            username = input("Username: ")
            password = input("Password: ")

            # If successful break
            if t.login(username, password):
                print(f"Logged in successfully as {t.current_user}!")
                break

            print("Wrong username or password!\n")

        # Must create account
        elif isAccountMade == "n":
            username = input("Choose a username: ")
            password = input("Choose a password: ")

            # If sucessful break
            if t.create_account(username, password):
                print(f"Account created successfully! Logged in as {t.current_user}.")
                break

            print("Username already exists!\n")

    post = t.create_post()
    if post is not None:
        t.save_post(post)
    t.display_feed()

        
            