import random
from kaggle_environments.envs.rps.utils import get_score


def random_agent(observation, configuration):
    # возвращает случайно камень, ножницы или бумагу
    return random.randrange(0, configuration.signs)


def only_rock(observation, configuration):
    # возвращает только камень
    return 0


def only_paper(observation, configuration):
    # возвращает только бумагу
    return 1


def only_scissors(observation, configuration):
    # возвращает только ножницы
    return 2


def rock_and_paper(observation, configuration):
    # случайным образом возвращает камень или бумагу
    return random.randrange(0, 1)


def rock_and_scissors(observation, configuration):
    # случайным образом возвращает камень или ножницы
    return random.randrange(0, 3, step=2)


def paper_and_scissors(observation, configuration):
    # случайным образом возвращает бумагу или ножницы
    return random.randrange(1, 2)


def last_action(observation, configuration):
    # повторяет последнее действие противника, при первом запусе случайный выбор
    if observation.step == 0:
        return random.randrange(0, configuration.signs)
    else:
        return observation.lastOpponentAction


def random_by_even(observation, configuration):
    # случайный выбор межну камнем или ножницами если четный шаг боя
    # на нечетных шагах возвращает бумагу
    if observation.step % 2:
        return random.randrange(0, configuration.signs, step=2)
    else:
        return 1


last_action = None


def repeat_win(observation, configuration):
    # повторяет свою последнюю успешную игру
    global last_action
    if observation.step == 0:
        last_action = random.randrange(0, configuration.signs)
    elif get_score(last_react_action, observation.lastOpponentAction) <= 1:
        last_action = (observation.lastOpponentAction + 1) % configuration.signs

    return last_action


ps_repeat_count = None


def paper_scissors_repeat(observation, configuration):
    # первый ход камень, далее бумага и 5 ходов ножницы
    global ps_repeat_count
    if observation.step == 0:
        return 0
    else:
        if ps_repeat_count == 0:
            ps_repeat_count = 5
            return 1
        else:
            ps_repeat_count -= 1
            return 2


rp_repeat_count = None


def rock_paper_repeat(observation, configuration):
    # первый ход ножницы, далее камень и 5 ходов бумага
    global rp_repeat_count
    if observation.step == 0:
        return 2
    else:
        if rp_repeat_count == 0:
            rp_repeat_count = 5
            return 0
        else:
            rp_repeat_count -= 1
            return 1


agents = {
    "random_agent": random_agent,
    "only_rock": only_rock,
    "only_paper": only_paper,
    "only_scissors": only_scissors,
    "rock_and_paper": rock_and_paper,
    "rock_and_scissors": rock_and_scissors,
    "paper_and_scissors": paper_and_scissors,
    "last_action": last_action,
    "random_by_even": random_by_even,
    "repeat_win": repeat_win,
    "paper_scissors_repeat": paper_scissors_repeat,
    "rock_paper_repeat": rock_paper_repeat
}
