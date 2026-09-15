# n_lines, m_lines = ([int(el) for el in input().split()])
n_lines, m_lines = map(int, input().split())

n_set = set()
m_set = set()

for _ in range(n_lines):
    n_set.add(int(input()))

for _ in range(m_lines):
    m_set.add(int(input()))

elements = n_set.intersection(m_set)
print(*elements, sep='\n')