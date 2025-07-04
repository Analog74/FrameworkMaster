# SpellCombatSystem Integration into FrameworkMaster

## Key Points
- The SpellCombatSystem is a modular framework for a Roblox RPG, inspired by games like *Dark Age of Camelot* and *World of Warcraft*, designed to deliver engaging spell-based combat.
- It seems likely that integrating this system into the `FrameworkMaster` repository will enhance gameplay with dynamic spellcasting, supporting solo, group (up to five players), raid, and PvP modes.
- The system leverages existing modules like `CharacterSheet` and `MoveSet`, ensuring all components share data seamlessly with real-time updates.
- Research suggests that *Dark Age of Camelot*’s battletags and overhead GUIs can inspire intuitive player interfaces, while survival mechanics from *Fallout 76* add depth.
- The integration process involves placing scripts in the `FrameworkMaster` directory structure, using JSON for configurations, and testing for performance and balance.

## System Overview
The SpellCombatSystem is designed to provide a flexible, scalable spellcasting framework for a post-apocalyptic cyberpunk-themed Roblox RPG. It supports various playstyles, including solo adventures, small group dynamics (up to five players), larger raid groups, and competitive PvP, drawing inspiration from games like *Dark Age of Camelot*, *Asheron’s Call*, *Ultima Online*, *World of Warcraft*, *New World*, *Cyberpunk 2077*, *Neuromancer*, *Diablo IV*, *Guild Wars*, *Fallout 76*, and *Brotato*. The system integrates with the `CharacterSheet` for centralized data management, ensuring all components (e.g., movement, inventory, HUD) reflect changes in real-time.

## Core Components
- **Spell Database**: Defines spells with properties like mana cost, cooldown, and effects, stored in `ReplicatedStorage/SpellConfigs`.
- **Spell Caster**: Handles spellcasting logic, including mana checks and effect application, located in `ServerScriptService/SpellCombatSystem`.
- **Effect System**: Applies spell effects (e.g., damage, healing, buffs) to targets, supporting area-of-effect (AOE) mechanics.
- **GUI Integration**: Uses Roact and RoactRadial for spell books, hotbars, and battletags, adapting to mouse/keyboard, gamepad, and touch inputs.
- **FX System**: Manages client-side visual effects (particles, beams) for immersive spell visuals.
- **CharacterSheet**: Centralizes player attributes (e.g., health, mana, energy), ensuring data consistency across systems.

## Integration Approach
The system will be integrated into the `FrameworkMaster` repository at `/Users/analog/Documents/Roblox/_Projects/FrameworkRestructure`, following the directory structure in `DIRECTORY_STRUCTURE.md.html`. The integration leverages existing modules (e.g., `ProfileService`, `Roact`) and ensures compatibility with Roblox APIs as of July 4, 2025.

---

## Detailed Project Analysis and Integration Plan

### Project Overview
The SpellCombatSystem is a modular framework designed to enhance the `FrameworkMaster` repository, a collection of reusable Roblox modules for structured game development. The system aims to deliver a dynamic spellcasting experience, inspired by classic and modern RPGs, with a focus on a post-apocalyptic cyberpunk theme featuring neon-lit ruins and bioluminescent environments. It builds on existing components like `CharacterSheet` and `MoveSet`, adding spell-based combat mechanics that support solo play, small groups (up to five players), larger raid groups, and PvP battlegrounds.

### Inspirations and Mechanics
The system draws from the following games to create an engaging experience:
- **Dark Age of Camelot**: Realm vs. Realm PvP and battletags/overhead GUIs inspire syndicate-based PvP and intuitive interfaces showing player syndicate, level, and health.
- **Asheron’s Call**: Dynamic events and skill-based progression add `eventProgress` and `skillPoints` for flexible stat allocation.
- **Ultima Online**: Open-world freedom and economy suggest `reputation` and `craftingSkill`.
- **World of Warcraft**: PvP battlegrounds and raids inspire `battlegroundScore` and `raidContribution`.
- **New World**: Crafting and faction missions add `craftingLevel` and `missionProgress`.
- **Cyberpunk 2077/Neuromancer**: Cybernetic enhancements introduce `cyberwareLevel` and `hackResistance`.
- **Diablo IV**: Loot-driven progression adds `gearScore`.
- **Guild Wars**: Cooperative play enhances `teamSynergy` for group buffs.
- **Fallout 76**: Survival mechanics add `energy`, `thermal`, and `radiationLevel`.
- **Brotato**: Fast-paced combat inspires `combatStreak` for kill streak bonuses.

### System Components
The SpellCombatSystem comprises several interconnected modules, each with specific roles:

| **Component** | **Description** | **Location** | **API** |
|---------------|-----------------|--------------|---------|
| **Spell Database** | Lua tables defining spell properties (e.g., mana cost, effects). | `src/ReplicatedStorage/SpellConfigs` | Access via `require` |
| **Spell Caster** | Server-side logic for casting spells, checking mana/cooldowns. | `src/ServerScriptService/SpellCombatSystem/SpellCaster.luau` | `CastSpell(player, spellName, target)` |
| **Effect System** | Applies spell effects (damage, healing, AOE). | `src/ServerScriptService/SpellCombatSystem/EffectSystem.luau` | `ApplyEffect(spell, target)` |
| **GUI Integration** | Roact-based spell book, hotbars, and battletags. | `src/StarterPlayer/StarterPlayerScripts/SpellCombatSystemClient` | Roact components |
| **FX System** | Client-side visual effects (particles, beams). | `src/StarterPlayer/StarterPlayerScripts/SpellCombatSystemClient/FXSystem.luau` | Triggered via `SpellFXEvent` |
| **CharacterSheet** | Centralized player data (health, mana, energy). | `src/ReplicatedStorage/FrameworkModules/CharacterSheet.luau` | `get(attribute)`, `set(attribute, value)` |
| **MoveSet** | Template-based movement system. | `src/ReplicatedStorage/FrameworkModules/MoveSet.luau` | `activateMove(moveName)` |
| **Inventory** | Manages items affecting attributes. | `src/ReplicatedStorage/FrameworkModules/Inventory.luau` | `addItem(itemName, quantity)` |
| **Environmental Effects** | Handles survival mechanics (e.g., energy depletion). | `src/ServerScriptService/SpellCombatSystem/EnvironmentalEffects.luau` | `init()`, `handlePlayer(player)` |
| **MoveSetEditorPlugin** | GUI for editing attributes. | `src/Plugin/MoveSetEditorPlugin.lua` | Iris-based GUI |

