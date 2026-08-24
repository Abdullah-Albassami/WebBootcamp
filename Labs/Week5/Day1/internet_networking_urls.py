# Week 5 - Day 1
# Internet & Web Fundamentals

# TOPIC 1 — INTERNET VS WEB
# Internet: the global network infrastructure connecting devices and networks worldwide.
# It includes routers, cables, ISPs and other networking infrastructure.
# It carries different services such as the Web, email, DNS, SSH and FTP.
# Web: a service that runs over the Internet using technologies such as HTTP/HTTPS, URLs, browsers and web servers.
# Internet != Web; the Web is one service that uses the Internet.

# TOPIC 2 — PACKET SWITCHING
# Data sent across the Internet is divided into smaller pieces called packets.
# Packets contain information needed to reach their destination.
# Different packets may take different routes through the network.
# The destination receives the packets and reconstructs the original data.
# Packet switching allows traffic to use alternative routes when a path is unavailable.

# TOPIC 3 — INTERNET DEVELOPMENT
# Packet switching was an important foundation for modern computer networking.
# ARPANET was an early packet-switched network and an important predecessor to the Internet.
# TCP/IP became the standard communication model used to connect networks.
# The Web was later created as a service running on top of the Internet.
# Commercial ISPs, broadband, mobile networks and cloud computing expanded Internet usage.

# TOPIC 4 — CLIENTS AND SERVERS
# Client: sends requests; examples include browsers, mobile apps and Python applications.
# Server: listens for requests, processes them and sends responses.
# Basic flow: Client -> Request -> Server -> Response -> Client.
# A browser acts as a client when requesting a website from a web server.

# TOPIC 5 — DNS
# DNS = Domain Name System.
# DNS translates human-readable domain names into IP addresses.
# Example: example.com -> DNS lookup -> IP address.
# DNS is distributed and hierarchical, not a single server.
# A lookup may involve caches, a recursive resolver, root servers, TLD servers and authoritative DNS servers.
# TLD = Top-Level Domain, such as .com, .org or .net.
# The authoritative DNS server provides DNS records for a domain.
# DNS results can be cached to make later lookups faster.

# TOPIC 6 — PRIVATE AND PUBLIC IP ADDRESSES
# An IP address identifies a network interface/device on a network.
# Private IP: used inside a local/private network and is not directly routed across the public Internet.
# Common private addresses may look like 192.168.1.20.
# Public IP: used for communication across the public Internet.
# A home or office router commonly has a public IP provided by the ISP.
# NAT = Network Address Translation.
# NAT allows multiple devices using private IP addresses to communicate externally through a public IP address.

# TOPIC 7 — ROUTING AND HOPS
# Packets usually pass through multiple routers before reaching their destination.
# Router: forwards packets between networks using routing information.
# Gateway: the router/device used to leave the local network.
# ISP = Internet Service Provider; provides connectivity to the Internet.
# Backbone: high-capacity network infrastructure that carries large amounts of Internet traffic.
# IXP = Internet Exchange Point; infrastructure where different networks exchange traffic.
# Hop: one router/step along the route toward a destination.
# Routes may change because of congestion, failures or other network conditions.
# traceroute/tracert can be used to inspect the hops toward a destination.
# Some routers may not respond to traceroute, so not every hop is always visible.

# LAB 1 — INSPECT THE NETWORK
# Goal: inspect the local IP, gateway, connectivity, route hops and latency.
# macOS/Linux: ifconfig
# Get the IP of a specific interface on macOS: ipconfig getifaddr en0
# Find the default gateway on macOS: route -n get default
# Test connectivity: ping google.com
# Send only 4 packets on macOS/Linux: ping -c 4 google.com
# Trace the route on macOS/Linux: traceroute google.com
# Windows: ipconfig
# Send only 4 packets on Windows: ping -n 4 google.com
# Trace the route on Windows: tracert google.com
# Observe: private IP, default gateway, destination IP, hops and latency.

# TOPIC 8 — URL STRUCTURE
# URL = Uniform Resource Locator.
# A URL identifies where a resource is located and how it should be accessed.
# Example: https://example.com:443/products?category=laptop#reviews
# https -> protocol/scheme
# example.com -> domain
# 443 -> port
# /products -> path
# ?category=laptop -> query parameter
# #reviews -> fragment

# TOPIC 9 — PROTOCOLS
# A protocol defines rules that systems follow when communicating.
# HTTP = Hypertext Transfer Protocol; used for web communication.
# HTTPS = HTTP over TLS; provides encrypted web communication.
# SSH = Secure Shell; used for secure remote access.
# SMTP = Simple Mail Transfer Protocol; used for email transmission.
# FTP = File Transfer Protocol; used for file transfer.

