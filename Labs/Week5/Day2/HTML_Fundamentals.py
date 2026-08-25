# Week 5 - Day 2
# HTTP & HTML Fundamentals

# TOPIC 1 — CLIENT-SERVER REQUEST/RESPONSE CYCLE
# Web communication commonly follows a request-response cycle between a client and a server.
# Client: sends an HTTP request; examples include browsers, mobile apps and API clients.
# Server: receives the request, processes it and sends an HTTP response.
# Basic flow: Client -> HTTP Request -> Server -> HTTP Response -> Client.
# An HTTP request commonly contains a method, path, headers and an optional body.
# An HTTP response commonly contains a status code, headers and a body.

# TOPIC 2 — HTTP REQUESTS
# An HTTP request is a message sent from a client to a server.
# Example request: GET /products/laptops HTTP/1.1
# GET = HTTP method.
# /products/laptops = requested path/resource.
# HTTP/1.1 = HTTP protocol version.
# Additional information about the request can be sent through HTTP headers.

# TOPIC 3 — HTTP HEADERS AND BODY
# HTTP headers contain metadata about a request or response.
# Host: identifies the target host/server.
# User-Agent: identifies the client making the request.
# Accept: describes the content types the client accepts.
# Content-Type: describes the format of the data being sent.
# Authorization: can carry authentication information.
# The request body carries data when needed.
# Request bodies may contain form data, JSON or uploaded files.
# GET requests usually do not contain a request body.
# POST, PUT and PATCH commonly send data in the request body.

# TOPIC 4 — HTTP METHODS
# HTTP methods describe the action the client wants the server to perform.
# GET: retrieve/read data.
# POST: send/create new data.
# PUT: replace or fully update a resource.
# PATCH: update part of an existing resource.
# DELETE: remove a resource.
# Example: GET /products retrieves products.
# Example: POST /users can create a new user.
# Example: PATCH /users/1 can update part of an existing user.
# Example: DELETE /users/1 can remove a user.

# TOPIC 5 — HTTP RESPONSES
# An HTTP response is the message a server sends back after processing a request.
# A response commonly contains a status line, headers and a body.
# Example status line: HTTP/1.1 200 OK
# HTTP/1.1 = HTTP protocol version.
# 200 = status code.
# OK = status description.
# Response headers contain metadata about the response.
# Example: Content-Type: text/html tells the browser that the response body contains HTML.
# The response body contains the actual returned content.
# Response bodies may contain HTML, JSON, images, files or other data.

# TOPIC 6 — HTTP STATUS CODES
# HTTP status codes describe the result of a request.
# 2xx = Success.
# 3xx = Redirection.
# 4xx = Client error.
# 5xx = Server error.
# 200 OK: the request succeeded.
# 201 Created: a resource was successfully created.
# 301 Moved Permanently: the resource has permanently moved.
# 302 Found: commonly used for temporary redirection.
# 400 Bad Request: the server cannot process the request because of a client-side request problem.
# 404 Not Found: the requested resource was not found.
# 500 Internal Server Error: an error occurred on the server.
# Status codes are important when debugging HTTP requests and responses.

# TOPIC 7 — HTTP IS STATELESS
# HTTP is stateless, meaning each request is independent by default.
# The server does not automatically remember previous requests from the same client.
# Web applications use additional mechanisms when they need to maintain state between requests.
# Cookies: small pieces of information stored by the browser and sent with later requests.
# Sessions: allow the server to maintain information associated with a user across requests.
# Tokens: can carry authentication or authorization information between clients and servers.
# Cookies, sessions and tokens become important when working with authentication in Django.

# TOPIC 8 — HTTPS AND TLS
# HTTPS = HTTP communication protected using TLS.
# HTTP commonly uses port 80.
# HTTPS commonly uses port 443.
# HTTP itself does not encrypt transmitted data.
# HTTPS uses TLS to protect data while it travels between the client and server.
# TLS helps protect passwords, personal information, payment information and authentication data.
# POST does not automatically make information secure.
# POST defines an HTTP method; HTTPS/TLS provides encrypted communication.

