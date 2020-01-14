import numpy as np

class Distribution:
    def __init__(self, weights = None):
        self.weights = weights
    def generate(self, n, sparsity = 0, **kwargs):
        if self.weights == None:
            self.weights = np.array([1/n] * n)
            self.sparse_scale(sparsity)
        return list(self.weights)
    def sparse_scale(self, sparsity):
        minw = np.min(self.weights)
        if minw < 0:
            self.weights -= minw
        self.weights = (100 * (((1-sparsity) * (self.weights)) / np.sum(self.weights)))
        
class UniformDistribution(Distribution):
    def generate(self, n, sparsity = 0, **kwargs):
        self.weights = np.random.uniform(size = n)
        self.sparse_scale(sparsity)
        return list(self.weights)
    
class NormalDistribution(Distribution):
    def generate(self, n, sparsity = 0, **kwargs):
        scale = 1.0
        if kwargs and 'scale' in kwargs:
            scale = kwargs['scale']
        self.weights = np.random.normal(size = n, scale = scale)
        self.sparse_scale(sparsity)
        return list(self.weights)

class PowerLawDistribution(Distribution):
    def generate(self, n, sparsity = 0, **kwargs):
        a = 0.5
        if kwargs and 'a' in kwargs:
            a = kwargs['a']
        if a <= 0:
            raise AttributeError('Parameter a must be > 0')
        self.weights = np.random.power(size = n, a = a)
        self.sparse_scale(sparsity)
        return list(self.weights)    

    
class ExponentialDistribution(Distribution):
    def generate(self, n, sparsity = 0, **kwargs):
        scale = 2
        if kwargs and 'scale' in kwargs:
            scale = kwargs['scale']
        if scale == 0:
            raise AttributeError('scale cannot be 0')
        self.weights = np.random.exponential(size = n, scale = scale)
        self.sparse_scale(sparsity)
        return list(self.weights)

class LaplaceDistribution(Distribution):
    def generate(self, n, sparsity = 0, **kwargs):
        loc = 0
        scale = 2
        if kwargs:
            if 'loc' in kwargs:
                loc = kwargs['loc']
            if 'scale' in kwargs:
                scale = kwargs['scale']
        if scale == 0:
            raise AttributeError('scale cannot be 0')
        self.weights = np.random.laplace(size = n, loc = loc, scale = scale)
        self.sparse_scale(sparsity)
        return list(self.weights)