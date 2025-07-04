local Bezier = require(game.ReplicatedStorage.FrameworkModules.Bezier)

local Grounded = {
    name = "Grounded",
    speed = 16,
    jumpPower = 50,
    spellModifiers = { castTimeMultiplier = 1 }
}

function Grounded:Apply(character)
    local humanoid = character:FindFirstChildOfClass("Humanoid")
    if humanoid then
        humanoid.WalkSpeed = self.speed
        humanoid.JumpPower = self.jumpPower
    end
end

return Grounded
