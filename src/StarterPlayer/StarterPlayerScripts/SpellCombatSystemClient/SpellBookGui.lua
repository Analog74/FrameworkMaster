local Roact = require(game.ReplicatedStorage.ThirdParty.Roact)
local RoactRadial = require(game.ReplicatedStorage.ThirdParty.RoactRadial)
local UserInputService = game:GetService("UserInputService")

local SpellBookGui = Roact.Component:extend("SpellBookGui")

function SpellBookGui:init()
    self.state = { selectedSpell = nil }
end

function SpellBookGui:render()
    local inputType = UserInputService:GetLastInputType()
    local isGamepadOrTouch = inputType == Enum.UserInputType.Gamepad1 or inputType == Enum.UserInputType.Touch

    if isGamepadOrTouch then
        return Roact.createElement(RoactRadial, {
            Size = UDim2.new(0, 200, 0, 200),
            Position = UDim2.new(0.5, 0, 0.5, 0),
            Items = {
                { Label = "PlasmaBurst", Icon = "rbxasset://textures/spell_plasma.png", OnClick = function() self:setState({ selectedSpell = "PlasmaBurst" }) end },
                { Label = "QuantumBolt", Icon = "rbxasset://textures/spell_quantum.png", OnClick = function() self:setState({ selectedSpell = "QuantumBolt" }) end },
            }
        })
    else
        return Roact.createElement("ScreenGui", {}, {
            Frame = Roact.createElement("Frame", {
                Size = UDim2.new(0, 300, 0, 400),
                Position = UDim2.new(0.5, -150, 0.5, -200),
                BackgroundColor3 = Color3.new(0, 0, 0),
            }, {
                ListLayout = Roact.createElement("UIListLayout"),
                PlasmaBurst = Roact.createElement("TextButton", {
                    Size = UDim2.new(1, 0, 0, 50),
                    Text = "PlasmaBurst",
                    [Roact.Event.Activated] = function() self:setState({ selectedSpell = "PlasmaBurst" }) end
                }),
                QuantumBolt = Roact.createElement("TextButton", {
                    Size = UDim2.new(1, 0, 0, 50),
                    Text = "QuantumBolt",
                    [Roact.Event.Activated] = function() self:setState({ selectedSpell = "QuantumBolt" }) end
                })
            })
        })
    end
end

return SpellBookGui
