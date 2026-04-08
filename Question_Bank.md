# OCR J277/01 — Exam Question Bank
## Tier 1 & Tier 2 Topics Only | All questions styled after real OCR papers

---

# TOPIC 1: NUMBER SYSTEMS

## 1.1 Denary ↔ Binary Conversions

**Q1.** Convert the denary number **185** into 8-bit binary. Show your working. [2]

**Mark scheme:**
- 1 mark: correct working shown (e.g. using column headers 128/64/32/16/8/4/2/1)
- 1 mark: **10111001**

---

**Q2.** Convert the 8-bit binary number **01101010** into denary. Show your working. [2]

**Mark scheme:**
- 1 mark: correct working (64+32+8+2 = ...)
- 1 mark: **106**

---

**Q3.** Convert the denary number **221** into 8-bit binary. Show your working. [2]

**Mark scheme:**
- 1 mark: correct working
- 1 mark: **11011101**

---

## 1.2 Binary ↔ Hexadecimal Conversions

**Q4.** Convert the binary number **10110100** into hexadecimal. [1]

**Mark scheme:**
- **B4** (split into nibbles: 1011=B, 0100=4)

---

**Q5.** Convert the hexadecimal number **3F** into denary. Show your working. [2]

**Mark scheme:**
- 1 mark: working shown (3×16 + 15×1 OR 3×16=48, F=15, 48+15=...)
- 1 mark: **63**

---

**Q6.** Convert the hexadecimal number **A7** into denary. Show your working. [2]

**Mark scheme:**
- 1 mark: working (A=10, 10×16=160, 7×1=7, 160+7=...)
- 1 mark: **167**

---

**Q7.** Complete the table by writing in the missing value for each number. [4]

| Denary | 8-bit Binary | 2-digit Hexadecimal |
|--------|-------------|---------------------|
| 45     |             | 2D                  |
|        | 10010110    | 96                  |
| 200    | 11001000    |                     |
|        |             | FF                  |

**Mark scheme (1 mark each correct box):**
- Row 1: **00101101**
- Row 2: **150**
- Row 3: **C8**
- Row 4: **255** / **11111111**

---

## 1.3 File Size Units

**Q8.** Tick (✓) one box to identify the quantity of kilobytes that is the same as 3 gigabytes. [1]

- [ ] 300 KB
- [ ] 3,000 KB
- [ ] 3,000,000 KB
- [ ] 300,000 KB

**Mark scheme:** **3,000,000 KB** ✓

---

**Q9.** Tick (✓) one box to identify the largest file size. [1]

- [ ] 5,000,000 bytes
- [ ] 4,800 KB
- [ ] 4.9 MB
- [ ] 0.005 GB

**Mark scheme:** **0.005 GB** (= 5 MB = 5,000,000 bytes; 4,800 KB = 4.8 MB; 4.9 MB; **0.005 GB = 5 MB** ✓)

---

**Q10.** Tick (✓) two file sizes that are equal to each other. [1]

- [ ] 1,024,000 bytes
- [ ] 1000 KB
- [ ] 1 MB
- [ ] 0.001 GB

**Mark scheme:** **1000 KB** and **1 MB** ✓ (both = 1,000,000 bytes using 1000-based units)

---

## 1.4 Binary Shifts

**Q11.** Tick (✓) one box to identify the result of a **3-place right binary shift** on **10110000**. [1]

- [ ] 00010110
- [ ] 11000000
- [ ] 00011011
- [ ] 10000001

**Mark scheme:** **00010110** ✓

---

**Q12.** Describe the binary shift that can be used to **multiply** any number by **4**. [2]

**Mark scheme:**
- 1 mark: **left shift**
- 1 mark: **2 places**

---

**Q13.** Describe the binary shift that can be used to **divide** any number by **8**. [2]

**Mark scheme:**
- 1 mark: **right shift**
- 1 mark: **3 places**

---

**Q14.** A binary number **00000110** has a left binary shift of 2 places applied to it. State the result and the denary value it represents. [2]

**Mark scheme:**
- 1 mark: **00011000**
- 1 mark: **24** (denary)

---

## 1.5 Binary Addition

**Q15.** Complete the binary addition of these two 8-bit binary numbers. Show your working. [2]

```
  01011010
+ 00110101
```

**Mark scheme:**
- 1 mark: working showing all correct carries
- 1 mark: **10001111**

