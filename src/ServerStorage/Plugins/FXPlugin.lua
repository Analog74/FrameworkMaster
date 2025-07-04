local Iris = require(game.ReplicatedStorage.ThirdParty.Iris)

Iris.Init()
Iris:Connect(function()
    Iris.Window({"FX Editor"})
    for _, fxConfig in pairs(game.ReplicatedStorage.SpellCombatSystem.EffectConfigs:GetChildren()) do
        local config = require(fxConfig)
        Iris.Text({fxConfig.Name})
        Iris.InputNumber({"Rate", config.Properties.Rate, function(newValue) config.Properties.Rate = newValue end})
    end
    Iris.End()
end)
