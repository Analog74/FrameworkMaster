local Bezier = require(game.ReplicatedStorage.FrameworkModules.Bezier)
local CameraShake = require(game.ReplicatedStorage.FrameworkModules.CameraShake)

return {
    ClassName = "ParticleEmitter",
    Properties = {
        Rate = 100,
        Lifetime = NumberRange.new(1, 2),
        Color = ColorSequence.new({Color3.new(1, 0, 0), Color3.new(1, 0.5, 0)}),
        Texture = "rbxasset://textures/particles/fire_main.dds"
    },
    Animation = function(part)
        local path = Bezier:CreateCurve(part.Position, part.Position + Vector3.new(10, 0, 10))
        CameraShake:Apply(game.Players.LocalPlayer, { intensity = 0.3, duration = 0.5 })
        return path
    end
}
