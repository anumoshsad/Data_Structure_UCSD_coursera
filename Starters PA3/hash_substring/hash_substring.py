# python3

x = 263
p = 1000000007

def PolyHash(s):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % p
    return ans

def PreComputeHashes(T, plen):
	H = [0]*(len(T) - plen + 1)
	S = T[len(T)-plen:len(T)]
	H[len(T) - plen] = PolyHash(S)
	y = 1
	for i in range(1, plen+1):
		y = (y*x)%p
	for i in range(len(T) - plen - 1, -1,-1):
		H[i] = (x*H[i+1] + ord(T[i])-y*ord(T[i+plen]))%p
	return H

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, T):
	result = []
	pHash = PolyHash(pattern)
	H = PreComputeHashes(T, len(pattern))
	for i in range(len(T) - len(pattern)+1):
		if pHash != H[i]: continue
		if pattern == T[i: i + len(pattern)]:
			result.append(i)
	return result	
    # return [
    #     i 
    #     for i in range(len(text) - len(pattern) + 1) 
    #     if text[i:i + len(pattern)] == pattern
    # ]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

