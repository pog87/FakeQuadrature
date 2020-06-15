import numpy as np
import numpy.matlib
from scipy.integrate import quad


def lagrange_k(x, nodes, k):
    nodes_ = np.delete(nodes,k)
    l_k = np.prod((x-nodes_)/(nodes[k]-nodes_) )
    return l_k

def quadrature_weights(nodes, interval, mapping = None):
    N_nodes = len(nodes)
    a,b = interval
    if mapping is None:
        mapping = lambda x: x       
    funcf = lambda y,k: lagrange_k(mapping(y),mapping(nodes),k)
    weights = [ quad( funcf, a, b, epsabs = 1.e-9, limit=250, args=(k,))[0] for k in range(N_nodes) ]
    return np.array(weights)

