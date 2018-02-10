# python3
from collections import deque

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = deque([])

    def Process(self, request):
        # write your code here
        while self.finish_time_ and self.finish_time_[0] <= request.arrival_time:
                g = self.finish_time_.popleft() 
        if len(self.finish_time_) == size: 
            return Response(True, -1)
            print(self.finish_time_)

        else:
            if self.finish_time_ : 
                last_finished = self.finish_time_[-1]
                self.finish_time_.append(last_finished + request.process_time)
                #print(self.finish_time_)
            else: 
                last_finished = request.arrival_time
                self.finish_time_.append(last_finished + request.process_time)
            #print(self.finish_time_, last_finished)
            return Response(False , last_finished)


def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
