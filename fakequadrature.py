import numpy as np
import numpy.matlib
from scipy.integrate import quad
from scipy.integrate import simps


def lagrange_k(x, nodes, k):
    nodes_but = np.delete(nodes,k)
    D = x-nodes_but[:,None]
    N = nodes[k]-nodes_but
    l_k = np.prod(D/N[:,None], axis = 0 )
    return l_k

def quadrature_weights(nodes, interval, mapping = None):
    N_nodes = len(nodes)
    a,b = interval
    if mapping is None:
        mapping = lambda x: x       
    lagr = lambda y,k: lagrange_k(mapping(y),mapping(nodes),k)
    weights = [ quad( lagr, a, b, epsabs = 1.e-9, limit=250, args=(k,))[0] for k in range(N_nodes) ]
    #x = np.linspace( a, b, 10*N_nodes+1 )
    #weights = [ simps(lagr(x,k), x) for k in range(N_nodes) ]
    return np.array(weights)

