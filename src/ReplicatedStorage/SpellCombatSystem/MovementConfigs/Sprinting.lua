local Bezier = require(game.ReplicatedStorage.FrameworkModules.Bezier)

local Sprinting = {
    name = "Sprinting",
    speed = 24,
    jumpPower = 50,
    spellModifiers = { castTimeMultiplier = 0.8 }
}

function Sprinting:Apply(character)
    local humanoid = character:FindFirstChildOfClass("Humanoid")
    if humanoid then
        humanoid.WalkSpeed = self.speed
        humanoid.JumpPower = self.jumpPower
    end
end

return Sprinting
