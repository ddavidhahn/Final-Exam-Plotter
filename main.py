#!/usr/bin/python

from sys import version_info
from Constants import *
from Calendar import *
from Class import *

def main():
    args = sys.argv
    num_args = len(args)
    if num_args > 1:
        if num_args > 2:
            print("Expected 2 arguments but got {}. Arguments: {}".format(num_args, str(args)))
            sys.exit(1)
        else:
            file_name = args[1]
            automated_head(file_name)

    else:
        if sys.version_info < (3, 0):
            print("Interactive mode requires Python version 3.x.")
            sys.exit(1)
        else:
            interactive_head()

def interactive_head():
    base_commands = OptionsCollection([
        ("1", Command("(1) Generate a new schedule", generate_schedule, loop=True)),
        ("2", Command("(2) Help", lambda: input(HELP_MESSAGE), loop=True)),
        ("3", Command("(3) Quit", sys.exit))
    ])

    print(WELCOME_MESSAGE)
    base_commands.prompt()


def automated_head(file_name):
    user_calendar = Calendar()
    ignored_entries = []
    try:
        with open(file_name) as f:
            for line in f:
                lecture_string = line[:-1]
                lecture_string = lecture_string.strip()

                if len(lecture_string) == 0 or \
                   (len(lecture_string) > 0 and lecture_string[0] == '#') or \
                   (len(lecture_string) > 1 and lecture_string[:2] == "//"):
                    continue

                lecture_parameters = lecture_string.split("|")
                validate_parameters(lecture_parameters, lecture_string)

                for i in range(len(lecture_parameters)):
                    lecture_parameters[i] = lecture_parameters[i].strip()


                course_name, course_days, course_time = lecture_parameters
                final_day, final_time = validate_course_days_and_time(course_days, course_time, lecture_string)
                if final_day is None or final_time is None:
                    ignored_entries.append(lecture_string)
                    continue

                course = Class(course_name, course_days, course_time, final_day, final_time)
                user_calendar.add_class(course)

    except IOError as e:
        print(e)
        sys.exit(1)

    print(user_calendar.generate_calendar())
    ignored_entries_message = IGNORED_ENTRIES_MESSAGE
    for entry in ignored_entries:
        ignored_entries_message += entry + "\n"
    print(ignored_entries_message)

def validate_parameters(lecture_parameters, lecture_string):
    NUM_PARAMETERS = 3
    try:
        assert len(lecture_parameters) == NUM_PARAMETERS
    except AssertionError as e:
        print(LINE_NOT_FORMATTED_CORRECTLY.format(lecture_string) +
              EXTRA_PARAMETERS_FOUND.format(lecture_parameters[NUM_PARAMETERS:]))
        sys.exit(1)


def validate_course_days_and_time(course_days, course_time, lecture_string):
    if course_days not in LECTURE_DAY_OPTIONS and course_days not in CLASS_TO_EXAM_TIME.keys():
        print(LINE_NOT_FORMATTED_CORRECTLY.format(lecture_string) +
              DAY_NOT_VALID.format(course_days))
        sys.exit(1)

    if course_days not in CLASS_TO_EXAM_TIME and course_time not in LECTURE_START_TIMES:
        print(LINE_NOT_FORMATTED_CORRECTLY.format(lecture_string) +
              TIME_NOT_VALID.format(course_time))
        sys.exit(1)

    if course_days in CLASS_TO_EXAM_TIME:
        return CLASS_TO_EXAM_TIME[course_days]

    course_day_time_key = course_days + " " + course_time
    if course_day_time_key in LECTURE_TIME_TO_EXAM_TIME:
        return LECTURE_TIME_TO_EXAM_TIME[course_day_time_key]
    else:
        return None, None


