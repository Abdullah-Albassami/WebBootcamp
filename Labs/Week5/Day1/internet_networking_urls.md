# Week 5 Day 1 — Internet, Networking & URLs

> Unit 3 — The Web Foundation Before Django

---

## Topic 1 — Internet vs Web

The **Internet** and the **Web** are related, but they are not the same thing.

### Internet

- Global network infrastructure connecting devices.
- Includes routers, cables, and Internet Service Providers (ISPs).
- Moves packets using TCP/IP.
- Carries many different services, including:
  - Web
  - Email
  - DNS
  - SSH
  - FTP

### Web

- A service that runs on top of the Internet.
- Includes websites, browsers, and hyperlinks.
- Mainly uses HTTP/HTTPS, HTML, and URLs.
- Modern web systems also include web applications and APIs.

**Important:** The Internet is not the Web. The Web is only one service that uses the Internet.

---

## Topic 2 — Packet Switching

Data sent across the Internet is split into smaller pieces called **packets**.

- Data is split into small packets.
- Each packet carries destination information.
- Packets can take different routes through the network.
- The destination reassembles the packets.

```text
Message
  |
  +--> Packet 1
  +--> Packet 2
  +--> Packet 3
  +--> Packet 4
         |
         v
     Destination
```

There is no single dedicated path. If one path fails or becomes unavailable, packets may travel through another.

---

## Topic 3 — A Short History of the Internet

| Period | Development |
|---|---|
| 1960s | Packet switching |
| 1969 | ARPANET |
| 1983 | TCP/IP |
| 1990 | Web |
| 1990s | Commercial ISPs |
| 2000s+ | Broadband, mobile, and cloud |

The important idea is not memorizing every date. The history helps explain why the Internet and Web work the way they do today.

---

## Topic 4 — Clients and Servers

Web communication commonly follows the **client-server model**.

### Client

A client sends requests.

Examples:

- Browser
- Mobile app
- Python script
- VS Code extension

### Server

A server:

- Listens for requests.
- Runs application logic.
- Retrieves data when necessary.
- Sends responses.

```text
Client -------- Request --------> Server
Client <------- Response -------- Server
```

---

## Topic 5 — The Journey of a Web Request

What happens after a user enters a URL and sends the request?

```text
Browser
   |
   v
  DNS
   |
   v
Gateway
   |
   v
  ISP
   |
   v
Server
   |
   v
Browser
```

1. The browser prepares the request.
2. DNS finds the IP address associated with the domain.
3. The request leaves the local network through the gateway.
4. The ISP routes the traffic outward.
5. The server receives and processes the request.
6. The server sends a response.
7. The browser receives and renders the response.

---

## Topic 6 — DNS: The Internet's Address Book

**DNS** stands for **Domain Name System**.

Humans prefer names such as:

```text
www.example.com
```

Computers communicate using IP addresses.

DNS translates **domain names into IP addresses**.

### Simplified DNS Lookup

```text
Browser Cache
     |
     v
OS Cache
     |
     v
DNS Resolver
     |
     v
DNS Root
     |
     v
TLD Server (.com, .org, etc.)
     |
     v
Authoritative DNS Server
     |
     v
IP Address Returned
```

The browser, operating system, or router may already have the DNS result cached.

If not, a recursive resolver performs the lookup through the DNS hierarchy.

The authoritative server provides the relevant DNS record.

DNS results can then be cached to make future lookups faster.

**Important:** DNS is not one server. It is a distributed hierarchical system.

---

## Topic 7 — Private and Public IP Addresses

Every networked device needs an address, but not every IP address is publicly reachable.

### Example Local Network

```text
Phone  -> 192.168.1.22
Laptop -> 192.168.1.35
Tablet -> 192.168.1.41
```

These devices use **private IP addresses** inside the local network.

```text
Private Devices
      |
      v
Home Router / NAT
      |
      v
Public IP assigned by ISP
      |
      v
Internet
```

### Private IP

- Used inside a local/private network.
- Not directly routed across the public Internet.

### Public IP

- Used to communicate across the Internet.
- Typically assigned to the router/customer connection by the ISP.

### NAT

**NAT** stands for **Network Address Translation**.

NAT allows multiple private devices to communicate externally using the router's public IP address.

