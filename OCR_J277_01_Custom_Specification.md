# OCR J277/01 Computer Systems — Custom Priority Specification
## Based on ALL questions from June 2022, June 2023, May 2024, May 2025

> **The 80:20 Verdict: CONFIRMED.**
> Analysis across 4 exam years shows that approximately 7–8 topic areas (out of ~25+ in the full spec)
> account for **55–65 marks out of 80 every single year**. The remaining spec content (embedded systems,
> protocol layers, client-server, Ethernet standards, physical security, fetch-execute standalone, etc.)
> accounts for the remaining 15–25 marks and rotates unpredictably.
> Focus your revision energy on Tier 1 and Tier 2 below.

---

## TIER 1 — Guaranteed Every Year (4/4 years)
*These topics have appeared in every paper without exception. Learn these to near-perfection.*

---

### 1. Number Systems — Binary, Denary, Hexadecimal
**Marks: ~10–13 every year | Always appears as Question 1 or 5**

**What gets tested (every year):**
- Convert denary → 8-bit binary (show working)
- Convert binary → hexadecimal (and vice versa)
- Convert hexadecimal → denary (and vice versa)
- Complete a conversion table (denary / 8-bit binary / 2-digit hex — fill the missing column)
- Identify the largest or smallest from a mixed list of file sizes (bytes, KB, MB, GB, TB)
- File size unit conversions (e.g. how many MB in 2 TB?)

**Binary shifts — always sub-question within Q1/Q5:**
- Identify the result of a left/right binary shift
- State what shift multiplies/divides a number by a power of 2
- E.g. "Describe the binary shift to multiply by 8" → Left shift 3 places

**Binary addition — appeared 2023, 2024, 2025:**
- Add two 8-bit binary numbers, show carries
- Result stays within 8 bits (no overflow tested at GCSE)

**Key facts to know:**
- 1 nibble = 4 bits, 1 byte = 8 bits
- 1 KB = 1000 bytes (or 1024 for KiB — OCR accepts either)
- 1 MB = 1000 KB, 1 GB = 1000 MB, 1 TB = 1000 GB
- Hex digits: 0–9 then A=10, B=11, C=12, D=13, E=14, F=15
- IPv4: each octet is 0–255 (8 bits), four octets separated by full stops
- Left shift = multiply by 2 per place; Right shift = divide by 2 per place

---

### 2. Networking — LAN, WAN, Topologies, Wired vs Wireless
**Marks: ~13–26 every year | Always a major multi-part question**

**What gets tested (every year):**

**LAN vs WAN:**
- Give reasons why a network is a LAN (small/single geographical area, hardware owned by organisation, not using external infrastructure)
- Define LAN and WAN characteristics

**Network topologies (2024, 2025 — strong trend):**
- Describe mesh topology (all/most devices connected to each other, multiple routes, no central device)
- Describe star topology (all devices connect to central switch)
- Benefit and drawback: mesh vs star
  - Mesh benefit: no single point of failure / multiple routes
  - Mesh drawback: expensive — more cables needed / harder to manage
  - Star benefit: easy to add devices / fault isolation
  - Star drawback: if central switch fails, whole network fails

**Wired vs wireless (2023, 2024, 2025):**
- Benefits of adding Wi-Fi: more devices can connect, no cables needed, portable devices can move around
- Drawbacks of wireless: slower speeds, security risks, interference, limited range
- Benefits of wired: faster, more secure, more reliable

**Network performance factors (2022, 2025):**
- Bandwidth: more bandwidth = faster data transfer
- Number of users: more users = more congestion = slower

**What to know about hardware:**
- Router: connects LAN to internet, directs packets between networks
- Switch: connects devices within a LAN, directs data to correct device using MAC address
- "Identify one device to connect the LAN to the internet" → **Router** (came up 2025)

---

### 3. Secondary Storage — Types, Comparison, Justification
**Marks: ~4–9 every year**

