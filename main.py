from agent import Agent
from environment import Environment
from parse_arguments import get_arguments


def print_action(environment, action):
    state_room_a = ' Suja' if environment.is_dirty_a else 'Limpa'
    state_room_b = ' Suja' if environment.is_dirty_b else 'Limpa'

    mask_text = 'Sala A: {}, Sala B: {}, Local: {}, Ação escolhida: {}'

    print(mask_text.format(state_room_a, state_room_b, environment.get_location(), action))


def main():
    arguments = get_arguments()

    is_dirty_a = arguments['is_dirty_a']
    is_dirty_b = arguments['is_dirty_b']
    agent_location = arguments['agent_location']

    environment = Environment(is_dirty_a, is_dirty_b, agent_location)
    agent = Agent()

    for i in range(arguments['number_of_steps']):
        action = agent.act(environment)

        print_action(environment, action)

        environment.update_state(action)


if __name__ == '__main__':
    main()
