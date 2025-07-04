# Third-Party Libraries and References

This document summarizes all third-party libraries, APIs, and helpful references used in this project, including installation, usage, documentation, and citation links.

---

## 1. Iris
- **Type:** Immediate-Mode GUI Library for Roblox (inspired by Dear ImGui)
- **Source:** `src/ReplicatedStorage/ThirdParty/Iris/Iris/`
- **Purpose:** For debug, visualization, and tool UIs in Roblox.
- **Key Features:**
  - Immediate-mode UI (no need to retain references to UI elements)
  - Simple API for creating windows, text, buttons, inputs, trees, etc.
  - Fully customizable appearance (themes, colors, fonts)
  - Demo place: [https://rblx.games/11145814918](https://rblx.games/11145814918)
  - Example usage and advanced examples in the README and `lib/demoWindow.lua`
- **Documentation:**
  - [Iris Docs](https://sirmallard.github.io/Iris/)
  - [Dear ImGui Paradigm](https://github.com/ocornut/imgui/wiki/About-the-IMGUI-paradigm)
- **License:** MIT
- **Cite:** SirMallard/Iris, GitHub, https://github.com/SirMallard/Iris

---

## 2. Roact
- **Type:** Declarative UI library for Roblox Lua, inspired by React.
- **Source:** `src/ReplicatedStorage/ThirdParty/Roact/Roact/`
- **Purpose:** For building complex, maintainable Roblox UIs using a component-based approach.
- **Key Features:**
  - Virtual DOM, component-based UI, state management, lifecycle methods
  - Used for building complex, maintainable Roblox UIs
  - Example usage and API in [official docs](https://roblox.github.io/roact)
- **Documentation:**
  - [Roact Documentation](https://roblox.github.io/roact)
- **Status:** Archived (no longer maintained as of Dec 2023). Successor: [react-lua](https://github.com/Roblox/react-lua)
- **License:** Apache 2.0
- **Cite:** Roblox/roact, GitHub, https://github.com/Roblox/roact

---

## 3. ZonePlus
- **Type:** Roblox module for spatial zone management (e.g., triggers, regions, area events).
- **Source:** `src/ReplicatedStorage/ThirdParty/ZonePlus/`
- **Purpose:** For managing spatial zones, triggers, and area-based events in Roblox games.
- **Key Features:**
  - Create and manage 3D zones
  - Detect player and object entry/exit
  - Useful for area-based effects, triggers, and region logic
- **Documentation:**
  - No official docs available at this time. For usage, refer to the code and any local documentation.
  - [ZonePlus GitHub](https://github.com/Zone-Plus/ZonePlus) (currently 404, but widely used in the community)
- **License:** MIT
- **Cite:** Zone-Plus/ZonePlus, GitHub, https://github.com/Zone-Plus/ZonePlus (if/when available)

---

## 4. RoactRadial
- **Type:** Custom/internal module for radial menus in Roact-based UIs.
- **Source:** `src/ReplicatedStorage/ThirdParty/RoactRadial/roactradial.luau`
- **Purpose:** For creating radial menu UIs, likely as a Roact component.
- **Documentation:**
  - No official documentation found. Refer to the code and any project-level docs.
- **Cite:** Internal module unless a public source is available.

---

## 5. RbxGuiLib
- **Type:** Custom/internal GUI library.
- **Source:** `src/ReplicatedStorage/ThirdParty/RbxGuiLib/`
- **Purpose:** For reusable GUI components and utilities.
- **Documentation:**
  - No official documentation found. Refer to the code and any project-level docs.
- **Cite:** Internal module unless a public source is available.

---

## 6. Roblox API and Developer Resources
- **Official API Docs:**
  - [Roblox Creator Docs](https://create.roblox.com/docs/)
  - [Roblox Developer Hub (legacy)](https://developer.roblox.com/)
- **Use these for all Roblox engine classes, services, and scripting references.**

---

## General Tips for Using Third-Party Libraries
- Always check the official documentation and README files for installation and usage instructions.
- For open-source libraries, check the LICENSE file for usage and distribution rights.
- Cite the original repository and author(s) when using or distributing third-party code.
- For custom/internal modules, maintain your own documentation and usage notes for future maintainers.

---

## Example Citation Table

| Library     | Docs/Reference URL(s)                                 | License      | Notes                        |
|-------------|------------------------------------------------------|--------------|------------------------------|
| Iris        | https://github.com/SirMallard/Iris <br> https://sirmallard.github.io/Iris/ | MIT          | Immediate-mode UI, ImGui     |
| Roact       | https://github.com/Roblox/roact <br> https://roblox.github.io/roact | Apache 2.0    | Archived, React-like         |
| ZonePlus    | https://github.com/Zone-Plus/ZonePlus                | MIT          | 404 currently, community lib |
| Roblox API  | https://create.roblox.com/docs/                      | N/A          | Official API docs            |

---

If you need more detailed API documentation, code samples, or usage guides for any of these libraries, refer to their documentation or request a focused summary.
