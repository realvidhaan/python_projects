queue = []  #defining an empty queue
front = 0  #making a variable front, that is equal to 0
rear = 0  #making a variable rear, that is equal to 0
size = int(input("Enter size of queue: ")
           )  # asking user for what the size of the queue should be

# Initialize the queue with None
queue = [None] * size


def addQ(item):  # defining a function that will add to queue
  global rear, size, front, queue  #making these variables global
  rear = (rear + 1) % size  #changing rear to be rear + 1 % size
  if front == rear:  #if front is equal to rear...
    print("Queue is full")  #...show that the queue is full
    if front == 0:  #if front is equal to 0...
      rear = size - 1  #...rear will be equal to size
    else:  #if not any of those cases...
      rear -= 1  #...rear is equal to rear minus 1
    return False  #then return the Boolean expression False
  else:  #if not any of those cases...
    queue[rear] = item #...the variable rear in queue is item
    print(f'Added: {item}') #showing the item that is added
    print(queue) #showing the queue
    return True  #then return the Boolean expression True


def deleteQ():
  global front, rear, size, queue
  if front == rear:
    print("Queue is empty")
    return False
  else:
    front = (front + 1) % size
    item = queue[front]
    queue[front] = None
    print(f'Deleted: {item}')
    print(queue)
    return True


def main():
  addQ(item=4)
  addQ(item=5)
  addQ(item=9)
  deleteQ()
  deleteQ()
  deleteQ()
  deleteQ()
  addQ(item=99)
  addQ(item=199)
  addQ(item=1199)
  addQ(item=399)

if __name__ == "__main__":
  main()
