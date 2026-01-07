import pytest
# Файл в котором должны лежать фикстуры

@pytest.fixture
def music_data():
    music = [
        {"id": 1, "name": "track_1", "duration": 192},
        {"id": 2, "name": "track_2", "duration": 172},
        {"id": 3, "name": "track_3", "duration": 151}
    ]
    return music
