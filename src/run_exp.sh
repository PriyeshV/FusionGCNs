    #!/usr/bin/env bash

    python run_citeseer.py simple x h 0 1 0 & # 61
    sleep 2s
    #python run_cora.py kipf h h 1 1 1 &
    #sleep 2s
    python run_citeseer.py simple x h 0 5 2 &
    sleep 2s
    #python run_cora.py kipf h h 1 5 3 &
    #sleep 2s

python run_ppigs_trans.py simple x h 0 1 0 & # 61
sleep 2s
python run_ppigs_trans.py kipf h h 1 1 1 &
sleep 2s
python run_ppigs_trans.py simple x h 0 5 2 &
sleep 2s
python run_ppigs_trans.py kipf h h 1 5 3 &
sleep 2s



python run_reddit_trans.py simple x h 0 5 0 & # 59
sleep 2s
python run_reddit_trans2.py simple x h 0 5 1 & # 59
sleep 2s
python run_reddit_trans.py kipf h h 1 5 2 & # 59
sleep 2s
python run_reddit_trans2.py kipf h h 1 5 3 & # 59
sleep 2s

python run_reddit_trans.py simple x h 0 1 0 & # 60
sleep 2s
python run_reddit_trans2.py simple x h 0 1 1 &
sleep 2s
python run_reddit_trans.py kipf h h 1 1 2 & # 59
sleep 2s
python run_reddit_trans2.py kipf h h 1 1 3 & # 59
sleep 2s


# Try I-FGN also

python run_pubmed.py simple x h 0 1 0       # Running
sleep 2s
python run_mlgene.py simple x h 0 1 2      # Running
sleep 2s
python run_reddit_trans.py simple x h 0 5 1 &
sleep 2s
python run_reddit_trans2.py simple x h 0 5 6 &
sleep 2s


python run_reddit_trans.py simple x h 0 1 5 &
sleep 2s
python run_reddit_trans2.py simple x h 0 1 7 &
sleep 2s

python run_pubmed.py simple x h 0 5 0 # Running
sleep 2s
python run_mlgene.py simple x h 0 5 0 # Running
sleep 2s

python run_ppigs_trans.py simple x h 0 1 1 & # Run machine 2
sleep 2s
python run_ppigs_trans.py simple x h 0 5 0 & # Running run2
sleep 2

python run_amazon.py simple x h 0 1 0 & # Running
sleep 2s
python run_amazon.py simple x h 0 5 0 # Running
sleep 2s

python run_cora_multi.py simple x h 0 1 1 & # Running
sleep 2s
python run_cora_multi.py simple x h 0 5 0 & # Running
sleep 2s
