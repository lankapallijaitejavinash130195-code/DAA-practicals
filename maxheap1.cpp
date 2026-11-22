#include <iostream>
using namespace std;

// This function makes sure one part of the array follows the max-heap rule
// every parent must be bigger than its children.
// "i" is the index we are checking -> treating it as the parent
void heapify(int arr[], int size, int i) {
    int largest = i;          // Assuming the current node is the largest --> O(1)
    int left = 2 * i + 1;     // Formula to find the left child     --> O(1)
    int right = 2 * i + 2;    // Formula to find the right child    --> O(1)

    //  Comparing parent with left child
    if (left < size && arr[left] > arr[largest]) {
        largest = left;       // Left child is bigger, so update "largest"
    }

    //  Comparing current largest with right child
    if (right < size && arr[right] > arr[largest]) {
        largest = right;      // Right child is bigger, so update "largest"
    }

    //  If the parent was NOT the largest, swap and keep fixing below
    if (largest != i) {                                                // --> O(1)
        swap(arr[i], arr[largest]);   // Move the bigger value up
        heapify(arr, size, largest);  // Recursively fix the  subtree
    }
}

//  function turns the WHOLE array into a valid max-heap.
// start from the last parent node and heapify backwards to the root.
void buildMaxHeap(int arr[], int size) {            // --> O(1)
    int lastParent = size / 2 - 1;   // Index of the last non-leaf node. --> n/2 iterations

    for (int i = lastParent; i >= 0; i--) {
        heapify(arr, size, i);
    }
}

//  main sorting function.
void heapSort(int arr[], int size) {
    //   a max-heap so the biggest number is at the top 
    buildMaxHeap(arr, size);

    // Repeatedly take the biggest number out and place it at the end
    for (int end = size - 1; end > 0; end--) {              // n-1 iterations
        swap(arr[0], arr[end]);   // Moving current biggest to its correct final spot. --> O(1)
        heapify(arr, end, 0);     // Fixing the heap for the remaining  array
    }
}

//  print the array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int size = sizeof(arr) / sizeof(arr[0]);

    cout << "Before sorting: ";
    printArray(arr, size);

    heapSort(arr, size);

    cout << "After sorting:  ";
    printArray(arr, size);

    return 0;
}

// T(n) = T(n/2) + O(1) (Recurrence Relation)