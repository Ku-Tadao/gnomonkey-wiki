# Gearscape

<div class="mbox" markdown="1" data-search-exclude>
This article is compiled from the videos of [GnomonkeyRS](https://www.youtube.com/@GnomonkeyRS). It records what Gnomonkey said, with sources, not verified game fact. See [About](index.md).
</div>

<div class="infobox" markdown="1">
<div class="infobox-title">Gearscape</div>
<div class="infobox-image" markdown="1">![Gearscape](https://i.ytimg.com/vi/yswYFNgsA6s/mqdefault.jpg)</div>

| | |
|---|---|
| **Type** | Other |
| **Videos** | 11 (first 2024-05-06, latest 2025-09-26) |
| **Main source** | [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md) |
</div>

Gearscape (gearscape.net) is the OSRS DPS calculator and best-setup website that Gnomonkey uses for nearly all of his gear calculations from 2024 onward. He calls it the best tool for working out how to gear for combat, far more feature rich than the OSRS Wiki's DPS calculator, and says it makes the wiki's gear setups obsolete.

[TOC]

## Opinion and stance

- In May 2024 he wrote that with Gearscape the OSRS Wiki is pretty obsolete for gear setups and "can be thrown in the trash" for them, and said the video was not sponsored[^zHxGjKaeTNU-0][^zHxGjKaeTNU-1058]. He says it can completely replace the wiki's downgrade charts and gives the exact best DPS for any gp budget[^zHxGjKaeTNU-1058]. See also [OSRS Wiki downgrade gear charts](Opinion_OSRS_Wiki_downgrade_gear_charts.md).
- He calls it the best DPS calculator available, even better than the Oblivion spreadsheet, and says it has replaced everything else[^9cYL7QTJ5G8-479]. In July 2024 he said he did all of his wiki guide videos with it and that it is infinitely more useful than any wiki setup and constantly updated[^e0y_auD9JhY-1261].
- In September 2025 he still prefers it to the OSRS Wiki's calculator, which he also calls really good, because it is far more feature rich[^yswYFNgsA6s-0].
- The developers are described as friendly, active in chat and Discord, and quick to fix bugs; in July 2024 he said they were working on open-sourcing the tool and more RuneLite integration[^WvmEY9v6AnI-421][^e0y_auD9JhY-1840]. In 2025 he credits a developer called Kenny with adding the average-hit defence-drain figure for godswords a day after he suggested it[^yswYFNgsA6s-1462].
- He argues it can be used to quickly check claims such as "use a Bofa on Baba" rather than repeating misconceptions[^yswYFNgsA6s-1522], and advises checking the calculator rather than going blind into a raid[^vEs4Qvs_Rag-343].

## DPS calculator

- Gear is entered slot by slot, then the monster, combat style, potions, prayers, spell and toggles such as being on a Slayer task; the chosen style changes the DPS[^yswYFNgsA6s-147]. Setups can be saved under a name, reloaded and shown against the current monster[^yswYFNgsA6s-207], and any number of setups can be compared[^zHxGjKaeTNU-648].
- The small lock in the top right is the most important button; unlocking lets the layout be customised, setups be duplicated or removed, and control panels (green when movable, red when not) be dragged to the side so they apply to every setup. Missing features are probably hidden under the lock, and there is a tutorial button many miss[^yswYFNgsA6s-62][^yswYFNgsA6s-88][^yswYFNgsA6s-119].
- A share preset button, added by July 2024, generates a link giving someone the same calculator layout[^e0y_auD9JhY-1806].
- **Stats and toggles:** levels can be imported by player name via Wise Old Man (which may require the Wise Old Man [RuneLite](RuneLite_plugins.md) plugin to upload first)[^e0y_auD9JhY-1294][^yswYFNgsA6s-296], with toggles for being on task, in the Wilderness, hard Seers' diary done or using sunfire runes[^e0y_auD9JhY-1294]. The stats panel includes Mining level (used by [Chambers of Xeric](Chambers_of_Xeric.md) mining guardians) and a second current-health field for [Dharok's armour](Dharok's_armour.md)[^yswYFNgsA6s-296].
- **Monsters:** boss input includes team size, difficulty modifiers, stats, weaknesses and tags (for example [Kephri](Kephri.md) as a [Tombs of Amascut](Tombs_of_Amascut.md) boss so the shadow and fang are multiplied), and custom monsters can be entered to test future content[^e0y_auD9JhY-1320]. The monster DPS output also shows how hard monsters hit the player in tank gear, useful at [Nex](Nex.md) or the [God Wars Dungeon](God_Wars_Dungeon.md)[^e0y_auD9JhY-1818]. Default numbers can mislead because monsters have states and variants, so the specific enemy toggle should be checked[^yswYFNgsA6s-1288].
- **Specials:** the calculator does not assume a spec is used, so the user toggles between "poke" and "spec"[^yswYFNgsA6s-270].
- **Potions and prayers:** potions are removed by right-clicking them, which shows how much being potted matters; raid potions, overloads and smelling salts are included[^yswYFNgsA6s-324]. Prayers can be compared (for example Chivalry against Piety), with the difference mostly accuracy[^yswYFNgsA6s-358].
- **Area spells:** single-target DPS is multiplied by the number of targets, which he gives as why Ice Barrage is so strong[^yswYFNgsA6s-385].
- **Effects modelled:** Ruby and Diamond bolt procs, [Atlatl](Atlatl.md) burn damage, multi-hit weapons, scythe size scaling, Venator bow multi-target hits and chinchompas hitting the target[^yswYFNgsA6s-506]. Variants exist for weapons, bosses and armour, so only XP-granting damage can be computed, such as Atlatl without Eclipse burn[^yswYFNgsA6s-533].
- **Advanced toggles:** a quest tab with toggles such as being on task, and an advanced section with Soul reaper axe stacks, distance and a flinching toggle that models attacking only when stepping in (for example against [Kalphite Queen](Kalphite_Queen.md))[^yswYFNgsA6s-787]. For [Verzik Vitur](Verzik_Vitur.md) a scythe toggle models never being bounced, losing one attack tick in 16[^yswYFNgsA6s-815]. He says Arclight is awful on [Duke Sucellus](Duke_Sucellus.md) because of the forced five-tick, which the toggle shows[^yswYFNgsA6s-842].
- **Ruby bolts and health:** ruby bolts do less damage per hit point below 500 of the target, and a button accounts for monster health; it does not work on the Gemstone Crab so he demonstrates it on [Zebak](Zebak.md)[^yswYFNgsA6s-561]. Against Zebak with salts and bone dagger drain it showed the Atlatl far stronger than a crossbow at full health[^yswYFNgsA6s-590], and with a [Zaryte crossbow](Zaryte_crossbow.md) it said to use the crossbow until Zebak reaches 463 health before swapping[^yswYFNgsA6s-621].
- **Detailed mode:** shows prices and stats on hover, totals, and the strength bonus that can be gained or lost before the max hit changes[^yswYFNgsA6s-679]. He says that if more than four extra strength bonus is needed for a higher max hit, adding strength probably will not help[^yswYFNgsA6s-706].
- **Groups tab:** puts a whole raid or area into the calculator at once and shows the best weapon per boss[^vEs4Qvs_Rag-284][^yswYFNgsA6s-651]. In the [Inferno](Inferno.md) he found the Zaryte crossbow only wins against Jad and Zuk[^yswYFNgsA6s-651]. In Tombs of Amascut he found the blowpipe better than the [Osmumten's fang](Osmumten's_fang.md) on Akkha's shadows, the fang better on the obelisk and very close on Wardens P3[^vEs4Qvs_Rag-284].
- **Leagues:** the developer adds relic unlocks and area restrictions, so [Leagues](Leagues.md) setups can be checked from the bank; he calls this probably its most powerful use and plans to use it a lot for [Gridmaster](Gridmaster.md)[^yswYFNgsA6s-1434].

### Worked examples

- Gemstone Crab (2025): a strength amulet beat an amulet of glory because the extra strength outweighed lost accuracy[^yswYFNgsA6s-237]; the [Dragon dagger](Dragon_dagger.md) special (18 DPS) and Arcane blade special came out extremely close with the dagger slightly ahead[^yswYFNgsA6s-237]; Ibans blast with early mage gear gave about 4.27 DPS (26 max hit, Augury), about 4.09 without prayer[^yswYFNgsA6s-385].
- He calls the Eclipse atlatl an amazing, underrated early weapon using no ammunition[^yswYFNgsA6s-413]. In black dragonhide with no combat potion it reached 7.45 DPS, almost double the staff[^yswYFNgsA6s-413]; 7.96 with a Berserker helm and 9.33 after a super strength potion, and more with the set's burn damage[^yswYFNgsA6s-478]. Atlatl scales with strength bonus, so a strength amulet can reduce its DPS while a Fighter torso raised it[^yswYFNgsA6s-447]. See [Eclipse atlatl](Eclipse_atlatl.md).
- Tormented Demon: about 60% of the kill they are 100% accurate, so mage looks best, but inaccurate high-DPS options such as Atlatl and Dragon dagger specs become very good[^yswYFNgsA6s-1314]. See [Tormented Demon](Tormented_Demon.md).
- [Yama](Yama.md): the default calculation with a [Tumeken's shadow](Tumeken's_shadow.md) assumes negative 30 magic defence for one cast; afterwards mage tank mode gives plus 60 magic defence, an extra 90, and the realistic DPS (he cites 9.12) is much lower[^yswYFNgsA6s-1347]. He says the default setting is not always what is wanted and context, including Slayer contract toggles, matters[^yswYFNgsA6s-1374].

## Best Setup tool

- Takes a gp budget, a cash stack or a bank, and outputs the best gear for a given monster[^zHxGjKaeTNU-648][^yswYFNgsA6s-903]. Output shows DPS, max hit, accuracy, average hit, total cost, and the prayer, potion and style it expects (for example super combat, aggressive stab and Piety); setups can be exported as a bank tab or saved and imported into RuneLite[^e0y_auD9JhY-1504][^9cYL7QTJ5G8-457][^yswYFNgsA6s-1169]. It also gives an expected time to kill that excludes downtime and specials[^9cYL7QTJ5G8-414].
- **Ironman and Wilderness use:** an Ironman can import owned items, a whole bank through the Bank Memory plugin (copy item data to clipboard, then "import from RuneLite") or a bank tag tab, and the "only include selected items" toggle ignores the cash stack, making the search about 10 seconds[^e0y_auD9JhY-1408][^yswYFNgsA6s-1202]. For the Wilderness it takes a number of expensive items risked (typically four) and a value per item, and 11 assumes risk is no worry[^e0y_auD9JhY-1444]. See [Ironman Mode](Ironman_Mode.md).
- **Exclude and include:** untradeable items, prayers not owned (such as Infernal cape, quivers, Rigour, Augury) and Zamorakian brews should be excluded; the include tab is mainly for Ironmen, set to "mark free" for mains and "only include" for Irons[^e0y_auD9JhY-1378]. Untradeables otherwise count as having no value[^zHxGjKaeTNU-678]. Excluding the Infernal cape makes it recommend the fire cape[^zHxGjKaeTNU-1089], and unneeded attack styles can be turned off to speed the search of a minute or two[^yswYFNgsA6s-1053].
- **Limits:** it gives the best setup at one boss only and cannot find switches across multiple bosses, so full raid setups ([Chambers of Xeric](Chambers_of_Xeric.md), [Tombs of Amascut](Tombs_of_Amascut.md)) still need a calculator and thought; he doubts multi-boss support will be added because it would slow calculation[^e0y_auD9JhY-1572][^yswYFNgsA6s-903]. It ignores context and maximises DPS only, so it can recommend paper armour or Void against a boss like [Vardorvis](Vardorvis.md) where that is a bad idea[^yswYFNgsA6s-961]. [Lightbearer](Lightbearer.md) adds only to spec DPS, so Best Setup will not choose it; slots can be locked to force an item[^yswYFNgsA6s-1261][^e0y_auD9JhY-1504].
- Baba example (Tombs of Amascut raid level 300, path level 1, one player): smelling salts excluded, bone dagger or BGS damage set to the 20 cap, which Gearscape knows even if a larger number is entered[^yswYFNgsA6s-994]. With 100m the ranged option reached 7.8 DPS against 7 for the crossbow; imported into the calculator it showed 7.37 in a best case, and Atlatl and mage were much lower (about 4.4 for the Atlatl)[^yswYFNgsA6s-1111]. See [Ba-Ba](Ba-Ba.md).

## Use in the Wiki Guides videos

In the May 2024 and September 2025 [Wiki Guides](Wiki_Guides_challenge_series.md) videos he used it to build budget setups to replace the wiki's downgrade setups.

| Date | Boss | Result |
|---|---|---|
| 2024-05-06 | [Phosani's Nightmare](Phosani's_Nightmare.md) | At a 15 million gp budget it recommended Maracas, 7.3 DPS[^zHxGjKaeTNU-678] |
| 2024-05-06 | [Giant Mole](Giant_Mole.md) | 100 million gp gave mixed hide armour with a fang, which he says looks goofy but will be correct every time[^zHxGjKaeTNU-1058] |
| 2024-05-10 | [Whisperer](Whisperer.md) | Expected time to kill of 140 seconds for his budget setup[^9cYL7QTJ5G8-414] |
| 2024-05-12 | [K'ril Tsutsaroth](K'ril_Tsutsaroth.md) | 6.7 million gp gave a void-based setup; max hit 43 (from 30), mage attack bonus 131 (from 88), accuracy 34% to 50%, max hit 37 to 43, average hit 6.4 to 10.7, DPS up 50%, kill time 2 minutes to 75 seconds[^_nMz6X90hb0-377][^_nMz6X90hb0-462][^_nMz6X90hb0-521][^_nMz6X90hb0-530][^_nMz6X90hb0-538] |
| 2024-05-18 | [Vorkath](Vorkath.md) | With ranged and mage excluded at the wiki setup's budget it left about 5 million gp to spare[^WvmEY9v6AnI-378] |
| 2024-05-20 | Giant Mole | At 60 stats it suggested a dragon sword and an unimbued treasonous ring; he had not known the dragon sword was an option and calls its special very good[^NSiTMTXHDXQ-481][^NSiTMTXHDXQ-548] |
| 2025-09-01 | [Yama](Yama.md) | 47 million gp, enrage phase: basically the wiki setup with an [Emberlight](Emberlight.md) and strength upgrades, so no spec weapon is needed[^KIII4sXUDTk-936][^KIII4sXUDTk-970] |
| 2025-09-03 | [Phantom Muspah](Phantom_Muspah.md) | The wiki's worst setup priced at 443 million gp; Gearscape gave almost full max [Inquisitor's armour](Inquisitor's_armour.md), with the [Soulreaper axe](Soulreaper_axe.md) about 0.4 worse[^vuti6ln_q10-403][^vuti6ln_q10-471] |
| 2025-09-06 | Vorkath | Old wiki setup priced at about 400M; at 53M it gave a fire cape and [Burning claws](Burning_claws.md) setup, about 73 to 76 seconds plus immunity to specials, roughly 90 seconds in total[^qCsJAdpSeTU-568][^qCsJAdpSeTU-626][^qCsJAdpSeTU-714] |

- For K'ril it would not allow forcing Demon Bane spells and preferred an ancient sceptre; Infinity kits cost 160k each[^_nMz6X90hb0-391][^_nMz6X90hb0-447].
- He also used it for [Tombs of Amascut](Tombs_of_Amascut.md) DPS per Wardens phase[^zHxGjKaeTNU-648], and in the Vorkath V2 video said a good melee Vorkath setup is crazy cheap these days[^qCsJAdpSeTU-652].

## Revision history

| Date | Video | Change |
|---|---|---|
| 2025-09-26 | [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md) | Added a full walkthrough of the DPS calculator, groups tab, Best Setup tool, Ironman import, Leagues use and example calculations. |
| 2025-09-06 | [WIKI GUIDES - VORKATH V2 (OSRS)](videos/2025-09-06_qCsJAdpSeTU.md) | Added Vorkath V2 example (53M budget, about 90 seconds total). |
| 2025-09-03 | [WIKI GUIDES - MELEE MUSPAH (OSRS)](videos/2025-09-03_vuti6ln_q10.md) | Added Phantom Muspah example (443M wiki setup versus Inquisitor's budget set). |
| 2025-09-01 | [WIKI GUIDES - YAMA MELEE AND MAGE (OSRS)](videos/2025-09-01_KIII4sXUDTk.md) | Added Yama 47M example and bank import for personal setups. |
| 2024-10-24 | [EASY 300 ToA Budget Guide (OSRS)](videos/2024-10-24_vEs4Qvs_Rag.md) | Added groups tab for Tombs of Amascut and blowpipe versus fang comparisons. |
| 2024-07-07 | [Ultimate Account Building Guide (OSRS)](videos/2024-07-07_e0y_auD9JhY.md) | Added import, exclude and include, Ironman bank, Wilderness risk, lock and share preset features, and the single-boss limitation. |
| 2024-05-20 | [WIKI GUIDES - GIANT MOLE (OSRS)](videos/2024-05-20_NSiTMTXHDXQ.md) | Added Giant Mole example at 60 stats (dragon sword). |
| 2024-05-18 | [WIKI GUIDES - VORKATH (OSRS)](videos/2024-05-18_WvmEY9v6AnI.md) | Added Vorkath example and developer feedback note. |
| 2024-05-12 | [WIKI GUIDES - KRIL/ZAMMY (OSRS)](videos/2024-05-12__nMz6X90hb0.md) | Added K'ril Tsutsaroth before-and-after figures. |
| 2024-05-10 | [WIKI GUIDES - Whisperer](videos/2024-05-10_9cYL7QTJ5G8.md) | Added expected time to kill, bank tab export and the Oblivion spreadsheet comparison. |
| 2024-05-06 | [WIKI GUIDES: Phosani's Nightmare (OSRS)](videos/2024-05-06_zHxGjKaeTNU.md) | Page created: Gearscape as a replacement for the wiki's gear setups, with the Phosani's Nightmare and Giant Mole examples. |
## See also

* [Wiki gear setup template](Wiki_gear_setup_template.md)
* [Wiki Guides challenge series](Wiki_Guides_challenge_series.md)
* [Opinion: OSRS Wiki downgrade gear charts](Opinion_OSRS_Wiki_downgrade_gear_charts.md)
* [Void Knight equipment](Void_Knight_equipment.md)
* [Osmumten's fang](Osmumten's_fang.md)
* [Vorkath](Vorkath.md)

## References

///Footnotes Go Here///
[^zHxGjKaeTNU-0]: [WIKI GUIDES: Phosani's Nightmare (OSRS)](videos/2024-05-06_zHxGjKaeTNU.md), 2024-05-06. [▶ 0:00](https://youtu.be/zHxGjKaeTNU)
[^zHxGjKaeTNU-1058]: [WIKI GUIDES: Phosani's Nightmare (OSRS)](videos/2024-05-06_zHxGjKaeTNU.md), 2024-05-06. [▶ 17:38](https://youtu.be/zHxGjKaeTNU?t=1058)
[^9cYL7QTJ5G8-479]: [WIKI GUIDES - Whisperer](videos/2024-05-10_9cYL7QTJ5G8.md), 2024-05-10. [▶ 7:59](https://youtu.be/9cYL7QTJ5G8?t=479)
[^e0y_auD9JhY-1261]: [Ultimate Account Building Guide (OSRS)](videos/2024-07-07_e0y_auD9JhY.md), 2024-07-07. [▶ 21:01](https://youtu.be/e0y_auD9JhY?t=1261)
[^yswYFNgsA6s-0]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 0:00](https://youtu.be/yswYFNgsA6s)
[^WvmEY9v6AnI-421]: [WIKI GUIDES - VORKATH (OSRS)](videos/2024-05-18_WvmEY9v6AnI.md), 2024-05-18. [▶ 7:01](https://youtu.be/WvmEY9v6AnI?t=421)
[^e0y_auD9JhY-1840]: [Ultimate Account Building Guide (OSRS)](videos/2024-07-07_e0y_auD9JhY.md), 2024-07-07. [▶ 30:40](https://youtu.be/e0y_auD9JhY?t=1840)
[^yswYFNgsA6s-1462]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 24:22](https://youtu.be/yswYFNgsA6s?t=1462)
[^yswYFNgsA6s-1522]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 25:22](https://youtu.be/yswYFNgsA6s?t=1522)
[^vEs4Qvs_Rag-343]: [EASY 300 ToA Budget Guide (OSRS)](videos/2024-10-24_vEs4Qvs_Rag.md), 2024-10-24. [▶ 5:43](https://youtu.be/vEs4Qvs_Rag?t=343)
[^yswYFNgsA6s-147]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 2:27](https://youtu.be/yswYFNgsA6s?t=147)
[^yswYFNgsA6s-207]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 3:27](https://youtu.be/yswYFNgsA6s?t=207)
[^zHxGjKaeTNU-648]: [WIKI GUIDES: Phosani's Nightmare (OSRS)](videos/2024-05-06_zHxGjKaeTNU.md), 2024-05-06. [▶ 10:48](https://youtu.be/zHxGjKaeTNU?t=648)
[^yswYFNgsA6s-62]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 1:02](https://youtu.be/yswYFNgsA6s?t=62)
[^yswYFNgsA6s-88]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 1:28](https://youtu.be/yswYFNgsA6s?t=88)
[^yswYFNgsA6s-119]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 1:59](https://youtu.be/yswYFNgsA6s?t=119)
[^e0y_auD9JhY-1806]: [Ultimate Account Building Guide (OSRS)](videos/2024-07-07_e0y_auD9JhY.md), 2024-07-07. [▶ 30:06](https://youtu.be/e0y_auD9JhY?t=1806)
[^e0y_auD9JhY-1294]: [Ultimate Account Building Guide (OSRS)](videos/2024-07-07_e0y_auD9JhY.md), 2024-07-07. [▶ 21:34](https://youtu.be/e0y_auD9JhY?t=1294)
[^yswYFNgsA6s-296]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 4:56](https://youtu.be/yswYFNgsA6s?t=296)
[^e0y_auD9JhY-1320]: [Ultimate Account Building Guide (OSRS)](videos/2024-07-07_e0y_auD9JhY.md), 2024-07-07. [▶ 22:00](https://youtu.be/e0y_auD9JhY?t=1320)
[^e0y_auD9JhY-1818]: [Ultimate Account Building Guide (OSRS)](videos/2024-07-07_e0y_auD9JhY.md), 2024-07-07. [▶ 30:18](https://youtu.be/e0y_auD9JhY?t=1818)
[^yswYFNgsA6s-1288]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 21:28](https://youtu.be/yswYFNgsA6s?t=1288)
[^yswYFNgsA6s-270]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 4:30](https://youtu.be/yswYFNgsA6s?t=270)
[^yswYFNgsA6s-324]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 5:24](https://youtu.be/yswYFNgsA6s?t=324)
[^yswYFNgsA6s-358]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 5:58](https://youtu.be/yswYFNgsA6s?t=358)
[^yswYFNgsA6s-385]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 6:25](https://youtu.be/yswYFNgsA6s?t=385)
[^yswYFNgsA6s-506]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 8:26](https://youtu.be/yswYFNgsA6s?t=506)
[^yswYFNgsA6s-533]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 8:53](https://youtu.be/yswYFNgsA6s?t=533)
[^yswYFNgsA6s-787]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 13:07](https://youtu.be/yswYFNgsA6s?t=787)
[^yswYFNgsA6s-815]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 13:35](https://youtu.be/yswYFNgsA6s?t=815)
[^yswYFNgsA6s-842]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 14:02](https://youtu.be/yswYFNgsA6s?t=842)
[^yswYFNgsA6s-561]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 9:21](https://youtu.be/yswYFNgsA6s?t=561)
[^yswYFNgsA6s-590]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 9:50](https://youtu.be/yswYFNgsA6s?t=590)
[^yswYFNgsA6s-621]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 10:21](https://youtu.be/yswYFNgsA6s?t=621)
[^yswYFNgsA6s-679]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 11:19](https://youtu.be/yswYFNgsA6s?t=679)
[^yswYFNgsA6s-706]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 11:46](https://youtu.be/yswYFNgsA6s?t=706)
[^vEs4Qvs_Rag-284]: [EASY 300 ToA Budget Guide (OSRS)](videos/2024-10-24_vEs4Qvs_Rag.md), 2024-10-24. [▶ 4:44](https://youtu.be/vEs4Qvs_Rag?t=284)
[^yswYFNgsA6s-651]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 10:51](https://youtu.be/yswYFNgsA6s?t=651)
[^yswYFNgsA6s-1434]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 23:54](https://youtu.be/yswYFNgsA6s?t=1434)
[^yswYFNgsA6s-237]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 3:57](https://youtu.be/yswYFNgsA6s?t=237)
[^yswYFNgsA6s-413]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 6:53](https://youtu.be/yswYFNgsA6s?t=413)
[^yswYFNgsA6s-478]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 7:58](https://youtu.be/yswYFNgsA6s?t=478)
[^yswYFNgsA6s-447]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 7:27](https://youtu.be/yswYFNgsA6s?t=447)
[^yswYFNgsA6s-1314]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 21:54](https://youtu.be/yswYFNgsA6s?t=1314)
[^yswYFNgsA6s-1347]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 22:27](https://youtu.be/yswYFNgsA6s?t=1347)
[^yswYFNgsA6s-1374]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 22:54](https://youtu.be/yswYFNgsA6s?t=1374)
[^yswYFNgsA6s-903]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 15:03](https://youtu.be/yswYFNgsA6s?t=903)
[^e0y_auD9JhY-1504]: [Ultimate Account Building Guide (OSRS)](videos/2024-07-07_e0y_auD9JhY.md), 2024-07-07. [▶ 25:04](https://youtu.be/e0y_auD9JhY?t=1504)
[^9cYL7QTJ5G8-457]: [WIKI GUIDES - Whisperer](videos/2024-05-10_9cYL7QTJ5G8.md), 2024-05-10. [▶ 7:37](https://youtu.be/9cYL7QTJ5G8?t=457)
[^yswYFNgsA6s-1169]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 19:29](https://youtu.be/yswYFNgsA6s?t=1169)
[^9cYL7QTJ5G8-414]: [WIKI GUIDES - Whisperer](videos/2024-05-10_9cYL7QTJ5G8.md), 2024-05-10. [▶ 6:54](https://youtu.be/9cYL7QTJ5G8?t=414)
[^e0y_auD9JhY-1408]: [Ultimate Account Building Guide (OSRS)](videos/2024-07-07_e0y_auD9JhY.md), 2024-07-07. [▶ 23:28](https://youtu.be/e0y_auD9JhY?t=1408)
[^yswYFNgsA6s-1202]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 20:02](https://youtu.be/yswYFNgsA6s?t=1202)
[^e0y_auD9JhY-1444]: [Ultimate Account Building Guide (OSRS)](videos/2024-07-07_e0y_auD9JhY.md), 2024-07-07. [▶ 24:04](https://youtu.be/e0y_auD9JhY?t=1444)
[^e0y_auD9JhY-1378]: [Ultimate Account Building Guide (OSRS)](videos/2024-07-07_e0y_auD9JhY.md), 2024-07-07. [▶ 22:58](https://youtu.be/e0y_auD9JhY?t=1378)
[^zHxGjKaeTNU-678]: [WIKI GUIDES: Phosani's Nightmare (OSRS)](videos/2024-05-06_zHxGjKaeTNU.md), 2024-05-06. [▶ 11:18](https://youtu.be/zHxGjKaeTNU?t=678)
[^zHxGjKaeTNU-1089]: [WIKI GUIDES: Phosani's Nightmare (OSRS)](videos/2024-05-06_zHxGjKaeTNU.md), 2024-05-06. [▶ 18:09](https://youtu.be/zHxGjKaeTNU?t=1089)
[^yswYFNgsA6s-1053]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 17:33](https://youtu.be/yswYFNgsA6s?t=1053)
[^e0y_auD9JhY-1572]: [Ultimate Account Building Guide (OSRS)](videos/2024-07-07_e0y_auD9JhY.md), 2024-07-07. [▶ 26:12](https://youtu.be/e0y_auD9JhY?t=1572)
[^yswYFNgsA6s-961]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 16:01](https://youtu.be/yswYFNgsA6s?t=961)
[^yswYFNgsA6s-1261]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 21:01](https://youtu.be/yswYFNgsA6s?t=1261)
[^yswYFNgsA6s-994]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 16:34](https://youtu.be/yswYFNgsA6s?t=994)
[^yswYFNgsA6s-1111]: [The ONLY Gear Calculator You’ll Ever Need in OSRS (Gearscape Guide)](videos/2025-09-26_yswYFNgsA6s.md), 2025-09-26. [▶ 18:31](https://youtu.be/yswYFNgsA6s?t=1111)
[^_nMz6X90hb0-377]: [WIKI GUIDES - KRIL/ZAMMY (OSRS)](videos/2024-05-12__nMz6X90hb0.md), 2024-05-12. [▶ 6:17](https://youtu.be/_nMz6X90hb0?t=377)
[^_nMz6X90hb0-462]: [WIKI GUIDES - KRIL/ZAMMY (OSRS)](videos/2024-05-12__nMz6X90hb0.md), 2024-05-12. [▶ 7:42](https://youtu.be/_nMz6X90hb0?t=462)
[^_nMz6X90hb0-521]: [WIKI GUIDES - KRIL/ZAMMY (OSRS)](videos/2024-05-12__nMz6X90hb0.md), 2024-05-12. [▶ 8:41](https://youtu.be/_nMz6X90hb0?t=521)
[^_nMz6X90hb0-530]: [WIKI GUIDES - KRIL/ZAMMY (OSRS)](videos/2024-05-12__nMz6X90hb0.md), 2024-05-12. [▶ 8:50](https://youtu.be/_nMz6X90hb0?t=530)
[^_nMz6X90hb0-538]: [WIKI GUIDES - KRIL/ZAMMY (OSRS)](videos/2024-05-12__nMz6X90hb0.md), 2024-05-12. [▶ 8:58](https://youtu.be/_nMz6X90hb0?t=538)
[^WvmEY9v6AnI-378]: [WIKI GUIDES - VORKATH (OSRS)](videos/2024-05-18_WvmEY9v6AnI.md), 2024-05-18. [▶ 6:18](https://youtu.be/WvmEY9v6AnI?t=378)
[^NSiTMTXHDXQ-481]: [WIKI GUIDES - GIANT MOLE (OSRS)](videos/2024-05-20_NSiTMTXHDXQ.md), 2024-05-20. [▶ 8:01](https://youtu.be/NSiTMTXHDXQ?t=481)
[^NSiTMTXHDXQ-548]: [WIKI GUIDES - GIANT MOLE (OSRS)](videos/2024-05-20_NSiTMTXHDXQ.md), 2024-05-20. [▶ 9:08](https://youtu.be/NSiTMTXHDXQ?t=548)
[^KIII4sXUDTk-936]: [WIKI GUIDES - YAMA MELEE AND MAGE (OSRS)](videos/2025-09-01_KIII4sXUDTk.md), 2025-09-01. [▶ 15:36](https://youtu.be/KIII4sXUDTk?t=936)
[^KIII4sXUDTk-970]: [WIKI GUIDES - YAMA MELEE AND MAGE (OSRS)](videos/2025-09-01_KIII4sXUDTk.md), 2025-09-01. [▶ 16:10](https://youtu.be/KIII4sXUDTk?t=970)
[^vuti6ln_q10-403]: [WIKI GUIDES - MELEE MUSPAH (OSRS)](videos/2025-09-03_vuti6ln_q10.md), 2025-09-03. [▶ 6:43](https://youtu.be/vuti6ln_q10?t=403)
[^vuti6ln_q10-471]: [WIKI GUIDES - MELEE MUSPAH (OSRS)](videos/2025-09-03_vuti6ln_q10.md), 2025-09-03. [▶ 7:51](https://youtu.be/vuti6ln_q10?t=471)
[^qCsJAdpSeTU-568]: [WIKI GUIDES - VORKATH V2 (OSRS)](videos/2025-09-06_qCsJAdpSeTU.md), 2025-09-06. [▶ 9:28](https://youtu.be/qCsJAdpSeTU?t=568)
[^qCsJAdpSeTU-626]: [WIKI GUIDES - VORKATH V2 (OSRS)](videos/2025-09-06_qCsJAdpSeTU.md), 2025-09-06. [▶ 10:26](https://youtu.be/qCsJAdpSeTU?t=626)
[^qCsJAdpSeTU-714]: [WIKI GUIDES - VORKATH V2 (OSRS)](videos/2025-09-06_qCsJAdpSeTU.md), 2025-09-06. [▶ 11:54](https://youtu.be/qCsJAdpSeTU?t=714)
[^_nMz6X90hb0-391]: [WIKI GUIDES - KRIL/ZAMMY (OSRS)](videos/2024-05-12__nMz6X90hb0.md), 2024-05-12. [▶ 6:31](https://youtu.be/_nMz6X90hb0?t=391)
[^_nMz6X90hb0-447]: [WIKI GUIDES - KRIL/ZAMMY (OSRS)](videos/2024-05-12__nMz6X90hb0.md), 2024-05-12. [▶ 7:27](https://youtu.be/_nMz6X90hb0?t=447)
[^qCsJAdpSeTU-652]: [WIKI GUIDES - VORKATH V2 (OSRS)](videos/2025-09-06_qCsJAdpSeTU.md), 2025-09-06. [▶ 10:52](https://youtu.be/qCsJAdpSeTU?t=652)

<div class="navbox" markdown="1" data-search-exclude>
<div class="navbox-title">Other topics</div>

[RuneLite plugins](RuneLite_plugins.md) • [RuneLite](RuneLite.md) • **Gearscape** • [Tombs of Amascut gear setup](Tombs_of_Amascut_gear_setup.md) • [Jal-Zek](Jal-Zek.md) • [Leagues V: Raging Echoes](Leagues_V_Raging_Echoes.md) • [Doom of Mokhaiotl: gear and inventory](Doom_of_Mokhaiotl_gear_and_inventory.md) • [RuneScape 3](RuneScape_3.md) • [Jal-Xil](Jal-Xil.md) • [Odablock Warriors](Odablock_Warriors.md) • [Yama: budget setup](Yama_budget_setup.md) • [Gargoyle](Gargoyle.md) • [Maw of Whispers](Maw_of_Whispers.md) • [Dagannoth](Dagannoth.md) • [Deadman All-Stars](Deadman_All-Stars.md) • [Kurask](Kurask.md) • [Jagex](Jagex.md) • [Ankou](Ankou.md) • [Run setup](Run_setup.md) • [Shadow rebuild setup](Shadow_rebuild_setup.md) • [Sulphur naga](Sulphur_naga.md) • [Suqah](Suqah.md) • [Kick](Kick.md) • [Troll](Troll.md) • [Shadow of Tumeken boss analysis](Shadow_of_Tumeken_boss_analysis.md) • [Advertising](Advertising.md) • [RS3 Curses](RS3_Curses.md) • [Varlamore](Varlamore.md) • [Westham Weasels](Westham_Weasels.md) • [Gambit](Gambit.md) • [Inferno simulator](Inferno_simulator.md) • [Rebuke](Rebuke.md) • [Rejuvenation](Rejuvenation.md) • [Tree Gnome Stronghold](Tree_Gnome_Stronghold.md) • [Metabolize](Metabolize.md) • [Trinitas](Trinitas.md)

</div>

<div class="catlinks" markdown="1" data-search-exclude>**Category:** [Other topics](topics.md#other)</div>
