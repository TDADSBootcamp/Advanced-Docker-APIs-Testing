'''
Example unit tests for the buggy code
'''
import io
import unittest

import testing.buggy_doctests as buggy


class BuggyTests(unittest.TestCase):
  '''
  Example behavioural tests of the buggy code
  '''

  def test_main(self):
    sales = io.StringIO('''
x,y,rate,campaign_name,Y
2,3,r,d1,1
3,9,r,d1,1
4,8,r,d1,0
5,9.8,s,d2,1
''')

    rates = io.StringIO('''
rate,val
r,0.5
s,1.0
''')

    expected = '''x,campaign,charge
2,d1,£1.50
3,d1,£4.50
4,d1,£4.00
5,d2,£8.00
'''

    actual = io.StringIO()

    buggy.main(sales, rates, actual)

    self.assertEqual(actual.getvalue(), expected)
