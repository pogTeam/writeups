# Labour

## Description

Follow your heart, for it leads you straight to the answer.

## Solution

This challenge gave us a file full of GPS coordinates.

```xml
...
<wpt lat="23.71697" lon="89.45508">
	<ele>12.1</ele>
	<name>WP01-A</name>
</wpt>
<wpt lat="22.82885" lon="80.79786">
	<name>WP02-B</name>
</wpt>
<wpt lat="39.88276" lon="58.81642">
	<name>WP03-C</name>
</wpt>
...
```

Our first instinct was decode the coordinates to analyze the results:


* Jalan Kuala Tembeling - Kuala Lipis, Kampung Kerambit, 27200 Kuala Lipis, Pahang, <b>M</b>alaysia
* Unnamed Road, <b>A</b>fghanistan
* Unnamed Road, <b>P</b>akistan
* Unnamed Road, 26630 Çakmak/Günyüzü/Eskisehir, <b>T</b>urkey
* Cegléd, 311, 2700 <b>H</b>ungary
* Al Kharga - Mut, Qesm Al Wahat Ad Dakhlah, New Valley Governorate, <b>E</b>gypt
* Unnamed Road, Durocher, <b>H</b>aiti
* Unnamed Road, <b>A</b>ngola
* 419 Xian Dao, Maqu Xian, Gannan Zangzuzizhizhou, Gansu Sheng, <b>C</b>hina
* Zhanaarka District,a 100000, <b>K</b>azakhstan

Joining the first letter of each country, we got the following string: MAPTHEHACK.
Following the instructions at the head of the file, the flag is: BITSCTF{MAP_THE_HACK}