---

**Q16.** Complete the binary addition. Show your working. [2]

```
  01110011
+ 00101100
```

**Mark scheme:**
- 1 mark: correct carries shown
- 1 mark: **10011111**

---

**Q17.** Complete the binary addition. Show your working. [2]

```
  01101011
+ 00000111
```

**Mark scheme:**
- 1 mark: correct carries
- 1 mark: **01110010**

---

---

# TOPIC 2: NETWORKS

## 2.1 LAN vs WAN

**Q18.** A school has 200 computers all connected within the school building. Identify **two** reasons why this network is a LAN and not a WAN. [2]

**Mark scheme (any 2):**
- It covers a small/single geographical area/location
- All hardware is owned and managed by the school
- It does not use external/public infrastructure
- It does not connect separate networks together (like a WAN does)

---

**Q19.** State **one** characteristic of a LAN, other than covering a small geographical area. [1]

**Mark scheme (any 1):**
- Hardware is owned/managed by the organisation
- Does not use external infrastructure
- Uses dedicated hardware not shared with others

---

## 2.2 Network Topologies

**Q20.** Describe what is meant by a **mesh topology**. [2]

**Mark scheme (any 2):**
- (Partial mesh) each device is connected to one or more other devices // (Full mesh) every device is connected to every other device
- There is no need for a central device/switch/server // all devices are equal/decentralised
- There are multiple routes/paths between devices

---

**Q21.** Describe **one benefit** and **one drawback** of a **mesh topology** compared to a **star topology**. [4]

**Mark scheme (2 marks per point: state + expand):**

Benefit (any 1 + expansion):
- No single point of failure // if one connection breaks, devices can still communicate via another route
- No need to purchase a central switch // lower cost to install/maintain
- More scalable // easier to add devices without impacting others

Drawback (any 1 + expansion):
- Requires more cables/connections // more expensive and impractical to set up
- Reduced central management/oversight // less control over network security/traffic
- Harder to find errors // because there are many routes where an error could occur

---

**Q22.** Describe what is meant by a **star topology**. [2]

**Mark scheme:**
- All devices are connected to a **central device** (switch/hub)
- Each device has its own dedicated connection to the central switch
- (If one device/connection fails, others are not affected)

---

**Q23.** Give **one benefit** and **one drawback** of a **star topology** compared to a **mesh topology**. [2]

**Mark scheme:**
- Benefit: Easy fault isolation // if one cable fails only that device is affected // easy to add new devices
- Drawback: If the central switch fails the whole network goes down // single point of failure

---

## 2.3 Wired vs Wireless

**Q24.** A company currently uses only wired connections. Explain **three** benefits of also providing wireless (Wi-Fi) connections. [3]

**Mark scheme (any 3):**
- Easier to add more devices/users (without buying cables)
- Devices are not fixed to one location // devices can be moved around freely
- Mobile devices (phones, tablets) that don't have wired ports can connect
- Reduces trailing cables/wires around the workplace
- Can support more simultaneous connections more cheaply

---

**Q25.** State **two** drawbacks of using wireless connections instead of wired connections. [2]

**Mark scheme (any 2):**
- Slower data transfer speeds
- Less secure — signal can be intercepted by others in range
- Signal can be affected by interference (walls, other devices)
- Limited range — signal weakens with distance
- Can be disrupted by other wireless networks

---

**Q26.** Describe **two** benefits of using **wired** connections in an office network. [4]

**Mark scheme (2 marks per benefit: state + expand):**
- Faster speeds // because there is no interference or signal loss over the cable
- More secure // the signal cannot be intercepted wirelessly, harder to access without physical connection
- More reliable // wired connections are not affected by interference or distance

---

## 2.4 Network Performance

**Q27.** Complete the table by explaining how each factor affects the performance of a network. [4]

| Factor | How it affects performance |
|--------|--------------------------|
| Bandwidth | |
| Number of users accessing the network at the same time | |

**Mark scheme (2 marks per factor):**
- Bandwidth: More bandwidth = faster network/better performance // because more data can be transferred simultaneously per second
- Number of users: More users = slower network // because more data is being transferred simultaneously / bandwidth is shared / more congestion

---

## 2.5 DNS and IP Addresses

**Q28.** A user types a URL into their web browser. Describe the steps that take place to convert the URL into an IP address. [4]

