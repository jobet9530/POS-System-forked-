import unittest

loader = unittest.TestLoader()
suite = loader.discover('/app')

runner = unittest.TextTestRunner()
runner.run(suite)
