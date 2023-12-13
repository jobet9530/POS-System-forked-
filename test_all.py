import unittest

loader = unittest.TestLoader()
suite = loader.discover('app/tests')

runner = unittest.TextTestRunner()
runner.run(suite)
