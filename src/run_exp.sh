#!/usr/bin/env bash

python run_amazon.py kipf linear h h 1 1 0 & #
sleep 2s
python run_amazon.py kipf max_pool h h 1 1 0  #
sleep 2s
python run_amazon.py kipf attention h h 1 1 0 &
sleeep 2s
python run_amazon.py kipf lstm_attention h h 1 1 0 & #
sleep 2s
#python run_amazon.py chebyshev linear h h 1 1 1 & #
#sleep 2s

python run_citeseer.py kipf linear h h 1 1 1 & #
sleep 2s
python run_citeseer.py kipf max_pool h h 1 1 1 & #
sleep 2s
python run_citeseer.py kipf attention h h 1 1 1 &
sleeep 2s
python run_citeseer.py kipf lstm_attention h h 1 1 1 #
sleep 2s

python run_cora.py kipf linear h h 1 1 1 & #
sleep 2s
python run_cora.py kipf max_pool h h 1 1 1 & #
sleep 2s
python run_cora.py kipf attention h h 1 1 1 &
sleeep 2s
python run_cora.py kipf lstm_attention h h 1 1 1 #
sleep 2s

python run_cora_multi.py kipf linear h h 1 1 0 & #
sleep 2s
python run_cora_multi.py kipf max_pool h h 1 1 0 & #
sleep 2s
python run_cora_multi.py kipf attention h h 1 1 1 &
sleeep 2s
python run_cora_multi.py kipf lstm_attention h h 1 1 1 #
sleep 2s

python run_facebook.py kipf linear h h 1 1 2 & #
sleep 2s
python run_facebook.py kipf max_pool h h 1 1 2 & #
sleep 2s
python run_facebook.py kipf attention h h 1 1 2 &
sleeep 2s
python run_facebook.py kipf lstm_attention h h 1 1 2 #
sleep 2s

python run_mlgene.py kipf linear h h 1 1 2 & #
sleep 2s
python run_mlgene.py kipf max_pool h h 1 1 2 #
sleep 2s
python run_mlgene.py kipf attention h h 1 1 2 &
sleeep 2s
python run_mlgene.py kipf lstm_attention h h 1 1 2 #
sleep 2s

python run_movie.py kipf linear h h 1 1 0 & #
sleep 2s
python run_movie.py kipf max_pool h h 1 1 3 #
sleep 2s
python run_movie.py kipf attention h h 1 1 0 &
sleeep 2s
python run_movie.py kipf lstm_attention h h 1 1 3 #
sleep 2s

python run_pubmed.py kipf linear h h 1 1 1 & #
sleep 2s
python run_pubmed.py kipf max_pool h h 1 1 2 #
sleep 2s
python run_pubmed.py kipf attention h h 1 1 1 &
sleeep 2s
python run_pubmed.py kipf lstm_attention h h 1 1 1 #
sleep 2s
#python run_reddit_trans.py chebyshev linear h h 1 1 2 &
#sleep 2s


python run_ppigs_trans.py kipf linear h h 1 1 4 & #
sleep 2s
python run_ppigs_trans.py kipf max_pool h h 1 1 5 &
sleep 2s
python run_ppigs_trans.py kipf attention h h 1 1 6 &
sleeep 2s
python run_ppigs_trans.py kipf lstm_attention h h 1 1 7 #
sleep 2s

########## Machine 2

python run_reddit_trans.py kipf linear h h 1 1 0 &
sleep 2s
python run_reddit_trans.py kipf max_pool h h 1 1 1 &
sleep 2s
python run_reddit_trans.py kipf attention h h 1 1 2 &
sleeep 2s
python run_reddit_trans.py kipf lstm_attention h h 1 1 3 #
sleep 2s

python run_ppigs.py kipf linear h h 1 1 4 & #
sleep 2s
python run_ppigs.py kipf max_pool h h 1 1 5 &
sleep 2s
python run_ppigs.py kipf attention h h 1 1 6 &
sleeep 2s
python run_ppigs.py kipf lstm_attention h h 1 1 7 #
sleep 2s
