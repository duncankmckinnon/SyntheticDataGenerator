from Distribution import Distribution
class DistributionFactory:
    def create(self, distribution, weights = None):
        distribution_class = None
        if distribution == 'custom':
            distribution_class = Distribution.Distribution(weights)
        elif distribution == 'uniform':
            distribution_class = Distribution.UniformDistribution()
        elif distribution == 'normal':
            distribution_class = Distribution.NormalDistribution()
        elif distribution == 'power':
            distribution_class = Distribution.PowerLawDistribution()
        elif distribution == 'exponential':
            distribution_class = Distribution.ExponentialDistribution()
        elif distribution == 'laplace':
            distribution_class = Distribution.LaplaceDistribution()
        else:
            raise AttributeError('distribution is not valid (must be one of [custom, uniform, normal, power, exponential, laplace])')
        return distribution_class
