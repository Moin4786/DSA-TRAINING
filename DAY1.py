'''
#QUESTION: STACK CONCEPT


class Stack:
    def __init__(self,max_size):
        self.__max_size = max_size
        self._elements = [None] * self.__max_size
        self.__top = -1
        
    def is_full(self):
        if self.__top == self.__max_size - 1:
            return True
        return False
        
    def is_empty(self):
        if self.__top == -1:
            return True
        return False
        
    def push(self,data):
        if self.is_full():
            print("The stack is full !!")
        else:
            self.__top += 1
            self._elements[self.__top] = data
    
    def pop(self):
        if self.is_empty():
            print("The stack is empty !!")
        else:
            data = self._elements[self.__top]
            self.__top -= 1
            return data
    
    def display(self):
        if self.is_empty():
            print("The stack is empty !!")
        else:
            index = self.__top
            while index >= 0:
                print(self._elements[index])
                index -= 1
                
    def get_max_size(self):
        return self.__max_size

ball_stack = Stack(4)
print("Is it empty", ball_stack.is_empty())
ball_stack.push(5)
print("Is it empty", ball_stack.is_empty())
ball_stack.push(6)
ball_stack.push(7)
ball_stack.push(8)
ball_stack.display()
print("Size of the stack", ball_stack.get_max_size())
print("The element deleted", ball_stack.pop())
print("After deleting the element")
ball_stack.display()
print("Size of the stack", ball_stack.get_max_size())



#QUESTION= ENQUEUE AND DEQUEUE


class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.elements = [None] * self.max_size
        self._rear = -1
        self._front = 0

    def is_full(self):
        if self._rear == self.max_size - 1:
            return True
        return False
    
    def is_empty(self):
        if self._front > self._rear:
            return True
        return False
    
    def enqueue(self, data):
        if self.is_full():
            print("Queue is full!!!")
        else:
            self._rear += 1
            self.elements[self._rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!!!")
        else:
            data = self.elements[self._front]
            self._front += 1
            return data

    def display(self):
        for index in range(self._front, self._rear+1):
            print(self.elements[index])

    def get_max_size(self):
        return self.max_size

queue1 = Queue(10)

print("Is it full", queue1.is_full())
print("Is it empty", queue1.is_empty())

queue1.enqueue(100)
queue1.display()

queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.enqueue(500)
queue1.display()

print("Element deleted", queue1.dequeue())
queue1.display()'''



#QUESTION Given a queue of whole numbers. Write a python function to return a new queue which contains the evenly divisible numbers.

#Note: A number is said to be evenly divisible if it is divisible by all the numbers in the given range without any remainder. Consider the range to be from 1 to 10 (both

#inclusive).

#Assume that there will always be few elements in the input queue, which are evenly divisible by the numbers in the mentioned range.

#Example:Input Queue: 13983, 10080, 7113, 2520, 2500 (front rear) Output Queue: 10080, 2520 (front-rear)


def get_evenly_divisible_numbers(queue):
    divisible_queue = []
    for num in queue:
        if all(num % i == 0 for i in range(1, 11)):
            divisible_queue.append(num)
    return divisible_queue
input_queue = [13983, 10080, 7113, 2520, 2500]
output_queue = get_evenly_divisible_numbers(input_queue)
print(output_queue)


#4
#Given two lists, both having String elements, write a python program using python lists to create a new string as per the rule given below:
#The first element in list1 should be merged with last element in list2, second element in list1 should be merged with second last element in list2 and so on.
#If an element in list1 and list2 is None, then the corresponding element in the other list should be kept as it is in the merged list.

#Sample Input
#list1-['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
#list2-['y', 'tor', 'e', 'eps', 'ay', None, 'le', 'n']

#Expected Output
# "An apple a day keeps the doctor away"

list1 = ['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
list2 = ['y', 'tor', 'e', 'eps', 'ay', None, 'le', 'n']

new_list = []
for i in range(len(list1)):
    if list1[i] is None:
        new_list.append(list2[-(i+1)])
    elif list2[-(i+1)] is None:
        new_list.append(list1[i])
    else:
        new_list.append(list1[i] + list2[-(i+1)])

merged_str = ' '.join(new_list)
print(merged_str)



#5
#Given two queues, one integer queue and another character  queue, write a python program to merge them to form a single queue.
#Follow the below rules for merging: Merge elements at the same position starting with the integer queue.

#If one of the queues has more elements than the other, add all the additional elements at the end of the output queue.
#Note: max_size of the merged queue should be the sum of the size of both the queues. 1

#For example,
#Input --> queue: 3,6,8 queue2: b,y,u,t,r,o Output: [3, 'b', 6, 'y', 8, 'u', 't', 'r', 'o']

def merge_queues(queue1, queue2):
    len1 = len(queue1)
    len2 = len(queue2)
    merged_queue = []
    for i in range(min(len1, len2)):
        merged_queue.append(queue1[i])
        merged_queue.append(queue2[i])
    if len1 > len2:
        merged_queue += queue1[len2:]
    elif len2 > len1:
        merged_queue += queue2[len1:]
    return merged_queue
queue1 = [3, 6, 8]
queue2 = ['b', 'y', 'u', 't', 'r', 'o']
merged_queue = merge_queues(queue1, queue2)
print(merged_queue)




























