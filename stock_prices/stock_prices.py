#!/usr/bin/python

import argparse

def find_max_profit(prices):
    
    largest_num_index = prices.index(max(prices))
    largest_num = max(prices)
    if largest_num_index > 0 and largest_num > prices[largest_num_index -1]:
        return largest_num - prices[largest_num_index-2]
    
    if largest_num_index < 1:
          new_array = prices[1:]
          new_largest_num_index = new_array.index(max(new_array))
          new_largest_num = max(new_array)
          return new_largest_num - prices[new_largest_num_index]

    
   

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))





