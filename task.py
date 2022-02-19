#NOTE: While running this file through cmd write python task.py --input_file_path="access_log.txt"
import re
from collections import defaultdict 
import argparse

if __name__=='__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--input_file_path', help="Please provide a text file")
  args = parser.parse_args()

from collections import defaultdict

class status_code:
  def __init__(self, file_path):
    '''
    input: file_path, dtype : str
    -------
    output: None
    '''
    try:
      with open(file_path,'r') as f:
        self.file = f.read() #read file
      #finds http response with status code from all lines of log and store in a list
      self.file_data = re.findall('HTTP[^"]*"\s\d{3}',self.file)
      #store information of different status codes.
      self.status_codes = {"1":"Information Codes", "2":"Success Codes",
                          "4":"Client Error Codes", "3":"Redirection Codes",
                          "5":"Server Error Codes"}
      #keep tracks of codes and their count e.g success code : {200:45}
      self.status_code_result = {val:defaultdict(lambda:0) for i,val in self.status_codes.items()}
      #keep track of status Response and their count e.g success codes : 303
      self.status_code_count = {key:status_count(key) for key in self.status_code_result.keys()}
    except:
      pass 

  def process_file(self):
    '''
    input: None
    -------
    output: None
    '''
    try:
      for code in self.file_data: #read data line by line
        code = code[-3:]
        #store status code and their code.
        self.status_code_result[self.status_codes[code[0]]][code] += 1
        #store status reponse count
        self.status_code_count[self.status_codes[code[0]]].count += 1
    except:
      pass

  def display_status_occurrence(self):
    try:
      self.process_file() # process all information here.
      for key,val in self.status_code_result.items(): #Results are displayed
        if len(val) == 0:
          continue
        print("status code : ",key)
        for k,v in val.items():
          print("\tcode : {0} -> count : {1}".format(k,v))
        print()
        print("\tTotal {0} count : ".format(self.status_code_count[key].response), 
              self.status_code_count[key].count)
        print("-"*50)
    except:
      pass

class status_count(status_code):
  def __init__(self,response):
    '''
    input: response, dtype : str
    -------
    output: None

    child class to keep track of Total status response count.
    '''
    self.response = response
    self.count = 0

if __name__=='__main__':
  log = status_code(args.input_file_path)
  log.display_status_occurrence()


