#!/usr/bin/env bash

python run_pubmed.py simple x h 0 1 0 &      # F-NIP
sleep 2s
python run_mlgene.py simple x h 0 1 2 &      # F-NIP
sleep 2s
python run_reddit_trans.py simple x h 0 5 4 &      # F-NIP
sleep 2s
python run_reddit_trans2.py simple x h 0 5 6 &      # F-NIP
sleep 2s


python run_reddit_trans.py simple x h 0 1 5 &      # Node
sleep 2s
python run_reddit_trans2.py simple x h 0 1 7 &      # Node
sleep 2s

python run_pubmed.py simple x h 0 5 1      # Node
sleep 2s
python run_mlgene.py simple x h 0 5 3      # Node
sleep 2s

python run_ppigs_trans.py simple x h 0 1 1 &      # Node
sleep 2s
python run_ppigs_trans.py simple x h 0 5 3 &     # Node
sleep 2

python run_amazon.py simple x h 0 1 1 &
sleep 2s
python run_amazon.py simple x h 0 5 1
sleep 2s

python run_cora_multi.py simple x h 0 1 1 &
sleep 2s
python run_cora_multi.py simple x h 0 5 1 &
sleep 2s
