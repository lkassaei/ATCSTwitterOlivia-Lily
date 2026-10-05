class Twitter:
    def __init__(self, login_JSON, post_JSON, logins, user_posts, current_user):
        self.loginJSON = login_JSON
        self.post = post_JSON
        self.logins = logins
        self.user_posts = user_posts
        self.current_user = current_user