# Movement Guide (High Level PVM (Raids/Inferno)/Skilling) OSRS 2020

| | |
|---|---|
| **Date** | 2020-12-09 |
| **Type** | guide |
| **Video** | [youtu.be/CfKUQwVJbi0](https://youtu.be/CfKUQwVJbi0) |

## Summary

A guide to OSRS movement mechanics for high-level PvM and skilling: the tick system, true tile, running over hazards, diagonal and L running, pathfinding, click-queue priority, ping effects, training tools, and how monsters path. Gnomonkey argues that knowing exactly where your character will go gives huge control for avoiding hazards.

## Outline

- [0:00](https://youtu.be/CfKUQwVJbi0) Why movement is an overlooked mechanic
- [0:26](https://youtu.be/CfKUQwVJbi0?t=26) The tick system and walking versus running
- [0:47](https://youtu.be/CfKUQwVJbi0?t=47) True tile and running over hazards
- [1:22](https://youtu.be/CfKUQwVJbi0?t=82) Boss mechanics you can run through, and ones with line of sight checks
- [2:04](https://youtu.be/CfKUQwVJbi0?t=124) Diagonal movement and L running
- [3:24](https://youtu.be/CfKUQwVJbi0?t=204) Predictable pathfinding and the Pathfinder plugin
- [4:11](https://youtu.be/CfKUQwVJbi0?t=251) Being dragged towards a monster: moving and attacking on the same tick
- [4:50](https://youtu.be/CfKUQwVJbi0?t=290) Tick queues: the second click takes priority
- [5:30](https://youtu.be/CfKUQwVJbi0?t=330) How world ping affects timing
- [6:05](https://youtu.be/CfKUQwVJbi0?t=365) Training: Hallowed Sepulchre, True Tile, Metronome plugins
- [6:48](https://youtu.be/CfKUQwVJbi0?t=408) Bank standing manoeuvres
- [7:16](https://youtu.be/CfKUQwVJbi0?t=436) Monster pathfinding, safespots and corner trapping

## Topics covered

### [Game tick](../Game_tick.md)

- ([0:00](https://youtu.be/CfKUQwVJbi0)) Gnomonkey says movement is one of the most overlooked mechanics in RuneScape, and that knowing where your character will go after you click gives a huge degree of control and helps avoid hazards in PvM and skilling.
- ([0:26](https://youtu.be/CfKUQwVJbi0?t=26)) The game updates every 0.6 seconds, which is a game tick, so 100 game ticks pass per minute.
- ([0:26](https://youtu.be/CfKUQwVJbi0?t=26)) You move one tile per tick while walking and two tiles per tick while running.
- ([0:26](https://youtu.be/CfKUQwVJbi0?t=26)) Clicking something queues that action for the next tick, so your character moves towards where you clicked as soon as the next tick starts.
- ([4:50](https://youtu.be/CfKUQwVJbi0?t=290)) Because actions are queued per tick, if you click somewhere at the start of a tick and somewhere else near the end of the same tick, the second click takes priority as the next tick's action.
- ([4:50](https://youtu.be/CfKUQwVJbi0?t=290)) Gnomonkey says this threw him off while learning Raids 2 in particular because so many actions in the raid are tick perfect.
- ([5:03](https://youtu.be/CfKUQwVJbi0?t=303)) While learning the Scythe walk at Verzik phase 2, Gnomonkey was clicking off Verzik and back onto her so fast that both clicks landed in the same tick, which stopped his character from running away and got him bounced by Verzik every time.
- ([5:03](https://youtu.be/CfKUQwVJbi0?t=303)) Gnomonkey says OSRS is basically a rhythm game and getting a rhythm for the tick system greatly improves clicks and timings in all aspects of the game.

### [True tile](../True_tile.md)

- ([0:56](https://youtu.be/CfKUQwVJbi0?t=56)) While running you are not moving the whole distance from the game's perspective; you effectively teleport two tiles per game tick, skipping every other tile.
- ([0:56](https://youtu.be/CfKUQwVJbi0?t=56)) The highlight current true tile option and the tile indicators plugin show this: the blue tile is where you actually are from the server's perspective.
- ([0:56](https://youtu.be/CfKUQwVJbi0?t=56)) Because of the true tile, you can run over traps in the Rogues' Den without getting hit, and the same applies in many PvM situations.
- ([0:56](https://youtu.be/CfKUQwVJbi0?t=56)) Gnomonkey says lightning in the Hydra fight, the Olm fight, the Gauntlet, and Verzik phase 3 can all be run through if properly timed.
- ([1:29](https://youtu.be/CfKUQwVJbi0?t=89)) Bosses' ground splats that damage you can be run over for free, including Maiden's blood splats from her and her blood spawns, Vorkath's acid (though Gnomonkey would not recommend running in that fight), and Zalcano's red ground traps, which can be run over the corners.
- ([1:29](https://youtu.be/CfKUQwVJbi0?t=89)) You can also run right over the skull bombs in Verzik's phase two.
- ([1:29](https://youtu.be/CfKUQwVJbi0?t=89)) Some attacks have line of sight checks that hit you regardless of running: Xarpus's poison, Galvek's wave walls, and the arrow trap in the Hallowed Sepulchre.
- ([6:05](https://youtu.be/CfKUQwVJbi0?t=365)) Gnomonkey says the True Tile plugin feature is extremely useful because it is always accurate to the server, so you always know where you are.

### [L running](../L_running.md)

- ([2:02](https://youtu.be/CfKUQwVJbi0?t=122)) You can move two tiles in any direction in one tick, including diagonally, so you technically cover distance fastest diagonally; a shorter distance is not always faster.
- ([2:02](https://youtu.be/CfKUQwVJbi0?t=122)) L running means running in an L to any of the eight tiles two away from you, all of which can be reached in a single game tick.
- ([2:29](https://youtu.be/CfKUQwVJbi0?t=149)) On Verzik phase 1, Gnomonkey and a teammate left at the same time to the right side of her and arrived on the same tick even though his character ran diagonally rather than a shorter path.
- ([2:29](https://youtu.be/CfKUQwVJbi0?t=149)) On floor four of the Hallowed Sepulchre, clearing the long arrow trap most efficiently requires clicking two tiles ahead of your true tile to avoid the next arrow, and you can always move out of the way in one tick when clicking properly.
- ([2:59](https://youtu.be/CfKUQwVJbi0?t=179)) You cannot run through objects, so the best you can do is path around them in an L or directly around a corner.
- ([2:59](https://youtu.be/CfKUQwVJbi0?t=179)) Running diagonally one tile normally uses no run energy because you can walk a diagonal tile in one tick, but pathing around an obstacle wastes run energy for very little distance covered, which comes into play at Bloat in the Theatre of Blood.
- ([3:31](https://youtu.be/CfKUQwVJbi0?t=211)) Your character always runs in a straight line before moving diagonally, so L running means running straight along any sized L you click to and then diagonally for the last tile.
- ([3:31](https://youtu.be/CfKUQwVJbi0?t=211)) Gnomonkey says mastery of this is useful for nearly any boss that requires movement, with the most obvious use being the Sotetseg mazes in the Theatre, where L movements and diagonal running let you get through the maze without wasting ticks.

### Pathfinding

- ([2:59](https://youtu.be/CfKUQwVJbi0?t=179)) The game always paths you the shortest distance, and this is predictable if you know how it works.
- ([3:31](https://youtu.be/CfKUQwVJbi0?t=211)) Turning on the Pathfinder external plugin shows exactly how your character will path to any game tile.
- ([6:36](https://youtu.be/CfKUQwVJbi0?t=396)) Gnomonkey says the Pathfinding plugin on the plugin hub may help you understand where your character is going to go; he learned before it existed so did not use it, but calls it a great training tool.
- ([7:16](https://youtu.be/CfKUQwVJbi0?t=436)) Monsters path differently from your character: the game calculates everything for monsters from their south-westernmost tile, and as far as the game sees it that is the only tile that matters.
- ([7:34](https://youtu.be/CfKUQwVJbi0?t=454)) Monsters always path their south-westernmost tile east or west towards you before they path north or south, and a one-tile monster's south-western tile is its only tile.
- ([7:34](https://youtu.be/CfKUQwVJbi0?t=454)) Safespots work on monsters because if the south-western tile tries to walk towards you but the rest of the body is blocked, the monster stands motionless unable to reach you.
- ([8:02](https://youtu.be/CfKUQwVJbi0?t=482)) Corner trapping a monster is used a lot in the Inferno and in raids for mystics. If a monster is diagonally a tile away from you it always tries to path east or west towards you, so if you stand east or west of it and its east and west directions are blocked by obstacles, it never reaches you.

### Dragging

- ([4:01](https://youtu.be/CfKUQwVJbi0?t=241)) If you click a monster outside your attack range, you are dragged towards it and attack, so your character moves and attacks on the exact same game tick.
- ([4:01](https://youtu.be/CfKUQwVJbi0?t=241)) This is visible when players take a first-hit twisted bow shot running up to a boss in the Theatre of Blood, then click to continue running so they reach the boss at the same time as the rest of the team.
- ([4:33](https://youtu.be/CfKUQwVJbi0?t=273)) Gnomonkey says this is most heavily abused at Olm in the Chambers of Xeric, but is useful for almost every boss.
- ([4:33](https://youtu.be/CfKUQwVJbi0?t=273)) When meleeing, if a boss exits an invulnerability period you can stand up to two tiles away and still hit it on the first tick, as if you were standing right next to it.

### Ping

- ([5:30](https://youtu.be/CfKUQwVJbi0?t=330)) World ping does not affect what you click, but visual or sound cues you react to are delayed by the ping time, so you need to click a bit earlier to offset it.
- ([5:39](https://youtu.be/CfKUQwVJbi0?t=339)) On a standard West Coast world, Gnomonkey usually gets 20 to 30 ms of ping, roughly one twentieth of a tick of lag; on an Australian server he gets about 200 ms, about one third of a tick to correct for.
- ([5:39](https://youtu.be/CfKUQwVJbi0?t=339)) If you are not used to higher ping you can lose ticks even while moving if you do not click earlier.

### Movement training tools

- ([6:05](https://youtu.be/CfKUQwVJbi0?t=365)) Gnomonkey highly suggests training Agility at the Hallowed Sepulchre to get a feel for L running, diagonal running and ticks in general; it is how he got his own feel for them.
- ([6:05](https://youtu.be/CfKUQwVJbi0?t=365)) Gnomonkey says Hallowed Sepulchre agility makes ridiculous money at then-current ring prices and is the best Agility XP in the game.
- ([6:05](https://youtu.be/CfKUQwVJbi0?t=365)) The Metronome plugin is always accurate to game ticks; Gnomonkey finds it annoying to use but says it is great for training you to the tick timings.
- ([6:48](https://youtu.be/CfKUQwVJbi0?t=408)) Gnomonkey lists named bank-standing movement tricks: the loop-de-loop and pull, the box trot, the boxer, the baby spike dance, the spike dance, the super spike dance, the slip and slide, and more yet to be named.
- ([7:04](https://youtu.be/CfKUQwVJbi0?t=424)) Bank-standing manoeuvres efficiently waste run energy as quickly as possible, and Gnomonkey suggests practising them while waiting in the Chambers of Xeric lobby for teammates to gear up.
