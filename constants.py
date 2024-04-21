supported_extensions = [
    "flac",
    "m4a",
    "mp3",
    "mp4",
    "mpeg",
    "mpga",
    "oga",
    "ogg",
    "wav",
    "webm",
    "mp4",
    "mkv",
    "avi",
    "pdf"
]


ma_prompt_cascade = f"""
Tu es un assistant scientifique qui me prépare une note extrèmement detaillée, uniqument en francais, au format markdown texte fourni.
Avec cette note, je comprends en detail les conseils donnés dans le texte et je peux tous les appliquer dans ma vie de tous les jours, sans exceptions.

- Rédige un résumé très très détaillé, complet, approfondi.
- S'appuyer strictement sur le texte fourni, sans inclure d'informations externes.
- Formate le résumé sous forme de section avec différents niveaux de titres. Pas de liste à puces, mais du texte détaillé à la place.
- Soit le plus précis possible, ne pas hésiter à ajouter des détails. Recopie les exemples à partir du texte afin que je puisse le reproduire dans ma vie.
- Le texte de sortie doit être très long et structuré. C'est important qu'il soit long.
- Ne fait pas de conclusions ni d'introduction


Voici un exemple du format de la sortie attendue. L'exemple est structuré et détaillé, il explique en détails les éléments du texte : 


## Titre de la partie 1 du texte 

### 1) Sous partie de la partie 1 du texte

Texte detaillé expliquant la sous partie 1 du texte en detail. Cette partie n'utilise pas de bullet points, à part dans l'introduction, mais du texte détaillé à la place. Les chiffres donnés par le scipt, les études et les exemples sont cités de mainère tres detaille. 

### 2) Sous partie de la partie 1 du texte

Texte detaillé expliquant la sous partie 2 du texte en detail. Cette partie n'utilise pas de bullet points, à part dans l'introduction, mais du texte détaillé à la place. Les chiffres donnés par le scipt, les études et les exemples sont cités de mainère tres detaille.

[ un maximum de sous-partie ici ]  

## Titre de la partie 2 du texte 

### 1) Sous partie de la partie 2 du texte

....

Important !!!  La réponse comporte le maximum d'éléments du texte possible, et suit l'ordre chronologique du texte. Respecte bien le format ci-dessus.
Même si le script est en anglais, la réponse doit être en français.
 """

ma_prompt_cascade_serie2 = "Reorganise le texte en ne modifiant que les titres : tu dois impérativement garder le contenu exact de tous les paragraphes mais tu peux renommer les titres et bouger les paragraphes afin d'avoir un texte plus cohérents. Tous les paragraphes doivent être recopiées, sans AUCUNE modifications. ta réponse doit recopier l'ensemble des paragraphes, dans leur integralité.  < Début du markdown >  : "



# ma_prompt_cascade_serie = (
#     ma_prompt_cascade
#     + """   
# Un markdown de la partie précédente existe déja. Tu dois le compléter. Ta sortie doit donc être un markdown complétant le markdown précédent, sans le recopier. Voici le markdown précédent :
# """
# )
