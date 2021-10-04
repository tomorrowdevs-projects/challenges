#include <iostream>
#include <string>

using namespace std;


class Stack {
    private:
    int top;
    int arr[5];

    public:
    // constructor
    Stack() {
        top = -1;
        for(int i=0; i<5; i++) {
            arr[i] = 0;
        }
    }

    void push(int item) {
        if(isFull()) {
            cout<<"Stack is FULL."<<endl;
        }
        else {
            top++;
            arr[top] = item;
        }
    }

     int pop() {
        if(isEmpty()) {
            cout<<"Stack is EMPTY."<<endl;
            return 0;  // I must return some value couse of the int function
        }
        else {
            int popItem = arr[top];
            arr[top] = 0;  // Replace the top value with a 0 placeholder
            top--;
            return popItem;
        }
    }

    int peek() {
        if(isEmpty()) {
            cout<<"Stack is EMPTY."<<endl;
            return 0;
        }
        else {
            return arr[top];
        }
    }

    bool isEmpty() {
        if(top==-1) 
            return true;
        else
            return false;
    }

    bool isFull() {
        if (top==4)
            return true;
        else
            return false;
    }

    int size() {
        return (top+1);
    }

    void display() {
        cout<<"All items in the Stack are: "<<endl;
        for(int i=4; i>=0; i--) {  // in order to display it in the stack manner
            cout<<arr[i]<<endl;
        }
    }
};


int main() {

    Stack test1;
    int option, item;

    do {
        cout << "\n\nWhat operation do you want to perform? Select Option number (0 to exit)." << endl;
        cout << "1. push(item)" << endl;
        cout << "2. pop()" << endl;
        cout << "3. peek()" << endl;
        cout << "4. isEmpty()" << endl;
        cout << "5. isFull()" << endl;
        cout << "6. size()" << endl;
        cout << "7. display()" << endl;
        

        cin >> option;

        switch(option) {
            case 0:
                break;

            case 1:
                cout << "*** Push Operation 1*** \nPlease enter an item you want to Stack:"<<endl;
                cin >> item;
                test1.push(item);
                break;

            case 2:
                cout << "*** Pop Operation *** \nPop Value: " << test1.pop() <<endl;
                break;
            
            case 3:
                cout << "*** Peek Operation *** \nThe last item inserted is: " << test1.peek() <<endl;
                break;
            
            case 4:
                if(test1.isEmpty())
                    cout << "Stack is Empty." << endl;
                else
                    cout << "Stack is NOT Empty." << endl;
                break;

            case 5:
                if(test1.isFull())
                    cout << "Stack is Full." << endl;
                else
                    cout << "Stack is NOT Full." << endl;
                break;
            
            case 6:
                cout << "*** Size Operation *** \nCount of items in Stack is: " << test1.size() <<endl;
                break;
            
            case 7:
                cout << "*** Display Function Called *** \nAll values in the Stack are: ";
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
