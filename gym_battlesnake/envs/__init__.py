"""
Battlesnake Gym enviroments.
"""


from gym_battlesnake.envs.battlesnake_env import BattlesnakeEnv


class BattlesnakeEnv7x7(BattlesnakeEnv):
    def __init__(self):
        super().__init__(width=9, height=9, num_snakes=1, stacked_frames=2)


class BattlesnakeEnv11x11(BattlesnakeEnv):
    def __init__(self):
        super().__init__(width=13, height=13, num_snakes=1, stacked_frames=2)


class BattlesnakeEnv19x19(BattlesnakeEnv):
    def __init__(self):
        super().__init__(width=21, height=21, num_snakes=1, stacked_frames=2)
