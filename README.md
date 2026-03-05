# Reflection Report – UCSC Vibe Day 01

## Overview

This report documents the AI-assisted development session for the **Student Profile Card** project, built using HTML and CSS as part of the UCSC Vibe Day 01 activity.

---

## Prompts Used

Below are the prompts submitted to GitHub Copilot during this session:

1. **"create a student profile card with pure html and css. Card should include name, stream, short bio and a profile image placeholder. Structure with divs and include a header section as well."**  
   Generated the initial `index.html` with a styled student profile card containing a coloured header band, an avatar placeholder, student name, stream badge, divider, and bio — all built with pure HTML and CSS.

2. **"remove header and footer"**  
   Removed the page-level `<header>` and `<footer>` elements, leaving only the core profile card centered on the page.

3. **"change the primary color to #FE2A14"**  
   Applied the new primary color (`#FE2A14`) across the card header gradient, the stream badge text color, and the badge background tint in `index.html`.

4. **"suggest possible improvements to the id card page using only pure html and css"**  
   Received a set of design and UX improvement suggestions — including dark mode support, micro-interactions, refined typography, CSS custom properties for theming, and subtle shadows and gradients — all achievable without JavaScript or external libraries.

5. **"add dark mode support, subtle micro interactions. Improve the design to match an official academic setting. Slight curves and gradients and slight shadows are required."**  
   Implemented the full redesign: introduced CSS custom properties with a `@media (prefers-color-scheme: dark)` block for automatic dark mode, added hover lift and avatar scale micro-interactions, redesigned the card header with an academic crimson gradient, added a university name label, refined badge and typography styles, and applied consistent subtle shadows throughout.

6. **"relax the spacing among elements and increase the scale of the card a bit"**  
   Increased the card width from 320px to 360px, expanded the header band height, enlarged the avatar, loosened internal padding on the card content, added more breathing room between the stream badge and divider, and improved the bio line-height for a more open, readable layout.

---

## Reflections

Working with an AI coding assistant significantly accelerated the development workflow. Natural-language prompts handled complex, multi-property changes simultaneously — from color theming to full dark mode implementation — without needing to manually locate each CSS rule. The session demonstrated how vibe coding translates intent directly into precise, production-ready code with minimal friction.

---

## GitHub Repository

[https://github.com/ravmax-rdl/UCSC_Vibe_Day01](https://github.com/ravmax-rdl/UCSC_Vibe_Day01)
