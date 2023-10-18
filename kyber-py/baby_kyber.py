######################################################
#Baby Kyber
#Coded by Kasra Ahmadi
#Cryptographic Hardware Lab @USF_ENB323
#Supervised by Pr. Mehran Mozaffari Kermani
######################################################

from polynomials import *
import math

######################################################
#Key_Gen
######################################################
err_msg = "Please change v accordingly to  equation v = Transpose(t)*r + e2 - m"
err_msg_2 = "Please change m_n accordingly to  equation v - Transpose(s) * u"

q = 17
n = 4
R = PolynomialRing(q,n)
x = R.gen()

# Private_key = |s0 s1|
s0 = -1*x**3 + -1*x**2 + x
s1 = -1*x**3 + -1*x

# Generating random polynomial A
# A = |A00  A01|
#     |A10  A11|
A00 = 6*x**3 + 16*x**2 + 16*x + 11
A01 = 9*x**3 + 4*x**2 + 6*x + 3
A10 = 5*x**3 + 3*x**2 + 10*x + 1
A11 = 6*x**3 + x**2 + 9*x + 15

# Generating error
# z = |z0 z1|
z0 = x**2
z1 = x**2 - x

# t = As + e
t0 = A00 * s0 + A01 * s1 + z0
t1 = A10 * s0 + A11 * s1 + z1

# Private_key = s
# Public_key = (A,t)
def encryption(A00,A01,A10,A11,t0,t1):
    # r = |r0 r1|
    r0 = -1*x**3 + x**2
    r1 = 1*x**3 + 1*x**2 -1 * x**0
    # e1 = |e10 e11|
    e10 = x**2 + x
    e11 = x**2
    e2 = -x**3 - x**2
    #Encrypting message
    # M = 1011 in binary
    m_b = math.ceil(q/2)
    m = x**3 + x + 1
    m = m * m_b
    # u =  A^T*r + e1
    # u = |u0 u1|
    u0 = A00 * r0 + A10 * r1 + e10
    u1 = A01 * r0 + A11 * r1 + e11
    v = 0 # Modify it based on  v = Transpose(t)*r + e2 - m
    v = (t0 * r0) + (t1 * r1) + e2 - m

    return u0,u1,v
def decryption(u0,u1,v):
    try:
        assert v != 0, err_msg
        m_n = 0 # Modify it based on  m_n = v - Transpose(s) * u
        assert m_n != 0, err_msg_2
        compress_mod = 2
        compress_float = compress_mod / q
        m_n.coeffs = [round_up(compress_float * c) % compress_mod for c in m_n.coeffs ]
        print("Well done \nDecrypted data is: " + str(m_n))
    except Exception as e:
        print(e)

u_0,u_1,v = encryption(A00,A01,A10,A11,t0,t1)
decryption(u_0,u_1,v)
