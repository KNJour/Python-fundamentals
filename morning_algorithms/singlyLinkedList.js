class SLNode{
	constructor(val){
		this.val = val;
        //pointet to next node
		this.next = null;
	}
}

class SLL {
    constructor(){
        this.head = null;
    }
}
// basically is asking if there IS a runner and iterates through list. 

var runner = this.head;
while(runner.next) {
    runner = runner.next;
}
//iterate to get to end of list
function addBack(val){
    var node = new SLNode(val)
    if (this.head == null) {
        this.head = node;
        return this;
    }
    var runner = this.head;
    while(runner.next) {
        runner = runner.next;
    }
    runner.next = node; //adding to end of the list
    return this; 
}

function printVals(){
    var runner = this.head;
    while(runner) {
        console.log(runner.val);
        runner = runner.next;
    }
}
var list = new SLL();

list.addback(4);
list.addback(18);
list.addback(24)

printVals();

// export default class Node {
//     constructor (data, next = null) {
//         this.data = data;
//         this.next - next;
//     }
// }

// export default class LinkedList {
//     constructor() {
//         this.length - 0;
//         this.head = null;
//     }
// }

// push(data) {
//     this.length++;

//     if (!this.head) {
//         this.head = new Node(date);
//     } else {
//         let currNode = this.head;
//     }

//     while (currNode.next) {
//         currNode = currNode.next;
//     }

//     currNode.next = new Node(data);
}
//create method to add a SLNode to the end of the list

