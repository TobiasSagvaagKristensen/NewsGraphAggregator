from rdflib import Graph, XSD
import os
import threading
import time

knowledge_bank = 'knowledge_graph'

object_dict = {}
object_list = []
knowledge_path = []


def the_banker():
    global filename
    for filename in os.listdir(knowledge_bank):
        graphs = os.path.join(knowledge_bank, filename)
        if os.path.isfile(graphs):
            knowledge_path.append(graphs)
            the_handler()



def the_handler():
    global g
    if len(knowledge_path) > 0:
        g = knowledge_path[-1]
        g = Graph()
        g.parse(location=knowledge_path[-1], format="turtle")
        graph_shredder()


def graph_shredder():
    global g
    if len(knowledge_path) > 0:
        object_dict[knowledge_path[-1]] = []
        for subject, predicate, object in g:
            object_list.append(object[:])
        for num in object_list:
            object_dict[knowledge_path[-1]].append(num)
        knowledge_path.pop(-1)
        the_handler()

def main():
    if len(object_dict) == 0:
        the_banker()
    if len(knowledge_path) == 0:
        print('All graph are reddy for proses ')
        print(len(object_dict.keys()))



if __name__ == "__main__":
    main()

'''
 def main():
      thread = threading.Thread(target = graph_shredder())
      thread.start()
      thread.join()

      for x, y in object_dict.items():
           print(x,y)

 if name == 'main':
      main()


      object_list.append(object)



 object_list.sort()
 print(object_list[5])
 print(object_list)


 for x in object_list:
      print(x)



print(graph.serialize(format='turtle').decode('utf-8'))
#import threading
import time

g = Graph()


object_list = []

for subject,predicate,object in graph:
     object_list.append(object)


object_list.sort()
print(object_list[5])
print(object_list)


# for x in object_list:
#      print(x)








#print(graph.serialize(format='turtle').decode('utf-8'))





Dette vil vi ha ut 'https://twitter.com/i/status/1310747766067527686,
 http://dbpedia.org/resource/Coronavirus, https://www.wikidata.org/entity/Q918


'''
