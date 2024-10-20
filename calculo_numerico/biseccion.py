#!/usr/bin/env python3
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
            er = fabs(((m_actual-m_previo)/m_actual))

            print("iter =",i)
            print("a =", a ,"\nb =", b,f'\nm{i}= {m_actual}')
            print("error =", f'{round(er*100,6)}%')

            if(f(m_actual)*f(b)<0):
                a = m_actual
            elif(f(m_actual)*f(a)<0):
                b = m_actual
            else:
                return m_actual,er
            
            i = i+1
        print('-'*100)
    
    return m_actual,er
    
            
    



if __name__ == '__main__':
    def f(x):
        return sin(x)-exp(-x)
    a = 0
    b = 1
    resultado = biseccion(f,a,b,0.03,20)
    print(f"Raiz: {resultado[0]:0.7f}\nError: {resultado[1]:0.4f}")