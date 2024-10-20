from math import *

def biseccion(f,a,b,tol,Ni):
    m_actual = 0
    m_previo = 0
    er = 100
    i = 1
    
    if(f(a)*f(b)<0):
        while(er > tol and i < Ni):
            print('-'*100)
            m_previo = m_actual
            m_actual = (a+b)/2
            er = abs(((m_actual-m_previo)/m_actual))*100.0

            print("iter =",i)
            print("a =", a ,"\nb =", b,f'\nm{i}= {m_actual}')
            print("error =", f'{round(er,6)}%')

            if(f(m_actual)*f(b)<0):
                a = m_actual
            else:
                b = m_actual
            
            i = i+1
        print('-'*100)
    
            
    



if __name__ == '__main__':
    def f(x):
        return sin(x)-exp(-x)
    
    a = 0
    b = 1
    biseccion(f,a,b,3,20)