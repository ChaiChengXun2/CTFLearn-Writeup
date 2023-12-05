import gmpy2

n = 245841236512478852752909734912575581815967630033049838269083
e = 1
c = 9327565722767258308650643213344542404592011161659991421

for t in range(10):
    m, is_true_root = gmpy2.iroot(t * n + c, e)
    if is_true_root:
        print(f"Found, Iteration = {t}")
        print(m)
        print(f"Flag: {bytearray.fromhex(format(m, 'x')).decode()}")
        break