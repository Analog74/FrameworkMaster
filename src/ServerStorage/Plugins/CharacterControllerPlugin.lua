local Iris = require(game.ReplicatedStorage.ThirdParty.Iris)

Iris.Init()
Iris:Connect(function()
    Iris.Window({"Character Controller Editor"})
    for _, movementConfig in pairs(game.ReplicatedStorage.SpellCombatSystem.MovementConfigs:GetChildren()) do
        local config = require(movementConfig)
        Iris.Text({config.name})
        Iris.InputNumber({"Speed", config.speed, function(newValue) config.speed = newValue end})
    end
    Iris.End()
end)
