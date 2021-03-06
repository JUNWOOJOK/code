for i in $(ls|grep gdc);do cd $i;less colon_genecatalogue.sam |grep -v "^@"|cut -f 3|grep -v "*"|sort|uniq -c|awk 'BEGIN{OFS="\t"}{print $2,$1}' > read_count;cd ..;done#
import numpy as np
import pandas as pd
from tqdm import tqdm
import sys
input_file=sys.argv[1]
cluster_name=[]
my_list=[]
my_dict={}
with open(input_file) as file:
    for i in file:
        mapped_gene=i.split("\t")[0]
        read_count=i.split("\t")[1]
        my_dict[mapped_gene.strip()]=read_count.strip()

with open('/media/junwoojo/62aa5c79-9b02-4538-a8c9-4ce80ad6013b/TCGA/tumor/header') as file:
    for i in file:
        my_list.append(i.strip())

#print(my_list)
#print(my_dict)

k=np.zeros(len(my_list),int)
input_file=input_file.strip('.d/read_count').strip('.bam')
zz=pd.DataFrame(k,index=np.array(my_list),columns=[input_file])
rows=zz.index
for i in my_dict.items():
    gene=i[0].strip()
    count=i[1].strip()
    rn=rows.get_loc(gene)
    zz.iloc[rn,0]=int(count)

zz.to_csv(f'{input_file}.csv')