---

## Topic 8 — Routing and Hops

Packets travel through multiple networking devices before reaching their destination.

```text
You
 |
 v
Gateway
 |
 v
ISP
 |
 v
Backbone
 |
 v
IXP
 |
 v
Data Center
 |
 v
Server
```

### Gateway

The device/router used to leave the local network.

### ISP

**Internet Service Provider** — provides connectivity to the Internet.

### Backbone

High-capacity networks that carry large amounts of Internet traffic.

### IXP

**Internet Exchange Point** — infrastructure where different networks exchange traffic.

### Hop

One router/step along the route toward the destination.

Routes can change when paths are unavailable, congested, or damaged.

`traceroute` or `tracert` can show the hops along a route.

Some network devices may not respond to traceroute, so not every hop is always visible.

**Important:** Routers do not know everything about the Internet. They forward traffic according to routing information available to them.

---

## Lab 1 — Inspect Your Network

### Goal

Inspect your:

- Local/private IP
- Default gateway
- Public IP
- Route hops
- Latency

### Windows

```bash
ipconfig
```

### macOS/Linux

Common commands include:

```bash
ifconfig
```

or:

```bash
ip addr
```

### Tasks

1. Find your local/private IP.
2. Find your default gateway.
3. Find your public IP.
4. Trace the route to `google.com`.
5. Record the hops and latency.

### Windows

```bash
tracert google.com
```

### macOS/Linux

```bash
traceroute google.com
```

---

## Topic 9 — URLs

**URL** stands for **Uniform Resource Locator**.

A URL tells the client where a resource is and how to access it.

Example:

```text
https://www.example.com:443/store/products/laptops?brand=apple&sort=price#reviews
```

### URL Structure

| Part | Example | Purpose |
|---|---|---|
| Protocol | `https` | Communication protocol |
| Domain | `www.example.com` | Server/domain name |
| Port | `443` | Identifies the service |
| Path | `/store/products/laptops` | Identifies a resource |
| Query | `?brand=apple&sort=price` | Additional parameters |
| Fragment | `#reviews` | Location/state inside the page |

---

## Topic 10 — Protocols

A **protocol** defines rules for communication between systems.

### HTTP

**Hypertext Transfer Protocol**

- Used for web communication.

### HTTPS

- HTTP over TLS.
- Encrypts web communication using TLS.
- Standard for modern web applications.

### Other Protocols

| Protocol | Purpose |
|---|---|
| HTTP | Web communication |
| HTTPS | Encrypted web communication |
| FTP | File transfer |
| SMTP | Email transmission |
| SSH | Secure remote access |

---

## Topic 11 — Domains

A **domain** is a human-readable name used to identify an Internet resource.

Example:

```text
api.company.org
```

Domain names are hierarchical and interpreted from right to left.

```text
api.company.org
            ^^^
            TLD

    company
    domain

api
subdomain
```

Other examples:

```text
api.company.org
store.shop.co.uk
```

---

## Topic 12 — Ports

A machine can run many network services at the same time.

**Ports help identify which service/process should receive traffic.**

### Common Ports

| Service | Port |
|---|---:|
| HTTP | 80 |
| HTTPS | 443 |
| SSH | 22 |
| Django development server | 8000 |
| Node.js development | Commonly 3000 |
| PostgreSQL | 5432 |

Example:

```text
http://localhost:8000
```

Here:

- `http` → Protocol
- `localhost` → Current machine
- `8000` → Port

**Important:** Ports are not simply random numbers. Many services use standardized or conventional ports.

---

## Topic 13 — Paths

The **path** identifies a particular resource or route.

Example:

```text
/products/laptops/macbook
```

In web frameworks such as Django, paths can map to application routes.

---

## Topic 14 — Query Parameters

Query parameters provide additional information to the server.

They begin after `?`.

Example:

```text
?category=shoes&sort=price
```

Multiple parameters are commonly separated using `&`.

Query parameters can be used for:

- Filtering
- Sorting
- Searching
- Pagination

Query parameters are sent to the server as part of the request URL.

---

## Topic 15 — URL Fragments

A fragment begins with `#`.

Example:

```text
#installation
```

A fragment usually identifies a location or state within the page.

