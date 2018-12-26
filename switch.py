# this program was written to replicate the Monty Python problem - it was really not intuitive when I initially heard the answer.

import random
# change the key of the rng every time this function is called

ctr_ch, ctr_noch = 0, 0

for _ in range(100000):
	type = ['cgg','gcg','ggc']

	ques = type[random.randint(0,2)]
	print("Q: ", ques)
	# ggc

	fp = random.randint(0,2)
	print("fp: ", fp)
	# 1

	new_q = list(set(range(0,3)).difference({fp}))
	# 0, 2

	if ques[new_q[0]]=='g' and ques[new_q[1]]=='g':
		sp = random.choice(new_q)
	else:
		for ind in new_q:
			if ques[ind]=='g':
				sp = ind

	print("ann pick: ", sp)
	# 0

	tp_change = list(set(new_q).difference({sp}))
	# 2

	tp_nochange = fp
	# 1

	if ques[tp_change[0]]=='c':
		print("Change helped")
		ctr_ch += 1

	if ques[tp_nochange]=='c':
		print("Change did not help")
		ctr_noch += 1

	print("########")

tot = ctr_noch + ctr_ch
print("No change helped: ", ctr_noch/tot) # approximates to 0.3333
print("Change helped: ", ctr_ch/tot) # approximates to 0.66666
