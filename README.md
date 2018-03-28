# Poetic_Language

This is my graduation project，something about NLP and front-end. As the repository name, this project try to analyze the feelings behind the poem, based on The Whole Tang Poetry. 

## Forward-looking work

At first, I do a samll experimental work with some skills maybe used in later. This work, which is originated from an accidental inspiration, randomly grabbed a song list from WangYi Music, analyzing the lyrics of all songs from the list to get hidden information. Then, to visualize the result，I make a word-cloud picture using Pypackge--wordcloud.

You can find the code and result in folder /wangyi.

skills:
 1. jieba is a tool for word segmentation. 
 2. wordcloud to visualize the result.
 
It's first but a good attempt for me. If I want to do simple project I can finish now, because maybe it's enough; but if more challange I want, I must try more difficult thing.
 
## Participle （Chinese word segmentation）

Word segmentation is the foundation of NLP, whether later it is to do emotional analysis or content understanding or anything else. So, a good beginning is half the battle.

Modern Chinese word segmentation is a huge challange, not to motion Middle Chinese. The meaning of a word(字) forming a phrase （词）maybe different from that of a word. 
There is my strategy is as follows:
 1. first, participle with jieba to have most words.
 2. second, using informationentropy to get unregistered words, which are more common in Tang Poem, rather than modern Chinese.
 
About these two methods, I will do a detailed explanation in Wiki-Participle