**Important:** The URL fragment is handled by the client/browser. It is not sent to the server as part of the HTTP request.

---

## Topic 16 — Endpoints

An **endpoint** is an address representing a resource or action exposed by a web application or API.

Example:

```text
https://api.example.com:443/v1/users?active=true&page=2
```

Breaking it down:

```text
Domain: api.example.com
Port:   443
Path:   /v1/users

Query Parameters:
active=true
page=2
```

Endpoint thinking appears in:

- REST APIs
- Django routes
- JavaScript `fetch`
- GraphQL APIs

In Django, incoming paths are matched against URL routes to determine which view should handle the request.

---

## Lab 2 — URL Breakdown

### Goal

Stop viewing URLs as one large string and identify their individual components.

### Tasks

1. Pick three websites.
2. Examine each URL.
3. Identify:
   - Protocol
   - Domain
   - Port, if explicitly shown
   - Path
   - Query
   - Fragment
4. Modify a query parameter when possible.
5. Observe how the page behavior changes.

### Example

```text
https://youtube.com/watch?v=abc123xyz
```

Breakdown:

```text
Protocol = https
Domain   = youtube.com
Path     = /watch
Query    = v=abc123xyz
```

---

## Topic 17 — Localhost

`localhost` refers to the **current machine**.

Instead of sending a request to another computer on the Internet, the client connects to a service running on the same computer.

A common loopback address is:

```text
127.0.0.1
```

Example:

```text
http://localhost:8000
```

Breakdown:

```text
http      -> Protocol
localhost -> Current machine
8000      -> Port
```

---

## Lab 3 — Local Web Server

Python can start a simple local HTTP server.

### Start the Server

Run:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

In this example:

- Browser → Client
- Python `http.server` process → Server
- `localhost` → This machine
- `8000` → Port

### Communication

```text
Browser
   |
   | HTTP Request
   v
Python Server :8000
   |
   | HTTP Response
   v
Browser
```

---

## Topic 18 — Common Networking and Web Misconceptions

### Internet = Web ❌

The Web is only one service running on the Internet.

### DNS is one server ❌

DNS is distributed and hierarchical, and DNS results are cached.

### Routers know everything ❌

Routers make forwarding decisions using routing information available to them.

### Ports are random ❌

Ports identify services/processes, and many services use standardized or conventional port numbers.

### URL fragments go to the server ❌

Fragments remain on the client side and are not included in the HTTP request sent to the server.

---

## Topic 19 — Putting the Full Web Request Together

Consider this URL:

```text
https://www.example.com:443/products?category=laptops#reviews
```

The complete journey is:

1. The browser reads and parses the URL.
2. It identifies the protocol, domain, port, path, query, and fragment.
3. DNS resolves the domain name to an IP address.
4. The request leaves the local network through the gateway.
5. Routers forward packets through the Internet.
6. The packets eventually reach the destination server.
7. The appropriate server service receives the connection.
8. The server processes the request.
9. The server sends a response.
10. The response travels back to the client.
11. The browser processes and renders the response.
12. The browser can use the fragment locally to navigate to a particular part or state of the page.

### Complete Flow

```text
URL
 |
 v
Browser
 |
 v
DNS Resolution
 |
 v
Gateway
 |
 v
ISP
 |
 v
Routers / Internet
 |
 v
Server
 |
 v
Response
 |
 v
Browser
 |
 v
Rendered Page
```

---

# Consolidation Activity

Trace one website from its URL to the rendered page:

```text
Choose URL
    |
    v
Break URL
    |
    v
Resolve DNS
    |
    v
Trace Route
    |
    v
Explain Server Response
```

---

# Exit Ticket

By the end of Day 1, you should be able to:

1. Explain the difference between the **Internet and the Web**.
2. Trace the basic journey from **Browser → DNS → Network → Server → Browser**.
3. Identify **private vs public IP addresses**.
4. Break down a **complete URL**.
5. Explain what **`localhost:8000`** means.

---

# Unit Project Seed

Initial project structure:

```text
project/
├── index.html
├── css/
├── images/
└── README.md
```

Tasks:

- Create the folder structure.
- Write a README note explaining what a web request does.
- Save today's screenshots/observations.
- Carry this folder forward into the upcoming HTML/CSS work.