**Mark scheme (any 4):**
1. Browser checks its **cache** for a matching IP address
2. If not found, the URL/domain is sent to a **DNS server**
3. DNS looks up the URL in its **database/table** of URLs and IP addresses
4. If not found locally, the request is passed to a **higher-level DNS server**
5. DNS **returns the IP address** to the computer/browser
6. If not found, an **error** is returned/sent

---

**Q29.** Tick (✓) one box on each row to identify if the IPv4 address is **valid** or **invalid**. [4]

| IPv4 Address | Valid | Invalid |
|---|---|---|
| 192.168.1.1 | | |
| 300.0.0.1 | | |
| 10.256.3.4 | | |
| 172.16.254.1 | | |

**Mark scheme:**
- 192.168.1.1 → **Valid** (all octets 0–255)
- 300.0.0.1 → **Invalid** (300 > 255)
- 10.256.3.4 → **Invalid** (256 > 255)
- 172.16.254.1 → **Valid**

---

**Q30.** Identify **one** device that is required to allow a LAN to connect to the internet. [1]

**Mark scheme:** **Router** // modem (BOD)

---

**Q31.** Describe the role of a **router** in a network. [3]

**Mark scheme (any 3):**
- Connects different networks together (e.g. LAN to the internet)
- Directs/routes data packets between networks
- Uses IP addresses to determine the best route for packets
- Assigns IP addresses to devices on the network (DHCP)

---

## 2.6 Network Protocols

**Q32.** Complete the table by identifying the most appropriate protocol for each task. [4]

| Task | Protocol |
|------|----------|
| Viewing a webpage | |
| Logging into online banking securely | |
| Downloading a file from a server | |
| Sending an email | |

**Mark scheme:**
- Viewing a webpage: **HTTP**
- Secure banking login: **HTTPS**
- Downloading a file: **FTP**
- Sending an email: **SMTP**

---

**Q33.** Identify the protocol used to **receive/check emails**. [1]

**Mark scheme:** **IMAP** // POP3

---

---

# TOPIC 3: SECONDARY STORAGE

## 3.1 Types and Comparison

**Q34.** A student wants to transfer large video files between home and school. Identify whether they should use an **optical** or **solid-state** device. Justify your choice. [4]

**Mark scheme:**
- No mark for choice alone — marks for justified reasoning
- Solid-state e.g.:
  - Larger capacity // needed because video files could be very large
  - More durable / no moving parts // less likely to be damaged in transit
  - Faster to read/write // quicker to transfer large files
  - Portable / small in size
- Optical e.g.:
  - Sufficient capacity for the files
  - Cheaper cost per unit
  - Portable

---

**Q35.** State **two** differences between solid-state storage and magnetic (hard disk) storage. [2]

**Mark scheme (any 2):**
- Solid-state has no moving parts // magnetic has spinning disks and a read/write head
- Solid-state is faster to access data // magnetic is slower
- Solid-state is more durable // magnetic is more easily damaged
- Solid-state is more expensive per GB // magnetic is cheaper per GB

---

**Q36.** Identify **one** type of secondary storage **other than** solid-state and magnetic. [1]

**Mark scheme:** **Optical** (CD / DVD / Blu-ray)

---

## 3.2 Calculations

**Q37.** A musician records 500 audio files. Each file is 4 MB. Calculate the total storage needed in GB. Show your working. [2]

**Mark scheme:**
- 1 mark: 500 × 4 = 2000 MB
- 1 mark: **2 GB**

---

**Q38.** Tick (✓) one box to identify the **smallest** storage capacity. [1]

- [ ] 1.5 GB
- [ ] 1600 MB
- [ ] 1,400,000 KB
- [ ] 0.0015 TB

**Mark scheme:** **1.5 GB** ✓ (1.5 GB = 1500 MB; 1600 MB; 1,400,000 KB = 1400 MB; 0.0015 TB = 1500 MB → smallest is 1400 MB = **1,400,000 KB** ✓)

*Note: 1,400,000 KB = 1400 MB — smallest*

---

---

# TOPIC 4: SOUND REPRESENTATION

**Q39.** Complete the description of how a computer stores sound. Fill in the gaps using the given list of terms. Not all terms will be used.

*Terms: analogue, binary, bit depth, digital, hertz, lower, measuring, sample rate, sampling, seconds, unique*

An .................... sound wave needs to be converted into a digital sound wave.

