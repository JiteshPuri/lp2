#!/usr/bin/env python
# coding: utf-8

# In[11]:


graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}


# In[12]:


visited = set() 


# In[13]:


def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# In[14]:


dfs(visited, graph, 'B')


# In[ ]:




