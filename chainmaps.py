#ADT 
#chainmaps 
from  collections import ChainMap
defaults = {'theme':'Default','language':'eng','shadowIndex':True, 'showFooter':True}
cm = ChainMap(defaults) # creates a chainmap with default configuration
cm2 = cm.new_child({'theme':'bluesky'}) #creates a new cahinmap with a child that overides the parent
print(cm2['theme']) #returns the overidden theme  

print(cm2.pop('theme')) #returns and removes child theme value 

print(cm2['theme']) #returms the default theme 

cm2.maps[0] ={'theme':'desert','showIndex':False} # adds a 'root context' same as new_child
print(cm2['showIndex']) 
























































































