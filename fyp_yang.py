#!/usr/bin/env python
# coding: utf-8

# In[119]:


import numpy as np


# In[224]:


import pyrr
import svgwrite


# In[ ]:





# In[196]:


from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


# In[48]:


from ccdc.io import MoleculeReader


# In[269]:


import ATLK


# In[4]:


import math


# In[35]:


from ccdc import crystal


# In[36]:


from ccdc import io


# In[42]:


from ccdc import utilities


# In[53]:


csd = io.CrystalReader('ADTA4fold.cif')


# In[268]:


def distance(a,b):
    x = a.coordinates.x-b.coordinates.x
    y = a.coordinates.y-b.coordinates.y
    z = a.coordinates.z-b.coordinates.z
    distance = math.hypot(x,y,z)
    return round(distance,10)


# In[159]:


packed = csd[0].packing(((0,0,0),(1,1,1)),'Centroidincluded')


# In[56]:


def getSegments(atoms,limit):
    nums = len(atoms)
    segments = np.empty((0,2,3))
    for i in range(nums):
        atom1 = atoms[i]
        for  j in range(i+1,nums):
            atom2 = atoms[j]
            start = np.array(atom1.coordinates[0:3])
            end = np.array(atom2.coordinates[0:3])
            if(distance(atom1,atom2)<=limit):
                segments = np.concatenate((segments,np.array([[start,end]])),axis=0)
    return segments       


# In[205]:


def periodicSegments(atoms,atom1,atom2):
    label_1 = atom1.label
    label_2 = atom2.label
    dis = np.linlag(atom1,atom2)
    atoms_1 = []
    atoms_2 = []
    periodic_seg = np.empty((0,2,3))
    for atom in atoms:
        if (atom.label==label_1):
                atoms_1.append(atom)  
        if(atom.label == label_2):
                atoms_2.append(atom)
    for i in range(len(atoms_1)):
        if(distance(atoms_1[i],atoms_2[i])==dis):
            start = np.array(atoms_1[i].coordinates[0:3])
            end = np.array(atoms_2[i].coordinates[0:3])
            periodic_seg= np.concatenate((periodic_seg,np.array([[start,end]])),axis=0)
    return atoms_1,atoms_2,periodic_seg


# In[206]:


atoms_1,atoms_2,segments=periodicSegments(packed.atoms,atom_1,atom_2)


# In[235]:


segment_s = getSegments(packed.atoms,3)


# In[239]:


segment_s[0][1]


# In[192]:


print(atom_1,atom_2)


# In[83]:


len(mol.atoms)


# In[96]:


mol_1 = mol.components[0]
mol_2 = mol.components[1]


# In[180]:


print(len(mol_1.atoms))


# In[181]:


print(len(mol_2.atoms))


# In[100]:


atom = mol.atoms[0]


# In[108]:


atom.label


# In[73]:


t = np.empty(0)


# In[162]:


segments = np.empty((0,3))


# In[165]:


segments = np.concatenate((segments,np.array([[1,1,1]])),axis=0)


# In[167]:


segments[0]


# In[158]:


segments.shape


# In[12]:


print(packed.atoms)


# In[265]:


segp = ATLK.Segquad([segment_s[0],segment_s[100]])


# In[263]:


segment_s[0]


# In[264]:


segment_s[1]


# In[ ]:





# In[266]:


simplink=0


# In[267]:


simplink += segp.segatan()
print(simplink)


# In[ ]:




