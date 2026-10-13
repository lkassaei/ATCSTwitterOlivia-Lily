import json
from Twitter import Twitter
from Post import Post

# Helper that builds the Twitter object
def make_twitter(tmp_path):
    # Instead of using our actual file paths, create temporary files
    return Twitter(str(tmp_path / "logins.json"),
                   str(tmp_path / "posts.json"),
                   None, None, None)


# Account Tests
def test_create_account_new_user(tmp_path):
    t = make_twitter(tmp_path)
    assert t.create_account("lily67", "pw") is True
    assert t.current_user == "lily67"

def test_create_account_duplicate(tmp_path):
    t = make_twitter(tmp_path)
    t.create_account("lily67", "pw")
    assert t.create_account("lily67", "other") is False

def test_login_success(tmp_path):
    t = make_twitter(tmp_path)
    t.create_account("lily67", "pw")
    t.current_user = None
    assert t.login("lily67", "pw") is True
    assert t.current_user == "lily67"

def test_login_wrong_password(tmp_path):
    t = make_twitter(tmp_path)
    t.create_account("lily67", "pw")
    assert t.login("lily67", "nope") is False

def test_login_unknown_user(tmp_path):
    t = make_twitter(tmp_path)
    assert t.login("anonymous", "pw") is False


# Post Tests
def test_save_post(tmp_path):
    t = make_twitter(tmp_path)
    t.save_post(Post("liv", "T", "C", "M"))
    data = json.loads((tmp_path / "posts.json").read_text())
    assert data["liv"][0]["title"] == "T"

def test_save_two_posts_same_user(tmp_path):
    t = make_twitter(tmp_path)
    t.save_post(Post("liv", "T1", "C", "M"))
    t.save_post(Post("liv", "T2", "C", "M"))
    data = json.loads((tmp_path / "posts.json").read_text())
    assert len(data["liv"]) == 2

def test_create_post(tmp_path, monkeypatch):
    t = make_twitter(tmp_path)
    t.current_user = "liv"
    answers = iter(["y", "Title", "Cap", "Msg"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))
    post = t.create_post()
    assert post.title == "Title"
    assert post.author == "liv"

def test_create_post_declined(tmp_path, monkeypatch):
    t = make_twitter(tmp_path)
    monkeypatch.setattr("builtins.input", lambda prompt="": "n")
    assert t.create_post() is None


# Feed Tests
def test_feed_hides_own_posts(tmp_path, capsys):
    t = make_twitter(tmp_path)
    t.save_post(Post("liv", "Mine", "C", "M"))
    t.save_post(Post("bob", "Theirs", "C", "M"))
    t.current_user = "liv"
    t.display_feed()
    out = capsys.readouterr().out
    assert "Theirs" in out
    assert "Mine" not in out