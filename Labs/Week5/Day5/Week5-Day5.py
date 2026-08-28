# Week 5 - Day 5
# CSS Motion, Animations & Libraries

# TOPIC 1 — WHY MOTION MATTERS
# A webpage can work technically and still feel unfinished.
# Motion gives users visible feedback when they hover, click, focus or wait.
# Good animation guides attention without distracting the user.
# Motion is not only decoration; it helps polish the interface.
# The final project should feel responsive, alive and professional.
# Motion turns user actions into visible feedback.

# TOPIC 2 — FROM STATIC PAGE TO RESPONSIVE INTERFACE
# A static element can respond visually when the user interacts with it.
# Basic flow:
# Normal state -> User interaction -> Visual response.
# Common interactions include hover, focus, click and page load.
# Use transitions when moving between two states.
# Use animations when you need a sequence of multiple steps.

# TOPIC 3 — CSS TRANSITIONS
# A transition controls how a CSS property changes between states.
# property: specifies what changes.
# duration: specifies how long the change takes.
# timing-function: controls the speed curve.
# delay: adds optional waiting time before the transition starts.
# Example:
# button {
#     transition: background-color .3s ease, transform .3s ease;
# }
# button:hover {
#     transform: translateY(-4px);
# }

# TOPIC 4 — WHAT SHOULD TRANSITION
# transform is a good choice for movement.
# opacity is a good choice for fade effects.
# background-color is useful for button and interface state changes.
# width and height should usually be avoided for animation.
# Changing width or height can force layout reflow and feel laggy.
# General rule: animate transform and opacity first.

# LAB 1 — INTERACTIVE BUTTON
# Goal: make a button clearly respond to the user.
# Create a button class.
# Add a transition for background and transform.
# Add a :hover state.
# Add a :focus state for keyboard users.
# Test the button in the browser.
# Example:
# .cta {
#     background: var(--main-color);
#     transition: transform .25s ease, background .25s ease;
# }
# .cta:hover,
# .cta:focus {
#     transform: translateY(-4px);
#     background: var(--accent-color);
# }

# TOPIC 5 — CARD LIFT EFFECT
# Card lift is a common UI micro-interaction.
# The card moves slightly upward when hovered.
# A shadow can increase at the same time.
# Example:
# transform: translateY(-8px);
# This effect works well for feature cards and service cards.

# TOPIC 6 — CSS TRANSFORMS
# CSS transforms move, resize, rotate or slant elements.
# transform does not change the document structure.
# translate: moves an element.
# Example: transform: translate(10px, -6px);
# scale: grows or shrinks an element.
# Example: transform: scale(1.05);
# rotate: turns an element.
# Example: transform: rotate(5deg);
# skew: slants an element.
# Example: transform: skew(8deg);

# TOPIC 7 — CSS ANIMATIONS
# CSS animations create multi-step motion.
# Animations use @keyframes.
# Unlike transitions, animations can define several checkpoints over time.
# Animations are useful when motion needs a sequence rather than only two states.

# TOPIC 8 — KEYFRAMES AND ANIMATION TIMELINE
# Keyframes define checkpoints in an animation.
# 0% represents the start.
# 50% can represent a middle state.
# 100% represents the end.
# Example:
# @keyframes fadeIn {
#     0% {
#         opacity: 0;
#         transform: translateY(20px);
#     }
#     100% {
#         opacity: 1;
#         transform: translateY(0);
#     }
# }
# Apply the animation with:
# .hero {
#     animation: fadeIn 1s ease forwards;
# }

# TOPIC 9 — ANIMATION PROPERTIES
# animation-name: specifies which keyframes to use.
# animation-duration: specifies how long the animation runs.
# animation-timing-function: controls how speed changes.
# animation-delay: controls when the animation starts.
# animation-iteration-count: controls how many times it repeats.
# animation-fill-mode: controls which state remains after the animation ends.
# Example shorthand:
# .loader {
#     animation: spin .8s linear infinite;
# }
# spin = animation name.
# .8s = duration.
# linear = timing function.
# infinite = iteration count.

