local SpellRegistry = {}
local spells = {}

function SpellRegistry:RegisterAll()
    for _, module in pairs(game.ReplicatedStorage.SpellCombatSystem.Spells:GetChildren()) do
        spells[module.Name] = require(module)
    end
end

function SpellRegistry:GetSpells()
    return spells
end

return SpellRegistry
