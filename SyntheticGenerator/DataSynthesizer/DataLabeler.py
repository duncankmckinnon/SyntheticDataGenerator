import random
import pandas as pd

class DataLabeler:
    def __init__(self, synthetic_data, rule = None):
        self.data = synthetic_data
        self.rows = len(self.data)
        self.rule = rule
    def generate(self, rule = None, lrange = [0,1]):
        if self.rule == None and rule == None:
            self.rule = lambda row: random.choice(lrange)
        elif rule != None:
            self.rule = rule
        try:
            labels = self.data.apply(self.rule, axis = 1)
        except:
            raise RuntimeError('rule function failed to execute')
        return labels