from Attribute.AttributeFactory import AttributeFactory
import numpy as np
import pandas as pd


class DataSynthesizer:
    def __init__(self, rows = 1):
        self.rows = rows
        self.attribute_factory = AttributeFactory()
        self.attributes = {}
        self.dataframe = {}
    def generate(self, items, rows = None):
        if rows is not None:
            self.rows = rows
        self.items = items
        if type(self.items) == list:
            self._create_from_list_()
        if type(self.items) == dict:
            self._create_from_dict_()
        if type(self.items) == 'pandas.core.frame.DataFrame':
            self.items = self.items.T.to_dict()
            self._create_from_dict_()
        return pd.DataFrame(self.dataframe)
    def regenerate(self, rows = 1):
        self.rows = rows
        self.dataframe = {}
        for name, attribute in self.attributes.items():
            self.dataframe[name] = attribute.get_values(rows)
        return pd.DataFrame(self.dataframe)
    def _create_from_list_(self):
        for attribute in self.items:
            self._add_attribute_(attribute)
    def _create_from_dict_(self):
        for _, attribute in self.items.items():
            self._add_attribute_(attribute)
    def _add_attribute_(self, attribute):
        # Create attribute
        name = attribute.get('name')
        if name is None:
            raise KeyError('name is missing from attribute')
        dtype = attribute.get('dtype', 'boolean')
        init_item = self.attribute_factory.create(name, dtype)
        self.attributes[name] = init_item
        
        # Generate data 
        drange = attribute.get('drange', None)
        if drange is not None and type(drange) == str:
            drange = eval(drange)
        distribution = attribute.get('distribution','uniform')
        sparsity = attribute.get('sparsity', 0)
        kwargs = attribute.get('kwargs', {}) 
        if type(kwargs) == str:
            kwargs = eval(kwargs)
        self.dataframe[name] = init_item.generate(length = self.rows, distribution = distribution, drange = drange, sparsity = sparsity, **kwargs)
        