**What gets tested every year:**
- Identify the most suitable type of secondary storage for a scenario and justify
- Types: Magnetic (HDD), Solid-state (SSD/USB), Optical (CD/DVD/Blu-ray)
- Calculate storage requirements (e.g. 1000 files × 3 MB = 3000 MB = 3 GB)
- Compare capacity between given sizes

**Key comparison points:**
| | Magnetic (HDD) | Solid-state (SSD) | Optical |
|---|---|---|---|
| Speed | Slower | Fastest | Slow |
| Durability | Less (moving parts) | More (no moving parts) | Fragile |
| Cost per GB | Cheap | Expensive | Very cheap |
| Capacity | Large | Large | Small |
| Portability | Less | More (USB) | Portable |

**Justification question pattern:** State type → give reason linked to the scenario
- "Solid-state because it has no moving parts so is more durable for portable use"
- "Optical because files are only being copied (not run), so fast access speed is not required"

---

### 4. Data Representation — Sound
**Marks: ~3–6 | Appeared 2022, 2024, 2025 (3/4 years)**

**What gets tested:**
- Fill-in-the-blank passage about sound: analogue → digital conversion
- Effect of changing sample rate / bit depth on file size and quality
- Define: sample rate, bit depth, sampling

**Key facts:**
- Analogue sound wave is **sampled** — amplitude measured at regular intervals
- **Sample rate** = number of samples per second (measured in **Hertz**)
- **Bit depth** = number of bits used to represent each sample amplitude
- Higher sample rate → larger file size, better quality
- Higher bit depth → larger file size, wider range of amplitudes, more accurate
- File size formula: sample rate × bit depth × duration (in seconds)

---

### 5. The 8-Mark Extended Response (Ethics/Legal/Environmental)
**Marks: 8 every year | Always marked with * for Quality of Extended Response (QER)**

**What gets tested — different scenario each year but SAME structure:**
- 2022: AI used by social networking websites
- 2023: Facial recognition in a shopping centre
- 2024: Open source vs proprietary software for a game developer
- 2025: Manufacturing decisions — cheaper tablets, stopping software updates

**The question always asks you to include:**
- Ethical issues
- Environmental issues (e-waste, energy consumption, recycling)
- Benefits AND drawbacks (for both parties — company AND customer/user)

**How to get 6–8 marks (Mark Band 3):**
1. Cover at least ONE ethical issue with expansion
2. Cover at least ONE environmental issue with expansion
3. State benefits AND drawbacks
4. Reference BOTH sides (e.g. company AND customers)
5. Write in a structured, logical way

**Universal points that work across almost any tech scenario:**
- **Ethical:** Is it fair? Are users being deceived? Who benefits/loses out? Privacy concerns?
- **Environmental:** E-waste from disposing devices; energy used by servers/data centres; recycling components; carbon footprint of manufacturing
- **Benefits:** Lower cost for consumers, increased access, profit for company
- **Drawbacks:** Job losses, privacy invasion, increased e-waste, security risks, digital divide

---

## TIER 2 — Very Likely (3/4 years)
*These appear in 3 out of 4 years. High priority revision.*

---

### 6. CPU Registers
**Marks: 2–4 | Appeared 2022, 2024, 2025**

**What gets tested:**
- Name two registers and state the purpose of each
- Complete a table of register names and descriptions

**The four registers you must know:**
| Register | Purpose |
|---|---|
| **Program Counter (PC)** | Stores the address of the next instruction to be fetched |
| **Memory Address Register (MAR)** | Stores the address of the data/instruction to be fetched from or written to memory |
| **Memory Data Register (MDR)** | Stores the data/instruction that has been fetched from memory or is about to be written to memory |
| **Accumulator (ACC)** | Stores the result of calculations performed by the ALU |

**Also asked in 2024:** Fetch-execute cycle description — Fetch instruction from memory → Decode instruction → Execute instruction

**CPU performance factors (2024):**
- Clock speed (GHz) — more cycles per second = faster
- Number of cores — more cores = more tasks simultaneously
- Cache size — more cache = less time fetching from RAM

