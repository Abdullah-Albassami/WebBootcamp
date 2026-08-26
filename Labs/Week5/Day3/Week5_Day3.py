# Week 5 - Day 3
# Intermediate HTML & CSS

# TOPIC 1 — FORMS AND USER INPUT
# HTML forms collect information from users.
# Forms prepare webpage data to be handled by a backend later.
# <form> wraps the form fields.
# action: specifies where the submitted form data is sent.
# method: specifies the HTTP method used when submitting the form.
# Example: <form action="/contact" method="POST">
# Labels explain what each field means.
# Inputs collect typed or selected values.
# A submit button sends the form data.

# TOPIC 2 — CORE FORM ELEMENTS
# Text input: collects regular text.
# Email input: collects email addresses.
# Select list: lets the user choose from predefined options.
# Textarea: collects longer text.
# Checkbox: allows an option to be checked or unchecked.
# Radio button: lets the user choose one option from a group.
# Submit button: submits the form.
# Common examples:
# <input type="text" name="name">
# <input type="email" name="email">
# <textarea name="message"></textarea>
# <button type="submit">Send</button>

# TOPIC 3 — LABEL, ID AND NAME
# Label: tells the user what a field means.
# ID: identifies an element and connects labels, CSS and JavaScript.
# Name: identifies the submitted field for the backend.
# Example:
# <label for="email">Email</label>
# <input id="email" name="email">
# The label's for value should match the input's id.
# Missing name means a field may look correct but submit nothing useful.
# Simple distinction:
# Label = what the user understands.
# ID = identifies/connects the element.
# Name = what the backend receives.

# LAB 1 — CONTACT FORM
# Goal: build a complete form and make every field understandable.
# Create a form wrapper.
# Add text and email inputs.
# Add select, checkbox and textarea fields.
# Add labels for all fields.
# Check name attributes before submission.

# TOPIC 4 — TABLES FOR STRUCTURED DATA
# HTML tables are used for structured data.
# Do not use tables for page layout.
# <caption> explains the table purpose.
# <thead> groups the table header.
# <th> defines a header cell.
# <tbody> contains the actual data rows.
# <tr> defines a table row.
# <td> defines a data cell.
# <tfoot> can group footer rows.
# Basic structure: Caption -> Header -> Rows -> Cells -> Footer.
# Never use tables to position webpage sections.

# TOPIC 5 — MEDIA
# Media adds real content to a webpage.
# Images should include meaningful alt text.
# Example: <img src="photo.jpg" alt="Description of image">
# Audio and video should include controls when users need to interact with them.
# Media files should be optimized.
# Avoid huge uncompressed assets because they slow page loading.

# TOPIC 6 — ACCESSIBILITY BASICS
# Accessibility helps make webpages usable by more people.
# Add labels for all form fields.
# Add meaningful alt text to informative images.
# Use readable and semantic HTML structure.
# Make interactions keyboard-friendly.
# Use ARIA only when needed.
# Provide controls for interactive audio or video.

# TOPIC 7 — EXTERNAL CSS
# External CSS keeps HTML structure and styling separate.
# HTML remains responsible for meaning and structure.
# CSS handles presentation.
# Connect CSS inside the <head>:
# <link rel="stylesheet" href="css/styles.css">
# Example project structure:
# project/
# ├── index.html
# └── css/
#     └── styles.css

# TOPIC 8 — CSS RULE ANATOMY
# A CSS rule targets an element and applies styles to it.
# Selector: chooses the element.
# Property: specifies what is being changed.
# Value: specifies the setting.
# Declaration: a property-value pair.
# Rule set: the complete selector and declaration block.
# Example:
# p {
#     color: blue;
# }
# p = selector.
# color = property.
# blue = value.
# color: blue; = declaration.

# TOPIC 9 — CSS SELECTORS
# CSS selectors answer: which element do I want to style?
# Element selector targets HTML tags.
# Example: p { color: blue; }
# Class selector begins with a dot.
# Example: .btn { padding: 1rem; }
# ID selector begins with #.
# Example: #hero { min-height: 80vh; }
# Descendant selector targets an element inside another element.
# Example: nav a { text-decoration: none; }
# Classes are useful for reusable styles.
# IDs are usually used for specific elements.

# TOPIC 10 — CSS SPECIFICITY
# Specificity decides which CSS rule wins when multiple rules target the same element.
# Simplified order from strongest to weakest:
# Inline style.
# ID selector.
# Class / pseudo-class.
# Element selector.
# Universal selector / browser default.
# Example:
# <p id="main-note" class="note">Hello</p>
# p { color: blue; }
# .note { color: green; }
# #main-note { color: red; }
# The ID selector wins because it has higher specificity.
# The later rule wins only when specificity is equal.

# LAB 2 — SPECIFICITY CHALLENGE
# Goal: stop guessing and start predicting CSS behavior.
# Create one paragraph with a class and ID.
# Style it using element, class and ID selectors.
# Predict the winning color before refreshing.
# Add one hover state and test it.
# Example comparison: p vs .note vs #main-note.

# TOPIC 11 — CSS BOX MODEL
# Every HTML element can be treated as a box.
# Content: the actual text or image.
# Padding: space inside the box around the content.
# Border: line surrounding the padding and content.
# Margin: space outside the border.
# Full model: Margin -> Border -> Padding -> Content.
# The box model controls element size, spacing and layout.
# box-sizing: border-box; makes width and height include padding and border.
# Borders can also help visually debug element boundaries.

# TOPIC 12 — DISPLAY AND FLOW
# The display property affects how elements sit on the page.
# block: starts on a new line.
# inline: stays inside surrounding text.
# inline-block: stays inline but accepts width and height.
# Examples:
# display: block;
# display: inline;
# display: inline-block;

# TOPIC 13 — CSS UNITS
# rem: useful for relative typography and spacing.
# %: relative to another relevant size.
# vw: percentage of viewport width.
# vh: percentage of viewport height.
# Example: font-size: 1rem;
# Example: min-height: 80vh;

# LAB 3 — STYLE THE PROJECT
# Goal: turn the project from plain HTML into a styled webpage.
# Use the external stylesheet: css/styles.css
# Connect it with:
# <link rel="stylesheet" href="css/styles.css">
# Style body typography.
# Add section spacing.
# Style the contact form.
# Add button hover feedback.

# TOPIC 14 — COMMON HTML AND CSS MISTAKES
# Missing labels: forms become harder to use and inaccessible.
# Missing name: the backend receives no useful field value.
# Tables for layout: use CSS layout instead.
# Inline styles everywhere: move styling to external CSS.
# Too many IDs: use classes for reusable styling.

# LAB 4 — COURSE REGISTRATION PAGE
# Goal: build a complete course registration page.
# Create course-registration.html.
# Use semantic page structure.
# Add a page heading and introduction.
# Add an informative image with meaningful alt text.
# Add a table of available courses.
# Add a complete registration form.
# Use at least two fieldsets.
# Include text, email, date, select, radio and checkbox fields.
# Connect labels to their inputs.
# Give every submitted field a name.
# Use appropriate built-in validation.
# Add a submit button.
# Do not use inline styles.

# PROJECT BUILD — STYLE THE HTML PROJECT
# Day 3 moves the project from raw HTML structure toward styled content.
# Project structure:
# project/
# ├── index.html
# ├── css/
# │   └── styles.css
# ├── images/
# └── README.md
# Keep semantic HTML clean.
# Add a contact form with labels and names.
# Add tables and media where appropriate.
# Use external CSS only.
# Apply reusable selectors.
# Understand specificity.
# Apply spacing with the box model.
# Prepare the page for Flexbox and Grid later.

# CONSOLIDATION ACTIVITY
# Open the existing project.
# Add a form.
# Add table/media.
# Link the external CSS file.
# Inspect the result.
# Check that form fields have labels.
# Check that submitted fields have name attributes.
# Check that tables are used only for structured data.
# Check that images have meaningful alt text.
# Check that HTML remains semantic.
# Check that CSS is external.
# Check that selectors target the intended elements.
# Check that specificity behaves as expected.

# KEY TAKEAWAYS
# Form: collects user input.
# action: specifies where submitted form data is sent.
# method: specifies the HTTP method used to submit the form.
# label: explains a form field to the user.
# id: identifies an element and connects related markup or styling.
# name: identifies the submitted field for the backend.
# Table: displays structured data.
# Accessibility: makes webpages usable by more people.
# External CSS: keeps styling separate from HTML structure.
# Selector: targets HTML elements for styling.
# Property: specifies what CSS changes.
# Value: specifies the CSS setting.
# Specificity: decides which competing CSS rule wins.
# Box model: content, padding, border and margin.
# block: starts on a new line.
# inline: stays within the current line.
# inline-block: stays inline while accepting width and height.
# rem, %, vw and vh are common CSS units.
