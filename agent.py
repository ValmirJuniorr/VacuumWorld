from action import Action
from environment import Environment
from perception import Perception


class Agent:
    def choose_action(self, perception):
        if perception.is_dirty:
            return Action.ASPIRE
        elif perception.location == Environment.ROOM_A:
            return Action.RIGHT
        else:
            return Action.LEFT

    def perceives(self, environment):
        return Perception(environment.get_is_dirty(), environment.get_location())

    def act(self, environment):
        perception = self.perceives(environment)

        return self.choose_action(perception)