# LAB 1 — INSPECT BROWSER NETWORK TRAFFIC
# Goal: inspect real HTTP requests and responses using browser Developer Tools.
# Open Developer Tools and select the Network tab.
# Reload or visit a website to generate network requests.
# Select a request and inspect its method and URL.
# Inspect the request and response headers.
# Check the HTTP status code.
# Check the response and response time.
# Observe how the browser sends requests and receives responses from the server.

# TOPIC 9 — HTTP AND HTML
# HTTP and HTML have different responsibilities.
# HTTP handles communication between clients and servers.
# HTML describes the structure and meaning of a web page.
# A browser can request an HTML document using HTTP.
# The server can return HTML inside the body of an HTTP response.
# Basic flow: Browser -> HTTP Request -> Server -> HTTP Response containing HTML -> Browser.
# The browser then parses the returned HTML and builds the page.

# TOPIC 10 — HTML
# HTML = HyperText Markup Language.
# HTML provides the structure and meaning of a web page.
# HTML can define headings, paragraphs, images, links, lists, sections and forms.
# HTML is a markup language, not a programming language.
# HTML describes content and structure rather than implementing programming logic.
# Basic browser process: HTML -> Structure -> DOM -> Rendered Page.

# TOPIC 11 — BASIC HTML DOCUMENT STRUCTURE
# <!DOCTYPE html> tells the browser that the document uses modern HTML.
# <html> is the root element of an HTML document.
# <html lang="en"> identifies English as the document language.
# <head> contains information about the document.
# <body> contains the page content displayed by the browser.
# <meta charset="UTF-8"> defines the document character encoding.
# <title> defines the title shown in the browser tab.

# Example:
# <!DOCTYPE html>
# <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <title>My Page</title>
#     </head>
#     <body>
#         <h1>Hello World</h1>
#         <p>My first page</p>
#     </body>
# </html>

# TOPIC 12 — HEAD VS BODY
# <head> contains information about the HTML document.
# Common head content includes the page title, character encoding, CSS links and metadata.
# <body> contains the actual page content.
# Common body content includes headings, paragraphs, images, navigation, lists and buttons.
# Simple distinction: head = information about the document; body = page content.

# LAB 2 — HEAD OR BODY
# Goal: determine whether different HTML content belongs in <head> or <body>.
# Page title -> head.
# Character encoding -> head.
# CSS link -> head.
# SEO metadata -> head.
# Main heading -> body.
# Paragraph -> body.
# Image -> body.
# Navigation -> body.
# Button -> body.

# TOPIC 13 — HTML ELEMENTS, TAGS AND ATTRIBUTES
# HTML documents are built from elements.
# Example: <a href="/contact">Contact</a>
# <a> = opening tag.
# </a> = closing tag.
# Contact = element content.
# href = attribute.
# /contact = attribute value.
# Attributes provide additional information about HTML elements.
# href commonly specifies a link destination.
# src commonly specifies the location of an external resource such as an image.
# alt provides alternative text for an image.
# type can specify the type of an input element.
# name can identify a form field.

# TOPIC 14 — COMMON HTML TAGS
# <h1> = main/highest-level heading.
# <h2> through <h6> = additional heading levels.
# <p> = paragraph.
# <a> = hyperlink.
# <img> = image.
# <ul> = unordered list.
# <ol> = ordered list.
# <li> = list item.
# <div> = generic container.
# <button> = button.
# <section> = section/group of related content.
# Example link: <a href="https://example.com">Visit Website</a>
# Example image: <img src="photo.jpg" alt="Description of image">
# The href attribute specifies the link destination.
# The src attribute specifies the image location.
# The alt attribute provides alternative text describing an image.

# TOPIC 15 — HTML LISTS
# <ul> creates an unordered list where item order is not important.
# <ol> creates an ordered list where item order is important.
# <li> defines an individual list item.
# Example unordered list: <ul><li>Python</li><li>HTML</li><li>CSS</li></ul>
# Example ordered list: <ol><li>First</li><li>Second</li><li>Third</li></ol>

# TOPIC 16 — BLOCK VS INLINE ELEMENTS
# Block elements normally start on a new line and take the available width by default.
# Common block elements include <div>, <p>, <h1> and <section>.
# Two <p> elements normally appear on separate lines.
# Inline elements normally stay within the current line and use only the space they need.
# Common inline elements include <span>, <a>, <strong> and <img>.
# Example: a link inside a paragraph remains within the paragraph instead of starting a new block.

