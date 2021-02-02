from pathlib import Path

#Absolute path
#eg: Windows - c:\Program Files\Microsoft
  #  Mac - /usr/local/bin
#Relative path

path = Path("ecommerce")
print(path.exists())


#path = Path("vivi")
#print(path.mkdir()) # it will make a new directory
#print(path.rmdir()) # it will remove the directory

path =Path()
for file in path.glob('*.py'):
    print(file)
