local Iris = require(game.ReplicatedStorage.ThirdParty.Iris)

Iris.Init()
Iris:Connect(function()
    Iris.Window({"GUI Editor"})
    for _, guiConfig in pairs(game.ReplicatedStorage.SpellCombatSystem.GUIConfigs:GetChildren()) do
        local config = require(guiConfig)
        Iris.Text({guiConfig.Name})
        Iris.InputVector2({"Size", config.Size, function(newValue) config.Size = newValue end})
    end
    Iris.End()
end)
