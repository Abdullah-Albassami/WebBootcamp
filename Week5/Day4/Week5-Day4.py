# Week 5 - Day 4
# Flexbox, CSS Grid & Responsive Design

# TOPIC 1 — WHY RESPONSIVE LAYOUTS MATTER
# A webpage should adapt to different screen sizes.
# Flexbox helps align items and build simple rows or columns.
# Grid helps structure page sections, cards and galleries.
# Responsive design makes one page work across desktop, tablet and mobile.
# A good layout is not fixed; it responds.
# Avoid relying on hardcoded widths and manual spacing hacks.

# TOPIC 2 — FLEXBOX MENTAL MODEL
# Flexbox is a one-dimensional layout system.
# It is mainly used for rows, columns and component alignment.
# Flexbox is activated on the parent container.
# The direct children automatically become flex items.
# Example:
# .container {
#     display: flex;
# }
# The parent controls direction, alignment and spacing.
# Common uses include navbars, toolbars, hero content and simple rows.

# TOPIC 3 — MAIN AXIS AND CROSS AXIS
# Flexbox uses a main axis and a cross axis.
# The main axis follows the flex-direction.
# The cross axis runs perpendicular to the main axis.
# With flex-direction: row; the main axis is horizontal.
# With flex-direction: column; the main axis is vertical.
# Changing flex-direction changes how the axes behave.

# TOPIC 4 — JUSTIFY-CONTENT VS ALIGN-ITEMS
# justify-content controls alignment along the main axis.
# align-items controls alignment along the cross axis.
# With flex-direction: row:
# justify-content usually controls horizontal alignment.
# align-items usually controls vertical alignment.
# Common justify-content values:
# flex-start
# center
# flex-end
# space-between
# space-around
# space-evenly
# Common align-items values:
# stretch
# flex-start
# center
# flex-end
# Example:
# .container {
#     display: flex;
#     justify-content: space-between;
#     align-items: center;
# }

# TOPIC 5 — FLEX-DIRECTION, FLEX-WRAP AND GAP
# flex-direction controls whether items flow in a row or column.
# Example: flex-direction: row;
# Example: flex-direction: column;
# flex-wrap allows items to move onto a new line when space runs out.
# Example: flex-wrap: wrap;
# gap adds spacing between flex items.
# Example: gap: 20px;
# Prefer gap over margin hacks for spacing between layout items.
# Example:
# .cards {
#     display: flex;
#     flex-wrap: wrap;
#     gap: 20px;
# }

# TOPIC 6 — WRAPPING
# Without wrapping, content can overflow on narrow screens.
# With wrapping, the same items can move onto new lines.
# Wide screen example:
# Card | Card | Card | Card
# Narrow screen example:
# Card | Card
# Card | Card
# Wrapping is an important part of responsive layouts.

# TOPIC 7 — COMMON FLEXBOX PATTERNS
# Navbar: aligns a logo and navigation links.
# Hero: aligns or centers hero content.
# Buttons: aligns related actions.
# Card row: distributes cards along one row.
# Footer: groups links or sections.
# Form row: aligns labels and inputs.
# Use Flexbox when the main job is alignment.
# Not every layout needs Flexbox, but many components need alignment.

# LAB 1 — FLEXBOX NAVBAR
# Goal: turn the project header into a real navigation bar.
# Open the project from the previous day.
# Create a logo area and three navigation links.
# Apply display: flex to the header or nav container.
# Use justify-content, align-items and gap.
# Test the header at different browser widths.
# Example:
# header {
#     display: flex;
#     justify-content: space-between;
#     align-items: center;
#     gap: 1rem;
# }

# TOPIC 8 — CSS GRID MENTAL MODEL
# CSS Grid is a two-dimensional layout system.
# Grid works with rows and columns at the same time.
# Use Grid when the page needs structure.
# Common uses include cards, galleries, dashboards and page sections.
# Example:
# .features {
#     display: grid;
# }
# Grid does not replace Flexbox.
# Flexbox and Grid are often used together.

