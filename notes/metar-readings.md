---
type: Aviation-Reference
tags:
  - flight-training
related_to:
  - Magenta Debrief
---

[This is how you read a METAR](https://metar-taf.com/explanation)
A METAR has a fixed format. The definition of each part can be found below. Click on the item to jump to the correct paragraph.
**METAR/SPECI**
Indicates whether it is a regular observation `METAR` or extra (SPECI). The SPECI is not much used anymore because most weather stations issue a new observation every half hour.
**Place**
The ICAO code of the airport / weather station. Usually this is a 4 letter code. Example: `EHLE` means `Lelystad Airport`.
**Day and time**
The first 2 digits indicate the day of the month. Followed by the 2 digits of the hour (00-23) and the minutes (00-59). Z is the abbreviation for Zero, time zone 0 is Greenwich Mean Time (UTC). In the NATO phonetic alphabet, the Z is pronounced Zulu, which is why it is also called Zulu time. Note that both the day and time are displayed in UTC / zulu time. This is done to avoid misunderstandings. So `280925Z` means the 28th day of the month at 9:25 UTC.
**COR/AUTO/NIL**
COR means that this observation replaces a previously drawn up report. `AUTO` means that the observation is done automatically. Automatic observations are more limited than manually generated observations. NIL means that no data is known.
**Wind**
`10009G19KT 060V130` means that the mean wind direction is 100, variable between 60 and 130. The average wind speed is 9 knots (09) with peaks up to 19 knots (KT). The average wind speed is 9 knots (09) with peaks up to 19 knots (KT).
- The wind direction and strength are averaged over the last 10 minutes.
- Outliers are only listed if they are 10 knots above average.
- A variable wind direction is only reported if it deviates more than 10 from the mean.
- The wind direction is shown on a scale from 000-350 degrees, rounded to tens of degrees. Where 000 is the north, 090 is the east, 180 is the south and 270 is the west.
- The wind is measured at a height of 10 m. A METAR therefore does not provide information about high winds, these are usually a lot stronger. This wind information is therefore not useful for navigation.
- In some cases `VRB01KT` is indicated instead of the wind: if the wind speed is 3 knots or less, the wind is more than 3 knots but varies with more than 180 or when the direction cannot be determined.
- If there is no wind then `00000KT` is displayed.
- If both the wind direction and the wind speed cannot be determined `/////KT`
 In addition to knots, the wind speed can also be indicated in meters per second (MPS) or miles per hour (MPH).
**Visibility**
The visibility shown in the METAR is an average, minimum visibility. `5000` means visibility is 5000 meters. If visibility is less than 1000 meters, the number will be added to 4 characters.
This is to avoid confusion with the imperial system. Visibility can also be indicated in miles or parts thereof: `3SM` means the visibility is 3 miles (statute mile). `3/4SM` means visibility is 0.75 miles.
- Visibility can be different in different directions. In that case the lowest measured visibility is always displayed. If visibility is only measured in one direction then `NDV` (Non Directional Variation) is added to the code.
- Visibility can also be listed per direction. `1500SW 2000NE` means the visibility to the southwest is 1500 meters and 2000 meters to the northeast.
- In case of poor visibility, the direction can also be displayed per runway. This is also called the RVR (Runway Visual Range). An RVR is usually not reported until visibility is less than 2000 meters.
 Examples of an RVR:
- `R23/0500` visibility for runway 23 is 500 meters
- `R23/P0500` visibility for runway 23 is more (P) than 500 meters
- `R23/M0500` visibility for runway 23 is less (M) than 500 meters
- `R23/0500V1500` visibility for runway 23 varies between 500 and 1500 meters
- `R23/0500U` visibility for runway 23 is 500 meters but increases (U)
- `R23/0500D` visibility for runway 23 is 500 meters but decreases (D)
**Weather phenomena**
`-RA` means that there is currently light rain. This is a combination of RA (rain) and - (light intensity). The codes from the lists below can be combined with each other:
**Intensity**
|**+** |**heavy** |
| ------ | --------------- |
|**-** | light |
|**RE** | recent |
|**VC** | in the vicinity |
**Characteristic**
|**BC** |**patches of** |
| ------ | -------------- |
|**DR** | low drifting |
|**MI** | shallow |
|**PR** | partial |
|**BL** |**blowing** |
| ------ | ------------- |
|**FZ** | freezing |
|**SH** | showers |
|**TS** | thunderstorms |
**Type**
|**BR** |**mist** |
| ------ | --------------- |
|**DS** | dust storm |
|**DU** | widespread dust |
|**DZ** | drizzle |
|**FC** | funnel cloud |
|**FG** | fog |
|**FU** | smoke |
|**GR** | hail |
|**GS** |**small hail** |
| ------ | -------------- |
|**HZ** | haze |
|**IC** | ice crystals |
|**PE** | ice pellets |
|**PO** | sand whirls |
|**PY** | spray |
|**RA** | rain |
|**SA** | sand |
|**SG** |**snow grains** |
| ------ | --------------------- |
|**SN** | snow |
|**SQ** | squalls |
|**SS** | sand storm |
|**UP** | unknown precipitation |
|**VA** | volcanic ash |
**Remarks**
- The most significant form of precipitation is listed first. Example: `GRRA` means more hail than rain, contrary to: `RAGR` with more rain than hail.
- The intensity and whether it is showery `SH` is only used in combination with precipitation. For example when there are showers with heavy rain: `+SHRA`
- If no intensity is mentioned, it is moderate precipitation.
- `MI`, `BC` and `PR` are only used for fog: ground fog, fog banks and partial aerodrome cover.
- Freezing `FZ` is only used in conjunction with rain `RA`, drizzle `DZ` and fog `FG`. This means that it will immediately freeze if it comes into contact with a solid surface.
- Low drifting `DR` and low drifting `BL` are only used in conjunction with snow `SN`, sand `SA` and widespread dust `DU`.
**Differences**
- Rain `RA` or drizzle `DZ`: drops with a diameter of 0.5 mm or more are rain.
- Fog `FG` or mist `BR`: fog is less than 1000 meters visibility.
- Mist `BR` or haze `HZ`: if the humidity is more than 80% it is mist.
- Hail `GR` or small hail `GS`: with hail the grains are larger than 5 mm.
- Low drifting `DR` or blowing `BL`: low wind is less than 2 meters.
**Clouds**
The cloud cover is listed per layer. Per layer you see:
- The cover in octals (1/8 parts):
   - `FEW` few clouds: 1/8th or 2/8th cover
   - `SCT` scattered clouds: 3/8th or 4/8th cover
   - `BKN` broken clouds: 5/8th to 7/8th cover
   - `OVC` overcast clouds: 8/8th cover
- The height of the bottom of the cloud (cloud base) in hundreds of feet above the airport: `FEW007` means a cloud base of 700 ft above site height. If no cloud base can be established, a vertical view can be indicated. For example: `VV001` means a vertical view of 100 ft.
- Significant cloud cover: cumulonimbus `CB` or towering cumulus `TCU`. Other types of clouds are not mentioned. If the type of clouds cannot be measured, there are 3 slashes behind it. Example: `BKN013///`
- Special codes:
   - `NSC` No significant cloud cover. This means that there is no cloud below the 5,000 ft, but there is above it. That cloud cover is not cumulonimbus or towering cumulus.
   - `SKC` No cloud cover (Determined by meteorologist)
   - `NCD` No clouds measured (Automatic weather stations)
   - `CLR` No cloud cover detected below 12,000 ft (Automatic weather stations)
   - `OVC` overcast clouds: 8/8th cover
**Note**
Cloud base is also used for the bottom layer of clouds that has a minimum of 5/8 coverage. When we talk about a cloud base of 3,000 ft, we usually mean that there is broken or more cloud from 3,000 ft.
**Example**
`FEW007 BKN014CB BKN017` means three cloud layers:
- Few clouds at an altitude of 700 ft
- Broken clouds at an altitude of 1,400 ft, with cumulonimbus clouds
- Broken clouds at an altitude of 1,700 ft
 The cloud base, broken or more, is 1,400 ft
**CAVOK**
`CAVOK` means that clouds and visibility are okay ("clouds and visibility OK"). CAVOK is a special code, it replaces visibility, clouds and weather. To be CAVOK these conditions must be met:
- Visibility is more than 10 km+
- There are no clouds below 5,000 ft
- There is no significant cloud cover (cumulonimbus or towering cumulus)
- No significant weather
 With CAVOK, our example would look a lot shorter. That's why pilots sometimes jokingly put a rules next to the METAR to see if the weather is nice:
`METAR EHLE 280925Z 21009G19KT 060V130 CAVOK 02/M01 Q1001`
**Temperature**
Temperature and dew point are always stated in degrees Celsius in a METAR or TAF. `02/M01` means that the temperature is 2 C and the dew point is -1 C. Negative numbers are preceded by an M.
**Pressure**
In the METAR you will also find the air pressure at the mean sea level (QNH). This is calculated by recalculating the air pressure at terrain height (QFE) back to sea level. Air pressure can be expressed in inches of mercury (preceded by an A) or hectopascals (preceded by a Q).
- `A2994` means air pressure of 29.94 inHg.
- `Q1001` means an air pressure of 1001 hPa.
**Trends**
At the end of the METAR you will find information about the trend.
- `BECMG` is followed by a permanent change in the same coding as earlier in the METAR. For example: `BECMG 6000` means that the view will be 6 km.
- `TEMPO` is followed by a temporary change, less than an hour. For example: `TEMPO BKN007` means that there is a temporary cloud layer on 700 ft.
- `PROB30` is followed by a change with a probability of 30%. A change with less probability is not mentioned at all. Example: 30% chance that the view is temporary 200 m: `PROB30 TEMPO 0200`.
- `PROB40` is followed by a change with a probability of 40%. A change with a higher probability is listed without addition.
- `FM`, `TL` and `AT` is followed by a change occurring from, to or on, respectively, said time. For example: `FM1200 6000` means that the visibility will be 6 km from 12:00 UTC.
**Military color codes**
Military fields often use color codes instead of trends. These color codes summarize the visibility and cloud base. The trend is then displayed in the form of a color code. `GRN AMB TEMPO RED` means the color code is now Green, but it will turn Amber for the next 2 hours and will be temporarily Red. If the code is preceded by `BLACK` it means that the field is closed. `BLACKGRN` means a closed field, despite the fact that it would be a code Green again.
| Code | Visibility | Ceiling |
|---|---|---|
|**BLU** Blue | > 8 km | > 2,500 ft |
|**WHT** White | 5 - 8 km | 1,500 - 2,500 ft |
|**GRN** Green | 3.7 - 5 km | 700 - 1,500 ft |
|**YLO** Yellow | 1.8 - 3.7 km | 300 - 700 ft |
|**AMB** Amber | 800 m - 1.8 km | 200 - 300 ft |
|**RED** Red | < 800 m | < 200 ft |
**Information about the sea**
Weather stations located at sea can report the temperature of the sea water and the height of the waves. `W12/S8` means that it is sea water 12 C with heavy waves. The height of the waves is indicated from `0` (light) to `9` (heavy).
**Wind Shear**
If there is wind shear at one or all of the runways:
- `WS R23` means that wind shear is reported for runway 23.
- `WS ALL RWY` means that wind shear is reported for all runways.
**Runway conditions**
If it has snowed, the condition of the runways can be reported in METAR. A code is then added indicating the type of cover, thickness and braking capacity. For example, this code looks like this: `R05/629294`.
- `R05` is the runway
- `6` is the type of deposit
- `2` is the coverage
- `92` is the thickness
- `94` is the braking capacity
 This code means that 11-25% of track 05 is covered with a 10 cm layer of mud and the braking capacity is moderate to good.
These are all codes used:
**Type of deposit**
|**0** |**clear and dry** |
| ----- | ------------------------ |
|**/** | not reported |
|**1** | damp |
|**2** | wet or water patches |
|**3** | rime or frost covered |
|**4** | dry snow |
|**5** | wet snow |
|**6** | slush |
|**7** | ice |
|**8** | compacted or rolled snow |
|**9** | frozen ruts or ridges |
**Coverage**
|**/** | |
| ----- | ---------------- |
|**1** | 10% or less |
|**2** | from 11% to 25% |
|**5** | from 26% to 50% |
|**9** | from 51% to 100% |
**Thickness**
|**//** | |
| ------ | ------------- |
|**00** | less than 1mm |
|**92** | 10 cm |
|**93** | 15 cm |
|**94** | 20 cm |
|**95** | 25 cm |
|**96** | 30 cm |
|**97** | 35 cm |
|**98** | 40cm or more |
|**99** | closed |
**Braking capacity**
|**91** |**poor** |
| ------ | ------------------ |
|**92** | medium/poor |
|**93** | medium |
|**94** | medium/good |
|**95** | good |
|**99** | figures unreliable |
In addition to these codes, there is a special code `R/SNOCLO`. This means that the field is closed due to snow or ice.
**Color codes**
The color codes represent the different flight categories. These are derived from the FAA rules. The color codes you see on the site are calculated based on the visibility values and cloud base. These color codes do not tell anything about the temperature, wind, type of clouds and other warnings.
| Code | Visibility | Ceiling |
| --- | --- | --- |
|**VFR** Visual Flight Rules | > 8 km | > 3,000 ft |
|**MVFR** Marginal VFR | 5-8 km | 1,000-3,000 ft |
|**IFR** Instrument Flight Rules | 1.5-5 km | 500-1,000 ft |
|**LIFR** Low IFR | < 1.5 km | < 500 ft |
|**UNKN** | Incomplete or expired data | |
[This is how you read a METAR](https://metar-taf.com/explanation)

<!-- Merged from duplicate -->

---
type: Aviation-Reference
related_to:
  - Magenta Debrief
---

Metar: Readings
[This is how you read a METAR](https://metar-taf.com/explanation)
**METAR/SPECI**
Indicates whether it is a regular observation \METAR\ or extra (SPECI). The SPECI is not much used anymore because most weather stations issue a new observation every half hour.
**Place**
The ICAO code of the airport / weather station. Usually this is a 4 letter code. Example: \EHLE\ means \Lelystad Airport\.
**Day and time**
The first 2 digits indicate the day of the month. Followed by the 2 digits of the hour (00-23) and the minutes (00-59). Z is the abbreviation for Zero, time zone 0 is Greenwich Mean Time (UTC). In the NATO phonetic alphabet, the Z is pronounced Zulu, which is why it is also called Zulu time. Note that both the day and time are displayed in UTC / zulu time. This is done to avoid misunderstandings. So \280925Z\ means the 28th day of the month at 9:25 UTC.
**COR/AUTO/NIL**
COR means that this observation replaces a previously drawn up report. \AUTO\ means that the observation is done automatically. Automatic observations are more limited than manually generated observations. NIL means that no data is known.
**Wind**
\10009G19KT 060V130\ means that the mean wind direction is 100, variable between 60 and 130. The average wind speed is 9 knots (09) with peaks up to 19 knots (KT). The average wind speed is 9 knots (09) with peaks up to 19 knots (KT).
- The wind direction and strength are averaged over the last 10 minutes.
- Outliers are only listed if they are 10 knots above average.
- A variable wind direction is only reported if it deviates more than 10 from the mean.
- The wind direction is shown on a scale from 000-350 degrees, rounded to tens of degrees. Where 000 is the north, 090 is the east, 180 is the south and 270 is the west.
- The wind is measured at a height of 10 m. A METAR therefore does not provide information about high winds, these are usually a lot stronger. This wind information is therefore not useful for navigation.
- In some cases \VRB01KT\ is indicated instead of the wind: if the wind speed is 3 knots or less, the wind is more than 3 knots but varies with more than 180 or when the direction cannot be determined.
- If there is no wind then \00000KT\ is displayed.
- If both the wind direction and the wind speed cannot be determined \/////KT\
 In addition to knots, the wind speed can also be indicated in meters per second (MPS) or miles per hour (MPH).
**Visibility**
The visibility shown in the METAR is an average, minimum visibility. \5000\ means visibility is 5000 meters. If visibility is less than 1000 meters, the number will be added to 4 characters.\
This is to avoid confusion with the imperial system. Visibility can also be indicated in miles or parts thereof: \3SM\ means the visibility is 3 miles (statute mile). \3/4SM\ means visibility is 0.75 miles.
- Visibility can be different in different directions. In that case the lowest measured visibility is always displayed. If visibility is only measured in one direction then \NDV\ (Non Directional Variation) is added to the code.
- Visibility can also be listed per direction. \1500SW 2000NE\ means the visibility to the southwest is 1500 meters and 2000 meters to the northeast.
- In case of poor visibility, the direction can also be displayed per runway. This is also called the RVR (Runway Visual Range). An RVR is usually not reported until visibility is less than 2000 meters.
 Examples of an RVR:
- \R23/0500\ visibility for runway 23 is 500 meters
- \R23/P0500\ visibility for runway 23 is more (P) than 500 meters
- \R23/M0500\ visibility for runway 23 is less (M) than 500 meters
- \R23/0500V1500\ visibility for runway 23 varies between 500 and 1500 meters
- \R23/0500U\ visibility for runway 23 is 500 meters but increases (U)
- \R23/0500D\ visibility for runway 23 is 500 meters but decreases (D)
**Weather phenomena**
\-RA\ means that there is currently light rain. This is a combination of RA (rain) and - (light intensity). The codes from the lists below can be combined with each other:
**Intensity**
| | |
| ------ | --------------- |
| + | heavy |
|**-** | light |
|**RE** | recent |
|**VC** | in the vicinity |
**Characteristic**
|**BC** |**patches of** |
| ------ | -------------- |
|**DR** | low drifting |
|**MI** | shallow |
|**PR** | partial |
|**BL** |**blowing** |
| ------ | ------------- |
|**FZ** | freezing |
|**SH** | showers |
|**TS** | thunderstorms |
**Type**
|**BR** |**mist** |
| ------ | --------------- |
|**DS** | dust storm |
|**DU** | widespread dust |
|**DZ** | drizzle |
|**FC** | funnel cloud |
|**FG** | fog |
|**FU** | smoke |
|**GR** | hail |
|**GS** |**small hail** |
| ------ | -------------- |
|**HZ** | haze |
|**IC** | ice crystals |
|**PE** | ice pellets |
|**PO** | sand whirls |
|**PY** | spray |
|**RA** | rain |
|**SA** | sand |
|**SG** |**snow grains** |
| ------ | --------------------- |
|**SN** | snow |
|**SQ** | squalls |
|**SS** | sand storm |
|**UP** | unknown precipitation |
|**VA** | volcanic ash |
**Remarks**
- The most significant form of precipitation is listed first. Example: \GRRA\ means more hail than rain, contrary to: \RAGR\ with more rain than hail.
- The intensity and whether it is showery \SH\ is only used in combination with precipitation. For example when there are showers with heavy rain: \+SHRA\
- If no intensity is mentioned, it is moderate precipitation.
- \MI\, \BC\ and \PR\ are only used for fog: ground fog, fog banks and partial aerodrome cover.
- Freezing \FZ\ is only used in conjunction with rain \RA\, drizzle \DZ\ and fog \FG\. This means that it will immediately freeze if it comes into contact with a solid surface.
- Low drifting \DR\ and low drifting \BL\ are only used in conjunction with snow \SN\, sand \SA\ and widespread dust \DU\.
**Differences**
- Rain \RA\ or drizzle \DZ\: drops with a diameter of 0.5 mm or more are rain.
- Fog \FG\ or mist \BR\: fog is less than 1000 meters visibility.
- Mist \BR\ or haze \HZ\: if the humidity is more than 80% it is mist.
- Hail \GR\ or small hail \GS\: with hail the grains are larger than 5 mm.
- Low drifting \DR\ or blowing \BL\: low wind is less than 2 meters.
**Clouds**
The cloud cover is listed per layer. Per layer you see:
- The cover in octals (1/8 parts):
 - \FEW\ few clouds: 1/8th or 2/8th cover
 - \SCT\ scattered clouds: 3/8th or 4/8th cover
 - \BKN\ broken clouds: 5/8th to 7/8th cover
 - \OVC\ overcast clouds: 8/8th cover
- The height of the bottom of the cloud (cloud base) in hundreds of feet above the airport: \FEW007\ means a cloud base of 700 ft above site height. If no cloud base can be established, a vertical view can be indicated. For example: \VV001\ means a vertical view of 100 ft.
- Significant cloud cover: cumulonimbus \CB\ or towering cumulus \TCU\. Other types of clouds are not mentioned. If the type of clouds cannot be measured, there are 3 slashes behind it. Example: \BKN013///\
- Special codes:
 - \NSC\ No significant cloud cover. This means that there is no cloud below the 5,000 ft, but there is above it. That cloud cover is not cumulonimbus or towering cumulus.
 - \SKC\ No cloud cover (Determined by meteorologist)
 - \NCD\ No clouds measured (Automatic weather stations)
 - \CLR\ No cloud cover detected below 12,000 ft (Automatic weather stations)
 - \OVC\ overcast clouds: 8/8th cover
**Note**
Cloud base is also used for the bottom layer of clouds that has a minimum of 5/8 coverage. When we talk about a cloud base of 3,000 ft, we usually mean that there is broken or more cloud from 3,000 ft.
**Example**
\FEW007 BKN014CB BKN017\ means three cloud layers:
- Few clouds at an altitude of 700 ft
- Broken clouds at an altitude of 1,400 ft, with cumulonimbus clouds
- Broken clouds at an altitude of 1,700 ft
 The cloud base, broken or more, is 1,400 ft
**CAVOK**
\CAVOK\ means that clouds and visibility are okay ("clouds and visibility OK"). CAVOK is a special code, it replaces visibility, clouds and weather. To be CAVOK these conditions must be met:
- Visibility is more than 10 km+
- There are no clouds below 5,000 ft
- There is no significant cloud cover (cumulonimbus or towering cumulus)
- No significant weather
 With CAVOK, our example would look a lot shorter. That's why pilots sometimes jokingly put a rules next to the METAR to see if the weather is nice:\
\METAR EHLE 280925Z 21009G19KT 060V130 CAVOK 02/M01 Q1001\
**Temperature**
Temperature and dew point are always stated in degrees Celsius in a METAR or TAF. \02/M01\ means that the temperature is 2 C and the dew point is -1 C. Negative numbers are preceded by an M.
**Pressure**
In the METAR you will also find the air pressure at the mean sea level (QNH). This is calculated by recalculating the air pressure at terrain height (QFE) back to sea level. Air pressure can be expressed in inches of mercury (preceded by an A) or hectopascals (preceded by a Q).
- \A2994\ means air pressure of 29.94 inHg.
- \Q1001\ means an air pressure of 1001 hPa.
**Trends**
At the end of the METAR you will find information about the trend.
- \BECMG\ is followed by a permanent change in the same coding as earlier in the METAR. For example: \BECMG 6000\ means that the view will be 6 km.
- \TEMPO\ is followed by a temporary change, less than an hour. For example: \TEMPO BKN007\ means that there is a temporary cloud layer on 700 ft.
- \PROB30\ is followed by a change with a probability of 30%. A change with less probability is not mentioned at all. Example: 30% chance that the view is temporary 200 m: \PROB30 TEMPO 0200\.
- \PROB40\ is followed by a change with a probability of 40%. A change with a higher probability is listed without addition.
- \FM\, \TL\ and \AT\ is followed by a change occurring from, to or on, respectively, said time. For example: \FM1200 6000\ means that the visibility will be 6 km from 12:00 UTC.
**Military color codes**
Military fields often use color codes instead of trends. These color codes summarize the visibility and cloud base. The trend is then displayed in the form of a color code. \GRN AMB TEMPO RED\ means the color code is now Green, but it will turn Amber for the next 2 hours and will be temporarily Red. If the code is preceded by \BLACK\ it means that the field is closed. \BLACKGRN\ means a closed field, despite the fact that it would be a code Green again. | Code | Visibility | Ceiling | |---|---|---| |**BLU** Blue | > 8 km | > 2,500 ft | |**WHT** White | 5 - 8 km | 1,500 - 2,500 ft | |**GRN** Green | 3.7 - 5 km | 700 - 1,500 ft | |**YLO** Yellow | 1.8 - 3.7 km | 300 - 700 ft | |**AMB** Amber | 800 m - 1.8 km | 200 - 300 ft | |**RED** Red | < 800 m | < 200 ft |
**Information about the sea**
Weather stations located at sea can report the temperature of the sea water and the height of the waves. \W12/S8\ means that it is sea water 12 C with heavy waves. The height of the waves is indicated from \0\ (light) to \9\ (heavy).
**Wind Shear**
If there is wind shear at one or all of the runways:
- \WS R23\ means that wind shear is reported for runway 23.
- \WS ALL RWY\ means that wind shear is reported for all runways.
**Runway conditions**
If it has snowed, the condition of the runways can be reported in METAR. A code is then added indicating the type of cover, thickness and braking capacity. For example, this code looks like this: \R05/629294\.
- \R05\ is the runway
- \6\ is the type of deposit
- \2\ is the coverage
- \92\ is the thickness
- \94\ is the braking capacity
This code means that 11-25% of track 05 is covered with a 10 cm layer of mud and the braking capacity is moderate to good.
These are all codes used:
**Type of deposit**
|**0** |**clear and dry** |
| ----- | ------------------------ |
|**/** | not reported |
|**1** | damp |
|**2** | wet or water patches |
|**3** | rime or frost covered |
|**4** | dry snow |
|**5** | wet snow |
|**6** | slush |
|**7** | ice |
|**8** | compacted or rolled snow |
|**9** | frozen ruts or ridges |
**Coverage**
|**/** | |
| ----- | ---------------- |
|**1** | 10% or less |
|**2** | from 11% to 25% |
|**5** | from 26% to 50% |
|**9** | from 51% to 100% |
**Thickness**
|**//** | |
| ------ | ------------- |
|**00** | less than 1mm |
|**92** | 10 cm |
|**93** | 15 cm |
|**94** | 20 cm |
|**95** | 25 cm |
|**96** | 30 cm |
|**97** | 35 cm |
|**98** | 40cm or more |
|**99** | closed |
**Braking capacity**
|**91** |**poor** |
| ------ | ------------------ |
|**92** | medium/poor |
|**93** | medium |
|**94** | medium/good |
|**95** | good |
|**99** | figures unreliable |
In addition to these codes, there is a special code \R/SNOCLO\. This means that the field is closed due to snow or ice.
**Color codes**
The color codes represent the different flight categories. These are derived from the FAA rules. The color codes you see on the site are calculated based on the visibility values and cloud base. These color codes do not tell anything about the temperature, wind, type of clouds and other warnings.
|**Code** |**Visibility** |**Ceiling** |
| ------------------------------- | -------------------------- | -------------- |
|**VFR** Visual Flight Rules | > 8 km | > 3,000 ft |
|**MVFR** Marginal VFR | 5-8 km | 1,000‑3,000 ft |
|**IFR** Instrument Flight Rules | 1.5-5 km | 500‑1,000 ft |
|**LIFR** Low IFR | < 1.5 km | < 500 ft |
|**UNKN** | Incomplete or expired data | |