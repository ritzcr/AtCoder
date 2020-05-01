X = int(input())
happy = 0
d_500, m_500 = divmod(X, 500)
d_5, m_5 = divmod(m_500, 5)
print(d_500 * 1000 + d_5 * 5)
