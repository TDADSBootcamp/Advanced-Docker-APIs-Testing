'''
This example uses the doctest framework to perform simple tests of functions.


'''
from typing import TextIO

import pandas as pd


def format_charge(value: float) -> str:
  '''
  Formats the charge value with the appropriate currency symbol
  >>> format_charge(1)
  '£1.00'

  >>> format_charge(0.01)
  '£0.01'

  >>> format_charge(100.01)
  '£100.01'
  '''

  return str(value)


def apply_rates(sales_df: pd.DataFrame, rates_df: pd.DataFrame) -> pd.DataFrame:
  rated_sales = sales_df.join(rates_df, on='rate')
  rated_sales['charge'] = (rated_sales['y'] *
                           rated_sales['Y']).apply(format_charge)
  return rated_sales


def main(sales_io: TextIO, rates_io: TextIO, output_io: TextIO):
  sales_df = pd.read_csv(sales_io)
  rates_df = pd.read_csv(rates_io, index_col='rate')

  rated_data = apply_rates(sales_df, rates_df)

  rated_data.to_csv(output_io, columns=['x', 'campaign_name', 'charge'])


# this is a Python idiom - it allows this code to be run both as a script and imported into another module
if __name__ == '__main__':
  with open('mydata.csv') as sales, open('rates.csv') as rates, open(
      'out.csv') as output:
    main(sales_io=sales, rates_io=rates, output_io=output)
