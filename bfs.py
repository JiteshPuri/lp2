#!/usr/bin/env python
# coding: utf-8

# In[14]:


graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}


# In[15]:


visited=[]
queue=[]


# In[16]:


def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while(queue):
        s=queue.pop(0)
        print(s,end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited,graph,'B')


# In[ ]:




