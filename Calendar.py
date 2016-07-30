from Constants import *

class Calendar:
    def __init__(self):
        self.classes = []

    def add_class(self, class_to_add):
        self.classes.append(class_to_add)

    def remove_class(self, class_to_remove):
        index_to_remove = self.classes.index(class_to_remove)
        self.classes = self.classes[:index_to_remove] + self.classes[index_to_remove + 1:]
        return class_to_remove

    # Note that starting_index is the starting index for the keys of the returned dictionary.
    def convert_to_dict(self, starting_index=1):
        result = {}
        for i in range(starting_index, starting_index + len(self.classes)):
            result[str(i)] = self.classes[i - starting_index]
        return result

    def generate_calendar(self):
        print("generating calendar")
        bins = self._assign_classes_to_bins()

    def _assign_classes_to_bins(self):
        bins = {i: {j: [] for j in range(1, len(EXAM_TIME_BLOCKS) + 1)} for i in range(1, len(EXAM_DAYS) + 1)}
        for lecture in self.classes:
            final_day, final_time = lecture.final_day, lecture.final_time
            bins[final_day][final_time].append(lecture)
        return bins

    def __str__(self):
        result = ""
        for i in range(1, len(self.classes) + 1):
            entry = self.classes[i - 1]
            result += str(entry) + "\n"
        if result != "":
            return result
        return "No classes available. "
