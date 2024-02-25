#!/bin/bash

# Déclaration d'un tableau contenant les noms de dossiers avec guillemets
declare -a modules_with_quotes=(
    "\"Module_10_Exploitation_et_mise_en_location\""
    "\"Module_11_Le_cas_spécifique_de_la_location_meublée\""
    "\"Module_12_Les_montages_en_société_à_prépondérance_immobilière\""
    "\"Module_13_Créer_un_groupe_de_sociétés\""
    "\"Module_14_Trouver_des_investissements_profitables_grâce_aux_ventes_aux_enchères\""
    "\"Module_15_Trouver_et_exploiter_des_locaux_professionnels\""
    "\"Module_16_Initiation_à_l'activité_de_Marchand_de_Biens\""
    "\"Module_17_Les_investissements_en_viager\""
    "\"Module_1_Les_bases_de_l'investissement_immobilier\""
    "\"Module_2_Mettre_en_place_son_plan_d'action_opérationnel\""
    "\"Module_3_Trouver_les_investissements_profitables\""
    "\"Module_4_Bien_se_comporter_pendant_les_visites\""
    "\"Module_5_Les_bases_de_la_fiscalité_et_choix_du_montage_juridique\""
    "\"Module_6_Mener_les_négociations\""
    "\"Module_7_Gestion_et_pilotage_de_chantier\""
    "\"Module_8_Financer_ses_futures_acquisitions\""
    "\"Module_9_L'étape_administrative_du_notaire\""
)

# Boucle sur le tableau pour renommer chaque dossier
for module in "${modules_with_quotes[@]}"; do
    # Suppression des guillemets
    clean_name=${module//\"/}
    # Commande mv pour renommer le dossier (si nécessaire, ajoutez le chemin complet)
    mv $module $clean_name
done

echo "Renommage terminé."

