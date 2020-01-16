from Attribute.AttributeFactory import AttributeFactory
import numpy as np
import pandas as pd


class DataSynthesizer:
    """
    Generate unique synthetic datasets consisting of a set of attributes with 
    known value ranges, distributions and sparsities.
    
    Properties:
        - rows (int) - number of rows in dataset
        - attributes (dict) - name : Attribute() dict
    Implements
        - generate(items -> list|dict, rows? -> int) -> pandas.core.frame.DataFrame
        - regenerate(rows? -> int) -> pandas.core.frame.DataFrame
    """
    def __init__(self, rows = 1):
        self.rows = rows
        self.attribute_factory = AttributeFactory()
        self.attributes = {}
        self.dataframe = {}
    def generate(self, items, rows = None):
        """
        Generate pandas DataFrame to use in analysis using metadata about the set 
        of attributes from a list, DataFrame, or dict of attribute properties
        
        Parameters:
            - items (list|dict|DataFrame) - either a list of attribute properties dictionairies, or a dictionary of { name : attribute } pairs 
                (e.g. [{ name : str, drange : [] ... }] or { name : { drange : [] ...}, }
            - rows (int) - number of rows
        Returns:
            - DataFrame - the synthetic dataset with specified attribute properties and rows
        """
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
    def regenerate(self, rows = None):
        """
        Generate a new dataset from a previously-defined set of attribute properties 
        (after running generate a first time with the attribute metadata)
        
        Parameters:
            - rows (int) - the number of rows to generate
        Returns:
            - DataFrame - the synthetic dataset with specified attribute properties and rows 
        """
        if rows is not None:
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
    def __str__(self):
        v = [ None ]
        if self.attributes != {}:
            v = [i for i,j in self.attributes.items()] 
        return 'DataSynthesizer(): {}'.format(v)
    def __rep__(self):
        return self.__str__()
