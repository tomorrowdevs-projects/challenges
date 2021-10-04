#include <iostream>
using namespace std;

class Queue {
    private:
    int front;
    int rear;
    int arr[5];
    int itemCount;

    public:
    // constructor
    Queue() {
        int itemCount = 0;
        front = -1;
        rear = -1;
        for(int i=0; i<5; i++) {
            arr[i]=0;
        }
    }

    void enqueue(int item) {
        if(isFull()) {
            cout << "Queue is FULL" << endl;
            return;
        }
        else if(isEmpty()) {
            rear=0;
            front=0;
            arr[rear]=item;
        }
        else {
            /* e.g. 
            Assume we have added an element in our array that have at least one element already:
            rear == 0
            rear + 1 == 1
            1 % 5 == 1, so rear become == 1
            then put the new element in the position 1 of our array

            enqueue() again:
            rear == 1
            rear + 1 == 2
            2 % 5 == 2, so rear become == 2
            then put the new element in the position 2 of our array

            Let's say that we have 5 elements [5 4 3 2 1] in our array so the queue is full.
            In according to the algorithm, rear is == to 4
            If we dequeue(), the first element removed is 5
            then enqueue() the element 6:
            rear == 4
            rear + 1 == 5
            5 % 5 == 0, so rear become == 0
            then put the new element in the position 0 of our array
            (see dequeue() method to understand the logic for that process) 
        */
            rear = (rear+1)%5;
            arr[rear]=item;
            
        }
        itemCount++;
    }

    int dequeue() {
        int x = 0;
        if(isEmpty()) {
            cout << "Queue is EMPTY" << endl;
            return -1;  //we have to reurn some value couse of the int function
        }
        else if(front == rear) {
            /* 
            the only chance that could happen is when the arrey has only one element
            so front and rear come back to the initial situation --> front = rear = -1 
            */
            x = arr[front];  // I put the value wich I have to return at the variable x
            arr[front] = 0;  // I replace the value with a 0
            front = -1;
            rear = -1;
            itemCount--;
            return x;
        }
        else {
            /* e.g. 
            Assume we have at least two elements in the array [5 4]:
            front == 0
            x = arr[0] --> 5
            raplace arr[front] with 0 as a placeholder

            (front+1)%5 == 1
            then front become == 1 
            in that case, front = rear = 1. So if we dequeue() again, the second condition run

            dequeue() an array with 3 elements [5 4 3]:
            front == 0
            x = arr[0] --> 5
            raplace arr[front] with 0 as a placeholder

            (front+1)%5 == 1
            then front become == 1 
            in that case, front = 1 and rear = 2. So if we dequeue() again, the third condition run again
            
        */
            x = arr[front];
            arr[front] = 0;
            front = (front+1)%5;
            itemCount--;
            return x;
        }
    }

    int peek() {
        if(!isEmpty()) {
            return arr[front];
        }
    }

    bool isEmpty() {
        if(front==-1 && rear==-1)
            return true;
        else
            return false;
    }

    int size() {
        return itemCount;
    }

    bool isFull() {
        /* e.g. 
            Assume we have our array full of elements [5 4 3 2 1]:
            front == 0
            rear == 4
            rear + 1 == 5
            5 % 5 == 0
            so (rear+1)%5 == front and then the queue is full and the condition is true

            if we dequeue() one element:
            front == 1  // (see the dequeue() logic)
            rear == 4  // it remains the same as before till we enqueue() a new element
            rear + 1 == 5
            5 % 5 == 0
            so (rear+1)%5 != front and then the queue is not full and the condition is false
        */
        if((rear+1)%5 == front)
            return true;
        else
            return false;
    }

    void display() {
        for(int i=0; i<5; i++) {
            cout << arr[i] << " ";
        }
    }

};


int main() {

    Queue test1;
    int option, item;

    do {
        cout << "\n\nWhat operation do you want to perform? Select Option number (0 to exit)." << endl;
        cout << "1. enqueue(item)" << endl;
        cout << "2. dequeue()" << endl;
        cout << "3. peek()" << endl;
        cout << "4. isEmpty()" << endl;
        cout << "5. size()" << endl;
        cout << "6. isFull()" << endl;
        cout << "7. display()" << endl;
        

        cin >> option;

        switch(option) {
            case 0:
                break;

            case 1:
                cout << "*** Enqueue Operation 1*** \nPlease enter an item to Enqueue in the Queue:"<<endl;
                cin >> item;
                test1.enqueue(item);
                break;

            case 2:
                cout << "*** Dequeue Operation *** \nDequeued Value: " << test1.dequeue() <<endl;
                break;
            
            case 3:
                cout << "*** Peek Operation *** \nThe first item is: " << test1.peek() <<endl;
                break;
            
            case 4:
                if(test1.isEmpty())
                    cout << "Queue is Empty." << endl;
                else
                    cout << "Queue is NOT Empty." << endl;
                break;
            
            case 5:
                cout << "*** Size Operation *** \nCount of items in Queue: " << test1.size() <<endl;
                break;
            
            case 6:
                if(test1.isFull())
                    cout << "Queue is Full." << endl;
                else
                    cout << "Queue is NOT Full." << endl;
                break;
            
            case 7:
                cout << "*** Display Function Called *** \nAll values in the Queue are: ";
                test1.display();
                break;
            
            default:
                cout << "Please enter a valid option number. " << endl;
                break;
        }
    }
    while(option!=0);

    return 0;
}