import sys
from Commands import *

EXAM_DAYS = {
    1: "M",
    2: "Tu",
    3: "W",
    4: "Th",
    5: "F"
}

EXAM_TIME_BLOCKS = {
    1: "08:00am",
    2: "11:30am",
    3: "03:00pm",
    4: "07:00pm"
}

FORMATTED_EXAM_TIME_BLOCKS = {time: EXAM_TIME_BLOCKS[time] + " - " for time in EXAM_TIME_BLOCKS}

LECTURE_DAY_OPTIONS = ["MWF", "MTWTF", "TuTh", "Sa", "Su"]
LECTURE_START_TIMES = ["09:00am", "09:30am", "10:00am", "10:30am", "11:00am", "11:30am", "12:00pm", "12:30pm",
                       "01:00pm", "01:30pm", "02:00pm", "02:30pm", "03:00pm", "03:30pm", "04:00pm", "04:30pm",
                       "after 05:00pm"]

LECTURE_TIME_TO_EXAM_TIME = {
    "MWF 10:00am": (1, 1),
    "MWF 10:30am": (1, 1),
    "MTWTF 10:00am": (1, 1),
    "MTWTF 10:30am": (1, 1),

    "MWF 11:00am": (1, 2),
    "MWF 11:30am": (1, 2),
    "MTWTF 11:00am": (1, 2),
    "MTWTF 11:30am": (1, 2),

    "MWF 08:00am": (1, 4),
    "MWF 08:30am": (1, 4),
    "MTWTF 08:00am": (1, 4),
    "MTWTF 08:30am": (1, 4),

    "TuTh 02:00pm": (2, 1),
    "TuTh 02:30pm": (2, 1),

    "TuTh 09:00am": (2, 3),
    "TuTh 09:30am": (2, 3),

    "MWF 03:00pm": (2, 4),
    "MWF 03:30pm": (2, 4),
    "MTWTF 03:00pm": (2, 4),
    "MTWTF 03:30pm": (2, 4),

    "TuTh 11:00am": (3, 1),
    "TuTh 11:30am": (3, 1),

    "TuTh 08:00am": (3, 3),
    "TuTh 08:30am": (3, 3),
    "Sa": (3, 3),
    "Su": (3, 3),

    "MWF 01:00pm": (3, 4),
    "MWF 01:30pm": (3, 4),

    "MWF 04:00pm": (4, 1),
    "MWF 04:30pm": (4, 1),
    "MTWTF 04:00pm": (4, 1),
    "MTWTF 04:30pm": (4, 1),

    "TuTh after 05:00pm": (4, 2),

    "MWF 02:00pm": (4, 3),
    "MWF 02:30pm": (4, 3),
    "MTWTF 02:00pm": (4, 3),
    "MTWTF 02:30pm": (4, 3),

    "MWF 09:00am": (4, 4),
    "MWF 09:30am": (4, 4),
    "MTWTF 09:00am": (4, 4),
    "MTWTF 09:30am": (4, 4),


    "TuTh 12:00pm": (5, 1),
    "TuTh 12:30pm": (5, 1),
    "TuTh 01:00pm": (5, 1),
    "TuTh 01:30pm": (5, 1),

    "MWF 12:00": (5, 2),
    "MWF 12:00": (5, 2),
    "MTWTF 12:00": (5, 2),
    "MTWTF 12:00": (5, 2),

    "TuTh 10:00am": (5, 3),
    "TuTh 10:30am": (5, 3),
    "MWF after 05:00pm": (5, 3),

    "TuTh 03:00pm": (5, 4),
    "TuTh 03:30pm": (5, 4),
    "TuTh 04:00pm": (5, 4),
    "TuTh 04:30pm": (5, 4)
}

CLASS_TO_EXAM_TIME = OrderedDict([

    ("Chemistry 1A", (1, 3)),
    ("Chemistry 1B", (1, 3)),
    ("Economics 1", (2, 2)),
    ("Economics 100B", (2, 2)),
    ("Foreign Languages", (3, 2)),

])

WELCOME_MESSAGE = "Welcome to the final exam schedule plotter.\n"
FAREWELL_MESSAGE = "Thank you for visiting!"
PRESS_ENTER_MESSAGE = "(Press enter to continue)\n"
HELP_MESSAGE = "This tool will prompt you for your classes and generate a text-based calendar to display your final " \
               "exam schedule. Please follow the instructions on the screen and provide information as requested.\n" + \
               PRESS_ENTER_MESSAGE
SCHEDULER_MESSAGE = "Let's start building your final exam schedule!\n" + PRESS_ENTER_MESSAGE

IS_CLASS_SPECIAL = "Is your class in the following list? If so, please select the class:\n{}(Choose an option): "
NAME_OF_CLASS = "Name and course number of class: "
BLANK_NAME_OF_CLASS = "The name cannot be blank: "
DAYS_OF_LECTURE_PROMPT = "What day(s) does this class have lecture on?\n{}(Choose an option): "
START_TIMES_OF_LECTURE_PROMPT = "What time does this lecture start at?\n{}(Choose an option): "
CLASS_ADD_SUCCESS = "Successfully added class!\n{}\n\n" + PRESS_ENTER_MESSAGE
LECTURE_DATETIME_NOT_FOUND = "There is no record of a lecture starting on those days and at that time. "

WHICH_CLASS_TO_REMOVE = "Which class would you like to remove?\n{}(Choose an option): "
CLASS_REMOVE_SUCCESS = "Successfully removed class!\n{}\n\n" + PRESS_ENTER_MESSAGE
TRANSACTION_CANCELLED = "Remove cancelled.\n" + PRESS_ENTER_MESSAGE

NO_CLASSES_AVAILABLE_MESSAGE = "There are no classes available.\n" + PRESS_ENTER_MESSAGE
