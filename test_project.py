from project import setup, game_loop, game_end
from unittest.mock import MagicMock
import project

def test_setup(mocker):
    mocker.patch("project.Screen")
    mocker.patch("project.Player")

    setup()

    assert project.screen is not None
    assert project.player1 is not None
    assert project.player2 is not None

def test_game_loop(mocker):
    mocker.patch("time.sleep")
    project.car_manager = MagicMock()
    project.screen = MagicMock()
    project.player1 = MagicMock()
    project.player2 = MagicMock()
    project.player1.ycor.return_value = 0
    project.player1.xcor.return_value = 0
    project.player2.ycor.return_value = 100
    project.player2.xcor.return_value = 100

    def stop_loop():
            project.game_is_on = False

    project.screen.update.side_effect = stop_loop
    project.game_is_on = True

    game_loop()

    project.car_manager.create_car.assert_called()
    project.car_manager.move_all.assert_called()

def test_game_end():
    project.screen = MagicMock()

    game_end()

    project.screen.exitonclick.assert_called_once()