def add_class_helper(calendar):
    def add_class_procedure():
        special_class_options = convert_list_to_options_collection(list(CLASS_TO_EXAM_TIME.keys()), IS_CLASS_SPECIAL)
        option_index = str(len(special_class_options) + 1)
        option_to_add = (option_index, Command("({}) None of the above".format(option_index), helper_outer(lambda x: x, None)))
        special_class_options.add_option(option_to_add)
        special_class_name = special_class_options.prompt()

        name = input(NAME_OF_CLASS)
        while name == "":
            name = input(BLANK_NAME_OF_CLASS)
        print()

        if special_class_name is not None:
            final_day, final_time = CLASS_TO_EXAM_TIME[special_class_name]
            new_class = Class(name, special_class_name, "", final_day, final_time)
            calendar.add_class(new_class)
            input(CLASS_ADD_SUCCESS.format(str(new_class)))
        else:
            days_options = convert_list_to_options_collection(LECTURE_DAY_OPTIONS, prompt_message=DAYS_OF_LECTURE_PROMPT)
            day = days_options.prompt()

            time = ""
            if day != "Su" and day != "Sa":
                times_options = convert_list_to_options_collection(LECTURE_START_TIMES, prompt_message=START_TIMES_OF_LECTURE_PROMPT)
                time = times_options.prompt()
            datetime_key = "{} {}".format(day, time)
            if datetime_key in LECTURE_TIME_TO_EXAM_TIME:
                final_day, final_time = LECTURE_TIME_TO_EXAM_TIME[datetime_key]
                new_class = Class(name, day, time, final_day, final_time)
                calendar.add_class(new_class)
                input(CLASS_ADD_SUCCESS.format(str(new_class)))
            else:
                input(LECTURE_DATETIME_NOT_FOUND)
    return add_class_procedure


def remove_class_helper(calendar):
    def remove_class_procedure():
        remove_class_commands = convert_calendar_to_remove_options(calendar, allow_cancel=True)
        if len(remove_class_commands) > 0:
            removed_class = remove_class_commands.prompt()
            if removed_class is not None:
                input(CLASS_REMOVE_SUCCESS.format(removed_class))
            else:
                input(TRANSACTION_CANCELLED)
        else:
            input(NO_CLASSES_AVAILABLE_MESSAGE)
    return remove_class_procedure


def display_classes_helper(calendar):
    def display_classes_procedure():
        input(str(calendar) + PRESS_ENTER_MESSAGE)
    return display_classes_procedure


def generate_calendar_helper(calendar):
    def generate_calendar_procedure():
        input(calendar.generate_calendar() + PRESS_ENTER_MESSAGE)
    return generate_calendar_procedure


def generate_schedule(*args):
    user_calendar = Calendar()
    generate_schedule_commands = OptionsCollection([
        ("1", Command("(1) Add a class", add_class_helper(user_calendar), loop=True)),
        ("2", Command("(2) Remove a class", remove_class_helper(user_calendar), loop=True)),
        ("3", Command("(3) Display added classes", display_classes_helper(user_calendar), loop=True)),
        ("4", Command("(4) Generate calendar", generate_calendar_helper(user_calendar), loop=True)),
        ("5", Command("(5) Go back (your current calendar will be lost)", loop=False))
    ])

    input(SCHEDULER_MESSAGE)
    generate_schedule_commands.prompt()


def helper_outer(function, *args):
    def helper_inner():
        return function(*args)
    return helper_inner


def convert_calendar_to_remove_options(calendar, allow_cancel=False):
    commands_list = []
    classes_dict = calendar.convert_to_dict()
    for class_key in classes_dict:
        class_value = classes_dict[class_key]
        command_function = helper_outer(lambda x: calendar.remove_class(x), class_value)
        commands_list.append((class_key, Command("({}) {}".format(class_key, class_value), command_function)))
    if allow_cancel:
        cancel_key = max([int(key) for key in classes_dict.keys()])
        commands_list.append((str(cancel_key + 1), Command("({}) Cancel".format(cancel_key + 1), lambda: None)))
    return OptionsCollection(commands_list, prompt_message=WHICH_CLASS_TO_REMOVE)


def convert_list_to_options_collection(list_to_convert, prompt_message=None):
    commands_list = []
    for i in range(1, len(list_to_convert) + 1):
        list_option = list_to_convert[i - 1]
        commands_list.append((str(i), Command("({}) {}".format(i, list_option), helper_outer(lambda x: x, list_option))))
    if prompt_message is not None:
        return OptionsCollection(commands_list, prompt_message=prompt_message)
    return OptionsCollection(commands_list)


if __name__ == '__main__':
    main()