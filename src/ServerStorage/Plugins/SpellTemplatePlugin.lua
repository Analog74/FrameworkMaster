local Iris = require(game.ReplicatedStorage.ThirdParty.Iris)

Iris.Init()
Iris:Connect(function()
    Iris.Window({"Spell Template Editor"})
    for _, spellConfig in pairs(game.ReplicatedStorage.SpellCombatSystem.Spells:GetChildren()) do
        local config = require(spellConfig)
        Iris.Text({config.name})
        Iris.InputNumber({"Mana Cost", config.manaCost, function(newValue) config.manaCost = newValue end})
    end
    Iris.End()
end)
