from Constants import *

class Class:
    def __init__(self, name, days, time, final_day, final_time):
        self.name = name
        self.days = days
        self.time = time
        self.final_day = final_day
        self.final_time = final_time

    def __repr__(self):
        return self.name

    def __str__(self):
        return "\"{}\":\n    Final   [ {} | {} ]\n    Lecture [ {} | {} ]".format(self.name,
                                                                                  EXAM_DAYS[self.final_day],
                                                                                  EXAM_TIME_BLOCKS[self.final_time],
                                                                                  self.days,
                                                                                  self.time)