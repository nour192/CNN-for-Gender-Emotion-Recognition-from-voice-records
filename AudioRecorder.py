#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('sudo apt-get install libportaudio2')
get_ipython().system('pip install sounddevice')
get_ipython().system('pip install wavio')
get_ipython().system('pip3 install sounddevice')
get_ipython().system('pip3 install wavio')
get_ipython().system('pip3 install scipy')


# In[8]:


import sounddevice as sd
from scipy.io.wavfile import write
import os
i = len(os.listdir('./'))

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

print("Recording ... ")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()
print("done!")
write('record' + str(i) + '.wav', fs, myrecording)


# In[ ]:




