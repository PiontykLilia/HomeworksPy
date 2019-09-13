Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Записати в стрічку філософію Пайтона
#Знайти в заданій стрічці кількість входжень слів (better, never, is)
#Вивести весь текст у верхньому регістрі (всі великі літери)
#Замінити всі входження символу “і” на “&”


>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> z="The Zen of Python, by Tim Peters Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"
>>> type(z)
<class 'str'>
>>> z.count('better')
8
>>> z.count('never')
3
>>> z.count('is')
10
>>> z.upper()
"THE ZEN OF PYTHON, BY TIM PETERS BEAUTIFUL IS BETTER THAN UGLY. EXPLICIT IS BETTER THAN IMPLICIT. SIMPLE IS BETTER THAN COMPLEX. COMPLEX IS BETTER THAN COMPLICATED. FLAT IS BETTER THAN NESTED. SPARSE IS BETTER THAN DENSE. READABILITY COUNTS. SPECIAL CASES AREN'T SPECIAL ENOUGH TO BREAK THE RULES. ALTHOUGH PRACTICALITY BEATS PURITY. ERRORS SHOULD NEVER PASS SILENTLY. UNLESS EXPLICITLY SILENCED. IN THE FACE OF AMBIGUITY, REFUSE THE TEMPTATION TO GUESS. THERE SHOULD BE ONE-- AND PREFERABLY ONLY ONE --OBVIOUS WAY TO DO IT. ALTHOUGH THAT WAY MAY NOT BE OBVIOUS AT FIRST UNLESS YOU'RE DUTCH. NOW IS BETTER THAN NEVER. ALTHOUGH NEVER IS OFTEN BETTER THAN *RIGHT* NOW. IF THE IMPLEMENTATION IS HARD TO EXPLAIN, IT'S A BAD IDEA. IF THE IMPLEMENTATION IS EASY TO EXPLAIN, IT MAY BE A GOOD IDEA. NAMESPACES ARE ONE HONKING GREAT IDEA -- LET'S DO MORE OF THOSE!"
>>> z.replace('i','&')
"The Zen of Python, by T&m Peters Beaut&ful &s better than ugly. Expl&c&t &s better than &mpl&c&t. S&mple &s better than complex. Complex &s better than compl&cated. Flat &s better than nested. Sparse &s better than dense. Readab&l&ty counts. Spec&al cases aren't spec&al enough to break the rules. Although pract&cal&ty beats pur&ty. Errors should never pass s&lently. Unless expl&c&tly s&lenced. In the face of amb&gu&ty, refuse the temptat&on to guess. There should be one-- and preferably only one --obv&ous way to do &t. Although that way may not be obv&ous at f&rst unless you're Dutch. Now &s better than never. Although never &s often better than *r&ght* now. If the &mplementat&on &s hard to expla&n, &t's a bad &dea. If the &mplementat&on &s easy to expla&n, &t may be a good &dea. Namespaces are one honk&ng great &dea -- let's do more of those!"
>>>