# TOPIC 10 — DOMAINS
# A domain is a human-readable name used to identify an Internet resource.
# Example: api.company.org
# Domain names have a hierarchical structure and are interpreted from right to left.
# In api.company.org: org is the TLD, company is the domain and api is a subdomain.
# DNS is used to resolve domain names to IP addresses.

# TOPIC 11 — PORTS
# A computer can run multiple network services at the same time.
# Ports help identify which service/process should receive network traffic.
# HTTP: port 80.
# HTTPS: port 443.
# SSH: port 22.
# PostgreSQL: port 5432.
# Django development server commonly uses port 8000.
# Some development servers commonly use port 3000.
# Example: http://localhost:8000
# http = protocol, localhost = current machine, 8000 = port.
# Many services use standardized or conventional ports.

# TOPIC 12 — PATHS
# A path identifies a particular resource or route on a server/application.
# Example: /products/laptops/macbook
# In frameworks such as Django, URL paths can be matched to application routes.

# TOPIC 13 — QUERY PARAMETERS
# Query parameters provide additional information to the server through the URL.
# They begin after ?.
# Example: ?category=shoes&sort=price
# Multiple query parameters are separated using &.
# They are commonly used for filtering, sorting, searching and pagination.
# Query parameters are sent to the server as part of the request URL.

# TOPIC 14 — URL FRAGMENTS
# A fragment begins with #.
# Example: #reviews
# A fragment commonly identifies a location or state within a page.
# Fragments are handled by the client/browser.
# The fragment is not sent to the server as part of the HTTP request.

# TOPIC 15 — ENDPOINTS
# An endpoint represents a resource or action exposed by a web application or API.
# Example: https://api.example.com:443/v1/users?active=true&page=2
# Domain: api.example.com
# Port: 443
# Path: /v1/users
# Query parameters: active=true and page=2
# Endpoints are commonly used with REST APIs, Django routes, JavaScript fetch requests and GraphQL.
# In Django, URL routes help determine which view handles an incoming request.

# LAB 2 — URL BREAKDOWN
# Goal: practice identifying individual components of URLs.
# Pick three websites and inspect their URLs.
# Identify the protocol, domain, port if shown, path, query parameters and fragment.
# Modify a query parameter when possible and observe how the result changes.
# Example: https://youtube.com/watch?v=abc123xyz
# Protocol: https
# Domain: youtube.com
# Path: /watch
# Query parameter: v=abc123xyz

# TOPIC 16 — LOCALHOST
# localhost refers to the current computer.
# It allows a client to connect to a network service running on the same machine.
# 127.0.0.1 is the commonly used IPv4 loopback address.
# Example: http://localhost:8000
# http = protocol, localhost = current computer, 8000 = port.

# LAB 3 — LOCAL HTTP SERVER
# Python includes a simple HTTP server that can be started from the terminal.
# Start the server: python -m http.server 8000
# Open in the browser: http://localhost:8000
# Browser = client.
# Python http.server process = server.
# localhost = current machine.
# 8000 = port.
# The browser sends an HTTP request to the local Python server.
# The server processes the request and returns an HTTP response.
# Stop the server with Ctrl + C.

# TOPIC 17 — WEB REQUEST FLOW
# A web request combines many of the concepts above.
# 1. The user enters a URL in the browser.
# 2. The browser parses the URL and identifies its components.
# 3. DNS resolves the domain name to an IP address.
# 4. Traffic leaves the local network through the gateway.
# 5. Routers forward packets through networks toward the destination.
# 6. The packets reach the destination server.
# 7. The appropriate server service receives and processes the request.
# 8. The server sends an HTTP response.
# 9. The response travels back through the network.
# 10. The browser receives and renders the response.
# 11. If the URL contains a fragment, the browser handles it locally.

# KEY TAKEAWAYS
# Internet: global infrastructure connecting networks and devices.
# Web: a service that operates over the Internet.
# Packet: a smaller unit of data transmitted through a network.
# DNS: resolves domain names to IP addresses.
# Private IP: used within a private network.
# Public IP: used for communication across the public Internet.
# NAT: translates between private and public addressing.
# Router: forwards packets between networks.
# Gateway: provides a path out of the local network.
# Hop: one routing step toward a destination.
# Protocol: defines communication rules.
# Port: identifies a network service/process.
# URL: identifies where and how to access a resource.
# Path: identifies a resource or route.
# Query parameter: sends additional information to the server.
# Fragment: client-side reference within a page.
# Endpoint: address representing an application/API resource or action.
# localhost: refers to the current computer.
# Client: sends requests.
# Server: processes requests and returns responses.