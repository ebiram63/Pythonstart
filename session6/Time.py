class Time:
    def timeprint(tt):
        print(str(tt.hours) + ":" + str(tt.minutes) + ":" + str(tt.seconds))

time1 = Time()
time1.hours = 10
time1.minutes = 20
time1.seconds = 20

time1.timeprint()


