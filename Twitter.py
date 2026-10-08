import json

class Twitter:
    def __init__(self, login_JSON, post_JSON, logins, user_posts, current_user):
        self.loginJSON = login_JSON
        self.post = post_JSON
        self.logins = logins
        self.user_posts = user_posts
        self.current_user = current_user

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

    def login(self, name, password):
        pass

    def __init__(self):
        t = Twitter("logins.json", "posts.json", None, None, None)

        while True:
            # Infinitely try to get good input 
            try:
                isAccountMade = input("Do you have an account? (y/n)")

                # Login if account already exists
                if isAccountMade == "y" or isAccountMade == "Y":
                    username = input("Username: ")
                    password = input("Password: ")

                    # If successful, break out
                    if t.login(username, password):
                        break

                    print("Wrong username or password!")

                # If no account exists, create a new one
                elif isAccountMade == "n" or isAccountMade == "N":
                    username = input("Choose a username: ")
                    password = input("Choose a password: ")

                    # If successful, break out
                    if t.create_account(username, password):
                        break

                    print("Username already exists!")

                # If input is not y/n
                else:
                    raise ValueError

            # Reprompt
            except ValueError:
                print("Respond with (y/n).")

            # After other features are done, here we will display posts for the user to see


            

             


