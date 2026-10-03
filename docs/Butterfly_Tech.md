# Butterfly Tech

<div class="mbox" markdown="1" data-search-exclude>
This article is compiled from the videos of [GnomonkeyRS](https://www.youtube.com/@GnomonkeyRS). It records what Gnomonkey said, with sources, not verified game fact. See [About](index.md).
</div>

<div class="infobox" markdown="1">
<div class="infobox-title">Butterfly Tech</div>
<div class="infobox-image" markdown="1">![Butterfly Tech](https://i.ytimg.com/vi/pSBxLCy7-44/mqdefault.jpg)</div>

| | |
|---|---|
| **Type** | Mechanic |
| **Boss** | [Akkha](Akkha.md) ([Tombs of Amascut](Tombs_of_Amascut.md)) |
| **Discovered by** | Saxerpillar[^pSBxLCy7-44-0] |
| **Attack cycle** | 5 ticks[^pSBxLCy7-44-28] |
| **Requirements** | At least one stamina potion dose brought into the raid[^pSBxLCy7-44-28] |
| **Recommended weapon** | Tumeken's shadow[^pSBxLCy7-44-28] |
| **Videos** | 3 (first 2022-08-30, latest 2025-06-25) |
| **Main source** | [Raids 3 TOA Akkha "Butterfly Tech" OSRS](videos/2022-08-30_pSBxLCy7-44.md) |
</div>

**Butterfly Tech** is the name Gnomonkey and his clan use for a method for the Akkha fight, found by his clanmate and Discord member Saxerpillar. Gnomonkey calls it the greatest piece of tech found so far in Raids 3[^pSBxLCy7-44-0]. The player runs a cycle around Akkha, attacking from a set of attack tiles. It is a 5-tick attack cycle, so it is only really good with the new Tumeken's shadow, although it can be done with a Sanguinesti staff or Trident while losing a tick each attack[^pSBxLCy7-44-28]. A second guide in June 2025 updates the plugin setup[^6Qmuhnpa0gc-124].

[TOC]

## Requirements
At least one dose of stamina potion must be brought into the raid[^pSBxLCy7-44-28]. With salts the player has unlimited run energy, so stamina is unnecessary[^6Qmuhnpa0gc-408]. At most raid levels Akkha dies before run energy runs out if one stamina dose was drunk[^pSBxLCy7-44-384]. He could even manually cast Ice Barrage on each attack, but it would be very hard to click Barrage and then Akkha after pathing to the attack tile on a single game tick[^pSBxLCy7-44-28].

## RuneLite setup
* **Tile markers:** in 2022 the markers were provided through a pastebin link in the description. Copy them to the clipboard, right-click the world map and choose import to load them all[^pSBxLCy7-44-116]. The 2025 version uses the external plugin Tile Packs: search "butterfly" and use the four-tick tiles, not the normal butterfly tiles[^6Qmuhnpa0gc-124]. The same tiles are also available by Pastebin import, plus colour-coded radius markers via `!akkha color` in his Twitch chat[^7ZyZC0OcvsU-235].
* **True tile:** use NPC Indicators or his Akkha radius markers, which also show which style Akkha is attacking with[^pSBxLCy7-44-143]. Without the colour markers, add Akkha in NPC indicators with True Tile and Southwest True Tile highlights[^6Qmuhnpa0gc-148][^7ZyZC0OcvsU-267].
* **Menu Entry Swapper:** enable Shift Click Walk Here[^pSBxLCy7-44-143], which lets the player walk under the shadow without clicking it[^6Qmuhnpa0gc-320].
* **Custom Swapper:** add `attack Akkha's Shadow *` so that Attack is prioritised on the shadows and not on Akkha[^pSBxLCy7-44-143]. The 2025 text is `attack,akkha's shadow*`. The reason is that Akkha walks over the shadow and the invincible Akkha should not be clicked[^6Qmuhnpa0gc-295].
* **Monster HP percentage:** add Akkha to show a percentage over him, so the player knows when he phases each 20% HP at any raid level[^pSBxLCy7-44-173] and when to switch to the shadow[^6Qmuhnpa0gc-320].
* **Tombs of Amascut plugin:** a toggle shows the shadows' HP so the player can see whether the DPS check will be beaten, or whether a DPS skip is needed[^6Qmuhnpa0gc-1215][^7ZyZC0OcvsU-301].

## Method
1. **Preparation:** creep out of the stamina boost, activate Augury, take salts, summon a maze troll if available and start the ring. Starting from the north or south quadrant makes no difference[^pSBxLCy7-44-173].
2. **Starting the cycle:** stand still attacking Akkha until he crosses the attack tile, then run to the furthest quadrant's attack tile. Starting correctly is the hardest part and takes practice[^pSBxLCy7-44-200]. Look at which side of the quadrant Akkha is on and start on the opposite side, attack until his tile is one tile away, then click to start the cycle and follow the red tiles around him, attacking from each attack tile[^pSBxLCy7-44-233].
3. **Shadows at 80%:** attack Akkha again but hold shift when clicking run tiles so the player can walk through the shadow. Attack the shadow from the attack tiles and, once the cast has killed it, click Akkha again from the attack tiles[^pSBxLCy7-44-261].
4. **Next phase:** each time Akkha is nearly down another 20%, finish the phase with a cast and move to the next quadrant. It is very important to run vertically to the next quadrant, or Akkha will not drag properly, since going horizontally causes many problems[^pSBxLCy7-44-290]. His sequence is vertical first, then diagonal to the other quadrant, then vertical again for the final 20%[^pSBxLCy7-44-290].

## Tips
* If Akkha paths to the player directly from his centre tile, the method is impossible until he hits the player. Tank the hit and stand still for a couple of ticks before starting[^pSBxLCy7-44-356].
* Other actions such as drinking potions are extremely hard during the cycle, so use the transition between quadrants to drink stamina or heal[^pSBxLCy7-44-356].
* In teams, if Akkha passes over a teammate he will melee them while still going towards the tank. Communicate and stand in a quadrant corner out of his way[^pSBxLCy7-44-384].
* The Atlatl has six tile range, so the player can keep hitting Akkha during Simon Says (five rounds at his raid level 2-3), and does not always need to be on a specific tile[^7ZyZC0OcvsU-372].
* In the 2025 demonstration he brings a ranging potion and stamina[^6Qmuhnpa0gc-408].
* He does not know whether the OSRS wiki DPS calculator includes burn damage yet, but says Gearscape does[^7ZyZC0OcvsU-436].

## Revision history
| Date | Video | Change |
|---|---|---|
| 2025-06-25 | [BOFA 4T BUTTERFLY TOA GUIDE (OSRS)](videos/2025-06-25_6Qmuhnpa0gc.md) | Updated for 2025: Tile Packs four-tick tiles, Tombs of Amascut plugin shadow HP, true tile markers, Atlatl range and DPS calculator note. |
| 2022-08-30 | [Raids 3 TOA Akkha "Butterfly Tech" OSRS](videos/2022-08-30_pSBxLCy7-44.md) | Page created: Butterfly Tech discovered by Saxerpillar, with the 5-tick cycle, stamina requirement, RuneLite setup and quadrant method. |
## See also

* [Update: Tombs of Amascut changes](Update_Tombs_of_Amascut_changes.md)
* [Eclipse atlatl](Eclipse_atlatl.md)
* [Akkha](Akkha.md)

## References

///Footnotes Go Here///
[^pSBxLCy7-44-0]: [Raids 3 TOA Akkha "Butterfly Tech" OSRS](videos/2022-08-30_pSBxLCy7-44.md), 2022-08-30. [▶ 0:00](https://youtu.be/pSBxLCy7-44)
[^pSBxLCy7-44-28]: [Raids 3 TOA Akkha "Butterfly Tech" OSRS](videos/2022-08-30_pSBxLCy7-44.md), 2022-08-30. [▶ 0:28](https://youtu.be/pSBxLCy7-44?t=28)
[^6Qmuhnpa0gc-124]: [BOFA 4T BUTTERFLY TOA GUIDE (OSRS)](videos/2025-06-25_6Qmuhnpa0gc.md), 2025-06-25. [▶ 2:04](https://youtu.be/6Qmuhnpa0gc?t=124)
[^6Qmuhnpa0gc-408]: [BOFA 4T BUTTERFLY TOA GUIDE (OSRS)](videos/2025-06-25_6Qmuhnpa0gc.md), 2025-06-25. [▶ 6:48](https://youtu.be/6Qmuhnpa0gc?t=408)
[^pSBxLCy7-44-384]: [Raids 3 TOA Akkha "Butterfly Tech" OSRS](videos/2022-08-30_pSBxLCy7-44.md), 2022-08-30. [▶ 6:24](https://youtu.be/pSBxLCy7-44?t=384)
[^pSBxLCy7-44-116]: [Raids 3 TOA Akkha "Butterfly Tech" OSRS](videos/2022-08-30_pSBxLCy7-44.md), 2022-08-30. [▶ 1:56](https://youtu.be/pSBxLCy7-44?t=116)
[^7ZyZC0OcvsU-235]: [3T BUTTERFLY TOA GUIDE (OSRS)](videos/2025-06-25_7ZyZC0OcvsU.md), 2025-06-25. [▶ 3:55](https://youtu.be/7ZyZC0OcvsU?t=235)
[^pSBxLCy7-44-143]: [Raids 3 TOA Akkha "Butterfly Tech" OSRS](videos/2022-08-30_pSBxLCy7-44.md), 2022-08-30. [▶ 2:23](https://youtu.be/pSBxLCy7-44?t=143)
[^6Qmuhnpa0gc-148]: [BOFA 4T BUTTERFLY TOA GUIDE (OSRS)](videos/2025-06-25_6Qmuhnpa0gc.md), 2025-06-25. [▶ 2:28](https://youtu.be/6Qmuhnpa0gc?t=148)
[^7ZyZC0OcvsU-267]: [3T BUTTERFLY TOA GUIDE (OSRS)](videos/2025-06-25_7ZyZC0OcvsU.md), 2025-06-25. [▶ 4:27](https://youtu.be/7ZyZC0OcvsU?t=267)
[^6Qmuhnpa0gc-320]: [BOFA 4T BUTTERFLY TOA GUIDE (OSRS)](videos/2025-06-25_6Qmuhnpa0gc.md), 2025-06-25. [▶ 5:20](https://youtu.be/6Qmuhnpa0gc?t=320)
[^6Qmuhnpa0gc-295]: [BOFA 4T BUTTERFLY TOA GUIDE (OSRS)](videos/2025-06-25_6Qmuhnpa0gc.md), 2025-06-25. [▶ 4:55](https://youtu.be/6Qmuhnpa0gc?t=295)
[^pSBxLCy7-44-173]: [Raids 3 TOA Akkha "Butterfly Tech" OSRS](videos/2022-08-30_pSBxLCy7-44.md), 2022-08-30. [▶ 2:53](https://youtu.be/pSBxLCy7-44?t=173)
[^6Qmuhnpa0gc-1215]: [BOFA 4T BUTTERFLY TOA GUIDE (OSRS)](videos/2025-06-25_6Qmuhnpa0gc.md), 2025-06-25. [▶ 20:15](https://youtu.be/6Qmuhnpa0gc?t=1215)
[^7ZyZC0OcvsU-301]: [3T BUTTERFLY TOA GUIDE (OSRS)](videos/2025-06-25_7ZyZC0OcvsU.md), 2025-06-25. [▶ 5:01](https://youtu.be/7ZyZC0OcvsU?t=301)
[^pSBxLCy7-44-200]: [Raids 3 TOA Akkha "Butterfly Tech" OSRS](videos/2022-08-30_pSBxLCy7-44.md), 2022-08-30. [▶ 3:20](https://youtu.be/pSBxLCy7-44?t=200)
[^pSBxLCy7-44-233]: [Raids 3 TOA Akkha "Butterfly Tech" OSRS](videos/2022-08-30_pSBxLCy7-44.md), 2022-08-30. [▶ 3:53](https://youtu.be/pSBxLCy7-44?t=233)
[^pSBxLCy7-44-261]: [Raids 3 TOA Akkha "Butterfly Tech" OSRS](videos/2022-08-30_pSBxLCy7-44.md), 2022-08-30. [▶ 4:21](https://youtu.be/pSBxLCy7-44?t=261)
[^pSBxLCy7-44-290]: [Raids 3 TOA Akkha "Butterfly Tech" OSRS](videos/2022-08-30_pSBxLCy7-44.md), 2022-08-30. [▶ 4:50](https://youtu.be/pSBxLCy7-44?t=290)
[^pSBxLCy7-44-356]: [Raids 3 TOA Akkha "Butterfly Tech" OSRS](videos/2022-08-30_pSBxLCy7-44.md), 2022-08-30. [▶ 5:56](https://youtu.be/pSBxLCy7-44?t=356)
[^7ZyZC0OcvsU-372]: [3T BUTTERFLY TOA GUIDE (OSRS)](videos/2025-06-25_7ZyZC0OcvsU.md), 2025-06-25. [▶ 6:12](https://youtu.be/7ZyZC0OcvsU?t=372)
[^7ZyZC0OcvsU-436]: [3T BUTTERFLY TOA GUIDE (OSRS)](videos/2025-06-25_7ZyZC0OcvsU.md), 2025-06-25. [▶ 7:16](https://youtu.be/7ZyZC0OcvsU?t=436)

<div class="navbox" markdown="1" data-search-exclude>
<div class="navbox-title">Mechanics</div>

[Colosseum invocations](Colosseum_invocations.md) • [Yama contracts](Yama_contracts.md) • [Invocations (Tombs of Amascut)](Invocations_%28Tombs_of_Amascut%29.md) • [Jal-ImKot](Jal-ImKot.md) • [Inferno pillars](Inferno_pillars.md) • [Jal-Ak](Jal-Ak.md) • [Alt account](Alt_account.md) • [Thralls](Thralls.md) • [Nex gear setup](Nex_gear_setup.md) • [Tempoross](Tempoross.md) • [Turael](Turael.md) • [Inferno waves](Inferno_waves.md) • [Jal-Nib](Jal-Nib.md) • [Doom of Mokhaiotl: rock block method](Doom_of_Mokhaiotl_rock_block_method.md) • [Monkey Room](Monkey_Room.md) • [Fortis Colosseum pillars](Fortis_Colosseum_pillars.md) • [Phantom barrage](Phantom_barrage.md) • [Awakened bosses](Awakened_bosses.md) • [Melee gear progression](Melee_gear_progression.md) • [Demonic Brutus](Demonic_Brutus.md) • [Jal-MejRah](Jal-MejRah.md) • [Prayer flicking](Prayer_flicking.md) • **Butterfly Tech** • [Fortis Colosseum setup](Fortis_Colosseum_setup.md) • [Doom of Mokhaiotl: melee punish](Doom_of_Mokhaiotl_melee_punish.md) • [Sulliuscep](Sulliuscep.md) • [Botting](Botting.md) • [Off-ticking](Off-ticking.md) • [Corner trapping](Corner_trapping.md) • [Doom of Mokhaiotl: car attack](Doom_of_Mokhaiotl_car_attack.md) • [Combat Achievements](Combat_Achievements.md) • [Doom of Mokhaiotl: shield phase](Doom_of_Mokhaiotl_shield_phase.md) • [Pest Control](Pest_Control.md) • [Blood Barrage](Blood_Barrage.md) • [Nylocas](Nylocas.md) • [Great Olm 4-1 method](Great_Olm_4-1_method.md) • [Nex reset](Nex_reset.md) • [Triple Jad](Triple_Jad.md) • [RuneScape 3 combat](RuneScape_3_combat.md) • [Tightrope skip](Tightrope_skip.md)

</div>

<div class="catlinks" markdown="1" data-search-exclude>**Category:** [Mechanics](topics.md#mechanic)</div>
