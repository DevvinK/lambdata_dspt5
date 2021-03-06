#  test/pytest_assignment_test.py

from pandas import DataFrame
from my_lambdata.assignment import add_state_names

# OBJECTIVE: test the add_state_names() function from the my_lambdata/assignment.py file

def test_add_state_names():
  
  df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
  # self.assertEqual(list(df.columns),['abbrev'])
  assert list(df.columns) == ['abbrev']
  
  result = add_state_names(df)
  # self.assertEqual(list(result.columns),['abbrev', 'name'])
  # self.assertEqual(result.iloc[0]["abbrev"], "CA")
  # self.assertEqual(result.iloc[0]["name"], "Cali")
  assert list(result.columns) == ['abbrev', 'name']
  assert result.iloc[0]["abbrev"] == "CA"
  assert result.iloc[0]["name"] == "Cali"



#Afer we invoke the fucntion:
  #expect a second column with the same number of rows
  #expect certain column names exist before and after


  #df.columns
  #   self.assertEqual('foo'.upper(), 'FOO') #True or False

