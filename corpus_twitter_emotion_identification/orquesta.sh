#! /bin/sh
raiz="/home/dbarenas/corpus_twitter_emotion_identification"

for i in $(cat $raiz/lista_emociones);do
	d=$(date +%m%d%H%M%S%N)
	echo $i
	python $raiz/extract.py $i > $raiz/res/out_$d
	python $raiz/process.py $raiz/res/out_$d
done

#python $raiz/counter.py | wall

#mv /home/dbarenas/out* /home/dbarenas/corpus_twitter_social_analitics/. 
#python $raiz/process.py $raiz/res/out* | wall  