---

### 7. Character Sets — ASCII and Unicode
**Marks: 2–4 | Appeared 2022, 2023, 2025**

**What gets tested:**
- Given part of ASCII table, find binary code for a letter (use pattern — consecutive letters are consecutive binary values)
- Write binary code for a word using ASCII (e.g. "POP")
- Benefit and drawback of Unicode vs ASCII

**Key facts:**
- ASCII uses **7 bits** (128 characters) or 8 bits
- Unicode uses **16+ bits** — can represent characters from all languages, emojis
- **Unicode benefit:** Represents more/wider range of characters, supports all languages
- **Unicode drawback:** Larger file size (uses more bits per character than ASCII)
- In ASCII, letters are in sequential binary order — if K=01001011, then L=01001100, M=01001101

---

### 8. Image Representation and Colour Depth
**Marks: 2–5 | Appeared 2023, 2024, 2025**

**What gets tested:**
- Define pixel
- Calculate file size of bitmap image: width × height × colour depth (bits) ÷ 8 = bytes ÷ 1000/1024 = KB
- State minimum bits needed to represent N colours (find smallest power of 2 ≥ N, e.g. 240 colours → 2^8=256 → **8 bits**)
- Effect of increasing colour depth on file size and image quality
- Read pixel colours from binary data using a colour table

**Key formula:**
```
File size (bits) = width (pixels) × height (pixels) × colour depth (bits)
File size (bytes) = above ÷ 8
File size (KB) = above ÷ 1000 (or 1024)
```

---

### 9. Encryption
**Marks: 2–3 | Appeared 2022, 2024, 2025**

**What gets tested:**
- Explain the purpose AND function of encryption software
- Give reasons why a network should use encryption

**Key answer points:**
- Jumbles/scrambles/encodes the data using an algorithm and key
- Makes data meaningless/unreadable if intercepted
- Only someone with the correct key can decrypt it
- Protects data in transit across networks

---

### 10. DNS and IP Addresses
**Marks: 4–7 | Appeared 2022, 2024, 2025**

**What gets tested:**
- Describe the DNS process (URL → IP address)
- Identify valid vs invalid IPv4 addresses
- Fill-in-the-blank passage about how websites are accessed

**DNS process (must know these steps in order):**
1. Browser checks its **cache** for the IP address matching the URL
2. If not found, URL/domain is sent to a **DNS server**
3. DNS looks up the URL in its database/table
4. If not found, request is passed to a **higher-level DNS server**
5. DNS **returns the IP address** to the browser/computer
6. If not found anywhere, an error is returned

**IPv4 rules:**
- Four groups of numbers (octets) separated by full stops
- Each octet must be **0–255**
- Example: 192.168.1.1 ✓ | 258.0.0.1 ✗ (258 > 255) | 56.1.2.66.1 ✗ (5 octets)

---

### 11. Utility Software
**Marks: 1–3 | Appeared 2023, 2024, 2025**

**What gets tested:**
- State the purpose of utility software
- Explain the purpose and function of encryption software (also counted under encryption)
- Explain defragmentation software

**Key answer:**
- Utility software performs **housekeeping/maintenance** tasks to keep the computer running smoothly
- Examples: antivirus, encryption, defragmentation, backup software, compression tools

**Defragmentation:**
- Files get stored in fragments across the disk
- Defragmentation rearranges file fragments so they are stored contiguously
- This speeds up read/write access

---

### 12. Wired vs Wireless — Performance and Trade-offs
*(See also Networking section above — this gets its own sub-section due to frequency)*
**Appeared 2023, 2024, 2025**

**Wired benefits:** Faster speeds, more secure (harder to intercept), more reliable (no interference)
**Wireless benefits:** Mobile/portable devices can connect, no trailing cables, cheaper to set up (no cabling), more devices can join, accessible from anywhere in range

---

## TIER 3 — Recurring but Rotates (2/4 years)
*Know these — they rotate in roughly every other year. Worth revising after Tier 1 and 2.*

