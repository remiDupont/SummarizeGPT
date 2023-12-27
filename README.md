# Media Summary pipeline

This project mains a making a pipeline to takes detailes notes using chatGPT and Whisper. Whisper runs locally to save cost

## Write a markdown resume into resultat_final folder : 

```
python main.py ./download #folder containing video / audio to takes notes from
```

## Notes about the number of token

book : 146.414  tokens
Balex une heure : 6000
David une heure 30 : 29000

GPT4 turbo : 32 k tokens max, but doesn't works that well

0.01 centimes pour 1k tokens entrée
