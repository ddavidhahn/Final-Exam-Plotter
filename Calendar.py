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
        bins = self._assign_classes_to_bins()
        print(bins)
        max_widths = {}
        for i in range(1, len(EXAM_DAYS) + 1):
            max_widths[i] = self._get_max_width_for_day(bins, i)
        print(max_widths)

        max_heights = {}
        for i in range(1, len(EXAM_TIME_BLOCKS) + 1):
            max_heights[i] = self._get_max_height_for_time(bins, i)

        calendar_string = self._generate_day_header(max_widths)
        for time in bins:
            row = "|"

            for day in bins[time]:
                entries_for_time = 0

                cell = " {}".format(FORMATTED_EXAM_TIME_BLOCKS[time])
                lecture_list = bins[time][day] # TODO: Need to adapt this to handle multiple clases on same day to show collision
                max_width = max_widths[day]

                for i in range(len(lecture_list)):
                    lecture = lecture_list[i]
                    entry_string = lecture.name

                    if i != 0:
                        entry_string = " - " + entry_string
                        entry_string = " " * (max_width - len(entry_string)) + entry_string

                    cell += entry_string
                    entries_for_time += 1

                # Fill in the rest of the cell with spaces
                # Account for the extra space we prepended since max_width doesn't consider the formatting characters
                while len(cell) <= max_width:
                    cell += " "
                row += cell + " |"

                if entries_for_time < max_heights[time]:
                    pass
            calendar_string += row + "\n"
        print(calendar_string)

    def _generate_day_header(self, max_widths_for_days):
        header = "|"
        for i in range(1, len(EXAM_DAYS) + 1):
            exam_day = EXAM_DAYS[i]
            max_width = max_widths_for_days[i]
            spacers = max_width * " "

            current_cell_length = len(exam_day) + len(spacers)
            difference = current_cell_length - max_width
            index_to_cut_off_at = current_cell_length - difference - len(exam_day)
            print("{} {} {} {}".format(current_cell_length, max_width, difference, index_to_cut_off_at))

            if spacers == "":
                spacers == " "
            elif current_cell_length > max_width and index_to_cut_off_at >= 0 and index_to_cut_off_at < len(spacers):
                spacers = spacers[:index_to_cut_off_at]
            header += " {}".format(exam_day) + spacers + " |"

        header += "\n"
        hat = len(header) * "-" + "\n"
        return hat + header + hat

    def _generate_time_entry(self):
        pass

    def _assign_classes_to_bins(self):
        bins = {i: {j: [] for j in range(1, len(EXAM_DAYS) + 1)} for i in range(1, len(EXAM_TIME_BLOCKS) + 1)}
        for lecture in self.classes:
            final_day, final_time = lecture.final_day, lecture.final_time
            bins[final_time][final_day].append(lecture)
        return bins

    def _get_max_width_for_day(self, bins, day):
        max_width = 0
        for time in bins:
            lecture_list = bins[time][day]
            print(lecture_list)
            width = len(FORMATTED_EXAM_TIME_BLOCKS[time])
            if len(lecture_list) > 0:
                max_width_lecture = max(lecture_list, key=lambda e: len(e.name))
                width += len(max_width_lecture.name)
            max_width = max(max_width, width)

        # Check if max_width is smaller than the name of the day in the header
        header_day_length = len(EXAM_DAYS[day])
        if max_width < header_day_length:
            return header_day_length
        return max_width

    def _get_max_height_for_time(self, bins, time):
        max_height = 0
        for day in bins[time]:
            lecture_list = bins[time][day]
            height = len(lecture_list)
            max_height = max(max_height, height)
        return max_height

    def __str__(self):
        result = ""
        for i in range(1, len(self.classes) + 1):
            entry = self.classes[i - 1]
            result += str(entry) + "\n"
        if result != "":
            return result
        return "No classes available. "
