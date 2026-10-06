class Twitter:
    def __init__(self, login_JSON, post_JSON, logins, user_posts, current_user):
        self.loginJSON = login_JSON
        self.post = post_JSON
        self.logins = logins
        self.user_posts = user_posts
        self.current_user = current_user

    def create_account(self, name, password):
        with open (self.loginJSON, "r+") as f:
            f.load()

    def login(self, name, password):
        pass

    def __init__(self):
        t = Twitter("logins.json", "posts.json", None, None, None)
        while(True):
            try:
                isAccountMade = input("Do you have an account? (y/n)")
                if (isAccountMade == "y" or isAccountMade == "Y"):
                    while (True):
                        username = input("Username: ")
                        password = input("Password: ")
                        try:
                            if (self.login(username, password)):
                                break
                            print("Wrong Username or password!")
                        except:
                            ValueError
                elif (isAccountMade == "n" or isAccountMade == "N"):
                        while (True):
                            username = input("Choose a username: ")
                            password = input("Choose a passwrod: ")
                            try:
                                if (self.create_account(username, password)):
                                    break
                                print("Username already exists!")
                            except:
                                ValueError
                else:
                    raise ValueError

            except ValueError:
                print("Respond with (y/n).")

            

             


