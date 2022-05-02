# TV controller
# Create a simple prototype of a TV controller in Python.
# It’ll use the following commands:
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel.Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if
# the channel N or 'name' exists in the list, or "No" - in the other case.
# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.


CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel = channels[0]

    def first_channel(self):
        self.current_channel = self.channels[0]
        return self.current_channel

    def last_channel(self):
        self.current_channel = self.channels[-1]
        return self.current_channel

    def turn_channel(self, n):
        self.current_channel = self.channels[n - 1]
        return self.current_channel

    def next_channel(self):
        if self.current_channel == self.channels[-1]:
            self.current_channel = self.channels[0]
        else:
            current_channel_index = self.channels.index(self.current_channel)
            self.current_channel = self.channels[current_channel_index + 1]
        return self.current_channel

    def previous_channel(self):
        if self.current_channel == self.channels[0]:
            self.current_channel = self.channels[-1]
        else:
            current_channel_index = self.channels.index(self.current_channel)
            self.current_channel = self.channels[current_channel_index - 1]
        return self.current_channel

    def current_channel_(self):
        return self.current_channel

    def is_exist(self, value):
        if value is int:
            try:
                if self.channels[value]:
                    return 'Yes'
            except IndexError:
                return 'No'
        elif value is str:
            try:
                if self.channels.index(value):
                    return 'Yes'
            except IndexError:
                return 'No'


controller = TVController(CHANNELS)

controller.first_channel() == "BBC"

controller.last_channel() == "TV1000"

controller.turn_channel(1) == "BBC"

controller.next_channel() == "Discovery"

controller.previous_channel() == "BBC"

controller.current_channel_() == "BBC"

controller.is_exist(4) == "No"

controller.is_exist("BBC") == "Yes"

