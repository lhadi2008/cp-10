my_file = open("cp-0.txt", "r")
len_file = my_file.read()

file = "cp-0.txt"

def get_firstlines(line_number=0):
 line_number = int(input("Enter N value: "))
 with open(file, 'r') as filedata:
  linesList= filedata.readlines()
 print(f"The following are the first {line_number} lines of a text file:")
 for textline in (linesList[:line_number]):
  print(textline, end='')


def get_lastlines(line_number=0):
  line_number = int(input("Enter N value: "))

# Opening the given file in read-only mode
 
  with open(file, 'r') as filedata:  
# Read the file lines using readlines()
   linesList= filedata.readlines()
  print(f"The following are the last {line_number} lines of a text file:")
 #Traverse in the list of lines to retrieve the last N lines of a file
  for textline in (linesList[-line_number:]):
   print(textline, end='\n')


def getlen_file():
 my_file = open("cp-0.txt", "r")
 len_file = my_file.read()
 print(f'the file has {len(len_file)} words')


if __name__ == "__main__":
 get_firstlines()   # Get the first n lines of a file
 get_lastlines()    # Get  the last n lines of a file
 getlen_file()      #Get lenght of a file