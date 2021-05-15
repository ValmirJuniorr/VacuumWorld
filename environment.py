from action import Action


class Environment:
    ROOM_A = 'Sala A'
    ROOM_B = 'Sala B'

    def __init__(self, is_dirty_a, is_dirty_b, agent_location):
        self.is_dirty_a = is_dirty_a
        self.is_dirty_b = is_dirty_b
        self.agent_location = agent_location

    def get_location(self):
        return self.ROOM_A if self.agent_location else self.ROOM_B

    def get_is_dirty(self):
        return self.is_dirty_a if self.get_location() == self.ROOM_A else self.is_dirty_b

    def update_state(self, action):
        if action == Action.ASPIRE:
            if self.get_location() == Environment.ROOM_A:
                self.is_dirty_a = False
            else:
                self.is_dirty_b = False

        elif action == Action.RIGHT:
            if self.get_location() == Environment.ROOM_A:
                self.agent_location = False

        elif self.get_location() == Environment.ROOM_B:
            self.agent_location = True
