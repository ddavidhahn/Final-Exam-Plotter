# Final Exam Schedule Plotter

## Interactive Mode

Interactive mode will guide you through the process of adding classes to your calendar and additionally provides you the options of actively editing your added classes. This mode is ideal for users who want to be able to actively manipulate and view final exam schedules but do not want to hassle with writing an input file.

To run interactive mode, use the following command:
```
python3 main.py
```
* Please note that interactive mode requires Python 3.

## Automatic Mode

If you opt for a more systematic method of generating your calendar, you can use the automatic mode. This will take an input file and read its lines as parameters.

To run automatic mode on an input file named `sample_input_file.txt`, use the following command:
```
python main.py sample_input_file.txt
```
* Please note that automatic mode can be run in both Python 2 and Python 3.

### Input file formatting
Ensure that you are using the following guidelines for formatting the lines of your input file. Each line represents a course and should be formatted accordingly: `__course_name_and_number__ | __lecture_days__ | __lecture_start_time__`

Here is an example:
```
CS 161 | TuTh | after 5:00pm
```
* Note that your lecture day and lecture start time must match exactly. For a complete list, please consult the [list section](#daytime_list).

#### Special cases
If your course is a special course (Chemistry 1A, Chemistry 1B, Economics 1, or Economics 100B), simply leave the full course name and number in the `__lecture_days__` slot and leave the `__lecture_start_time__` empty:
```
Chem 1A | Chemistry 1A |
```
* Note that the entry for `__lecture_days__` must match exactly with one of the classes listed above but the label you provide for `__course_name_and_number__` will only be used to label the class in your calendar.

If your course is a foreign language, put "Foreign Language" in the `__lecture_days__` slot:
```
Korean 100BX | Foreign Language |
```

If your course takes place on a Saturday or Sunday, simply mark the `__lecture_days__` field as "Sa" or "Su" and leave the `__lecture_start_time__` field blank:
```
Some weekend class | Sa |
```

### Whitespace and comments
Also note that your calendar entries will be left and right stripped for white space. So "       CS 161        " will appear in the calendar as "CS 161".

Additionally, you can start comments using "\#" or "//"

## <a name="daytime_list"></a>List of Class Days and Times
```
MWF
MTWTF
TuTh
Sa
Su
Chemistry 1A
Chemistry 1B
Economics 1
Economics 100B
Foreign Language
```

```
8:00am
8:30am
9:00am
9:30am
10:00am
10:30am
11:00am
11:30am
12:00pm
12:30pm
1:00pm
1:30pm
2:00pm
2:30pm
3:00pm
3:30pm
4:00pm
4:30pm
after 5:00pm
```