---

### 13. Operating System Functions
**Appeared 2024, 2025**

The four OS management functions and what they do:
| Function | Manages |
|---|---|
| **Memory management** | Allocates RAM to programs; manages multitasking by swapping data in/out of RAM |
| **Peripheral management** | Manages communication with input/output devices; uses device drivers |
| **User management** | Creates/manages user accounts; access permissions |
| **File management** | Creates/renames/deletes files and folders; organises directory structure |

**Exam trick:** "Transfer of data to and from RAM" → Memory management. "Installation of printer driver" → Peripheral management. "Renaming a folder" → File management. "Creation of user accounts" → User management.

---

### 14. Network Protocols
**Appeared 2022, 2023**

| Protocol | Use |
|---|---|
| **HTTP** | View webpages (unsecured) |
| **HTTPS** | View webpages securely (encrypted) |
| **FTP** | Transfer/download files |
| **SMTP** | Send emails |
| **IMAP / POP** | Receive/check emails |

---

### 15. RAM, ROM, and Virtual Memory
**RAM/ROM appeared 2022, 2024 | Virtual memory appeared 2023, 2024**

**RAM vs ROM:**
- RAM: volatile (loses data when power off), stores currently running programs and data
- ROM: non-volatile (keeps data without power), stores firmware/boot instructions

**Virtual memory:**
- When RAM is full, the OS uses part of the hard drive as temporary RAM
- Slower than RAM because hard drives/SSDs are slower
- Allows more programs to run simultaneously than physical RAM allows
- An embedded system (e.g. car cruise control) doesn't need virtual memory because it runs a fixed, single task and always has enough RAM

---

### 16. Compression — Lossy and Lossless
**Appeared 2022, 2023**

| | Lossy | Lossless |
|---|---|---|
| How | Permanently removes data | Finds and removes repeated patterns — fully recoverable |
| File size reduction | Greater | Less |
| Quality | Reduced (permanently) | Unchanged |
| Use for | Images, audio, video (MP3, JPEG) | Text files, executables, anything where exact data matters |

**Why lossy is not suitable for all files:**
- Text documents and programs need exact data — lossy compression would corrupt them

---

### 17. Legislation
**Appeared 2022, 2025**

Three laws to know:
| Act | Covers |
|---|---|
| **Data Protection Act 2018 (DPA / GDPR)** | How personal data is collected, stored, used. Must be accurate, secure, not kept longer than needed, only used for stated purpose |
| **Computer Misuse Act 1990 (CMA)** | Unauthorised access to computer systems; spreading malware; hacking |
| **Copyright, Designs and Patents Act 1988 (CDPA)** | Protects creators' intellectual property; illegal to copy/distribute software without permission |

**DPA compliance steps (came up 2025 with 4 marks):**
- Keep data secure (firewalls, encryption, passwords)
- Don't share/sell data without consent
- Only collect data you need
- Don't keep data longer than necessary
- Ensure data is accurate and up to date
- Allow users to access their data on request
- Notify individuals of data breaches

---

### 18. Cyber Security Threats and Defences
**Appeared 2022, 2023**

**Common threats:**
- **Phishing:** Fake emails/websites trick users into revealing passwords/data
- **Malware:** Malicious software (viruses, ransomware, spyware, trojans)
- **Brute force:** Automated guessing of passwords
- **SQL injection:** Inserting malicious code into a database query
- **Data interception (Man-in-the-middle):** Intercepting data sent across a network

**Defences:**
| Defence | Protects against |
|---|---|
| Firewall | Unauthorised network access |
| Antivirus/anti-malware | Viruses, trojans, spyware |
| Encryption | Data interception |
| Strong passwords | Brute force |
| Two-factor authentication | Phishing, brute force |
| Penetration testing | Identifies vulnerabilities before attackers do |

---

### 19. Embedded Systems
**Appeared 2023, 2024**

**What is an embedded system?**
- A computer system built into a larger device with a specific, dedicated function
- Has its own processor and memory
- Runs software (firmware) stored in ROM
- Does not need a general-purpose OS

