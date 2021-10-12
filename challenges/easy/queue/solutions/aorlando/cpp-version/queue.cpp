#include <iostream>
#include <vector>
using namespace std;

class Queue 
{
    private:
    vector<int> myQueue;

    public:

    void enqueue(int item) {
        myQueue.push_back(item);
    }

    int dequeue() {
        int x = myQueue.at(0);
        myQueue.erase(myQueue.begin()); 
        return x;
    }

    int peek() {
        return myQueue.at(0);
    }

    bool isEmpty() {
        return myQueue.size() == 0;
    }

    int size() {
        return myQueue.size();
    }

    vector<int> display() {
        return myQueue;
    }
};


int main() {
    Queue test1;
    int option, item;
    vector<int> queue;

    do {
        cout << "\n\nWhat operation do you want to perform? Select Option number (0 to exit)." << endl;
        cout << "1. enqueue(item)" << endl;
        cout << "2. dequeue()" << endl;
        cout << "3. peek()" << endl;
        cout << "4. isEmpty()" << endl;
        cout << "5. size()" << endl;
        cout << "6. display()" << endl;
        

        cin >> option;

        switch(option) {
            case 0:
                break;

            case 1:
                cout << "*** Enqueue Operation *** \nPlease add an item to Queue:"<<endl;
                cin >> item;
                test1.enqueue(item);
                break;

            case 2:
                if(test1.isEmpty())
                    cout << "Queue is Empty" << endl;
                else
                    cout << "*** Dequeue Operation ***\nDequeued item: " << test1.dequeue() <<endl;
                break;
            
            case 3:
                if(test1.isEmpty())
                    cout << "Queue is Empty" << endl;
                else
                    cout << "*** Peek Operation ***\nThe first item inserted in Queue is: " << test1.peek() <<endl;
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
                if(test1.isEmpty())
                    cout << "Queue is Empty" << endl;
                else {
                    cout << "*** Display Function Called *** \nAll items in the Queue are: ";
                    queue = test1.display();
                    cout << "|";
                    for(int i = 0; i < queue.size(); i++) {
                        cout << queue[i] << "|";
                    }
                }
                break;
            
            default:
                cout << "Please enter a valid option number. " << endl;
                break;
        }
    }
    while(option!=0);

    return 0;
}