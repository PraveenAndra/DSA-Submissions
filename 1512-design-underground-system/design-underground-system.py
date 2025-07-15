class UndergroundSystem:

    def __init__(self):
        self.averageMap = {}
        self.checkin = {}

        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_station, checkin_time = self.checkin[id]
        del self.checkin[id]
        timeTaken = t-checkin_time
        if checkin_station not in self.averageMap:
            self.averageMap[checkin_station] = {}
        if stationName not in self.averageMap[checkin_station]:
            self.averageMap[checkin_station][stationName] = (0,0)
        curr_time,curr_count = self.averageMap[checkin_station][stationName]
        self.averageMap[checkin_station][stationName] = (curr_time+timeTaken, curr_count + 1)



    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time,count = self.averageMap[startStation][endStation]
        return time / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)