# TOPIC 17 — SEMANTIC HTML
# Semantic HTML uses elements whose names describe the meaning or role of their content.
# <header> = introductory or top-area content.
# <nav> = navigation links.
# <main> = primary page content.
# <section> = group of related content.
# <article> = independent/self-contained content.
# <footer> = footer or bottom information.
# <div> is a generic container without specific semantic meaning.
# Use semantic elements when an element accurately describes the content.
# Use <div> when a neutral container is actually needed.
# Semantic HTML creates clearer document structure.
# Semantic HTML can improve accessibility and SEO.
# Semantic HTML can also make code easier to understand and maintain.

# TOPIC 18 — DOM TREE
# DOM = Document Object Model.
# The browser parses HTML and converts the document into a tree of objects.
# HTML elements have hierarchical parent-child relationships.
# Example: if <p> is directly inside <body>, body is the parent and p is the child.
# A simplified DOM may look like: html -> head + body -> headings, paragraphs, images and other elements.
# Browser Developer Tools can be used to inspect the DOM while a page is running.

# LAB 3 — BUILD THE FIRST HTML PAGE
# Goal: create a basic HTML document and display it in the browser.
# Create index.html.
# Add the basic HTML document structure.
# Add a heading and paragraph.
# Add a list.
# Add a link.
# Add an image with alt text.
# Open the page in the browser.
# A local HTTP server can be started with: python -m http.server 8000
# Open the local server at: http://localhost:8000

# LAB 4 — PROFILE PAGE
# Goal: practice building a page using common HTML elements.
# Create profile.html.
# Add one <h1>.
# Add two <h2> headings.
# Add three paragraphs.
# Add one image.
# Add one external link.
# Add one unordered list.
# Add one ordered list.
# Add one button.

# LAB 5 — SEMANTIC HTML CHALLENGE
# Goal: replace unnecessary generic <div> elements with appropriate semantic HTML elements.
# Identify the purpose of each area before choosing an HTML element.
# A page header can use <header>.
# Navigation links can use <nav>.
# Primary page content can use <main>.
# Related content can use <section>.
# Bottom/footer content can use <footer>.
# The goal is not to remove every <div>; the goal is to choose elements based on the meaning of the content.

# TOPIC 19 — HTTP TO RENDERED PAGE FLOW
# HTTP and HTML work together when a browser loads a web page.
# 1. The browser sends an HTTP request.
# 2. The server receives the request.
# 3. The server processes the request.
# 4. The server sends an HTTP response.
# 5. The response body may contain HTML.
# 6. The browser receives the HTML.
# 7. The browser parses the HTML.
# 8. The browser constructs the DOM.
# 9. The browser renders the page.
# Complete flow: Browser -> HTTP Request -> Server -> HTTP Response -> HTML -> DOM -> Rendered Page.

# PROJECT BUILD — HTML SKELETON
# Initial structure:
# project/
# ├── index.html
# ├── css/
# ├── images/
# └── README.md
# Build the HTML structure before adding styling.
# Main page areas can include a header, navigation, hero section, features section, about section and footer.
# Use semantic HTML elements where appropriate.
# Focus first on correct structure and meaning; CSS styling comes later.

# KEY TAKEAWAYS
# HTTP: protocol used for communication between web clients and servers.
# Request: message sent from a client to a server.
# Response: message returned from a server to a client.
# HTTP method: describes the requested action, such as GET, POST, PUT, PATCH or DELETE.
# Header: metadata sent with an HTTP request or response.
# Body: carries the actual data/content when needed.
# Status code: describes the result of an HTTP request.
# Stateless: HTTP requests are independent by default.
# Cookie: small information stored by the browser and sent with later requests.
# Session: mechanism for maintaining server-side state across requests.
# HTTPS: HTTP protected using TLS.
# TLS: protects data while it travels between the client and server.
# HTML: markup language used to structure web content.
# Head: contains information about an HTML document.
# Body: contains the page content.
# Attribute: provides additional information about an HTML element.
# Block element: normally starts on a new line.
# Inline element: normally stays within the current line.
# Semantic HTML: uses elements that describe the meaning and role of content.
# DOM: browser representation of an HTML document as a tree of objects.
# Complete page flow: HTTP Request -> HTTP Response -> HTML -> DOM -> Rendered Page.