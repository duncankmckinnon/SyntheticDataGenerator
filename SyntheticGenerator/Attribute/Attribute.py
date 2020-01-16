import numpy as np
import string
import random

class Attribute:
    """
    Class for storing and generating attributes or columns of data
    from value ranges and weight distributions
    
    Properties:
        - name (str) - the attribute or column name
        - type (str) - the type of attribute (e.g. Custom, Boolean, etc.)
        - distribution_factory (DistributionFactory) - to generate specific distribution and weights
        - drange (list) - the set of unique values in the attribute (e.g. [0,1] for boolean)
        - cardinality (0 < int) - the number of unique values in drange
        - length (0 < int) - the number of entries in the attribute
        - sparsity (0 <= float <= 1.0) - the percentage of missing data
        - weights (list) - the distribution of weights for each unique value, to use when choosing values
        - values (list) - the actual values that make up the attribute
    Implements:
        - generate(length -> 0 < int, drange -> list, distribution -> str, sparsity -> 0 <= float <= 1, **kwargs -> dict) -> list
        - _weights_() --> { range : list, weights: list }
     """
    def __init__(self, name, distribution_factory, attribute_type = 'Custom'):
        self.name = name
        self.distribution_factory = distribution_factory
        self.type = attribute_type
        self.drange = None
        self.weights = []
        self.values = np.array([])
    def generate(self, length=1, drange = None, distribution='uniform', sparsity=0, **kwargs):
        self.sparsity = sparsity
        self.weights = None
        self.drange = self._check_range_(drange)
        self.cardinality = len(self.drange)
        self.drange.append(None)
        if kwargs and 'weights' in kwargs and type(kwargs['weights']) == list:
            self.weights = kwargs['weights']
        else:
            self.distribution = self.distribution_factory.create(distribution)
            self.weights = self.distribution.generate(self.cardinality, self.sparsity, **kwargs)
        self.weights.append( 100 * self.sparsity )
        return self.get_values(length)
    def _weights_(self):
        return {
            'range' : self.drange,
            'weights' : self.weights
        }
    def get_values(self, length):
        self.values = random.choices(self.drange, weights = self.weights, k = length)
        return self.values
    def _check_range_(self, drange):
        if drange != None and type(drange) == list:
            return drange
        return [0,1]
    def __str__(self):
        return '{}Attribute:{}, {}'.format(self.type, self.name, self.drange)
    def __rep__(self):
        return self.__str__()
    
class BooleanAttribute(Attribute):
    def __init__(self, name, distribution_factory):
        super().__init__(name, distribution_factory, 'Boolean')
    def _check_range_(self, drange):
        return [0,1]
class StringAttribute(Attribute):
    def __init__(self, name, distribution_factory):
        super().__init__(name, distribution_factory, 'String')
    def _check_range_(self, drange):
        if drange != None and type(drange) == list:
            if all([type(i) == str for i in drange]):
                return drange
            else:
                raise AttributeError('drange list is not of correct datatype')
        else:
            drange = [i for i in string.ascii_letters]
        return drange
class IntegerAttribute(Attribute):
    def __init__(self, name, distribution_factory):
        super().__init__(name, distribution_factory, 'Integer')
    def _check_range_(self, drange):
        if drange != None and type(drange) == list:
            if all([type(i) == int for i in drange]):
                return drange
            else:
                raise AttributeError('drange list is not of correct datatype')
        else:
            return [i+1 for i in range(10)]
class FloatAttribute(Attribute):
    def __init__(self, name, distribution_factory):
        super().__init__(name, distribution_factory, 'Float')
    def _check_range_(self, drange):
        if drange != None and type(drange) == list:
            if all([type(i) == float for i in drange]):
                return drange
            else:
                raise AttributeError('drange list is not of correct datatype')
        else:
            return [1/(i+2) for i in range(10000)]
