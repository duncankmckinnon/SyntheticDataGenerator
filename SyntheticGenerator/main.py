from DataSynthesizer import DataSynthesizer, DataLabeler


if __name__ == "__main__":
    SD = DataSynthesizer.DataSynthesizer(rows=10)
    data = SD.generate([{
        'name': 'BoolPowerTest',
        'dtype': 'boolean',
        'distribution': 'power',
        'sparsity': 0.5,
        'kwargs': {'a': 0.2}
    }, {
        'name': 'FloatExpTest',
        'dtype': 'float',
        'distribution': 'exponential',
        'drange': [1/(i*10+3) for i in range(1, 101)],
        'sparsity': 0.2,
        'kwargs': {'b': 3}
    },{
        'name': 'StringCustomTest',
        'dtype': 'string',
        'distribution': 'custom',
        'drange': ['alpha', 'beta', 'omega', 'epsilon', 'delta'],
        'sparsity': 0.05,
        'kwargs': {'weights': [0.2, 0.4, 0.1, 0.05, 0.2]}
    }, {
        'name': 'CustomNormalTest',
        'dtype': 'custom',
        'distribution': 'normal',
        'drange': ['alpha', 'beta', 'omega', 3, 'delta'],
        'sparsity': 0.5,
        'kwargs': {'scale' : 2}
    }, {
        'name': 'IntegerUniformTest',
        'dtype': 'int64',
        'distribution': 'uniform',
        'drange': [i for i in range(-27,28,3)],
        'sparsity': 0.8
    }])
    print(data)
