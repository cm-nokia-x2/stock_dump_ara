#!/system/bin/sh
#
#Get the date from custom/variants/package.json. If this is newer than current date,
#change current date to one day later than variant image. Sleep 5 is needed because
#otherwise startup without SIM changes the date back to 1970-2-Jan.

VARIANTDATE=$(ls -l /custom/variants/package.json | grep '[0-9]*-[0-9]*-[0-9][0-9]' -o)
sleep 5
for CHAR in $(echo $VARIANTDATE | grep '[0-9]\{1\}' -o)
do
    VARDATE=${VARDATE}$CHAR
done

CURRENTDATE=$(date +%Y-%m-%d)
for CHAR in $(echo $CURRENTDATE | grep '[0-9]\{1\}' -o)
do
    CURDATE=${CURDATE}$CHAR
done

if [ $CURDATE -lt $VARDATE ]; then
    let VARDATE=$VARDATE+1
    VARDATE=$VARDATE.000000
    date -s $VARDATE
fi
