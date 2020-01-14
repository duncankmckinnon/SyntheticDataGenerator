from Attribute import Attribute
from Distribution.DistributionFactory import DistributionFactory


class AttributeFactory:
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
            raise AttributeError('dtype is not valid (must be one of [boolean, string, int64, float64, custom])')
        return attribute_class