Sound .................... is when the amplitude of the sound wave is measured at set intervals.

The .................... is the number of times per second the sound wave is measured. This is given in Hertz.

Each amplitude is given a .................... binary number. The number of bits allocated to each sample is the ....................

The higher the number of bits, the wider the number of amplitudes that can be measured. [5]

**Mark scheme:**
1. **analogue**
2. **sampling**
3. **sample rate**
4. **unique**
5. **bit depth**

---

**Q40.** A sound file has a sample rate of 44,000 Hz, a bit depth of 16 bits, and a duration of 60 seconds. Calculate the file size in **megabytes**. Show your working. [3]

**Mark scheme:**
- 44,000 × 16 = 704,000 bits per second
- 704,000 × 60 = 42,240,000 bits
- 42,240,000 ÷ 8 = 5,280,000 bytes
- **5,280,000 ÷ 1,000,000 = 5.28 MB** (accept ÷ 1,048,576 = 5.03 MB)

---

**Q41.** Explain the effect on a sound file of **increasing the bit depth** from 8 bits to 16 bits. [2]

**Mark scheme:**
- More/wider range of amplitude values can be represented // more accurate recording
- The file size increases // because more bits are used per sample

---

**Q42.** Explain the effect on a sound file of **decreasing the sample rate** from 44 kHz to 22 kHz. [2]

**Mark scheme:**
- The sound quality decreases // fewer samples taken per second so less accurate
- The file size decreases // because fewer samples are stored per second

---

**Q43.** Tick (✓) one box to identify the correct description of **sound sampling**. [1]

- [ ] Converting a digital sound wave into an analogue sound wave
- [ ] Measuring the amplitude of a sound wave at set time intervals
- [ ] Increasing the bit depth to improve sound quality
- [ ] Storing sound as a series of colour values

**Mark scheme:** **Measuring the amplitude of a sound wave at set time intervals** ✓

---

---

# TOPIC 5: ETHICS / ENVIRONMENTAL EXTENDED RESPONSE

## 5.1 How to Structure an 8-mark Answer

**Template (use for ANY scenario):**

```
Para 1 — Ethical issue (linked to scenario) + expansion
Para 2 — Environmental issue + expansion
Para 3 — Benefit to [party 1] + expansion
Para 4 — Drawback to [party 2] + expansion
(Aim for at least one of each, expanded — do not just list)
```

---

**Q44.** A large technology company decides to collect data about users' browsing habits without clearly informing them, in order to sell targeted advertising.

Discuss the impact of this decision. Include in your answer:
- ethical issues
- environmental issues
- benefits and drawbacks [8]

**Mark scheme guidance (Level 3: 6–8 marks):**

Ethical issues (any expanded point):
- Users are not informed → they are being deceived / privacy is being violated
- Data is being collected without clear consent → may breach GDPR/DPA
- Users cannot opt out → unfair, especially for vulnerable people
- Data could be sold to third parties → misuse of personal information

Environmental issues (any expanded point):
- Storing large amounts of user data requires energy-intensive data centres
- Increased energy consumption contributes to carbon emissions
- Servers need cooling systems which use more electricity
- More data stored = more hardware needed = more manufacturing = more e-waste

Benefits:
- Company: generates revenue through advertising, allows services to remain "free" for users
- Users: may receive more relevant/personalised adverts

Drawbacks:
- Users: loss of privacy, data may be misused or stolen, no control over their personal data
- Company: reputational damage if exposed, legal fines under GDPR

---

**Q45.** A company manufactures smartphones and announces it will stop providing software updates for phones older than 2 years, meaning customers will need to buy new phones more frequently.

Discuss the impact of this decision on both the company and the customers. Include:
- ethical issues
- environmental issues
- benefits and drawbacks [8]

**Mark scheme guidance:**

Ethical:
- Customers may feel forced to buy new phones → is this fair/honest?
- Older phones become insecure without updates → company putting customers at risk
- Lower income customers may not be able to afford new phones → digital divide
- Company is prioritising profit over customer welfare

Environmental:
- More frequent device disposal → increased e-waste
- Manufacturing more phones uses raw materials and energy
- Older phones could be distributed to those without devices → reduces waste
- Components could be recycled → reduces environmental impact

Benefits:
- Company: increased sales/revenue, can use newer components to reduce manufacturing cost
- Customers: newer phones may have better features, may become available at lower cost

