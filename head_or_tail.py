toss=input("reads the flipped coin was head or tail or stop:")
head_count=tail_count=0
while (toss!="stop"):
        if(toss=="head"):
           head_count=head_count+1
        elif(toss=="tail"):
           tail_count=tail_count+1
        toss=input("reads the flipped coin was head or tail or stop:")
print("quit")
print("the head count is:" + str(head_count))
print("the tail count is:" + str(tail_count))
perc_head=(head_count/(head_count+tail_count))*100
perc_tail=(tail_count/(head_count+tail_count))*100
print("the percentage of head & tail:" + str(int(perc_head)) +"% & " + str(int(perc_tail)) +"% .")




