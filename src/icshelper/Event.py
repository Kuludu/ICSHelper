from uuid import uuid1
import time


class Event:
    event = dict()

    def __init__(self, paramenter: dict):
        self.event['DTSTART'] = paramenter['DTSTART']
        self.event['DTEND'] = paramenter['DTEND']
        self.event['DTSTAMP'] = time.strftime("%Y%m%dT%H%M%SZ", time.localtime())
        self.event['UID'] = str(uuid1())
        self.event['CREATED'] = time.strftime("%Y%m%dT%H%M%SZ", time.localtime())
        self.event['DESCRIPTION'] = paramenter['DESCRIPTION']
        self.event['LAST-MODIFIED'] = time.strftime("%Y%m%dT%H%M%SZ", time.localtime())
        self.event['LOCATION'] = paramenter['LOCATION']
        self.event['STATUS'] = "CONFIRMED"
        self.event['SUMMARY'] = paramenter['SUMMARY']
        self.event['TRANSP'] = "TRANSPARENT"

    def __str__(self):
        return_string = str()

        return_string += "BEGIN:VEVENT\n"

        for key, value in self.event.items():
            return_string += key + ":" + value + "\n"

        return_string += "END:VEVENT\n"

        return return_string
