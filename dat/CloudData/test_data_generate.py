
test_origin = 'E:\\Projects\\crf4j-master\\src\\main\\resources\\example\\ToyExample\\business-add_favorite_test_raw.txt'
output = 'E:\\Projects\\crf4j-master\\src\\main\\resources\\example\\ToyExample\\business-add_favorite_test.txt'
with open(test_origin,'r',encoding="utf-8") as f, open(output, 'w', encoding="utf-8") as f1:
    file = f.readlines()
    for line in file:
        line = line.rstrip()
        query = ''.join(line.split('###')[0].split())
        tags = line.rstrip('#').split('###')[1].split('##')
        label = ['O' for i in range(len(query))]
        for i in range(int(len(tags) / 2)):
            tag = ''.join(tags[2 * i + 1].split())
            start = query.find(tag)
            label[start] = 'B-' + tags[2*i]
            label[start+1:start+len(tag)] = ['I-' + tags[2*i]]*(len(tag)-1)
            for j in range(len(query)):
                f1.writelines("{} {}".format(query[j], label[j])+'\n')
            f1.writelines('\n')
        # line = line.rstrip()
        # query = ''.join(line.split('###')[0].split())
        # tags = line.rstrip('#').split('###')[1].split('##')
        # dict_tag = {}
        # for i in range(int(len(tags)/2)):
        #     tag = tags[2*i+1].split()
        #     for j in range(len(tag)):
        #         if j==0:
        #             dict_tag[tag[j]] = 'B-'+tags[2*i]
        #         else:
        #             dict_tag[tag[j]] = 'I-'+tags[2*i]
        # with open(output, 'a',encoding="utf-8") as f1:
        #     for x in query:
        #         if x in dict_tag:
        #             line1 = x+' '+dict_tag[x]
        #             f1.writelines(line1+'\n')
        #         else:
        #             line1 = x+' O'
        #             f1.writelines(line1 + '\n')
        #     f1.writelines('\n')


