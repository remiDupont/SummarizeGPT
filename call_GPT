from token_counter import get_number_of_tokens
from openai import OpenAI
import os
import datetime


client = OpenAI()

file_name = "./transcriptions/EPR-28-S5-1-TriadeSante.txt"
with open(file_name) as f:
    script = f.read()

# ma_prompt = f"""

# Tu es un assistant rigoureux, tu dois préparer un résumé extrèmement detaillé au format markdown à partir d'un script.
# - Rédige un résumé très très détaillé, complet, approfondi. Cite des parties du script.
# - S'appuyer strictement sur le texte fourni, sans inclure d'informations externes.
# - Formate le résumé en markdown, avec des sections ayant différents niveaux de titres.
# - Soit le plus précis possible, ne pas hésiter à ajouter des détails. Chaque exemple donné doit être cité, afin que je puisse le reproduire
# - Le but est de pouvoir appliquer en detail les conseils donnés dans sa vie de tous les jours, il faut donc que le résumé soit très détaillé et très complet. N'hésite pas à ajouter des exemples et des citations venant du texte. 
# - Donne tes exemples concrets pour chaque partie dès que c'est possible. Cite toujours les chiffres et les études.
# - Le texte de sortie doit être très long, rédigé et structuré. N'utilise pas de bullet points.

# Voici le script :

# """
    
ma_prompt = f"""
Tu es un assistant scientifique qui me prépare une note extrèmement detaillé au format markdown texte fourni.
Avec cette note, je comprends en detail les conseils donnés dans le script et je peux tous les appliquer dans ma vie de tous les jours, sans exceptions.

- Rédige un résumé très très détaillé, complet, approfondi.
- S'appuyer strictement sur le texte fourni, sans inclure d'informations externes.
- Formate le résumé sous forme de section avec différents niveaux de titres. Pas de liste à puces, mais du texte détaillé à la place.
- Soit le plus précis possible, ne pas hésiter à ajouter des détails. Recopie les exemples à partir du script afin que je puisse le reproduire dans ma vie.
- Le texte de sortie doit être très long et structuré. C'est important qu'il soit long.


Voici un exemple du format de la sortie attendue. L'exemple est structuré et détaillé, il explique en détails les éléments du script : 

# Titre global du script tel que donné en introduction :  "Nom du script"

## Introduction

Introduction du script.

## Titre de la partie 1 du script 

### 1) Sous partie de la partie 1 du script

Texte detaillé expliquant la sous partie 1 du script en detail. Cette partie n'utilise pas de bullet points, à part dans l'introduction, mais du texte détaillé à la place. Les chiffres donnés par le scipt, les études et les exemples sont cités de mainère tres detaille. 

### 2) Sous partie de la partie 1 du script

Texte detaillé expliquant la sous partie 2 du script en detail. Cette partie n'utilise pas de bullet points, à part dans l'introduction, mais du texte détaillé à la place. Les chiffres donnés par le scipt, les études et les exemples sont cités de mainère tres detaille.

[ un maximum de sous-partie ici ]  

## Titre de la partie 2 du script 

### 1) Sous partie de la partie 2 du script

....

Important ! :  Le réponse comporte le maximum d'éléments du script possible, et suit l'ordre du script. 

Fin de l'instruction. Voici le script : """



gpt_input = ma_prompt + "Nom du script : /n "  + file_name + " /n Script : "+ script


num_tok = get_number_of_tokens(gpt_input)
print(f"Nombre de tokens: {num_tok}, estimated cost is {num_tok * 0.00001} $")

completion = client.chat.completions.create(
    model=["gpt-4-32k", "gpt-4-0613", "gpt-4-1106-preview", "gpt-3.5-turbo-0301"][2],
    messages=[
        {
            "role": "user",
            "content": gpt_input,
        },
    ],
    # max_tokens=4096,
    temperature= 0,
    # n=1,
    seed=42,
)
print(completion.choices[0].message.content)

# sauvegarde la sortie dans un fichier dans le dossier resultat_final. Le nom du fichier depend de la date et de l'heure
now = datetime.datetime.now()
with open(f"./resultat_final/{now.strftime('%Y-%m-%d_%H-%M-%S')}.md", "w") as file:
    file.write(completion.choices[0].message.content + "\n " +  ma_prompt)

print()