7.19 打卡

# LC 24 两两交换链表中的节点

题目：给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
**注意**：你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例：

```c++
给定 1->2->3->4, 你应该返回 2->1->4->3.
```

思路：双指针，一前一后进行移动。注意的是遍历整个链表的指针是不能改变的

具体代码是：

```c++
    ListNode* swapPairs(ListNode* head) {
        if(head==NULL || head->next==NULL)
            return head;
        
        //记录交换后的表头
        ListNode* newhead=new ListNode(-1);
        newhead->next=head;
        
        //方便移动指针进行交换
        ListNode* cur_pos=newhead;
        while(cur_pos->next && cur_pos->next->next){
            //为了不改变移动指针
            ListNode* pos_1=cur_pos->next;
            ListNode* pos_2=cur_pos->next->next;

            //进行交换的具体操作
            cur_pos->next=pos_2;
            pos_1->next=pos_2->next;
            pos_2->next=pos_1;

            //指针的移动，注意是两步
            cur_pos=cur_pos->next->next;
        }
    return newhead->next;
    }
```