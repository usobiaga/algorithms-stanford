from heapq import heappush, heappop, heapify
from heapq_max import  heapify_max, heappop_max, heappush_max

FILE = "median.txt"

def medianMaintenance():
    with open(FILE, 'r') as f:
        h_high = [int(f.readline())]
        msum = h_high[0] 
        h_low = [int(f.readline())]
        lhigh = 1
        llow = 1
        if (h_high[0] < h_low[0]): h_high, h_low = h_low, h_high #swap
        msum += h_low[0] 
        heapify(h_high)
        heapify_max(h_low)
        line = int(f.readline())
        while line:

            ## push element into heap
            line = int(line)
            if (h_high[0] > line):
                 heappush_max(h_low, line)
            else:
                 heappush(h_high, line)
                 
            ## rebalance the stack
            diff =  len(h_low) - len(h_high)
            if diff == -2: ## h_high is too big
                heappush_max(h_low, h_high[0])
                heappop(h_high)
            if diff == 2:
                heappush(h_high, h_low[0])
                heappop_max(h_low)

            ## recompute the median dif
            diff = len(h_low) - len(h_high)
            if diff >= 0: #more elems in low than in high
                msum += h_low[0]
            else:
                msum += h_high[0]
            
            line = f.readline()

    return msum

            
if __name__ == '__main__':
    result = medianMaintenance()
    print("result is: ", result % 10000)
        
    
    
    


