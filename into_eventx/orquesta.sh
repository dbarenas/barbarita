#! /bin/sh
d=$(date +%m%d%H%M%S)
python /home/dbarenas/corpus_twitter_social_analitics/extract.py > /home/dbarenas/corpus_twitter_social_analitics/out$d
python /home/dbarenas/corpus_twitter_social_analitics/extract02.py > /home/dbarenas/corpus_twitter_social_analitics/out2$d
python /home/dbarenas/corpus_twitter_social_analitics/extract03.py > /home/dbarenas/corpus_twitter_social_analitics/out3$d
python /home/dbarenas/corpus_twitter_social_analitics/extract04.py > /home/dbarenas/corpus_twitter_social_analitics/out4-str1$d
python /home/dbarenas/corpus_twitter_social_analitics/extract04-2.py > /home/dbarenas/corpus_twitter_social_analitics/out4-2str1$d
python /home/dbarenas/corpus_twitter_social_analitics/extract04-3.py > /home/dbarenas/corpus_twitter_social_analitics/out4-3str1$d


#mv /home/dbarenas/out* /home/dbarenas/corpus_twitter_social_analitics/. 
python /home/dbarenas/corpus_twitter_social_analitics/process.py /home/dbarenas/corpus_twitter_social_analitics/out$d  
python /home/dbarenas/corpus_twitter_social_analitics/process.py /home/dbarenas/corpus_twitter_social_analitics/out2$d
python /home/dbarenas/corpus_twitter_social_analitics/process_04.py /home/dbarenas/corpus_twitter_social_analitics/out4-str1$d
python /home/dbarenas/corpus_twitter_social_analitics/process_04.py /home/dbarenas/corpus_twitter_social_analitics/out4-2str1$d
python /home/dbarenas/corpus_twitter_social_analitics/process_04.py /home/dbarenas/corpus_twitter_social_analitics/out4-3str1$d | wall
python /home/dbarenas/corpus_twitter_social_analitics/process.py /home/dbarenas/corpus_twitter_social_analitics/out3$d | wall

rm -Rf /home/dbarenas/corpus_twitter_social_analitics/out*
