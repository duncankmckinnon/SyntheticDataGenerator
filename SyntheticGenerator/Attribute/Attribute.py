import numpy as np
import string
import random

class Attribute:
    def __init__(self, name, distribution_factory):
        self.name = name
        self.distribution_factory = distribution_factory
        self.range = None
        self.weights = {}
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

    
class BooleanAttribute(Attribute):
    def _check_range_(self, drange):
        return [0,1]
class StringAttribute(Attribute):
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
    def _check_range_(self, drange):
        if drange != None and type(drange) == list:
            if all([type(i) == int for i in drange]):
                return drange
            else:
                raise AttributeError('drange list is not of correct datatype')
        else:
            return [i+1 for i in range(10)]
class FloatAttribute(Attribute):
    def _check_range_(self, drange):
        if drange != None and type(drange) == list:
            if all([type(i) == float for i in drange]):
                return drange
            else:
                raise AttributeError('drange list is not of correct datatype')
        else:
            return [1/(i+2) for i in range(10000)]