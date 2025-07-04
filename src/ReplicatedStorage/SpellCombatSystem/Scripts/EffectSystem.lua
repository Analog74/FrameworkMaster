local CollectiveWorldModel = require(game.ReplicatedStorage.FrameworkModules.CollectiveWorldModel)

local EffectSystem = {}

function EffectSystem:ApplyEffect(target, effectType, params)
    if effectType == "Damage" then
        -- Apply damage to target
    elseif effectType == "Overheat" then
        -- Apply DoT status effect
    end
    -- Add more effect types
end

return EffectSystem
