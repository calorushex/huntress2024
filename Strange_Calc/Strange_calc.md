# Strange_Calc

The medium challenge for the day starts with a zip file containing a calc.exe file. The first thing to do is to see what this file it. I like to open it in detect it easy first to get a view of how it's compiled.

![DIE](strange_calc_die.jpg)

You can see in the output that this is an AutoIT compiled script. We can use a tool called [autoit-extractor](https://github.com/digitalsleuth/autoit-extractor/releases/tag/v1.0.0) to decompile the executable in to it's original au3 script.

```
.\AutoIt-Extractor-net40-x86.exe .\calc.exe
```

![autoit](strange_calc_autoscript.jpg)

One of the functions of the script is to create a malicous JScript file using the contents of $a. The contents of $a is initially base64 encoded and is then further encoded. We can decode the contents of the script with CyberChef using the following recipe.

```
From_Base64('A-Za-z0-9+/=',true,false)
Microsoft_Script_Decoder()
```

![jse](jse.png)

Within the contents of the decoded script, we can see a string which is further encoded.

![encoded_string](encoded_string.png)

We can use some Python to decode the string (GPT did the work here), revealing the flag.

[password_decoder.py](https://github.com/calorushex/huntress2024/blob/main/Strange_Calc/password_decoder.py)

![decoded_string](decoded_string.png)