### Third-Party Dependencies
| **Module** | **Description** | **Source** | **Requirements** |
|------------|-----------------|-----------------|------------------|
| **ProfileService** | Data persistence | [ProfileService GitHub](https://github.com/MadStudioRoblox/ProfileService) | Lua scripting |
| **Roact** | Declarative UI | [Roact GitHub](https://github.com/Roblox/roact) | React-like knowledge |
| **RoactRadial** | Radial menus | `src/ReplicatedStorage/FrameworkModules/RoactRadial` | Roact knowledge |
| **Iris** | Immediate mode UI | `src/ReplicatedStorage/FrameworkModules/Iris` | Lua scripting |
| **ZonePlus** | Zone-based effects | [ZonePlus GitHub](https://github.com/1ForeverHD/ZonePlus) | Lua scripting |
| **Refx** | Visual effects | `src/ReplicatedStorage/FrameworkModules/Refx` | Lua scripting |

### Prototype Implementation
Below is a prototype of the SpellCombatSystem, with key modules implemented as Lua scripts.

#### Spell Database
```lua
return {
    name = "Fireball",
    description = "Launches a fireball, dealing fire damage.",
    manaCost = 20,
    cooldown = 5,
    range = 50,
    castTime = 2,
    effects = {
        damage = 30,
        damageType = "fire",
        aoeRadius = 0,
        duration = 0,
        buffType = nil,
        debuffType = nil
    },
    fx = {
        particle = "FireParticles",
        sound = "FireballSound",
        animation = "CastFireball"
    }
}
```

#### Spell Caster
```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local EffectSystem = require(game.ServerScriptService.SpellCombatSystem.EffectSystem)

local SpellCaster = {}

function SpellCaster:CastSpell(player, spellName, target)
    local spell = require(ReplicatedStorage.SpellConfigs[spellName])
    local characterSheet = player:GetAttribute("CharacterSheet")
    
    if characterSheet:get("mana") < spell.manaCost then
        return false, "Not enough mana"
    end
    
    if os.time() < (characterSheet:get("cooldowns")[spellName] or 0) then
        return false, "Spell on cooldown"
    end
    
    characterSheet:modify("mana", -spell.manaCost)
    characterSheet:set("cooldowns", {[spellName] = os.time() + spell.cooldown})
    
    EffectSystem:ApplyEffect(spell, target)
    ReplicatedStorage.SpellFXEvent:FireClient(player, spell, target)
    
    return true
end

return SpellCaster
```

#### Effect System
```lua
local EffectSystem = {}

function EffectSystem:ApplyEffect(spell, target)
    if spell.effects.aoeRadius > 0 then
        local targets = self:GetTargetsInRadius(target, spell.effects.aoeRadius)
        for _, t in pairs(targets) do
            self:ApplySingleEffect(spell, t)
        end
    else
        self:ApplySingleEffect(spell, target)
    end
end

function EffectSystem:ApplySingleEffect(spell, target)
    if spell.effects.damage then
        local characterSheet = target:GetAttribute("CharacterSheet")
        characterSheet:modify("health", -spell.effects.damage)
        ReplicatedStorage.DamageEvent:FireClient(target, spell.effects.damage, target.Character.HumanoidRootPart.Position)
    end
end

function EffectSystem:GetTargetsInRadius(center, radius)
    local targets = {}
    for _, player in pairs(game.Players:GetPlayers()) do
        if player.Character and (player.Character.HumanoidRootPart.Position - center.Position).Magnitude <= radius then
            table.insert(targets, player)
        end
    end
    return targets
end

return EffectSystem
```

#### Hotbar GUI
```lua
local Roact = require(game.ReplicatedStorage.FrameworkModules.Roact)
local RoactRadial = require(game.ReplicatedStorage.FrameworkModules.RoactRadial)
local UserInputService = game:GetService("UserInputService")

local Hotbar = Roact.Component:extend("Hotbar")

function Hotbar:render()
    local isGamepadOrTouch = UserInputService:GetLastInputType() == Enum.UserInputType.Gamepad1 or UserInputService:GetLastInputType() == Enum.UserInputType.Touch
    if isGamepadOrTouch then
        return Roact.createElement(RoactRadial, {
            Size = UDim2.new(0, 200, 0, 200),
            Position = UDim2.new(0.5, 0, 0.8, 0),
            Items = {
                { Label = "Fireball", Icon = "rbxasset://textures/spell1.png", OnClick = function()
                    game.ReplicatedStorage.CastSpellEvent:FireServer("Fireball", game.Players.LocalPlayer:GetMouse().Hit.Position)
                end }
            }
        })
    else
        return Roact.createElement("Frame", {
            Size = UDim2.new(0, 300, 0, 50),
            Position = UDim2.new(0.5, -150, 0.9, 0),
            BackgroundTransparency = 0.5,
            BackgroundColor3 = Color3.new(0, 0, 0)
        }, {
            Layout = Roact.createElement("UIListLayout", { FillDirection = Enum.FillDirection.Horizontal }),
            Spell1 = Roact.createElement("TextButton", {
                Size = UDim2.new(0, 50, 1, 0),
                Text = "1",
                [Roact.Event.Activated] = function()
                    game.ReplicatedStorage.CastSpellEvent:FireServer("Fireball", game.Players.LocalPlayer:GetMouse().Hit.Position)
                end
            })
        })
    end
end

return Hotbar
```

### Integration Steps
1. **Set Up Directory Structure**:
   - Create `src/ReplicatedStorage/SpellConfigs/` for spell definitions.
   - Create `src/ServerScriptService/SpellCombatSystem/` for server-side modules.
   - Create `src/StarterPlayer/StarterPlayerScripts/SpellCombatSystemClient/` for client-side modules.
   - Ensure `src/ReplicatedStorage/Assets/` contains animations, particles, and sounds.

2. **Implement Spell Database**:
   - Add `Fireball.luau` and other spell definitions to `src/ReplicatedStorage/SpellConfigs/`.
   - Use JSON-like Lua tables for modularity.

3. **Develop Spell Caster**:
   - Place `SpellCaster.luau` in `src/ServerScriptService/SpellCombatSystem/`.
   - Implement mana and cooldown checks, integrating with `CharacterSheet`.

4. **Develop Effect System**:
   - Place `EffectSystem.luau` in `src/ServerScriptService/SpellCombatSystem/`.
   - Implement AOE and single-target effect logic.

5. **Implement GUI Components**:
   - Place `Hotbar.luau` in `src/StarterPlayer/StarterPlayerScripts/SpellCombatSystemClient/`.
   - Add spell book and combat log components using Roact.

6. **Set Up FX System**:
   - Create `FXSystem.luau` in `src/StarterPlayer/StarterPlayerScripts/SpellCombatSystemClient/`.
   - Use Refx for particle effects triggered by `SpellFXEvent`.

7. **Integrate with CharacterSheet**:
   - Update `CharacterSheet.luau` to include spell-related attributes (e.g., `mana`, `cooldowns`).
   - Ensure `CharacterSheet` updates propagate to `SpellCaster` and GUI.

8. **Update Project Configuration**:
   - Modify `default.project.json` to include new paths:
     ```json
     {
         "name": "SpellCombatSystem",
         "tree": {
             "$className": "DataModel",
             "ReplicatedStorage": {
                 "$path": "src/ReplicatedStorage"
             },
             "ServerScriptService": {
                 "$path": "src/ServerScriptService"
             },
             "StarterPlayer": {
                 "$path": "src/StarterPlayer"
             },
             "Plugin": {
                 "$path": "src/Plugin"
             }
         }
     }
     ```

9. **Sync with Rojo**:
   - Run `rojo serve` in `/Users/analog/Documents/Roblox/_Projects/FrameworkRestructure`.

10. **Update Manifest**:
    - Run `python3 generate_systems_summary.py` to update `file_list.txt`.

11. **Test and Balance**:
    - Test spellcasting with 50+ players using `ProfileStore.Mock`.
    - Balance spell effects based on attachment 7 notes.
    - Verify GUI responsiveness across input methods (mouse/keyboard, gamepad, touch).

### Next Steps
- **Expand Spell Database**: Add more spells (e.g., healing, buffs) with varied effects.
- **Implement PvP Battlegrounds**: Create mini-games inspired by *World of Warcraft* using `battlegroundScore`.
- **Add Raid Events**: Develop dynamic events with `eventProgress` (*Asheron’s Call*).
- **Enhance GUI**: Add spell tooltips and customizable hotbar layouts (*Dark Age of Camelot*).
- **Test Multiplayer**: Simulate 100 players to ensure performance.
- **Gather Feedback**: Refine spell balance and GUI based on playtester input.
