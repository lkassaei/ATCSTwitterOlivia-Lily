import json
import os

class Twitter:
    def __init__(self, login_JSON, post_JSON, logins, user_posts, current_user):
        self.loginJSON = login_JSON
        self.post = post_JSON
        self.logins = logins
        self.user_posts = user_posts
        self.current_user = current_user

        # Create file with an empty dictionary if missing or empty
        if not os.path.exists(self.loginJSON) or os.path.getsize(self.loginJSON) == 0:
            with open(self.loginJSON, "w") as f:
                json.dump({}, f)

    # Scans the logins JSON file to see if the username already has an account
    # If the username isn't registered it creates a new account by adding the username/password to the JSON
    def create_account(self, name, password):
        with open(self.loginJSON, "r") as f:
            logins = json.load(f)

        # Check if username already exists
        if name in logins:
            return False

        # Add the new username and password
        logins[name] = password

        # Write the updated dictionary back to the JSON file
        with open(self.loginJSON, "w") as f:
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
            return True
        # In any other case, if the password does not exist or wrong password
        return False 

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
            