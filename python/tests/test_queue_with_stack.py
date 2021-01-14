import pytest
from code_challenges.queue_with_stacks.queue_with_stacks import InvalidOperationError,Node,Stack,PseudoQueue


def test_enqueue():
     pq = PseudoQueue()
     pq.stack_one.push(3)
     pq.stack_one.push(4)
     pq.stack_one.push(5)

     actual = str(pq.stack_one)
     expected = 'Null <- 5  <- 4  <- 3 '
     assert actual == expected

     pq.enqueue(6,pq.stack_one)

     actual = str(pq.stack_one)
     expected = 'Null <- 6  <- 5  <- 4  <- 3 '
     assert actual == expected



def test_dequeue():
    pq = PseudoQueue()
    pq.stack_one.push(3)
    pq.stack_one.push(4)
    pq.stack_one.push(5)

    actual = pq.dequeue(pq.stack_one)
    expected = 3

    assert expected == actual

    actual = str(pq.stack_one)
    expected = 'Null <- 5  <- 4 ' 
    
    assert expected == actual

    
  
