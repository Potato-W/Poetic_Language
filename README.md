# Poetic_Language

This project，something about NLP and front-end. As the repository name, this project try to analyze the feelings behind the poem, based on The Whole Tang Poetry. 

![image](https://github.com/changshunwang/Poetic_Language/blob/master/title.jpg)

## Forward-looking work

At first, I do a samll experimental work with some skills maybe used in later. This work, which is originated from an accidental inspiration, randomly grabbed a song list from WangYi Music, analyzing the lyrics of all songs from the list to get hidden information. Then, to visualize the result，I make a word-cloud picture using Pypackge--wordcloud.

You can find the code and result in folder /wangyi.

skills:
 1. jieba is a tool for word segmentation. 
 2. wordcloud to visualize the result.
 
It's first but a good attempt for me. If I want to do simple project I can finish now, because maybe it's enough; but if more challange I want, I must try more difficult thing.

## Architecture
![image](https://github.com/changshunwang/Poetic_Language/blob/master/architecture.jpg)
 
## Participle （Chinese word segmentation）


Word segmentation is the foundation of NLP, whether later it is to do emotional analysis or content understanding or anything else. So, a good beginning is half the battle.

Modern Chinese word segmentation is a huge challange, not to motion Middle Chinese. The meaning of a word(字) forming a phrase （词）maybe different from that of a word. 
There is my strategy is as follows:
 1. first, participle with jieba to have most words.
 2. second, using branch entropy to get unregistered words, which are more common in Tang Poem, rather than modern Chinese.
 
About these two methods, I will do a detailed explanation in Wiki-Participle.
 
It's really cooooool, I get single word mostly with method1, which are also common in modern Chinese. However, some meaningful phrases, including need to imagine or have historical culture found with method2. So, now, I have a rich thesaurus.

## Result

![image](https://github.com/changshunwang/Poetic_Language/blob/master/result.jpg)

## Postscript

Time flies, I have graduated nearly 1 year. I saw the scene about the last period of my university as soon as I see this project. To be honest, it is not the best project in my undergraduate stage, but it contains too much memory. 

I was thinking for a long time, 
Should I select this topic as my project? 
Should I use these called hi-tech(i.e. Machine Learing, NLP) try to understand the poem, especially Tang Poem?
Should I expect the machine can real understand pepople?

Actualy, I doubt whether I do the right thing. For now, I think it is not the right. I am not mean this project is not valuable. It does have value, we can use it to find the inheritance relationship between poets, we can better understand the evolation about Poem. No one can remember 100000+ poems, but the machine can, ALthough it can't understand it can get information. In this side, Sensible things also have a rational relationship.

BUT tech can make our life better, in sooooo many feilds, not only in this rhetoric direction.


