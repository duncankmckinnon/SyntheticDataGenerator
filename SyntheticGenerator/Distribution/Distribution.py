import numpy as np

class Distribution:
    """
    Distribution class - generates values to be used when weighting
    attribute prevalence
    
    Properties:
        - name (str) - the object name (Distribution)
        - type (str) - the type of distribution (constant, uniform, etc.)
        - weights (np.array) - the array of weights corresponding to unique values of an attribute
    Implements:
        - generate(n -> int, sparsity -> float, **kwargs -> dict) --> list
    """
    def __init__(self, distribution_type, weights = None):
        self.name = 'Distribution'
        self.type = distribution_type
        self.weights = weights
    def generate(self, n, sparsity = 0, **kwargs):
        """
        generate a distribution of weights for n cardinality attribute
        with sparsity% missing data
        
        Parameters:
            - n (0 < integer) - number of unique attribute values
            - sparsity (0 <= float <= 1) - percentage of missing values (None)
            - **kwargs - arguments to scipy.stats distribution function
        """
        if self.weights == None:
            self.weights = np.array([1/n] * n)
            self.sparse_scale(sparsity)
        return list(self.weights)
    def _sparse_scale_(self, sparsity):
        """
        scale weights to collectively sum to 100 - (100 * sparsity%)
        
        Parameters:
            - sparsity (0 <= float <= 1) - percentage of missing values (None)
        """
        minw = np.min(self.weights)
        if minw < 0:
            self.weights -= minw
        self.weights = (100 * (((1-sparsity) * (self.weights)) / np.sum(self.weights)))
    def __str__(self):
        return '{}{}():{}'.format(self.type, self.name, self.weights)
    def __rep__(self):
        return self.__str__()
        
class UniformDistribution(Distribution):
    def __init__(self):
        super().__init__('Uniform')
    def generate(self, n, sparsity = 0, **kwargs):
        self.weights = np.random.uniform(size = n)
        self._sparse_scale_(sparsity)
        return list(self.weights)
    
class NormalDistribution(Distribution):
    def __init__(self):
        super().__init__('Normal')
    def generate(self, n, sparsity = 0, **kwargs):
        scale = 1.0
        if kwargs and 'scale' in kwargs:
            scale = kwargs['scale']
        self.weights = np.random.normal(size = n, scale = scale)
        self._sparse_scale_(sparsity)
        return list(self.weights)

class PowerLawDistribution(Distribution):
    def __init__(self):
        super().__init__('Power')
    def generate(self, n, sparsity = 0, **kwargs):
        a = 0.5
        if kwargs and 'a' in kwargs:
            a = kwargs['a']
        if a <= 0:
            raise AttributeError('Parameter a must be > 0')
        self.weights = np.random.power(size = n, a = a)
        self._sparse_scale_(sparsity)
        return list(self.weights)    

    
class ExponentialDistribution(Distribution):
    def __init__(self):
        super().__init__('Exponential')
    def generate(self, n, sparsity = 0, **kwargs):
        scale = 2
        if kwargs and 'scale' in kwargs:
            scale = kwargs['scale']
        if scale == 0:
            raise AttributeError('scale cannot be 0')
        self.weights = np.random.exponential(size = n, scale = scale)
        self._sparse_scale_(sparsity)
        return list(self.weights)

class LaplaceDistribution(Distribution):
    def __init__(self):
        super().__init__('Laplace')
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
        self._sparse_scale_(sparsity)
        return list(self.weights)