# TOPIC 9 — GRID COLUMNS, ROWS AND GAP
# grid-template-columns defines the grid columns.
# Example:
# .cards {
#     display: grid;
#     grid-template-columns: 1fr 1fr 1fr;
#     gap: 20px;
# }
# 1fr means one share of the available space.
# 1fr 1fr 1fr creates three equal columns.
# gap controls spacing between rows and columns.
# Avoid hardcoded widths when responsiveness is expected.

# TOPIC 10 — RESPONSIVE GRID WITH AUTO-FIT AND MINMAX
# A common responsive Grid pattern is:
# grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
# auto-fit fills as many columns as the available width allows.
# minmax(250px, 1fr) gives each column a minimum width of 250px.
# 1fr lets the column grow and use available space.
# This pattern lets cards wrap naturally.
# Example:
# .features-grid {
#     display: grid;
#     grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
#     gap: 1.5rem;
# }

# TOPIC 11 — GRID LINES AND SPANNING
# Grid items can occupy more than one column.
# Example:
# .featured {
#     grid-column: 1 / 3;
# }
# This makes the item start at grid line 1 and end at grid line 3.
# Spanning can make featured content occupy more space.
# Use spanning for meaningful structure, not random decoration.

# TOPIC 12 — FLEXBOX VS GRID
# Use Flexbox for navbar alignment.
# Use Flexbox for buttons and actions.
# Use Flexbox for centering content.
# Use Flexbox for one row or one column.
# Use Grid for card galleries.
# Use Grid for page sections.
# Use Grid for two-dimensional layouts.
# Use Grid for responsive content blocks.
# Simple rule:
# Flexbox aligns.
# Grid structures.
# Most real webpages use both.

# TOPIC 13 — COMBINING FLEXBOX AND GRID
# Different sections of the same page can use different layout systems.
# Header: usually Flexbox.
# Hero: Flexbox or Grid.
# Features: Grid.
# About: often a two-column layout.
# Footer: Flexbox or Grid.
# Use each layout tool where it fits best.

# TOPIC 14 — RESPONSIVE DESIGN
# Responsive design makes the same webpage work on different screen sizes.
# Desktop, tablet and mobile should use the same content.
# The layout should reorganize instead of simply shrinking everything.
# Example:
# Desktop: Text | Image
# Mobile:
# Text
# Image
# Content should stack when horizontal space becomes too small.

# TOPIC 15 — MEDIA QUERIES
# Media queries apply different CSS rules at certain screen widths.
# Example:
# @media (max-width: 768px) {
#     .hero {
#         grid-template-columns: 1fr;
#     }
#
#     nav {
#         flex-direction: column;
#     }
# }
# max-width: 768px means the rules apply when the viewport is 768px or smaller.
# Media queries can change layout, spacing and direction.
# Responsive design is reorganizing content, not just shrinking it.

# TOPIC 16 — RESPONSIVE HEADER
# A desktop navbar may place the logo and links in one row.
# Desktop example:
# LOGO   Home | Courses | About | Contact
# On mobile, the links can stack vertically.
# Mobile example:
# LOGO
# Home
# Courses
# About
# Contact
# flex-direction can be changed inside a media query.

# TOPIC 17 — RESPONSIVE HERO SECTION
# A hero section may contain text and an image.
# Desktop:
# Text | Image
# Mobile:
# Text
# Image
# The content should stack instead of becoming extremely narrow.
# Flexbox can use flex-wrap to help the layout adapt.
# Example:
# .container {
#     display: flex;
#     flex-wrap: wrap;
#     gap: 20px;
# }

