def bubble_sort(arr):
    n = len(arr)
  
    for i in range(n):
      
        for j in range(0, n-i-1):
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
  
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
if __name__ == "__main__":
    arr_bubble = [20, 3, 15, 7, 9, 12, 18, 5, 1, 25, 8, 16, 14, 6, 11]
    arr_insertion = [20, 3, 15, 7, 9, 12, 18, 5, 1, 25, 8, 16, 14, 6, 11]

    bubble_sort(arr_bubble)
    print("Arreglo ordenado por Bubble Sort:", arr_bubble)

    insertion_sort(arr_insertion)
    print("Arreglo ordenado por Insertion Sort:",arr_insertion)