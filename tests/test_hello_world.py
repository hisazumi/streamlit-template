from streamlit.testing.v1 import AppTest


def test_hello_world_app() -> None:
    app = AppTest.from_file("hello_world.py").run()

    assert not app.exception
    assert app.title[0].value == "👋 Hello World"


def test_greeting_uses_the_entered_name() -> None:
    app = AppTest.from_file("hello_world.py").run()

    app.text_input[0].set_value("太郎").run()

    assert not app.exception
    assert app.success[0].value == "こんにちは、太郎さん！"
