from Post import Post

def test_init_sets_fields():
    p = Post("liv", "hello", "cap", "msg")
    assert p.author == "liv"
    assert p.title == "hello"
    assert p.caption == "cap"
    assert p.message == "msg"

def test_to_dict():
    p = Post("liv", "hello", "cap", "msg")
    assert p.to_dict() == {
        "author": "liv",
        "title": "hello",
        "caption": "cap",
        "message": "msg",
    }