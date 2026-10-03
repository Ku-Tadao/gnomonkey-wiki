---
Type: Mechanic
Boss: [[Akkha]] ([[Tombs of Amascut]])
Discovered by: Saxerpillar [c1]
Attack cycle: 5 ticks [c2]
Requirements: At least one stamina potion dose brought into the raid [c3]
Recommended weapon: Tumeken's shadow [c2]
---
**Butterfly Tech** is the name Gnomonkey and his clan use for a method for the Akkha fight, found by his clanmate and Discord member Saxerpillar. Gnomonkey calls it the greatest piece of tech found so far in Raids 3 [c1]. The player runs a cycle around Akkha, attacking from a set of attack tiles. It is a 5-tick attack cycle, so it is only really good with the new Tumeken's shadow, although it can be done with a Sanguinesti staff or Trident while losing a tick each attack [c2]. A second guide in June 2025 updates the plugin setup [c20].

## Requirements
At least one dose of stamina potion must be brought into the raid [c3]. With salts the player has unlimited run energy, so stamina is unnecessary [c24]. At most raid levels Akkha dies before run energy runs out if one stamina dose was drunk [c18]. He could even manually cast Ice Barrage on each attack, but it would be very hard to click Barrage and then Akkha after pathing to the attack tile on a single game tick [c4].

## RuneLite setup
* **Tile markers:** in 2022 the markers were provided through a pastebin link in the description. Copy them to the clipboard, right-click the world map and choose import to load them all [c5]. The 2025 version uses the external plugin Tile Packs: search "butterfly" and use the four-tick tiles, not the normal butterfly tiles [c20]. The same tiles are also available by Pastebin import, plus colour-coded radius markers via `!akkha color` in his Twitch chat [c26].
* **True tile:** use NPC Indicators or his Akkha radius markers, which also show which style Akkha is attacking with [c7]. Without the colour markers, add Akkha in NPC indicators with True Tile and Southwest True Tile highlights [c21 c27].
* **Menu Entry Swapper:** enable Shift Click Walk Here [c6], which lets the player walk under the shadow without clicking it [c23].
* **Custom Swapper:** add `attack Akkha's Shadow *` so that Attack is prioritised on the shadows and not on Akkha [c8]. The 2025 text is `attack,akkha's shadow*`. The reason is that Akkha walks over the shadow and the invincible Akkha should not be clicked [c22].
* **Monster HP percentage:** add Akkha to show a percentage over him, so the player knows when he phases each 20% HP at any raid level [c10] and when to switch to the shadow [c23].
* **Tombs of Amascut plugin:** a toggle shows the shadows' HP so the player can see whether the DPS check will be beaten, or whether a DPS skip is needed [c25 c28].

## Method
1. **Preparation:** creep out of the stamina boost, activate Augury, take salts, summon a maze troll if available and start the ring. Starting from the north or south quadrant makes no difference [c9].
2. **Starting the cycle:** stand still attacking Akkha until he crosses the attack tile, then run to the furthest quadrant's attack tile. Starting correctly is the hardest part and takes practice [c11]. Look at which side of the quadrant Akkha is on and start on the opposite side, attack until his tile is one tile away, then click to start the cycle and follow the red tiles around him, attacking from each attack tile [c12].
3. **Shadows at 80%:** attack Akkha again but hold shift when clicking run tiles so the player can walk through the shadow. Attack the shadow from the attack tiles and, once the cast has killed it, click Akkha again from the attack tiles [c13].
4. **Next phase:** each time Akkha is nearly down another 20%, finish the phase with a cast and move to the next quadrant. It is very important to run vertically to the next quadrant, or Akkha will not drag properly, since going horizontally causes many problems [c14]. His sequence is vertical first, then diagonal to the other quadrant, then vertical again for the final 20% [c15].

## Tips
* If Akkha paths to the player directly from his centre tile, the method is impossible until he hits the player. Tank the hit and stand still for a couple of ticks before starting [c16].
* Other actions such as drinking potions are extremely hard during the cycle, so use the transition between quadrants to drink stamina or heal [c17].
* In teams, if Akkha passes over a teammate he will melee them while still going towards the tank. Communicate and stand in a quadrant corner out of his way [c19].
* The Atlatl has six tile range, so the player can keep hitting Akkha during Simon Says (five rounds at his raid level 2-3), and does not always need to be on a specific tile [c29].
* In the 2025 demonstration he brings a ranging potion and stamina [c24].
* He does not know whether the OSRS wiki DPS calculator includes burn damage yet, but says Gearscape does [c30].

## Revision history
| c1 | Page created: Butterfly Tech discovered by Saxerpillar, with the 5-tick cycle, stamina requirement, RuneLite setup and quadrant method. |
| c20 | Updated for 2025: Tile Packs four-tick tiles, Tombs of Amascut plugin shadow HP, true tile markers, Atlatl range and DPS calculator note. |
