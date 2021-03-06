from test.data.auth_data import (
    PASSWORD,
    SOBOLEV_EMAIL,
    SOBOLEV_FIRSTNAME,
    SOBOLEV_LASTNAME,
    SOBOLEV_USERNAME,
)


POST_DATA = {
    "name": "test name",
    "url_content": "http://localhost:8000/post/content/post_uml_zgqeuipptbrjwhd.html",
    "skill": {
        "key": "3ed34r43f3",
        "name": "UML-диаграммы",
        "scope": "Программирование",
        "url": "http://localhost:8000/skill/icon/uml.png",
    },
}
NO_EXIST_POST_KEY = "no_exist_post_key"
COMMENT_DATA = {
    "text": "Автор прекрасно объяснил данный материал",
    "name": "Прекрасная статья",
}
NO_EXIST_COMMENT_KEY = "no_exist_comment_key"
SOBOLEV_REGISTRATION_VALID_DATA = {
    "email": SOBOLEV_EMAIL,
    "username": SOBOLEV_USERNAME,
    "password": PASSWORD,
    "lastname": SOBOLEV_LASTNAME,
    "firstname": SOBOLEV_FIRSTNAME,
}
SOBOLEV_AUTH_VALID_DATA = {"email": SOBOLEV_EMAIL, "password": PASSWORD}
