
# coding: utf-8

# In[2]:


import os
import nbconvert
from nbconvert.exporters import PythonExporter


# In[56]:


def initConversion():
    path = "/home/apil/Git/fastai/"
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".ipynb") and 'checkpoint' not in file:
                source_nb = os.path.join(root, file)
                try:
                    exportToFile(source_nb)
                except:
                    print("failed to export: ",source_nb)


# In[57]:


def exportToFile(source_nb):
    dest = "/home/apil/Git/fastai/nb_dump/"
    (content, resource) = nbconvert.export(PythonExporter, source_nb)
    xs = source_nb[ source_nb.rfind('/')+1 : source_nb.rfind('.ipynb')]
    destpy = dest + xs + '.py'

    with open(destpy, 'w') as f:
        f.write(content)
    f.close()
    print("wrote to: ",destpy)


# In[58]:


if __name__ == '__main__':
    initConversion()

