import numpy as np
import numpy.matlib
from scipy.integrate import quad

def lebesgue(x, xx):
    L = np.abs( lagrange(x,xx) )
    return np.sum( L, axis = -1 )

def lagrange_k(x, nodes, k):
    nodes_ = list(np.delete(nodes,k))
    #l_k=1
    #for nj in nodes_:
    #    l_k *= (x-nj)/(nodes[k]-nj)
    l_k = np.prod((x-nodes)/(nodes[k]-nodes) )
    return l_k

def quadrature_weights(nodes, Interval, S = None):
    N_nodes = len(nodes)
    a,b = Interval
    if S is None:
        S=lambda x:x
    lagrange_functs = lambda x: lagrange_k(S(x), S(nodes),k)
    weights = [quad( lagrange_functs, a, b)[0] for k in range(N_nodes)]
    return np.array(weights)
