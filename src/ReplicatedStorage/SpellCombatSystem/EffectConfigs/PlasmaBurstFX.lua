local Bezier = require(game.ReplicatedStorage.FrameworkModules.Bezier)
local CameraShake = require(game.ReplicatedStorage.FrameworkModules.CameraShake)

return {
    ClassName = "ParticleEmitter",
    Properties = {
        Rate = 200,
        Lifetime = NumberRange.new(1, 3),
        Color = ColorSequence.new({Color3.new(0, 0.5, 1), Color3.new(0, 0, 1)}),
        Texture = "rbxasset://textures/particles/nano.dds"
    },
    Animation = function(part)
        local path = Bezier:CreateCurve(part.Position, part.Position + Vector3.new(10, 0, 10))
        CameraShake:Apply(game.Players.LocalPlayer, { intensity = 0.5, duration = 1 })
        return path
    end
}