Drawbacks:
- Company: loss of customer trust/loyalty, reputational damage
- Customers: increased expense, time/effort to switch devices, working phones wasted

---

---

# TOPIC 6: CPU REGISTERS

**Q46.** Complete the table by identifying **two** registers and stating the purpose of each. [4]

| Register | Purpose |
|----------|---------|
| | |
| | |

**Mark scheme (1 mark name + 1 mark purpose, per row):**

Acceptable answers:
- **Program Counter (PC)** — stores the address of the next instruction to be fetched
- **Memory Address Register (MAR)** — stores the address of data/instruction to be fetched from or written to memory
- **Memory Data Register (MDR)** — stores the data/instruction fetched from memory / about to be written to memory
- **Accumulator (ACC)** — stores the result of calculations performed by the ALU

---

**Q47.** Describe what happens during the **fetch** stage of the fetch-execute cycle. [2]

**Mark scheme:**
- The address of the next instruction is taken from the **Program Counter (PC)**
- The instruction is **fetched from memory** (RAM) at that address
- The instruction is placed in the **MDR** // the address is placed in the **MAR**
- The PC is incremented to point to the next instruction

---

**Q48.** State **three** characteristics of a CPU that affect its performance. [3]

**Mark scheme:**
- **Clock speed** (measured in GHz)
- **Number of cores**
- **Cache size** // amount of cache memory

---

---

# TOPIC 7: CHARACTER SETS (ASCII / UNICODE)

**Q49.** Part of the ASCII character set is shown below.

| Character | Denary | Binary |
|-----------|--------|--------|
| A | 65 | 01000001 |
| B | 66 | 01000010 |
| C | 67 | 01000011 |

Write the binary code to represent the word **"CAB"** using ASCII. [2]

**Mark scheme:**
- 1 mark: at least one correct code
- 2 marks: **01000011 01000001 01000010** (all correct, correct order)

---

**Q50.** Identify **one** benefit and **one** drawback of using **Unicode** instead of **ASCII**. [2]

**Mark scheme:**
- Benefit: Can represent more/a wider range of characters // supports characters from different languages // can store emojis
- Drawback: Larger file size // uses more bits per character than ASCII // requires more storage/processing

---

**Q51.** Identify a character set **other than** ASCII. [1]

**Mark scheme:** **Unicode** // UTF-8 // UTF-16 // UTF-32

---

---

# TOPIC 8: IMAGE REPRESENTATION / COLOUR DEPTH

**Q52.** Define the term **pixel**. [1]

**Mark scheme:**
- The smallest unit/part of an image // a single square/dot that has one colour

---

**Q53.** An image has a resolution of 1200 × 800 pixels and a colour depth of 24 bits. Calculate the file size in **kilobytes**. Show your working. [2]

**Mark scheme:**
- 1 mark: 1200 × 800 × 24 = 23,040,000 bits → ÷ 8 = 2,880,000 bytes
- 1 mark: **2,880 KB** (÷ 1000) // 2,812.5 KB (÷ 1024)

---

**Q54.** State the **minimum number of bits** needed to represent **200 different colours**. [1]

**Mark scheme:** **8** (2^7=128 < 200, 2^8=256 ≥ 200)

---

**Q55.** State **two** effects of increasing the colour depth of an image from 8 bits to 24 bits. [2]

**Mark scheme (any 2):**
- The file size increases // more bits are used per pixel
- The image quality improves // more colours can be represented // more accurate colours
- More storage space is required

---

---

# TOPIC 9: ENCRYPTION

**Q56.** Explain the **purpose** and **function** of encryption software. [3]

**Mark scheme (any 3):**
- Purpose: To protect data from being read/used if intercepted // makes data secure during transmission
- Function:
  - Jumbles/scrambles/encodes the data using an **algorithm** and a **key**
  - Makes the data **meaningless/unreadable** to anyone who intercepts it
  - Only someone with the correct **key** can **decrypt** it and read the original data

---

**Q57.** Give **two** reasons why a business should use encryption when sending data across the internet. [2]

**Mark scheme (any 2):**
- Prevents unauthorised users from reading intercepted data
- Protects sensitive/personal data during transmission
- Ensures only the intended recipient can access the data
- Required for compliance with data protection legislation

---

---

# TOPIC 10: UTILITY SOFTWARE & OS FUNCTIONS

