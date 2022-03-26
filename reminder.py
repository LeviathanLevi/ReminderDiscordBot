class Reminder:
    def __init__(self, message, user):
        self.message = message
        self.user = user

    async def sendMessage(self):
        await self.user.send(self.message)

class IntervalReminder(Reminder):
    def __init__(self, message, user, intervalInMinutes):
        super().__init__(message, user)
        self.intervalInMinutes = intervalInMinutes
        self.minutesRemaining = intervalInMinutes

#WIP:
class DateReminder(Reminder):
    def __init__(self, message, user, targetDateTime):
        super().__init__(message, user)
        self.targetDate = targetDateTime
        
    def checkReminder(self, currentDateTime):
        if currentDateTime == self.targetDate:
            self.sendMessage()
            return True
        return False