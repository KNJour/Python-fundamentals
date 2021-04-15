class SLNode {
	constructor(val){
		this.val = val;
        //pointet to next node
		this.next = null;
	}
}
class SLL {
    constructor(val){
        this.head = val;
    }
    addBack(val){
        var runner = this.head;
        while(runner.next) {
        runner = runner.next;
            }
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

     minToFront(){
         if(!this.head) return this;

         this.minNode = this.head;
         var runner = this.head;
         while(runner) {
             if (runner.val < this.minNode.val){
                 this.minNode = runner;
             }
             runner = runner.next
         }
         runner = this.head;
         while(runner){
             if(runner.next == this.minNode){
                 runner.next = this.minNode.nextthis.minNode.next = this.head;
                 this.head = this.minNode;
                 return this;
             }
         }
     }

    moveMaxToBack(){
        if(!this.head) return this;
        this.maxNode = this.head;
        var runner = this.head;
        
        while (runner){
            if(runner.val > this.maxNode.val){
                this.maxNode = runner;
            }
            runner = runner.next;
        }
        var prev = null;
        runner = this.head;
        while(runner){
            if(runner.next == this.maxNode){
                prev = runner;
            }
            if(!runner.next){
                break;
            }
            runner = runner.next;
        }
        prev.next = this.maxNode.next;
        runner.next = this.maxNode;
        this.maxNode.next = null;
        return this;
    }
//   moveMinToFront(){ //my attempt
//     console.log(this);
//     var runner = this.head;
//      var check = this.head;
//         while (runner.next) {
//             if (runner.val < check) {
//                 var check =  this.next.val
//             }
//             runner = runner.next;

//         }
    }
   
  }
var list = new SLL(4);
list.addBack(4);
list.addBack(8);
list.addBack(2);
list.moveMinToFront();

    // addFront(val){ //my attempt
    //     var node = new SLNode(val)
    //     if(this.head) {
    //      node.next = this.head;
    //      this.head = node;
    //      return this;
    //     } 
    //     this.head = node;
    //     return this;
    //  }

    // insertAt(element, index) {
    //     if (index < 0 || index  this.size)
    //         return console.log("please enter a valid index")
    // } else {
    //     var node = new SLNode(element)
    //     var curr, prev;
    //     curr = this.head;
    //     if (index == 0) {
    //         node.next = this.head;
    //         this.head = node;
    //     } else { 
    //         curr = this.head;
    //         var it = 0;

    //         while (it < index) {
    //             it++;
    //             prev = curr;
    //             curr = curr.next;
    //         }
    //         node.next = curr; 
    //         prev.
    //     }
//         }
//     }
// }
// basically is asking if there IS a runner and iterates through list. 

// var runner = this.head;
// while(runner.next) {
//     runner = runner.next;
    
// }
// //iterate to get to end of list
// function addBack(val){
//     var node = new SLNode(val)
//     if (this.head == null) {
//         this.head = node;
//         return this;
//     }
//     var runner = this.head;
//     while(runner.next) {
//         runner = runner.next;
//     }
//     runner.next = node; //adding to end of the list
//     return this; 
// }
// addFront(val)

// function printVals(){
//     var runner = this.head;
//     while(runner) {
//         console.log(runner.val);
//         runner = runner.next;
//     }
// }
// var list = new SLL();
// list.addback(4);
// list.addback(18);
// list.addback(24)

// printVals();

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

// //     currNode.next = new Node(data);
// }
// //create method to add a SLNode to the end of the list

