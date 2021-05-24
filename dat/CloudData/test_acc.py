test_result = 'E:\\Projects\\crf4j-master\\src\\main\\resources\\example\\ToyExample\\test_result.txt'
output = 'E:\\Projects\\crf4j-master\\src\\main\\resources\\example\\ToyExample\\test_acc.txt'
word_num = 0
sentence_num = 0
right_word = 0
wrong_sentence = 0
list1 = []
list2 = []
list3 = []
indicator = 0#用于记录这句话是否全部预测正确
with open(test_result,'r',encoding="utf-8") as f:
    file = f.readlines()
    for line in file:
        if line[0] == '\n':
            sentence_num +=1
            if indicator == 1:
                wrong_sentence += 1
                with open(output, 'a', encoding="utf-8") as f1:
                    for i in range(len(list1)):
                        f1.writelines("{} {} {}".format(list1[i], list2[i], list3[i])+'\n')
                    f1.writelines('\n')
            list1 = []
            list2 = []
            list3 = []
            indicator = 0
        else:
            line = line.rstrip()
            word_num +=1
            line_list = line.split('\t')
            list1.append(line_list[0])
            list2.append(line_list[1])
            list3.append(line_list[2])
            if line_list[1] == line_list[2]:
                right_word += 1
            else:
                indicator = 1
with open(output, 'a', encoding="utf-8") as f1:
    f1.writelines("word acc:{}".format(right_word/word_num)+'\n')
    f1.writelines("sentence acc:{}".format(1-wrong_sentence/sentence_num) + '\n')