**How to answer "why is X an embedded system?":**
- It is a computer system built into [device]
- It performs a specific/single dedicated task
- It has its own processor/ROM/firmware
- It does not run general-purpose software

---

### 20. Open Source vs Proprietary Software
**Appeared 2023, 2024**

| | Open Source | Proprietary |
|---|---|---|
| Source code | Public — anyone can view/modify | Private — only developer sees it |
| Cost | Usually free | Usually paid |
| Developer benefits | Community contributes improvements | Full control, revenue from sales/licensing |
| User benefits | Free, customisable | Support provided, reliable, secure |
| Drawbacks for users | Less support, may have bugs | Expensive, cannot modify |

---

### 21. Cloud Storage
**Appeared 2025 (so far 1/4, but trending — likely to recur)**

**Drawbacks of cloud storage:**
- Requires internet connection to access data
- Ongoing subscription costs
- No control over security — reliant on provider
- Data may be stored in unknown locations (data sovereignty)
- Risk of provider going down
- No control over backups
- Privacy concerns — provider could misuse data

---

## TIER 4 — Low Priority (1/4 years — appeared once only)
*Know the basics, but don't sacrifice time on these over Tier 1-2.*

- **Fetch-execute cycle** (detailed description) — appeared 2024 only
- **CPU performance factors** (clock speed, cores, cache) — appeared 2024 only
- **Client-server model** — appeared 2023 only
- **MAC addresses** — appeared 2024 only
- **Protocol layers** — appeared 2023 only
- **Ethernet as a standard** — appeared 2022 only
- **Physical security methods** — appeared 2022 only
- **Image metadata** — appeared 2022 and 2023 (now 2 years — could rise to Tier 3)

---

## MARKS DISTRIBUTION REALITY CHECK

Based on the 4 papers analysed:

| Tier | Topics | Typical marks available |
|---|---|---|
| Tier 1 (always) | Number systems, Networks, Secondary storage, Sound, Ethics 8-mark | ~45–55 marks |
| Tier 2 (very likely) | CPU registers, ASCII/Unicode, Image/colour depth, Encryption, DNS, Utility software | ~15–20 marks |
| Tier 3 (rotates) | OS functions, Protocols, RAM/ROM, Virtual memory, Compression, Legislation, Threats, Embedded, Open source | ~10–15 marks |
| Tier 4 (rare) | Everything else | ~5–10 marks |

**The 80:20 rule is confirmed:**
Mastering Tier 1 alone puts you in a position to access roughly 55–65% of the marks.
Tier 1 + Tier 2 covers approximately **75–80% of the paper** and represents only about **20–25% of the full spec content.**

The full OCR J277 spec has 25+ distinct topic areas. Only about 5–6 of them appear every single year with significant mark weightings. This is a textbook case of the 80:20 principle in exam design.

---

## QUESTION TYPE PATTERNS

OCR J277/01 uses these question types every year — learn to spot and answer them efficiently:

| Question type | Typical marks | How to answer |
|---|---|---|
| Fill-in-the-blank passage | 4–7 | Read surrounding context carefully; not all words in the box are used |
| Tick box / MCQ | 1–4 | No working needed; read carefully |
| "Define / state what is meant by" | 1 | One precise sentence |
| "Calculate... show your working" | 2 | Show each step; partial marks for method |
| "Describe what is meant by X" | 2 | Two separate points |
| "Identify one/two [things]" | 1–2 | No explanation needed unless asked |
| "Explain why / how" | 2–4 | Point + reason (because...) |
| "Describe one benefit and one drawback" | 2–4 | State + expand each |
| "Justify your choice" | 2–4 | Choice + reason tied to scenario |
| Extended response (*) | 8 | Structured paragraphs: ethical, environmental, both sides |
| Complete the table | 4–5 | Match each row exactly |

---

*Generated from direct analysis of OCR J277/01 papers: June 2022, June 2023, May 2024, May 2025*
