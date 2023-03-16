from multiprocessing import Process
import time

start = time.perf_counter()

def bubble_sort(array):
    check = True
    while check == True:
      check = False
      for i in range(0, len(array)-1):
        if array[i] > array[i+1]:
          check = True
          temp = array[i]
          array[i] = array[i+1]
          array[i+1] = temp
    print("Array sorted: ", array)

if __name__ == '__main__':
    p1 = Process(target=bubble_sort, args=([1,9,4,5,2,6,8,4],))
    p2 = Process(target=bubble_sort, args=([2,6,56,3,8,52,0],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

end = time.process_time()

print(f'Time spent {start-end}')