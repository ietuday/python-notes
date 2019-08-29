from queue import queue

question_queue = queue()

for x in range(1,10):
    temp_dict = ('key', x)
    question_queue.put(temp_dict)
while(not question_queue.empty()):
    item = question_queue.get()
    print(str(item))