class Clock:
    def __init__(self, hours, minutes, seconds):
        self.__hours = self.__minutes = self.__seconds = 0
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, hours):
        if self.check_num(hours):
            self.__hours = hours

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes):
        if self.check_num(minutes):
            self.__minutes = minutes

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds):
        if self.check_num(seconds):
            self.__seconds = seconds

    def check_num(self, num):
        return True if (type(num) == int and num >= 0) else False

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2
        self.delta_h = self.clock1.hours - self.clock2.hours
        self.deta_m = self.clock1.minutes - self.clock2.minutes
        self.delta_s = self.clock1.seconds - self.clock2.seconds

    def __str__(self):
        h = '00' if '-' in str(self.delta_h) else ('0' + str(self.delta_h) if len(str(self.delta_h)) == 1 else str(self.delta_h))
        m = '00' if '-' in str(self.deta_m) else ('0' + str(self.deta_m) if len(str(self.deta_m)) == 1 else str(self.deta_m))
        s = '00' if '-' in str(self.delta_s) else ('0' + str(self.delta_s) if len(str(self.delta_s)) == 1 else str(self.delta_s))
        return f'{h}: {m}: {s}'

    def __len__(self):
        if self.clock1.get_time() - self.clock2.get_time() <= 0:
            return "00: 00: 00"
        else:
            return self.clock1.get_time() - self.clock2.get_time()
