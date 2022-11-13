#!/usr/bin/env python3
# coding:utf8
import string
import sys
import time
import hashlib
import argparse
import atexit
import urllib.request
import urllib.response
import urllib.error


def crack_en_ligne(md5):
    try:
        agent_utilisateur = "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
        headers = {'User-Agent': agent_utilisateur}
        url = "https://www.google.fr/search?hl=fr&q=" + md5
        requete = urllib.request.Request(url, None, headers)
        reponse = urllib.request.urlopen(requete)
    except urllib.error.HTTPError as e:
        print("[-] Erreur HTTP : " )
    except urllib.error.URLError as e:
        print( "[-] Erreur d'URL : " + e.reason)

    if "Aucun document" in reponse.read().decode("utf8"):
        print( "[-] HASH NON TROUVE VIA GOOGLE")
    else:
        print("[+] MOT DE PASSE TROUVE VIA GOOGLE : " + url )


def affiche_duree():
    # affiche la durée écoulée à la fin du script
    print("Durée écoulée : " + str(time.time() - debut) + " secondes")


parser = argparse.ArgumentParser(description="Casseur de mot de passe en Python")
parser.add_argument("-f", "--file", dest="file", help="Chemin du fichier de mots clés", required=False)
parser.add_argument("-g", "--gen", dest="gen", help="Génère un hash MD5 du mot de passe donné", required=False)
parser.add_argument("-md5", dest="md5", help="Mot de passe MD5 à casser", required=False)
parser.add_argument("-l", dest="plength", help="Password length", required=False, type=int)
parser.add_argument("-o", dest="online", help="Cherche le hash en ligne (google)", required=False, action="store_true")

args = parser.parse_args()

debut = time.time()
atexit.register(affiche_duree)

if args.gen:
    print("[*] HAHS MD5 DE " + args.gen + " : " + hashlib.md5(args.gen.encode("utf8")).hexdigest())

if args.md5:
    print("[*] CRACKING DU HASH " + args.md5)
    if args.online:
        print("[*] UTILISANT LE MODE EN LIGNE")
        crack_en_ligne(args.md5)
    else:
        print("[-] VEUILLEZ CHOISIR L'ARGUMENT -f ou -l avec -md5." )
else:
    print( "[-] HASH MD5 NON FOURNI." )


