# Media Summary pipeline

This project aims at making a pipeline to takes detailed notes using chatGPT and Whisper. 
Whisper runs locally (in GPY if possible) to save cost

## 1) Setup

### openai key : 
In your bashrc file : 
```bash
export OPENAI_KEY="sk-************************************"
```

### install the python env in conda 

```bash 
conda env create -f environment.yml
```

## 2) Downlaod videos from youtube

Please note this pipeline can take as input any video / audio input, not only youtube video. 
Enter your url in the variable `url_list` of download_from_youtube.py

```bash
python download_from_youtube.py 
```


## 3) Call the pipeline 

```bash
python main.py --input_dir_or_file /path/to/video_or_audio --final_output_dir /path_to_save_markdown 
```
Note that the chatGPT prompts are in french, do not hesitate to modify them within the file `constants.py`
## Notes about the number of token

book : 146.414  tokens
Balex une heure : 6000
David une heure 30 : 29000

GPT4 turbo : 32 k tokens max, but doesn't works that well

0.01 centimes pour 1k tokens entrée