# TOPIC 18 — RESPONSIVE FEATURES / COURSES
# Feature and course cards are good use cases for Grid.
# Desktop may show three cards per row.
# Tablet may show two cards per row.
# Mobile may show one card per row.
# Example:
# Desktop: Card | Card | Card
# Tablet:  Card | Card
# Mobile:  Card
# auto-fit and minmax can handle this automatically.

# TOPIC 19 — MOBILE BREAKPOINT CHECKLIST
# Add at least one mobile breakpoint.
# Change the navigation layout when the screen becomes narrow.
# Stack hero content.
# Reduce unnecessary spacing.
# Check that text remains readable.
# Make sure nothing extends outside the screen.
# Resize the browser and inspect the layout early.

# LAB 2 — RESPONSIVE CARD GRID
# Goal: turn the features or services section into a responsive Grid.
# Select the features/services section.
# Add display: grid to the card container.
# Use auto-fit and minmax for the columns.
# Use gap for spacing.
# Resize the browser and verify that the cards wrap correctly.
# Example:
# .features-grid {
#     display: grid;
#     grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
#     gap: 1.5rem;
# }

# LAB 3 — PROJECT LAYOUT UPGRADE
# Goal: apply the day's layout rules to the Unit Project.
# Header: Flexbox navbar.
# Hero: two-column layout.
# Features: responsive Grid.
# About: two-column layout.
# Footer: clean grouped layout.
# Keep all CSS external.
# Use relative paths for images and CSS.
# Avoid inline styles except for tiny demos.
# Test at mobile, tablet and desktop widths.

# TOPIC 20 — COMMON RESPONSIVE LAYOUT MISTAKES
# Using Flexbox for full page grids: use Grid for page structure.
# Hardcoded card widths: prefer %, fr or minmax when responsiveness is needed.
# Margins for everything: use gap inside Flexbox and Grid containers.
# Forgetting flex-wrap: allow items to wrap when needed.
# No mobile testing: resize and inspect the page early.
# The goal is a layout that survives resizing.

# PROJECT BUILD — RESPONSIVE LAYOUT UPGRADE
# Day 4 moves the project from basic styling toward a responsive layout.
# Project structure:
# project/
# ├── index.html
# ├── css/
# │   └── styles.css
# ├── images/
# └── README.md
# Use Flexbox for alignment.
# Use Grid for structured sections.
# Allow content to wrap.
# Use gap for layout spacing.
# Avoid unnecessary hardcoded widths.
# Add at least one mobile breakpoint.
# Test desktop, tablet and mobile widths.
# Keep all CSS external.

# CONSOLIDATION ACTIVITY
# Open the existing project.
# Build a Flexbox navbar.
# Create a responsive hero section.
# Convert the features section to Grid.
# Add a mobile breakpoint.
# Resize and inspect the page.
# Check that the navbar adapts on mobile.
# Check that hero content stacks when needed.
# Check that cards wrap naturally.
# Check that no content overflows the screen.
# Check that spacing remains consistent.
# Check that the page works at desktop, tablet and mobile widths.

# KEY TAKEAWAYS
# Flexbox: one-dimensional layout for rows, columns and alignment.
# Flex container: the parent with display: flex.
# Flex items: direct children of a flex container.
# Main axis: follows flex-direction.
# Cross axis: runs perpendicular to the main axis.
# justify-content: aligns items along the main axis.
# align-items: aligns items along the cross axis.
# flex-direction: controls row or column flow.
# flex-wrap: allows items to move to new lines.
# gap: adds spacing between layout items.
# Grid: two-dimensional layout using rows and columns.
# fr: a share of the available Grid space.
# grid-template-columns: defines Grid columns.
# auto-fit: fits as many columns as possible.
# minmax(): defines a minimum and maximum track size.
# grid-column: controls how many Grid columns an item spans.
# Media query: applies CSS rules based on viewport conditions.
# max-width: commonly defines a breakpoint for smaller screens.
# Flexbox aligns.
# Grid structures.
# Responsive design reorganizes content for different screen sizes.