# TOPIC 10 — COMMON ANIMATION PATTERNS
# fadeIn: useful for page or section entrance.
# slideIn: useful for hero text or images.
# pulse: useful for drawing attention to a call-to-action.
# spin: useful for loaders.
# bounce: should be used rarely and carefully.
# reveal: can be used later with JavaScript-controlled classes.
# Use enough motion to support the interface, not to decorate every element.

# LAB 2 — HERO ENTRANCE ANIMATION
# Goal: make the hero section appear intentionally instead of abruptly.
# Animate the hero heading.
# Animate the supporting text.
# Delay the button slightly.
# Use opacity and transform.
# Keep duration around 600-1200ms.
# Example:
# .hero-title {
#     animation: slideIn .9s ease forwards;
# }
# .hero-text {
#     animation: fadeIn 1s ease .25s forwards;
# }
# Suggested sequence:
# Heading -> Text -> Button.

# TOPIC 11 — ANIMATE.CSS
# Animate.css is a library that provides ready-made animation classes.
# It can be included using a stylesheet link.
# Example:
# <link rel="stylesheet"
# href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
# Example usage:
# <h1 class="animate__animated animate__fadeInUp">Welcome</h1>
# Common classes include:
# animate__fadeIn
# animate__slideInUp
# animate__zoomIn
# animate__pulse
# Use only a small library example.
# The main project should still demonstrate custom CSS.

# TOPIC 12 — BOOTSTRAP VS TAILWIND
# Bootstrap and Tailwind both help speed up UI development.
# Bootstrap provides pre-built components.
# Bootstrap includes a grid system.
# Bootstrap is useful for fast classic layouts.
# Bootstrap usually requires less custom CSS at first.
# Tailwind uses utility classes.
# Tailwind composes design directly in HTML.
# Tailwind is highly customizable.
# Tailwind is popular in modern development stacks.

# TOPIC 13 — USING LIBRARIES CAREFULLY
# Libraries can save time but can also hide the underlying CSS.
# Use a library when you need faster components.
# Use a library when you need a small animation.
# Use a library when you understand the CSS behind it.
# Avoid a library when it replaces learning.
# Avoid a library when it makes the page unnecessarily heavy.
# Avoid creating random class combinations without understanding them.
# Project rule:
# Custom CSS first.
# One optional library example.
# Explain the library choice in the README.

# PROJECT BUILD — POLISH THE INTERFACE
# Day 5 moves the project from a static responsive page to a polished interface.
# Add visible feedback for buttons.
# Add card hover effects.
# Add hero entrance animation.
# Prefer transform and opacity.
# Use transitions for state changes.
# Use keyframes for animation sequences.
# Keep motion intentional.
# Avoid over-animating the page.
# Use libraries only when they support the project.

# CONSOLIDATION ACTIVITY
# Open the existing project.
# Add button feedback.
# Add a card lift effect.
# Add a hero animation.
# Test hover states.
# Test focus states.
# Check animation timing.
# Check that motion is not distracting.
# Check that transform and opacity are preferred.
# Check that the page still feels responsive and professional.

# KEY TAKEAWAYS
# Transition: controls how a style changes between two states.
# transform: moves, scales, rotates or skews an element.
# translate: moves an element.
# scale: grows or shrinks an element.
# rotate: turns an element.
# skew: slants an element.
# opacity: controls transparency.
# Animation: creates multi-step motion.
# @keyframes: defines animation checkpoints.
# animation-name: chooses the keyframes.
# animation-duration: controls how long the animation runs.
# animation-timing-function: controls speed behavior.
# animation-delay: controls when the animation starts.
# animation-iteration-count: controls repetition.
# animation-fill-mode: controls the state that remains after animation.
# Animate.css: provides ready-made animation classes.
# Bootstrap: component-based CSS framework.
# Tailwind: utility-first CSS framework.
# Use custom CSS first and libraries only when they add clear value.
