#!/bin/bash
## Autor: Markisich Emiliano
## mail: emiliano@markisich.com.ar
## creado: 2021-01-10

#Objetivo del bot informar cada x tiempo la temperatura del rasberry pi

TOKEN="" #token del bot
ID="" #Id del canal

MENSAJE="La temperatura del pi es:  $(/opt/vc/bin/vcgencmd measure_temp)"
URL="https://api.telegram.org/bot$TOKEN/sendMessage"

curl -s -X POST $URL -d chat_id=$ID -d text="$MENSAJE"

