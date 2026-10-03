# RuneLite plugins

<div class="mbox" markdown="1" data-search-exclude>
This article is compiled from the videos of [GnomonkeyRS](https://www.youtube.com/@GnomonkeyRS). It records what Gnomonkey said, with sources, not verified game fact. See [About](index.md).
</div>

<div class="infobox" markdown="1">
<div class="infobox-title">RuneLite plugins</div>
<div class="infobox-image" markdown="1">![RuneLite plugins](https://i.ytimg.com/vi/9neaqoxR-nY/mqdefault.jpg)</div>

| | |
|---|---|
| **Type** | Other |
| **Videos** | 5 (first 2019-04-14, latest 2024-02-25) |
| **Main source** | [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md) |
</div>

This page collects the [RuneLite](RuneLite.md) plugins and settings Gnomonkey recommends or describes across five videos from 2019 to 2024: a 2019 list of eleven plugins, a full 2020 setup walkthrough, a 2020 Nightmare Zone note, a 2022 look at newly allowed plugins, and a 2024 PvM plugin guide. Most entries are his personal settings and opinions rather than general rules.

[TOC]

## Combat and bossing plugins

**Tile indicators.** Shift and right-click marks a tile with a uniquely coloured box; he called it practically necessary for most high-level bosses and the [Inferno](Inferno.md)[^w7POGb4jwco-134]. In 2020 he kept highlight hover tile (shows exactly where a click will go) and highlight current true tile (a blue tile showing the player's server position), the latter very helpful for the [Hallowed Sepulchre](Hallowed_Sepulchre.md) and any raiding or bossing[^9neaqoxR-nY-3854][^9neaqoxR-nY-3855]. In 2024 he said the true tile option helps with careful pathing around hazards such as Sotetseg's maze or Zebak's poison and waves[^Z5ZONYTlS1w-181]. See also [True tile](True_tile.md).

**NPC indicators.** In 2020 he highlighted gardeners, the Hespori flower, crystal implings, bankers, Hydra and bosses with both hull and timer[^9neaqoxR-nY-3090]. Hull highlighting shows the exact tiles an NPC occupies, which helps with stomp mechanics and which he uses for all Theatre of Blood bosses[^9neaqoxR-nY-3123]. The respawn timer option is good for Slayer tasks[^9neaqoxR-nY-3184]. In 2024 NPCs can be tagged by holding Shift and right-clicking, and he personally uses Highlight True Tile and Highlight Southwest True Tile[^Z5ZONYTlS1w-181].

**Monster true tiles (2022).** RuneLite added monster true tiles, showing exactly where a monster is. He found it one of the weirdest decisions that true tiles had been considered cheating, given that players could already see their own, and said it is useful where monsters stall, such as Inferno melee monsters and [Nex](Nex.md) resets[^3C7naDl1ieY-238].

**Entity hider.** In 2020 it was used to prevent flickering at Ardougne Knights and to hide all players or the local player for video footage[^9neaqoxR-nY-1380]. In June 2022 "hide dead NPCs" became a setting; he said it was practically necessary for speedrunning the Inferno or Gauntlet, since a dead NPC's clickbox sits at the top of the menu and eats clicks, and he would not run Inferno without it[^3C7naDl1ieY-31][^3C7naDl1ieY-60]. He noted bugs with multi-phase bosses, mainly Ice Demon, who disappears when the fight starts[^3C7naDl1ieY-87]. In 2024 it can hide dead targets and [thralls](Thralls.md); hiding corpses prevents misclicks and hiding thralls stops them obscuring ground hazards[^Z5ZONYTlS1w-239]. Companion Pet turns the thrall into a pet and can be combined with Entity Hider[^Z5ZONYTlS1w-386].

**Menu entry swapper and walk under.** In 2022 holding Shift while right-clicking an NPC gives a "shift-click walk here" option; when toggled on, Shift removes the NPC's whole menu so the player can move under it[^3C7naDl1ieY-116]. He said walk under is big for Nex resets, [Verzik](Verzik_Vitur.md) P3 tanking and bosses like Kalphite Queen or Bandos, though the implementation is clunky compared with another client[^3C7naDl1ieY-116], and later that it is not really necessary anywhere except manual Nex resets[^3C7naDl1ieY-146]. Shift-right-click on a pickpocketable NPC allows left-click pickpocketing of Elves and Vyres, but not left-click blackjacking[^3C7naDl1ieY-146].

**Monster HP plugins (2024).** Monster Menu HP shows the health of a group of enemies on right-click, useful for barrage and chinchompas[^Z5ZONYTlS1w-120]. Monster HP Percentage shows percent HP at a boss's centre, useful for phase thresholds at Baba, Akkha, Zebak, Wardens, Nex, Duke Sucellus and Vardorvis[^Z5ZONYTlS1w-120]. Radius Markers draws a box of customisable size around an NPC, for example Nex's aggression radius or Akkha's style changes[^Z5ZONYTlS1w-152].

**Gear and reminders (2024).** Dynamic Tags highlights an inventory piece when a weapon of a different style is worn; he uses a four second delay, and styles can be set by Shift and right-click under Gear Alert[^Z5ZONYTlS1w-208][^Z5ZONYTlS1w-239]. Customizable XP Drops predicts the hit from the XP drop, and he inputs a multiplier of 16 for Leagues[^Z5ZONYTlS1w-208]. Thrall Helper reminds when to resummon, and Death Charge Reminder does likewise ([Death Charge](Death_Charge.md)), mattering mostly with master combat achievements or better[^Z5ZONYTlS1w-356]. Charge Calculator recharges a staff with a custom number of charges[^Z5ZONYTlS1w-479].

**Timing.** The Visual Metronome counts server ticks over the character, true tile or a UI square, to a custom number (he uses four for the raid counter), with a reset hotkey; it suits Scythe Xarpus and Verzik P2 and P3[^Z5ZONYTlS1w-272]. He does not use the Audio Metronome but says it is useful for the Inferno[^Z5ZONYTlS1w-300]. Ping Grapher shows server stability, and Tick Tracker shows the percentage of ticks near 600 ms; 100% cannot be reached because running over loading lines counts as a lost tick[^Z5ZONYTlS1w-386]. The Timers plugin (anti-fire, cannon, divine potions) is incredibly important for bossing and he keeps it all on[^9neaqoxR-nY-3936].

**Party and group play.** In 2020 the Party plugin adds a join button in Discord and shows teammates' health and prayer; he said few use it but should, for example in Chambers of Xeric or Bandos trips[^9neaqoxR-nY-3301]. In 2022 it also shows which special attacks have landed, such as hammers and total BGS damage, which he said lets teams lower boss defence efficiently and should have been in the game ages ago[^3C7naDl1ieY-177][^3C7naDl1ieY-208]. He said nearly everything from the Socket plugins is now in RuneLite except the Sotetseg mazes[^3C7naDl1ieY-177]. In 2020 he also uses the members counter (a smiley icon beside clan members)[^9neaqoxR-nY-1557]. Player indicators highlight friends, clan and Discord party members, and others in red in the Wilderness[^9neaqoxR-nY-3355]. Opponent information can show a player's stats when they attack, trade or invite[^9neaqoxR-nY-3274].

## Input and menus

- **Anti-drag:** originally Shift anti-drag, later made general[^9neaqoxR-nY-416]. In 2020 he turned off shift-only, kept disable-on-control-press, and set the drag delay to 10, with eight to fifteen decent[^9neaqoxR-nY-416]; in 2024 he repeated that most people use 8 to 15 and one must experiment[^Z5ZONYTlS1w-300]. It makes item use on blocks (Blood Runecrafting) and gear switches at raids easier[^9neaqoxR-nY-448].
- **Key remapping:** in 2020 he called it gigantic: F keys can be remapped, Enter opens chat as in RS2, and WASD controls the camera when not typing; he hated using F keys for inventory setups[^9neaqoxR-nY-2635]. In 2024 he binds the number row (1 inventory, 2 prayer, 3 spells, 4 gear, 5 combat style) so his fingers stay near Shift and Control[^Z5ZONYTlS1w-330].
- **Menu Entry Swapper:** in 2020 one of the most useful plugins[^9neaqoxR-nY-2808], with customizable shift click (for example use instead of drop, or bank deposit all and withdraw all), bury swapping with Use, entering the Corrupted Gauntlet by default, NPC Contact repeats, and shift buy and sell set to 50[^9neaqoxR-nY-2824][^9neaqoxR-nY-2850][^9neaqoxR-nY-2881][^9neaqoxR-nY-2914][^9neaqoxR-nY-2941]. In 2024 he called Custom Menu Swaps one of, if not the, most useful plugins, since it reorders any menu; examples are Akkha's shadow as priority left click and Nex's ice prison stalagmite attack[^Z5ZONYTlS1w-414]. The bottom-most entry is listed at top and an asterisk is a wildcard[^Z5ZONYTlS1w-446]. He uses shift-click to swap quick prayers and hotkeys for banking[^Z5ZONYTlS1w-479].
- **Camera:** expanded inner zoom, outer limit 120 and vertical camera for top-down view[^9neaqoxR-nY-714].

## Inventory, bank and items

- **Inventory Setups** (Plugin Hub) was called so good and underrated; with bank filtering and highlighting it shows the setup including spellbook, can be exported to the clipboard, and he uses it for raids, Slayer, farm runs and everything[^9neaqoxR-nY-2333][^9neaqoxR-nY-2395].
- **Inventory tags** outline items; many players mark melee red, ranged green and magic blue, which he uses[^9neaqoxR-nY-2426]. Inventory Grid with drag delay 100 ms lines up with Anti-drag[^9neaqoxR-nY-2303]. He keeps Inventory viewer off, having used it while streaming[^9neaqoxR-nY-2501].
- **Bank:** GE price and seed vault value on hover, exact bank value off[^9neaqoxR-nY-508]; keyboard bank pin, which saves time and is stream safe[^9neaqoxR-nY-536]; bank tags[^9neaqoxR-nY-536].
- **Item charges, identification, prices and stats:** charges overlay and break warnings[^9neaqoxR-nY-2501]; identification labels for herbs and saplings[^9neaqoxR-nY-2540]; prices on examine, hiding high alchemy values[^9neaqoxR-nY-2570]; theoretical stat change in the item stats tooltip[^9neaqoxR-nY-2570].
- **Ground items:** his second favourite plugin; not seeing highlighted drops is why he rarely plays mobile[^9neaqoxR-nY-1782]. An asterisk wildcard covers sets such as dark totem pieces or all clues[^9neaqoxR-nY-1815]. He hides low-value items (300 GP or less), notifies on highlights, and keeps collapse ground items on[^9neaqoxR-nY-1873][^9neaqoxR-nY-1961]. Ground markers and object markers mark tiles and objects[^9neaqoxR-nY-1961][^9neaqoxR-nY-3254].
- **Loot tracker:** shows loot with total GE value[^w7POGb4jwco-173]. As of April 2019 it also syncs to RuneLite.net, and he advised making an account to keep loot and GE history permanently[^w7POGb4jwco-194]. In 2020 he again keeps it on and uses its ignore list[^9neaqoxR-nY-2735][^9neaqoxR-nY-2735].

## Performance and graphics

He called the GPU plugin his favourite in the game since it offloads work to the graphics card and reduces FPS drops[^9neaqoxR-nY-1609]. His settings: draw distance 90, anti-aliasing MSAA x2, UI scaling nearest neighbor, fog on and compute shaders on[^9neaqoxR-nY-1636][^9neaqoxR-nY-1667][^9neaqoxR-nY-1697]. Animation smoothing is controversial but he calls it important for the Hallowed Sepulchre[^9neaqoxR-nY-389]. As of 2020 maximum FPS is 50 on desktop and 60 on mobile, so FPS control is 50, and an unfocused cap saves CPU while AFKing[^9neaqoxR-nY-1409][^9neaqoxR-nY-1438]. He recommends the Skybox plugin[^9neaqoxR-nY-3750].

## Chat and notifications

- **Chat filter:** he pasted a giant regex to remove scams, beggars and double-money offers[^9neaqoxR-nY-923][^9neaqoxR-nY-955]. Chat notifications alert on his name and a dodgy necklace crumbling[^9neaqoxR-nY-1018]. Timestamps use HHMM[^9neaqoxR-nY-1051].
- **Idle Notifier:** HP warning 20, prayer warning 10, idle movement notifications for Blood Runecrafting[^9neaqoxR-nY-2085][^9neaqoxR-nY-2119].
- **Boost information:** in 2020 important, especially on an [alt](Alt_account.md); he used relative boost info boxes and a threshold warning[^9neaqoxR-nY-628][^9neaqoxR-nY-656]. In 2024 he uses compact mode from RuneLite base settings tucked against the inventory[^Z5ZONYTlS1w-330].
- **Regeneration meter:** spec regeneration ring and HP timer; useful for keeping boosted stats since flicking Rapid Heal resets the timer[^9neaqoxR-nY-3505][^9neaqoxR-nY-3533].
- **Prayer flick helper:** a one-tick timer for one-tick flicking, with exact prayer points kept visible[^9neaqoxR-nY-3385].

## Skilling and activity plugins (2020)

- Clue scroll solver and puzzle solver: some consider them cheating; he finds clues boring and uses them case by case[^9neaqoxR-nY-1083][^9neaqoxR-nY-3440].
- Cooking, Fishing, Mining and Motherlode, Runecrafting, Hunter, Farming Time tracking, Daily task indicator (he keeps herb boxes, battlestaves, bone meal and slime), Kourend Library and Miscellania[^9neaqoxR-nY-1139][^9neaqoxR-nY-1497][^9neaqoxR-nY-2970][^9neaqoxR-nY-3619][^9neaqoxR-nY-2025][^9neaqoxR-nY-3904][^9neaqoxR-nY-1199][^9neaqoxR-nY-2661].
- Implings notifications for dragon, lucky and crystal implings[^9neaqoxR-nY-2183]; Random events (Genie and Surprise Exam)[^9neaqoxR-nY-3475]; Slayer plugin highlights task monsters[^9neaqoxR-nY-3751]; Skill calculator[^9neaqoxR-nY-3705]; XP globes, tracker and updater, which he sends to Wise Old Man[^9neaqoxR-nY-4033][^9neaqoxR-nY-4066].
- NPC aggression timer (made by Woox) draws lines; walking over one resets the 20 minute timer[^9neaqoxR-nY-3030][^9neaqoxR-nY-3030].
- Nightmare Zone: he overrides the overlay and turns on power surge, overload and absorption warnings[^9neaqoxR-nY-3213]. A December 2020 video says the built-in NMZ plugin gives notifications for power-ups, overload and absorption[^czTknAPFq9Y-289]; Plugin Hub's NMZ Utilities adds left-click guzzle on rock cakes[^czTknAPFq9Y-321], and NMZ Optimal Points highlights the best-value bosses[^czTknAPFq9Y-321]. See [Nightmare Zone](Nightmare_Zone.md).
- Chambers of Xeric: scouts screenshot to clipboard and room whitelist and blacklist highlighting[^9neaqoxR-nY-714]. Others he lists: Discord, Emojis, Friend notes, Fairy rings, Tab chat, Interface styles, Login screen, Music, Notes, Screenshot, Twitch, Virtual levels, Wiki, World map, World hopper (ping display important), XP drop[^9neaqoxR-nY-1316][^9neaqoxR-nY-1346][^9neaqoxR-nY-1497][^9neaqoxR-nY-1583][^9neaqoxR-nY-2263][^9neaqoxR-nY-2685][^9neaqoxR-nY-3000][^9neaqoxR-nY-3243][^9neaqoxR-nY-3674][^9neaqoxR-nY-3912][^9neaqoxR-nY-3942][^9neaqoxR-nY-3968][^9neaqoxR-nY-3996].

## Changes over time

- 2019: a short list of eleven plugins (tile indicator, loot tracker, web loot tracking)[^w7POGb4jwco-134].
- 2020: a full from-scratch configuration.
- June 2022: plugins previously only in third-party clients (hide dead NPCs, walk under, monster true tiles, party special attacks) became available in RuneLite[^3C7naDl1ieY-31][^3C7naDl1ieY-116][^3C7naDl1ieY-238].
- 2024: a PvM-focused list with Plugin Hub tools such as Dynamic Tags, Radius Markers and Visual Metronome[^Z5ZONYTlS1w-120][^Z5ZONYTlS1w-208][^Z5ZONYTlS1w-272]. See also [Opinion: Jagex plugin rules](Opinion_Jagex_plugin_rules.md) and [Inferno plugins](Inferno_plugins.md).

## Revision history

| Date | Video | Change |
|---|---|---|
| 2024-02-25 | [Guide to PVM: Plugins (OSRS)](videos/2024-02-25_Z5ZONYTlS1w.md) | Added PvM plugin guide: Monster HP, Radius Markers, Dynamic Tags, metronomes, Custom Menu Swaps; updated key remapping to number row (was F keys remapped) and Boost Information to compact mode. |
| 2022-06-18 | [We Can Use THESE Plugins in Runelite (OSRS)](videos/2022-06-18_3C7naDl1ieY.md) | Added newly allowed plugins: hide dead NPCs, walk under, monster true tiles, party special-attack tracking. |
| 2020-12-24 | [Nightmare Zone Guide (AFK, Points, XP) NEW METHOD (OSRS 2021)](videos/2020-12-24_czTknAPFq9Y.md) | Added Nightmare Zone plugin notes (NMZ Utilities, NMZ Optimal Points). |
| 2020-07-21 | [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md) | Added full 2020 setup walkthrough of plugins and his settings. |
| 2019-04-14 | [11 OP Runelite Plugins!](videos/2019-04-14_w7POGb4jwco.md) | Page created: Tile Indicator and Loot Tracker, including RuneLite.net loot syncing. |
## See also

* [RuneLite](RuneLite.md)

## References

///Footnotes Go Here///
[^w7POGb4jwco-134]: [11 OP Runelite Plugins!](videos/2019-04-14_w7POGb4jwco.md), 2019-04-14. [▶ 2:14](https://youtu.be/w7POGb4jwco?t=134)
[^9neaqoxR-nY-3854]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 1:04:14](https://youtu.be/9neaqoxR-nY?t=3854)
[^9neaqoxR-nY-3855]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 1:04:15](https://youtu.be/9neaqoxR-nY?t=3855)
[^Z5ZONYTlS1w-181]: [Guide to PVM: Plugins (OSRS)](videos/2024-02-25_Z5ZONYTlS1w.md), 2024-02-25. [▶ 3:01](https://youtu.be/Z5ZONYTlS1w?t=181)
[^9neaqoxR-nY-3090]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 51:30](https://youtu.be/9neaqoxR-nY?t=3090)
[^9neaqoxR-nY-3123]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 52:03](https://youtu.be/9neaqoxR-nY?t=3123)
[^9neaqoxR-nY-3184]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 53:04](https://youtu.be/9neaqoxR-nY?t=3184)
[^3C7naDl1ieY-238]: [We Can Use THESE Plugins in Runelite (OSRS)](videos/2022-06-18_3C7naDl1ieY.md), 2022-06-18. [▶ 3:58](https://youtu.be/3C7naDl1ieY?t=238)
[^9neaqoxR-nY-1380]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 23:00](https://youtu.be/9neaqoxR-nY?t=1380)
[^3C7naDl1ieY-31]: [We Can Use THESE Plugins in Runelite (OSRS)](videos/2022-06-18_3C7naDl1ieY.md), 2022-06-18. [▶ 0:31](https://youtu.be/3C7naDl1ieY?t=31)
[^3C7naDl1ieY-60]: [We Can Use THESE Plugins in Runelite (OSRS)](videos/2022-06-18_3C7naDl1ieY.md), 2022-06-18. [▶ 1:00](https://youtu.be/3C7naDl1ieY?t=60)
[^3C7naDl1ieY-87]: [We Can Use THESE Plugins in Runelite (OSRS)](videos/2022-06-18_3C7naDl1ieY.md), 2022-06-18. [▶ 1:27](https://youtu.be/3C7naDl1ieY?t=87)
[^Z5ZONYTlS1w-239]: [Guide to PVM: Plugins (OSRS)](videos/2024-02-25_Z5ZONYTlS1w.md), 2024-02-25. [▶ 3:59](https://youtu.be/Z5ZONYTlS1w?t=239)
[^Z5ZONYTlS1w-386]: [Guide to PVM: Plugins (OSRS)](videos/2024-02-25_Z5ZONYTlS1w.md), 2024-02-25. [▶ 6:26](https://youtu.be/Z5ZONYTlS1w?t=386)
[^3C7naDl1ieY-116]: [We Can Use THESE Plugins in Runelite (OSRS)](videos/2022-06-18_3C7naDl1ieY.md), 2022-06-18. [▶ 1:56](https://youtu.be/3C7naDl1ieY?t=116)
[^3C7naDl1ieY-146]: [We Can Use THESE Plugins in Runelite (OSRS)](videos/2022-06-18_3C7naDl1ieY.md), 2022-06-18. [▶ 2:26](https://youtu.be/3C7naDl1ieY?t=146)
[^Z5ZONYTlS1w-120]: [Guide to PVM: Plugins (OSRS)](videos/2024-02-25_Z5ZONYTlS1w.md), 2024-02-25. [▶ 2:00](https://youtu.be/Z5ZONYTlS1w?t=120)
[^Z5ZONYTlS1w-152]: [Guide to PVM: Plugins (OSRS)](videos/2024-02-25_Z5ZONYTlS1w.md), 2024-02-25. [▶ 2:32](https://youtu.be/Z5ZONYTlS1w?t=152)
[^Z5ZONYTlS1w-208]: [Guide to PVM: Plugins (OSRS)](videos/2024-02-25_Z5ZONYTlS1w.md), 2024-02-25. [▶ 3:28](https://youtu.be/Z5ZONYTlS1w?t=208)
[^Z5ZONYTlS1w-356]: [Guide to PVM: Plugins (OSRS)](videos/2024-02-25_Z5ZONYTlS1w.md), 2024-02-25. [▶ 5:56](https://youtu.be/Z5ZONYTlS1w?t=356)
[^Z5ZONYTlS1w-479]: [Guide to PVM: Plugins (OSRS)](videos/2024-02-25_Z5ZONYTlS1w.md), 2024-02-25. [▶ 7:59](https://youtu.be/Z5ZONYTlS1w?t=479)
[^Z5ZONYTlS1w-272]: [Guide to PVM: Plugins (OSRS)](videos/2024-02-25_Z5ZONYTlS1w.md), 2024-02-25. [▶ 4:32](https://youtu.be/Z5ZONYTlS1w?t=272)
[^Z5ZONYTlS1w-300]: [Guide to PVM: Plugins (OSRS)](videos/2024-02-25_Z5ZONYTlS1w.md), 2024-02-25. [▶ 5:00](https://youtu.be/Z5ZONYTlS1w?t=300)
[^9neaqoxR-nY-3936]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 1:05:36](https://youtu.be/9neaqoxR-nY?t=3936)
[^9neaqoxR-nY-3301]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 55:01](https://youtu.be/9neaqoxR-nY?t=3301)
[^3C7naDl1ieY-177]: [We Can Use THESE Plugins in Runelite (OSRS)](videos/2022-06-18_3C7naDl1ieY.md), 2022-06-18. [▶ 2:57](https://youtu.be/3C7naDl1ieY?t=177)
[^3C7naDl1ieY-208]: [We Can Use THESE Plugins in Runelite (OSRS)](videos/2022-06-18_3C7naDl1ieY.md), 2022-06-18. [▶ 3:28](https://youtu.be/3C7naDl1ieY?t=208)
[^9neaqoxR-nY-1557]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 25:57](https://youtu.be/9neaqoxR-nY?t=1557)
[^9neaqoxR-nY-3355]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 55:55](https://youtu.be/9neaqoxR-nY?t=3355)
[^9neaqoxR-nY-3274]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 54:34](https://youtu.be/9neaqoxR-nY?t=3274)
[^9neaqoxR-nY-416]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 6:56](https://youtu.be/9neaqoxR-nY?t=416)
[^9neaqoxR-nY-448]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 7:28](https://youtu.be/9neaqoxR-nY?t=448)
[^9neaqoxR-nY-2635]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 43:55](https://youtu.be/9neaqoxR-nY?t=2635)
[^Z5ZONYTlS1w-330]: [Guide to PVM: Plugins (OSRS)](videos/2024-02-25_Z5ZONYTlS1w.md), 2024-02-25. [▶ 5:30](https://youtu.be/Z5ZONYTlS1w?t=330)
[^9neaqoxR-nY-2808]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 46:48](https://youtu.be/9neaqoxR-nY?t=2808)
[^9neaqoxR-nY-2824]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 47:04](https://youtu.be/9neaqoxR-nY?t=2824)
[^9neaqoxR-nY-2850]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 47:30](https://youtu.be/9neaqoxR-nY?t=2850)
[^9neaqoxR-nY-2881]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 48:01](https://youtu.be/9neaqoxR-nY?t=2881)
[^9neaqoxR-nY-2914]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 48:34](https://youtu.be/9neaqoxR-nY?t=2914)
[^9neaqoxR-nY-2941]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 49:01](https://youtu.be/9neaqoxR-nY?t=2941)
[^Z5ZONYTlS1w-414]: [Guide to PVM: Plugins (OSRS)](videos/2024-02-25_Z5ZONYTlS1w.md), 2024-02-25. [▶ 6:54](https://youtu.be/Z5ZONYTlS1w?t=414)
[^Z5ZONYTlS1w-446]: [Guide to PVM: Plugins (OSRS)](videos/2024-02-25_Z5ZONYTlS1w.md), 2024-02-25. [▶ 7:26](https://youtu.be/Z5ZONYTlS1w?t=446)
[^9neaqoxR-nY-714]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 11:54](https://youtu.be/9neaqoxR-nY?t=714)
[^9neaqoxR-nY-2333]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 38:53](https://youtu.be/9neaqoxR-nY?t=2333)
[^9neaqoxR-nY-2395]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 39:55](https://youtu.be/9neaqoxR-nY?t=2395)
[^9neaqoxR-nY-2426]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 40:26](https://youtu.be/9neaqoxR-nY?t=2426)
[^9neaqoxR-nY-2303]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 38:23](https://youtu.be/9neaqoxR-nY?t=2303)
[^9neaqoxR-nY-2501]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 41:41](https://youtu.be/9neaqoxR-nY?t=2501)
[^9neaqoxR-nY-508]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 8:28](https://youtu.be/9neaqoxR-nY?t=508)
[^9neaqoxR-nY-536]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 8:56](https://youtu.be/9neaqoxR-nY?t=536)
[^9neaqoxR-nY-2540]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 42:20](https://youtu.be/9neaqoxR-nY?t=2540)
[^9neaqoxR-nY-2570]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 42:50](https://youtu.be/9neaqoxR-nY?t=2570)
[^9neaqoxR-nY-1782]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 29:42](https://youtu.be/9neaqoxR-nY?t=1782)
[^9neaqoxR-nY-1815]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 30:15](https://youtu.be/9neaqoxR-nY?t=1815)
[^9neaqoxR-nY-1873]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 31:13](https://youtu.be/9neaqoxR-nY?t=1873)
[^9neaqoxR-nY-1961]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 32:41](https://youtu.be/9neaqoxR-nY?t=1961)
[^9neaqoxR-nY-3254]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 54:14](https://youtu.be/9neaqoxR-nY?t=3254)
[^w7POGb4jwco-173]: [11 OP Runelite Plugins!](videos/2019-04-14_w7POGb4jwco.md), 2019-04-14. [▶ 2:53](https://youtu.be/w7POGb4jwco?t=173)
[^w7POGb4jwco-194]: [11 OP Runelite Plugins!](videos/2019-04-14_w7POGb4jwco.md), 2019-04-14. [▶ 3:14](https://youtu.be/w7POGb4jwco?t=194)
[^9neaqoxR-nY-2735]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 45:35](https://youtu.be/9neaqoxR-nY?t=2735)
[^9neaqoxR-nY-1609]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 26:49](https://youtu.be/9neaqoxR-nY?t=1609)
[^9neaqoxR-nY-1636]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 27:16](https://youtu.be/9neaqoxR-nY?t=1636)
[^9neaqoxR-nY-1667]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 27:47](https://youtu.be/9neaqoxR-nY?t=1667)
[^9neaqoxR-nY-1697]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 28:17](https://youtu.be/9neaqoxR-nY?t=1697)
[^9neaqoxR-nY-389]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 6:29](https://youtu.be/9neaqoxR-nY?t=389)
[^9neaqoxR-nY-1409]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 23:29](https://youtu.be/9neaqoxR-nY?t=1409)
[^9neaqoxR-nY-1438]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 23:58](https://youtu.be/9neaqoxR-nY?t=1438)
[^9neaqoxR-nY-3750]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 1:02:30](https://youtu.be/9neaqoxR-nY?t=3750)
[^9neaqoxR-nY-923]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 15:23](https://youtu.be/9neaqoxR-nY?t=923)
[^9neaqoxR-nY-955]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 15:55](https://youtu.be/9neaqoxR-nY?t=955)
[^9neaqoxR-nY-1018]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 16:58](https://youtu.be/9neaqoxR-nY?t=1018)
[^9neaqoxR-nY-1051]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 17:31](https://youtu.be/9neaqoxR-nY?t=1051)
[^9neaqoxR-nY-2085]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 34:45](https://youtu.be/9neaqoxR-nY?t=2085)
[^9neaqoxR-nY-2119]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 35:19](https://youtu.be/9neaqoxR-nY?t=2119)
[^9neaqoxR-nY-628]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 10:28](https://youtu.be/9neaqoxR-nY?t=628)
[^9neaqoxR-nY-656]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 10:56](https://youtu.be/9neaqoxR-nY?t=656)
[^9neaqoxR-nY-3505]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 58:25](https://youtu.be/9neaqoxR-nY?t=3505)
[^9neaqoxR-nY-3533]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 58:53](https://youtu.be/9neaqoxR-nY?t=3533)
[^9neaqoxR-nY-3385]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 56:25](https://youtu.be/9neaqoxR-nY?t=3385)
[^9neaqoxR-nY-1083]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 18:03](https://youtu.be/9neaqoxR-nY?t=1083)
[^9neaqoxR-nY-3440]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 57:20](https://youtu.be/9neaqoxR-nY?t=3440)
[^9neaqoxR-nY-1139]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 18:59](https://youtu.be/9neaqoxR-nY?t=1139)
[^9neaqoxR-nY-1497]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 24:57](https://youtu.be/9neaqoxR-nY?t=1497)
[^9neaqoxR-nY-2970]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 49:30](https://youtu.be/9neaqoxR-nY?t=2970)
[^9neaqoxR-nY-3619]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 1:00:19](https://youtu.be/9neaqoxR-nY?t=3619)
[^9neaqoxR-nY-2025]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 33:45](https://youtu.be/9neaqoxR-nY?t=2025)
[^9neaqoxR-nY-3904]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 1:05:04](https://youtu.be/9neaqoxR-nY?t=3904)
[^9neaqoxR-nY-1199]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 19:59](https://youtu.be/9neaqoxR-nY?t=1199)
[^9neaqoxR-nY-2661]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 44:21](https://youtu.be/9neaqoxR-nY?t=2661)
[^9neaqoxR-nY-2183]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 36:23](https://youtu.be/9neaqoxR-nY?t=2183)
[^9neaqoxR-nY-3475]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 57:55](https://youtu.be/9neaqoxR-nY?t=3475)
[^9neaqoxR-nY-3751]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 1:02:31](https://youtu.be/9neaqoxR-nY?t=3751)
[^9neaqoxR-nY-3705]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 1:01:45](https://youtu.be/9neaqoxR-nY?t=3705)
[^9neaqoxR-nY-4033]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 1:07:13](https://youtu.be/9neaqoxR-nY?t=4033)
[^9neaqoxR-nY-4066]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 1:07:46](https://youtu.be/9neaqoxR-nY?t=4066)
[^9neaqoxR-nY-3030]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 50:30](https://youtu.be/9neaqoxR-nY?t=3030)
[^9neaqoxR-nY-3213]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 53:33](https://youtu.be/9neaqoxR-nY?t=3213)
[^czTknAPFq9Y-289]: [Nightmare Zone Guide (AFK, Points, XP) NEW METHOD (OSRS 2021)](videos/2020-12-24_czTknAPFq9Y.md), 2020-12-24. [▶ 4:49](https://youtu.be/czTknAPFq9Y?t=289)
[^czTknAPFq9Y-321]: [Nightmare Zone Guide (AFK, Points, XP) NEW METHOD (OSRS 2021)](videos/2020-12-24_czTknAPFq9Y.md), 2020-12-24. [▶ 5:21](https://youtu.be/czTknAPFq9Y?t=321)
[^9neaqoxR-nY-1316]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 21:56](https://youtu.be/9neaqoxR-nY?t=1316)
[^9neaqoxR-nY-1346]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 22:26](https://youtu.be/9neaqoxR-nY?t=1346)
[^9neaqoxR-nY-1583]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 26:23](https://youtu.be/9neaqoxR-nY?t=1583)
[^9neaqoxR-nY-2263]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 37:43](https://youtu.be/9neaqoxR-nY?t=2263)
[^9neaqoxR-nY-2685]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 44:45](https://youtu.be/9neaqoxR-nY?t=2685)
[^9neaqoxR-nY-3000]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 50:00](https://youtu.be/9neaqoxR-nY?t=3000)
[^9neaqoxR-nY-3243]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 54:03](https://youtu.be/9neaqoxR-nY?t=3243)
[^9neaqoxR-nY-3674]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 1:01:14](https://youtu.be/9neaqoxR-nY?t=3674)
[^9neaqoxR-nY-3912]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 1:05:12](https://youtu.be/9neaqoxR-nY?t=3912)
[^9neaqoxR-nY-3942]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 1:05:42](https://youtu.be/9neaqoxR-nY?t=3942)
[^9neaqoxR-nY-3968]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 1:06:08](https://youtu.be/9neaqoxR-nY?t=3968)
[^9neaqoxR-nY-3996]: [Runelite Plugins Setup From Scratch (OSRS 2020)](videos/2020-07-21_9neaqoxR-nY.md), 2020-07-21. [▶ 1:06:36](https://youtu.be/9neaqoxR-nY?t=3996)

<div class="navbox" markdown="1" data-search-exclude>
<div class="navbox-title">Other topics</div>

**RuneLite plugins** • [RuneLite](RuneLite.md) • [Gearscape](Gearscape.md) • [Tombs of Amascut gear setup](Tombs_of_Amascut_gear_setup.md) • [Jal-Zek](Jal-Zek.md) • [Leagues V: Raging Echoes](Leagues_V_Raging_Echoes.md) • [Doom of Mokhaiotl: gear and inventory](Doom_of_Mokhaiotl_gear_and_inventory.md) • [RuneScape 3](RuneScape_3.md) • [Jal-Xil](Jal-Xil.md) • [Odablock Warriors](Odablock_Warriors.md) • [Yama: budget setup](Yama_budget_setup.md) • [Gargoyle](Gargoyle.md) • [Maw of Whispers](Maw_of_Whispers.md) • [Dagannoth](Dagannoth.md) • [Deadman All-Stars](Deadman_All-Stars.md) • [Kurask](Kurask.md) • [Jagex](Jagex.md) • [Ankou](Ankou.md) • [Run setup](Run_setup.md) • [Shadow rebuild setup](Shadow_rebuild_setup.md) • [Sulphur naga](Sulphur_naga.md) • [Suqah](Suqah.md) • [Kick](Kick.md) • [Troll](Troll.md) • [Shadow of Tumeken boss analysis](Shadow_of_Tumeken_boss_analysis.md) • [Advertising](Advertising.md) • [RS3 Curses](RS3_Curses.md) • [Varlamore](Varlamore.md) • [Westham Weasels](Westham_Weasels.md) • [Gambit](Gambit.md) • [Inferno simulator](Inferno_simulator.md) • [Rebuke](Rebuke.md) • [Rejuvenation](Rejuvenation.md) • [Tree Gnome Stronghold](Tree_Gnome_Stronghold.md) • [Metabolize](Metabolize.md) • [Trinitas](Trinitas.md)

</div>

<div class="catlinks" markdown="1" data-search-exclude>**Category:** [Other topics](topics.md#other)</div>
