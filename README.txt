This project is for SemEval-16 Task6 subtaskA and subtaskB.
(paper link here.)
Description of these two tasks can be found here: http://alt.qcri.org/semeval2016/task6/ 

Note that code for subtaskB is almost the same as subtaskA, with slight difference between conv_net_classes.py and conv_net_sentence.py, since the probability distribution after sofemax layer should go through a threshold to perform 3-class classification.

Description of the project is as below:

1. Requirements:
	Code is written in Python (2.7) and requires Theano (0.7).
	We only use the CPU version. If you would like to run this project on GPU, please have a look at https://github.com/yoonkim/CNN_sentence , which this project is based on.

2. Code description:
	SE16-T6SA/process4T6SA.py and SE16-T6SB/process_T6SB_4label.py:
		Goal:
			Simple process on the original dataset provided by SE16-Task6 organizers to generate proper input files for preprocessing.
		Output files:
			For subtaskA, there are three output files - T6SA_stance.pos, T6SA_stance.neg and T6SA_stance.none. 
			For subtaskB, there are two output files - T6SB_stance.pos and T6SB_stance.neg.
			Sentences inside the original dataset are separated into different suffix files according to their stance.

	SE16-T6SA/T6SA_process_data.py and SE16-T6SB/T6SB_process_data.py:
		Goal:
			Data preprocessing and word index vocabulary building.

	SE16-T6SA/T6SA_conv_net_sentence.py and SE16-T6SB/T6SB_conv_net_sentence.py:
		Goal:
			Modify from sample code of paper Convolutional Neural Networks for Sentence Classification (http://arxiv.org/pdf/1408.5882v2.pdf)
			Training here.

	SE16-T6SA/conv_net_classes.py and SE16-T6SB/T6SB_conv_net_classes.py:
		Goal:
			Modify from sample code of paper Convolutional Neural Networks for Sentence Classification (http://arxiv.org/pdf/1408.5882v2.pdf)
			Provide theano specific neural network classes.
		
PS: Due to the tight schedule, this README is somewhat curt. If you have any question, feel free to connect with me: wanw at pku.edu.cn
		
	