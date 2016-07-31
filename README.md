# Final Exam Schedule Plotter

## Interactive Mode

Interactive mode will guide you through the process of adding classes to your calendar and additionally provides you the options of actively editing your added classes.
This mode is ideal for users who want to be able to actively manipulate and view final exam schedules but do not want to hassle with writing an input file.

To run interactive mode, use the following command:
```
python3 main.py
```
Please note that interactive mode requires Python 3.

## Automatic Mode

If you opt for a more systematic method of generating your calendar, you can use the automatic mode. This will take an input file and read its lines as parameters.

To run automatic mode on an input file named `sample_input_file.txt`, use the following command:
```
python main.py sample_input_file.txt
```

### Input file formatting
Please note that automatic mode can be run in both Python 2 and Python 3.

Ensure that you are using the following guidelines for formatting the lines of your input file. Each line represents a course and should be formatted accordingly: `__course_name_and_number__ | __lecture_days__ | __lecture_start_time__`

Here is an example:
```
CS 161 | TuTh | after 5:00pm
```
NOTE: Your lecture day and lecture start time must match exactly. For a complete list, please consult the README file.

### Special cases
If your course is a special course (Chemistry 1A, Chemistry 1B, Economics 1, or Economics 100B), simply leave the full course name and number in the `__lecture_days__` slot and leave the `__lecture_start_time__` empty.

Here is an example:
```
Chem 1A | Chemistry 1A |
```
NOTE: the entry for `__lecture_days__` must match exactly with one of the classes listed above but the label you provide for `__course_name_and_number__` will only be used to label the class in your calendar.

If your course is a foreign language, put "Foreign Language" in the `__lecture_days__` slot.
Here is an example:
```
Korean 100BX | Foreign Language |
```

If your course takes place on a Saturday or Sunday, simply mark the `__lecture_days__` field as "Sa" or "Su" and leave the `__lecture_start_time__` field blank.
Here is an example:
```
Some weekend class | Sa |
```

### Whitespace and comments
Also note that your calendar entries will be left and right stripped for white space. So "       CS 161        " will appear in the calendar as "CS 161".

Additionally, you can start comments using "\#" or "//"
