# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

"""Modify the directories according to your directory. """
File=['E:\\SE\\task6\\T6SB\\T6SB.txt'
		]

Result_File=['E:\\SE\\task6\\T6SB\\T6SB_stance.pos',
             'E:\\SE\\T6SB\\T6SB_stance.neg'
			]

if __name__=="__main__":
    for i in range(1):
        File[i]=unicode(File[i],'utf8')
        f_pos = open(unicode(Result_File[0],'utf8'),"wb")
        f_neg = open(unicode(Result_File[1],'utf8'),"wb")
        with open(File[i],"rb") as f:
            for line in f:
                tmp = line.lower()
                if tmp.find("idiot")!=-1 or tmp.find("fired")!=-1 or tmp.find("shit")!=-1 or tmp.find("fucdonaldtrump")!=-1 or tmp.find("bullshit")!=-1:
                    f_neg.write(line)
                if tmp.find("go trump")!=-1 or tmp.find("trump go")!=-1 or line.find("MakeAmericaGreatAgain")!=-1:
                    f_pos.write(line)
	f_pos.close()
    f_neg.close()
    f.close()

	
		
	
	
	
	
