# Discord Colored Text Generator
## Inspired by [rebane2001's app](https://rebane2001.com/discord-colored-text-generator/)

This is a command-line tool that you can use to create colorful discord messages using discord's built-in ANSI support.
Unlike rebane's, this tool is generally intended for larger sets of text with repeating use of colors. 

## Setting up:
### Creating a keywords JSON:
Use `keywords_template.json` as a template and create a separate file to determine a set of words you want to be colored. \ Naming should be in the format `keywords_{name}.json`, where name (without the brackets) is the name you call at runtime.

Keywords should be entered into the empty lists of the template, surrounded by quotes and comma-separated (regular JSON format). Capitilization does not matter. Do not use words in the form \_\_\_\_s and \_\_\_\_ed, the tool will handle these for you.

### Using the app
`build.py` takes two positional arguments and an optional nitro argument. To run, you must have a file with your input text in it. Your output will show up on your terminal and in the folder where `build.py` is located.

Positional Arguments:
* keywords - the name of your keyword file (`keywords_{name}.json`)
* input - the name of your input file (any format, include the .txt)

Optional Arguments:
* --help - bring up the help menu
* --nitro - doesn't split your message, so you can send it all as one large message.


## Example:
The following is using the patch notes for AOE4 from December 2023. The example folder contains the files for this.

```
python build.py aoe inputaoe.txt
```

returns the following:

![example](/Examples/example.png)

and looks like this on discord:

![discord](/Examples/discord.png)