from DataSynthesizer import DataSynthesizer, DataLabeler


if __name__ == "__main__":
    SD = DataSynthesizer.DataSynthesizer(rows=10)
    data = SD.generate([{
        'name': 'BoolTest',
        'dtype': 'boolean',
        'distribution': 'power',
        'sparsity': 0.5,
        'kwargs': {'a': 0.2}
    }, {
        'name': 'FloatTest',
        'dtype': 'float',
        'distribution': 'exponential',
        'drange': [1/(i*10+3) for i in range(1, 101)],
        'sparsity': 0.2,
        'kwargs': {'b': 3}
    }, {
        'name': 'StringTest',
        'dtype': 'string',
        'distribution': 'normal',
        'drange': ['alpha', 'beta', 'omega', 'epsilon', 'delta'],
        'sparsity': 0.05,
        'kwargs': {'weights': [0.2, 0.4, 0.1, 0.05, 0.2]}
    }, {
        'name': 'IntegerTest',
        'dtype': 'int64',
        'distribution': 'uniform',
        'drange': [1, 3, 5, 7, 9, 11, 14],
        'sparsity': 0.9
    }])
    print(data)
