from Attribute import Attribute
from Distribution.DistributionFactory import DistributionFactory

class AttributeFactory:
    """
    Class to generate and deploy specific attributes that 
    will share a distribution factory. Attributes types are:
    - custom
    - boolean
    - string
    - int or int64
    - float or float64
    
    Properties:
        - central_distribution_factory (DistributionFactory) - a DistributionFactory
    Implements:
        - create(name -> str, dtype -> str) --> Attribute()
    Raises:
        - AttributeError - dtype is not valid
    """
    def __init__(self):
        self.central_distribution_factory = DistributionFactory()
    def create(self, name, dtype, drange = None):
        attribute_class = None
        if dtype == 'boolean':
            attribute_class = Attribute.BooleanAttribute(name, self.central_distribution_factory)
        elif dtype == 'string':
            attribute_class = Attribute.StringAttribute(name, self.central_distribution_factory)
        elif dtype == 'int64' or dtype == 'int':
            attribute_class = Attribute.IntegerAttribute(name, self.central_distribution_factory)
        elif dtype == 'float64' or dtype == 'float':
            attribute_class = Attribute.FloatAttribute(name, self.central_distribution_factory)
        elif dtype == 'custom':
            attribute_class = Attribute.Attribute(name, self.central_distribution_factory)
        else:
            raise AttributeError('dtype is not valid (must be one of [boolean, string, int, int64, float, float64, custom])')
        return attribute_class
    def __str__(self):
        return 'AttributeFactory()'
    def __rep__(self):
        return self.__str__()
