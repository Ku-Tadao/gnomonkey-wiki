---
Type: Mechanic
Hatnote: This article is about the healing technique. For the spell itself see [[Blood barrage]].
Spell: [[Blood barrage]], cast manually [c34 c38]
Minimum distance: 8 tiles [c9 c16 c28]
Barrage range: 10 tiles [c6]
Typical heal: 10 to 20 health from the extra cast [c30]
Used in: [[Inferno]] [c17 c21 c31]
---
A **phantom barrage** (also "phantom") is a healing technique in which a [[Blood barrage]] is cast at a monster's corpse, so that the player is healed for the damage that cast would have dealt. [c9 c15 c26] It is a game engine quirk: if Blood barrage is cast from eight or more tiles away at a monster as it dies, the barrage still lands on the corpse and heals the player, even if the hit is a splash or only 1 damage. [c34]

Gnomonkey treats the phantom as the main way to regain health in the [[Inferno]]. In 2024 he called it the primary healing source, with blobs splitting into three bloblets that can be phantomed as three corpses at once. [c17 c21] By December 2025 he described it as the bread and butter of health recovery there, and advises doing one every time, even without needing health, since there is no reason not to. [c29 c31]

## How it works

Barrage has an invisible travel time. From far enough away the spell is still in the air when the target dies, so a second, manual cast can be aimed at the corpse, and the blood barrage still heals the full amount. [c3 c15 c16] The sequence is to cast a spell at a far-away target, then manually cast the next spell so that it is cast at the corpse as the monster dies. [c20] Because the extra cast counts as additional hits, it heals as if it had dealt its full damage. [c26]

Gnomonkey keeps his autocast on Blood barrage, since most barraging for health is done while AFKing, and casts [[Ice barrage]] manually for the most part. [c1] The phantom cast itself must be manual. Autocast has no delay (the autocast delay was removed in 2024), but it still does not produce a phantom: the corpse cast has to be done by hand. [c14 c33 c38] A common setup is to bring a blob down to a chosen pillar position, give it a Blood barrage, then manually cast again so the cast queues and lands on the corpse. [c2] It does not matter when the spell is clicked on the monsters after the first cast. [c5]

### Range

* A phantom needs the player to be at least eight tiles from the target, because the cast's travel time has to be long enough. [c6 c9 c16 c22 c28]
* Barrage has a 10-tile range, the same as a [[Twisted bow]], so at maximum range the phantom always works. [c6]
* The minimum distance is eight tiles, so the player should stand at the maximum range of their sceptre. [c28]

### Targets

* **Blobs and bloblets:** the strongest use. Each blob splits into three bloblets, so up to three corpses can be phantomed at once. [c3 c17 c21] A phantom on a set of bloblets from the good position returns about 40 health. [c27]
* **Nibblers:** nibblers have the least magic defence of any mob, so phantoming far-away nibblers can give a lot of health. A phantom off six nibblers returns about 80. [c12 c27] He also uses a phantom on nibblers to confirm that all of them are dead, to guarantee he can still cast at the pile, and he notes it can be done off pets. [c10 c23] He adds that nibblers can be phantomed straight off spawn when safe, and that nobody does this. [c39]
* **Rangers:** rangers have a fairly low magic level, so they can also be used to regain health. [c13] Barrage accuracy is checked for each monster, with chinchompas unique in that the roll is made off the target. [c13] A phantom still works on a blob and ranger stack if the ranger is at the back. [c19]
* **Any mob:** a phantom works on any monster, such as bats, rangers or melee monsters, but is less effective than with bloblets. [c7]

Gnomonkey took his shield off for the phantom in 2026 to raise his mage accuracy. [c35]

## Positioning

The blob must be close enough to the pillar for the phantom to work, and it does not work if the mage is not pulled in fully against the pillar, so the player should let it pull in first. [c18 c22] Gnomonkey names two positions in the Inferno from which a blob can be phantomed; the phantom also lets the player extend far out to get nibblers and tank damage, then return behind the pillar to heal. [c24 c37] He adds a third, secret spot, in which the player stands on the tile with the blob as far down as it can go, kills it, steps back up, and clicks when the bloblets appear. [c37]

Other positional tricks:

* If a blob is somewhere it cannot normally be phantomed, the player can stand at a position and wait a tick so the mage blocks two monsters, then run out and phantom off the blob. He says he almost never sees first-cape players do this. [c11]
* The "cheeky phantom": with the blob pulled down on the corner, the player steps into the pillar and steps back down when the bloblets appear, so only the mage is on them. [c32]

## Healing amounts

| Situation | Health gained |
|---|---|
| Demonstration from 84 health | to 98 [c4] |
| Bloblets from the good position | about 40 [c27] |
| Six nibblers | about 80 [c27] |
| Extra cast in general | usually 10 to 20, varies [c30] |
| 2026 demo, bloblet corpses / later phantom | 8 / 30 [c36] |

Gnomonkey advises healing on the blobs when below 60 health. [c8] He uses the Tizar HP tracker plugin to see health on the pillars and enemies, and for tile markers. [c25]

## Revision history

| c1 | Page created: autocast setup, phantom method, 8-tile and 10-tile range, healing on blobs below 60 health. |
| c9 | Added nibblers and rangers as targets, the mage-blocking positional trick, and magic-defence reasoning. |
| c14 | Added that autocast still cannot phantom after the autocast delay removal, and that bloblets are the main Inferno heal. |
| c21 | Added the three-corpse bloblet heal as the primary Inferno source, two phantom spots, nibbler pile check and HP tracker plugin. |
| c27 | Added heal amounts (about 40 bloblets, about 80 six nibblers, 10 to 20 per extra cast); advice to phantom every time; the cheeky phantom. |
| c34 | Described it as an engine quirk, added shield-off advice, third secret spot and phantoming nibblers off spawn. |
