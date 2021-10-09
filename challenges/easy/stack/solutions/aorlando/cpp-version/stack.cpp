#include <iostream>
#include <vector>
using namespace std;


class Stack 
{
    private:
    vector<int> myStack;

    public:

    void push(int item) {
        myStack.push_back(item);
    }

    int pop() {
        int x = 0;
        if(isEmpty()) {
            cout << "Stack is Empty." << endl;
            return -1;  //we have to reurn some value couse of the int function
        }
        else {
            x = myStack.size();
            myStack.pop_back();
            return myStack[x-1];
        }
    }

    int peek() {
        if(!isEmpty()) 
            return myStack.at(myStack.size() - 1);
        else 
            cout << "Stack is Empty." << endl;
            return -1;
    }

    bool isEmpty() {
        if(myStack.size() == 0)
            return true;
        else
            return false;
    }

    int size() {
        return myStack.size();
    }

    void display() {
        if (isEmpty())
            cout << "|None";
        cout << "|";
        for(int i = 0; i < myStack.size(); i++) {
            cout << myStack[i] << "|";
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
        cout << "5. size()" << endl;
        cout << "6. display()" << endl;
        

        cin >> option;

        switch(option) {
            case 0:
                break;

            case 1:
                cout << "*** Push Operation 1*** \nPlease enter an item to push in the Stack:"<<endl;
                cin >> item;
                test1.push(item);
                break;

            case 2:
                cout << "*** Pop Operation *** \nPop Value: " << test1.pop() <<endl;
                break;
            
            case 3:
                cout << "*** Peek Operation *** \nThe first item inserted in Stack is: " << test1.peek() <<endl;
                break;
            
            case 4:
                if(test1.isEmpty())
                    cout << "Stack is Empty." << endl;
                else
                    cout << "Stack is NOT Empty." << endl;
                break;
            
            case 5:
                cout << "*** Size Operation *** \nCount of items in Stack: " << test1.size() <<endl;
                break;
            
            case 6:
                cout << "*** Display Function Called *** \nAll items in the Stack are: ";
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