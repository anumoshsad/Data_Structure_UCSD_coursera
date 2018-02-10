# python3

from collections import deque
from queue import PriorityQueue

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        #self.assigned_workers = [None] * len(self.jobs)
        #self.start_times = [None] * len(self.jobs)
        #next_free_time = [0] * self.num_workers
        #for i in range(len(self.jobs)):
        #  next_worker = 0
        #  for j in range(self.num_workers):
        #    if next_free_time[j] < next_free_time[next_worker]:
        #     next_worker = j
        # self.assigned_workers[i] = next_worker
        # self.start_times[i] = next_free_time[next_worker]
        # next_free_time[next_worker] += self.jobs[i]
        jbs = self.jobs[:]
        jbs = deque(jbs)
        self.assigned_workers = []
        self.start_times = []
        pq = PriorityQueue()
        self.assigned_workers = []
        self.start_times = []
        n = self.num_workers
        i = 0
        while i < n and jbs:
            next_worker = i
            next_finish_time = jbs.popleft()
            pq.put((next_finish_time, next_worker, 0))
            i+=1
        #print(pq)
        while not pq.empty():
            (finish, worker, start ) = pq.get()
            #print(finish, worker, start)
            self.assigned_workers.append(worker)
            self.start_times.append(start)
            if jbs:
                job = jbs.popleft()
                pq.put((finish + job, worker, finish ))
            #print(jbs)
        assignment = [(i,j) for i,j in zip(self.assigned_workers, self.start_times)]
        assignment.sort(key= lambda tup: (tup[1],tup[0]))
        self.assigned_workers = [i[0] for i in assignment]
        self.start_times = [i[1] for i in assignment]

            
    




    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

