---
layout: page
title: 자연어 처리 - 텍스트
---

> ### AI is a Superpower {.callout}
>
> "AI is a superpower!!!", 인공지능을 체득하면 슈퍼파워를 손에 쥘 것이다. [Andrew Ng](https://twitter.com/andrewyng/status/728986380638916609)
>
> 금수저, 은수저 슈퍼파워를 받은 사람과 기계학습을 통달한 흑수저들간의 무한경쟁이 드뎌 시작되었다. 물론, 
> 금수저를 입에 물고 기계학습을 통달한 사람이 가장 유리한 출발을 시작한 것도 사실이다.



## 학습목차 

1. [텍스트 데이터](nlp-text.html)
    1. [단어주머니(Bag of Words)](nlp-bag-of-words.html)
    1. [텍스트 데이터와 저작](https://statkclee.github.io/ds-authoring/)
    1. [지프 법칙(Zipf law) - 시군 인구](nlp-zipf-law.html)    
    1. [텍스트 데이터 -- 트위터](nlp-text-twitter.html)
1. **텍스트 데이터 다루기**
    1. [대한민국 헌법](text-constitution.html)
    1. [숫자를 문자로 표현](nlp-number-to-text.html)
    1. [stringr을 통해 문자열/텍스트 다루기](nlp-stringr.html)
1. 단어주머니(Bag of Words)와 TF-IDF
    1. [BoW와 TF-IDF](nlp-bow-tf-idf.html)
1. 탐색적 데이터 분석
    1. [아마존 vs. 구글](nlp-amazon-google.html)
    1. [해외연극 등장인물 출현횟수](nlp-movie-play.html)
    1. [국내영화(건축학 개론) 등장인물 출현횟수](nlp-movie-arch101.html)
    1. [소설 텍스트 데이터 분석 -- 소나기](nlp-text-basic.html)
    1. [저녁이 있는 삶 -- 손학규](nlp-book.html)
    1. [연설문 판별 - 오바마 vs. 롬니](http://statkclee.github.io/politics/text-classify-speeches.html)
1. **감성분석(Sentiment Analysis)**
    1. [감성분석(Sentiment Analysis) - 깔끔한 텍스트 방식(tidytext)](nlp-sentiment.html)
    1. [고객 방문후기 평점 감성분석 - 옐프(Yelp)](nlp-text-sentiment-yelp.html)
    1. [영어 교과서 감성분석](nlp-english-textbook.html)
1. [토픽 모형 (Topic Model)](nlp-topic-modeling.html) 
    1. [셜록홈즈 - 단어구름에서 토픽모형](silge-topic-modeling.html) 
    1. [트위터 - `tidyverse` + `tidytext`](nlp-twitter-tidytext.html) 
1. **기계학습과 딥러닝(Deep Learning)**
    1. [객체 변환: `tm` &harr; `tidytext`](nlp-tm-tidytext.html)
    1. [`tm`: 텍스트 분류(Text Classification) - 나이브 베이즈(naive bayes)](nlp-text-classification.html)
    1. [`tidytext`: 텍스트 분류(Text Classification) - 나이브 베이즈(naive bayes)](nlp-text-classification-tidytext.html)
    1. [영화 평점 - 무비렌즈(MovieLens)](nlp-text-movielens.html)
    1. [SMS 스팸분류 - Random Forest](nlp-spam-machine-learning.html)
    1. [정규표현식에서 워드2벡(Word2Vec)](nlp-regex-word2vec.html)
    1. [캐글 - 전자상거래 옷 리뷰](text-kaggle-ecommerce-review.html)
    1. [재난 트윗 분류기 - `tidytext`와 `caret`](text-twitter-tidytext-caret.html)
1. **한국어**
    1. **한국어 R Meetup - 류충현**: [대통령 연설문 - 데이터 긁어오기](nlp-president-crawl.html), [대통령 연설문 - DTM 만들기](nlp-president-dtm.html)
    1. [`RmecabKo` 설치 - 맥(Mac)](nlp-rmecabko-install.html)
1. **[R 파이썬을 만나다.](text-r-meet-python.html)**
    1. [자연어 처리 입문](nlp-intro-python.html) - 텍스트 &rarr; 단어주머니(Bag of Words) 
    1. [자연어 처리 중급](nlp-intermediate-python.html) 
    1. [데이터과학 - 파이썬 자료구조](text-python-datatype.html)
1. [LangCon - 자연어 처리의 화장을 하지 않은 얼굴: 튜토리얼](langcon-2019-tutorial.html)
    - 영문
        1. [케인즈 vs 하이에크](langcon-keynes-hayek.html)
        1. [케인즈 vs 하이에크 - 감성, 핵심어, 연관단어](langcon-keynes-hayek-sentiment.html)
        1. [케인즈 vs 하이에크 - 토픽모형](langcon-keynes-hayek-topic.html)
        1. [케인즈 vs 하이에크 - `spacyr`](langcon-keynes-hayek-spacyr.html)
    - 유튜브
        1. 한글 
            1. [네이버 뉴스](nlp-naver-news.html)
            1. [깔끔한 텍스트 (Tidytext) - 신년기자회견(2019)](nlp-tidytext-moon-speech.html)
            1. [네이버 뉴스 - RmecabKo (형태소 분석)](nlp-naver-news-mecab.html)           
        1. [유트브 댓글](nlp-youtube-comment.html)
        1. [알릴레요 vs. 홍카콜라 - 댓글 분류](youtube-channel-comment-classification.html)
1. [공정거래법 전면개편안](text-fair-law.html)
    1. [최고의 OCR 엔진](text-fair-law-ocr.html)
    1. [EDA 텍스트 마이닝](text-fair-law-tm.html)
    1. [워드 임베딩(Word Embedding)](text-fair-law-word-embedding.html)
    1. [워드 임베딩(Word Embedding): 영어(`GloVe`)](text-fair-law-word-embedding-glove.html)
    1. [워드 임베딩(Word Embedding): 한국어](text-fair-law-word-embedding-korean.html)
    1. [기계독해(MRC): `RBERT`](text-fair-law-mrc.html)
 