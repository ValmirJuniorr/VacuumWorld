import argparse
import random

truthy_values = ['y', 'Y', 'yes', 'Yes', 'true', 'True']
falsy_values = ['n', 'N', 'no', 'No', 'false', 'False']

boolean_values_description = 'For Truthy Values use: {}\nFor Falsy values use: {}'.format(truthy_values, falsy_values)


def prepare_parse():
    description = 'You could specify the initial values for this agent.\n {}'.format(boolean_values_description)

    # Initialize parser
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("-n", "--number_of_steps", type=int, help="Number of steps", required=True)
    parser.add_argument("-a", "--is_dirty_a", help="Room A is Dirty?")
    parser.add_argument("-b", "--is_dirty_b", help="Room B is Dirty?")
    parser.add_argument("-l", "--agent_location", help="Initial Location Of Agent")

    return parser


def parse_boolean_arg(argument_name, argument_value):
    if argument_value in truthy_values:
        return True
    elif argument_value in falsy_values:
        return False

    mask = 'Invalid value for the argument {}. It\'s must be a boolean value try this:\n {}'
    exception_message = mask.format(argument_name, boolean_values_description)

    raise ValueError(exception_message)


def random_bool():
    return random.choice([True, False])


def get_arguments():
    parser = prepare_parse()
    args = parser.parse_args()

    number_of_steps = args.number_of_steps
    is_dirty_a = parse_boolean_arg('is_dirty_a', args.is_dirty_a) if args.is_dirty_a else random_bool()
    is_dirty_b = parse_boolean_arg('is_dirty_b', args.is_dirty_b) if args.is_dirty_b else random_bool()
    agent_location = parse_boolean_arg('agent_location', args.agent_location) if args.agent_location else random_bool()

    return {
        'number_of_steps': number_of_steps,
        'is_dirty_a': is_dirty_a,
        'is_dirty_b': is_dirty_b,
        'agent_location': agent_location
    }
