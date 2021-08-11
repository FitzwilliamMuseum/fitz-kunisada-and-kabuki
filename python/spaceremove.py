import os
path = '../images/prints/'
for filename in os.listdir(path):
    #print(filename)
    os.rename(os.path.join(path,filename),os.path.join(path, filename.replace(' ', '_').lower()))