**Q58.** Tick (✓) **one** box on each row to identify the operating system function that manages each task. [5]

| Task | Memory management | Peripheral management | User management | File management |
|------|---|---|---|---|
| Multitasking | | | | |
| Renaming a folder | | | | |
| Creating a user account | | | | |
| Installing a printer driver | | | | |
| Moving data to and from RAM | | | | |

**Mark scheme:**
- Multitasking → **Memory management**
- Renaming a folder → **File management**
- Creating a user account → **User management**
- Installing a printer driver → **Peripheral management**
- Moving data to/from RAM → **Memory management**

---

**Q59.** State the **purpose** of utility software. [1]

**Mark scheme (any 1):**
- To perform housekeeping/maintenance tasks on the computer
- To keep the computer running smoothly / efficiently
- To monitor, manage, or configure the computer system

---

**Q60.** Explain what **defragmentation** software does and why it is needed. [3]

**Mark scheme:**
- Files are stored in fragments/pieces scattered across the disk
- Defragmentation rearranges the fragments so files are stored contiguously/together
- This speeds up file access/read time because the read head doesn't need to move as far

---

---

# TOPIC 11: LEGISLATION

**Q61.** Identify **one** piece of legislation a company must follow when storing customers' personal data, and describe **two** steps they must take to comply. [3]

**Mark scheme:**
- 1 mark: **Data Protection Act 2018** // DPA // GDPR // Data Protection
- 1 mark each for steps (any 2):
  - Keep data secure (e.g. using a firewall / encryption / passwords / access rights)
  - Do not share or sell data without consent
  - Only collect data that is needed / don't collect unnecessary data
  - Do not keep data longer than necessary
  - Ensure data remains accurate and up to date
  - Allow users to access or delete their data on request
  - Notify individuals of data breaches

---

**Q62.** A student downloads a film from the internet without paying for it. State which piece of legislation this breaks and explain why. [2]

**Mark scheme:**
- **Copyright, Designs and Patents Act 1988** // CDPA
- Because the film is protected by copyright // the student does not have permission to copy/download it // it is intellectual property of the creator

---

**Q63.** A hacker gains unauthorised access to a company's computer system. State which legislation this breaks. [1]

**Mark scheme:** **Computer Misuse Act 1990** // CMA

---

---

# TOPIC 12: CYBER SECURITY THREATS

**Q64.** Name and describe **one** cyber security threat to a computer system. [3]

**Mark scheme (1 mark name, 2 marks description):**

Examples:
- **Phishing** — a fraudulent email/website that tricks users into entering their login credentials/personal data by appearing to be from a trusted source
- **Malware** — malicious software designed to damage, disrupt or gain unauthorised access to a system (e.g. ransomware encrypts files and demands payment)
- **Brute force attack** — automated software tries every possible password combination until the correct one is found
- **SQL injection** — malicious SQL code is inserted into a form/input field to manipulate a database into revealing or deleting data
- **Man-in-the-middle / Data interception** — attacker intercepts data being transmitted between two devices and reads or alters it

---

**Q65.** Tick (✓) all methods that would help prevent each threat. [4]

| Threat | Anti-malware | Encryption | Firewall | Strong passwords |
|--------|---|---|---|---|
| Brute force attack | | | | |
| Data interception | | | | |
| Malware infection | | | | |
| Unauthorised network access | | | | |

**Mark scheme:**
- Brute force: **Strong passwords** ✓ (also anti-malware BOD)
- Data interception: **Encryption** ✓
- Malware infection: **Anti-malware** ✓, **Firewall** ✓
- Unauthorised network access: **Firewall** ✓

---

---

# BONUS: CLOUD STORAGE (trending — appeared 2025)

**Q66.** Describe **three** drawbacks to an organisation of storing data on the cloud. [5]

**Mark scheme (any 5):**
- Requires an internet connection — if offline, cannot access data
- Can be expensive — ongoing subscription costs / hosting fees
- No control over security — must rely on the cloud provider
- Data may be hacked/intercepted/affected by a virus
- May not know where in the world the data is stored (data sovereignty issues)
- Cloud provider could go down / company could lose access
- No control over backups — data may not be retrievable
- Privacy concerns — provider may access or sell data
- Concerns over who owns the data

---

*End of Question Bank | 66 questions across all Tier 1 & Tier 2 topics*
