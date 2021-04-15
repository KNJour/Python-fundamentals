class SLNode {
	constructor(val){
		this.val = val;
        //pointet to next node
		this.next = next;
	}
}

class SLL {
    constructor(){
        this.head = null;
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
    printVals(){
        var runner = this.head;
        var node = SLNode(val);
        while(runner) {
            console.log(runner.val);
            runner = runner.next;
        }
}
    prependVal(val,before){
        var new_node = new SLNode(val)
        if(!this.head){
            this.head = new_node;
            return this;
        }
        var runner = this.head;
        if(runner.val == before){
            new_node.next = runner;
            this.head = new_node;
            }
        while(runner.next.val != before){
            runner = runner.next
        }
        new_node.next = runner.next;
        runner.next = new_node;
        return this;
    }
}


var list = new SLL();

list.addBack(8);
list.addBack(6);
list.addBack(2);
list.addBack(4);
list.addBack(19);
list.prependVal(22, 2);
list.printVals();