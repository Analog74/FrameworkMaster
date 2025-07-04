local CharacterController = {}

function CharacterController:ApplyState(character, stateName)
    local state = require(game.ReplicatedStorage.SpellCombatSystem.MovementConfigs[stateName])
    state:Apply(character)
end

return CharacterController
