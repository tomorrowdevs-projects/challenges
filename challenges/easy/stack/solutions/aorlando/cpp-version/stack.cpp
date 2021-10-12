#include <iostream>
#include <vector>
using namespace std;


class Stack {

    private:
    vector<int> myStack;

    public:

    void push(int item) {
        myStack.push_back(item);
    }

    int pop() {
        int x = myStack.size();
        myStack.pop_back();
        return myStack[x-1];
    }

    int peek() {
        return myStack.at(myStack.size() - 1);
    }

    bool isEmpty() {
        return myStack.size() == 0;
    }

    int size() {
        return myStack.size();
    }

    vector<int> display() {
        return myStack;
    }
};


int main() {
    Stack test1;
    int option, item;
    vector<int> stack;

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
                cout << "*** Push Operation 1***\nPlease enter an item to push in the Stack:"<<endl;
                cin >> item;
                test1.push(item);
                break;

            case 2:
                if(test1.isEmpty())
                    cout << "Stack is Empty." << endl;
                else
                    cout << "*** Pop Operation ***\nPop item: " << test1.pop() <<endl;
                break;
            
            case 3:
                if(test1.isEmpty())
                    cout << "Stack is Empty." << endl;
                else
                    cout << "*** Peek Operation ***\nThe last item inserted in Stack is: " << test1.peek() <<endl;
                break;
            
            case 4:
                if(test1.isEmpty())
                    cout << "Stack is Empty." << endl;
                else
                    cout << "Stack is NOT Empty." << endl;
                break;
            
            case 5:
                cout << "*** Size Operation ***\nCount of items in Stack: " << test1.size() <<endl;
                break;
            
            case 6:
                if(test1.isEmpty())
                    cout << "Stack is Empty." << endl;
                else {
                    cout << "*** Display Function Called ***\nAll items in the Stack are: ";
                    stack = test1.display();
                    cout << "|";
                    for(int i = 0; i < stack.size(); i++) {
                        cout << stack[i] << "|";
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