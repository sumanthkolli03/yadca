#TODO: maybe just posts to discord? is that possible?

import re
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("keywords", help="what keywords you want to use")
parser.add_argument("input", help="name of input text file")
parser.add_argument("-n", "--nitro", help = "use --nitro if you have nitro and want the whole output in one message", action="store_true")
#parser.add_argument("-d", "--discord", help = "use --discord {channel_name} to post directly to discord - channel name mapping WIP", action = "store")
args = parser.parse_args()

def import_settings(setting):
    #Imports pre-existing settings from json's and initializes constants

    #uses specified keyword setting
    with open(f"keywords_{setting}.json","r") as f:
        keywords = json.load(f)

    #define constants
    global punList
    punList = [
        ".", ">", "<", ",", "/", "?", '"', ":", ";", "[",
        "]", "{", "}", "|", "~", "+", "=", "!", "$", "%"
    ]
    return keywords

def re_text(text):
    #opens text file, splits text into words & whitespace, splits punctuation from words (will rejoin later)
    with open(text, "r", encoding='UTF-8') as f:
        inp = f.read()
        for pun in punList:
            inp = inp.replace(pun, f" {pun}")
        retext = re.split(r'(\s)', inp)
    return retext

def init_colors(keywords):
    # Initializes all variables used in the text replacement. 
    # TODO: make this file inputting/UI-able

    colors = {
        "start" : r"[1;", #start code for ansi color
        "end" : r"[0m",   #end code for ansi color
        "black": r"30m",    #color codes
        "red" : r"31m",     
        "green" : r"32m",
        "yellow" : r"33m",
        "blue" : r"34m",
        "magenta" : r"35m",
        "cyan": r"36m",
        "white": r"37m"
    }

    colordict = {}
    #iterates over every color in keywords
    #for each keyword, splits, lowers, and uses ___s format to 
    #associate each word with a color in colordict
    for color in keywords:
        for word in keywords[color]:
            for x in word.split():
                colordict[x.lower()] = colors[color]
                colordict[(x.lower() + "s")] = colors[color]
                colordict[(x.lower() + "ed")] = colors[color]


    return colors, colordict 

def colorize(colors, colordict, retext):
    # loops over every "word" in retext and colors them in according to colordict
    finaltldr = []
    for word in retext:
        if word.lower() in colordict:
            tempstr = colors["start"] + colordict[word.lower()] + word + colors["end"]
            finaltldr.append(tempstr)
        else:
            finaltldr.append(word)
    
    joined = "".join(finaltldr)
    #Reversing space in front of punctuation
    for pun in punList:
        joined = joined.replace(f" {pun}", pun)

    print(joined)
    print(len(joined))
    return joined

def output(joined):
    #outputs the final file
    #amount of outputs is determined by nitro/message length
    if (len(joined) > 1900) and (not args.nitro):
        lines = joined.split("\n")
        print("Creating Chunks")
        chunks = []
        curchunk = ""
        for line in lines:
            curchunk += line + "\n"
            if len(curchunk)>1500:
                chunks.append(curchunk)
                curchunk = ""
                print("Chunk Written")
        if curchunk != "":
            chunks.append(curchunk)
            print("Chunk Written")
        for i, chunk in enumerate(chunks):
            output = "```ansi" + "\n" + chunk + "\n" + "```" 

            with open(f"out{i}.txt", "w", encoding="utf-16") as f:
                f.write(output)
                print(f"outputted file {i}")

    else:
        output = "```ansi" + "\n" + joined + "\n" + "```" 
        with open("outn.txt", "w", encoding="utf-16") as f:
            f.write(output)
            print("outputted")



if __name__ == "__main__":
    keywords = import_settings(args.keywords)

    retext = re_text(args.input)

    colors, colordict = init_colors(keywords)
    joined = colorize(colors, colordict, retext)

    output(joined)

