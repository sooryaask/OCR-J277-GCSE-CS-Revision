#!/usr/bin/env python3
"""
OCR J277 GCSE Computer Science — Infinite Question Bank
Paper 1 (Computer Systems) + Paper 2 (Programming & Algorithms)
Built from 2022–2025 past paper analysis + custom-generated questions.

Anti-repetition: tracks recently asked questions per session; exhausts
the full pool before any question repeats. Parametric generators create
fresh numerical questions (binary, hex, sound, image) every time.
"""

import random
import os

G = "\033[92m"; R = "\033[91m"; Y = "\033[93m"
C = "\033[96m"; B = "\033[1m"; D = "\033[2m"; X = "\033[0m"

def clr():
    os.system('clear' if os.name == 'posix' else 'cls')

# ─────────────────────────────────────────────────────────────────────────────
# PARAMETRIC GENERATORS — produce a fresh unique question every call
# ─────────────────────────────────────────────────────────────────────────────

def gen_denary_to_binary():
    n = random.choice([x for x in range(1, 256) if x not in [0, 128, 255, 64, 32]])
    bits = format(n, '08b')
    return {
        "topic": "Number Systems", "paper": 1, "tier": 1, "type": "self_mark",
        "q": f"Convert the denary number {n} into 8-bit binary. Show your working. [2 marks]",
        "answer": f"Using columns (128 64 32 16 8 4 2 1):\n{n} → {bits}",
        "explanation": "1 mark: working shown (column method). 1 mark: correct 8-bit binary answer."
    }

def gen_binary_to_denary():
    n = random.randint(1, 254)
    bits = format(n, '08b')
    return {
        "topic": "Number Systems", "paper": 1, "tier": 1, "type": "self_mark",
        "q": f"Convert the 8-bit binary number {bits} into denary. Show your working. [2 marks]",
        "answer": f"Add up the column values where there is a 1:\n{bits} = {n}",
        "explanation": "1 mark: working shown (adding column values). 1 mark: correct denary answer."
    }

def gen_hex_to_denary():
    n = random.randint(10, 255)
    h = format(n, '02X')
    hi, lo = int(h[0], 16), int(h[1], 16)
    return {
        "topic": "Number Systems", "paper": 1, "tier": 1, "type": "self_mark",
        "q": f"Convert the hexadecimal number {h} into denary. Show your working. [2 marks]",
        "answer": f"{h[0]} = {hi}, {h[1]} = {lo}\n{hi} × 16 + {lo} × 1 = {hi*16} + {lo} = {n}",
        "explanation": "1 mark: working (multiply first digit by 16, add second). 1 mark: correct denary."
    }

def gen_binary_to_hex():
    n = random.randint(0, 255)
    bits = format(n, '08b')
    h = format(n, '02X')
    hi_nibble = bits[:4]; lo_nibble = bits[4:]
    return {
        "topic": "Number Systems", "paper": 1, "tier": 1, "type": "self_mark",
        "q": f"Convert the binary number {bits} into hexadecimal. [1 mark]",
        "answer": f"Split into nibbles: {hi_nibble} = {format(int(hi_nibble,2),'X')}, {lo_nibble} = {format(int(lo_nibble,2),'X')}\nAnswer: {h}",
        "explanation": "Split into two 4-bit nibbles, convert each to hex. 1 mark: correct hex."
    }

def gen_left_shift():
    places = random.choice([1, 2, 3])
    base = random.randint(1, 15)
    bits = format(base, '08b')
    shifted = format((base << places) & 0xFF, '08b')
    multiplier = 2 ** places
    return {
        "topic": "Number Systems", "paper": 1, "tier": 1, "type": "self_mark",
        "q": f"Show the result of a LEFT binary shift of {places} place(s) on the binary number {bits}. State what multiplication this represents. [2 marks]",
        "answer": f"Result: {shifted}\nThis multiplies the number by {multiplier} (2^{places}).",
        "explanation": f"1 mark: correct shifted result. 1 mark: × {multiplier}."
    }

def gen_right_shift():
    places = random.choice([1, 2, 3])
    base = random.randint(16, 240)
    bits = format(base, '08b')
    shifted = format(base >> places, '08b')
    divisor = 2 ** places
    return {
        "topic": "Number Systems", "paper": 1, "tier": 1, "type": "self_mark",
        "q": f"Show the result of a RIGHT binary shift of {places} place(s) on the binary number {bits}. State what division this represents. [2 marks]",
        "answer": f"Result: {shifted}\nThis divides the number by {divisor} (2^{places}).",
        "explanation": f"1 mark: correct shifted result. 1 mark: ÷ {divisor}."
    }

def gen_binary_addition():
    a = random.randint(10, 100)
    b = random.randint(10, 100)
    while a + b > 255:
        a = random.randint(10, 80)
        b = random.randint(10, 80)
    ba = format(a, '08b'); bb = format(b, '08b'); br = format(a+b, '08b')
    return {
        "topic": "Number Systems", "paper": 1, "tier": 1, "type": "self_mark",
        "q": f"Complete the binary addition. Show your working including any carries. [2 marks]\n\n    {ba}\n  + {bb}",
        "answer": f"  {ba}\n+ {bb}\n= {br}   (denary: {a} + {b} = {a+b})",
        "explanation": "1 mark: correct carries shown. 1 mark: correct 8-bit result."
    }

def gen_sound_filesize():
    sr = random.choice([8000, 11025, 22050, 44100, 48000])
    bd = random.choice([8, 16, 24])
    dur = random.choice([30, 60, 90, 120, 180, 300])
    bits = sr * bd * dur
    bytez = bits // 8
    kb = bytez / 1000
    mb = kb / 1000
    return {
        "topic": "Sound Representation", "paper": 1, "tier": 1, "type": "self_mark",
        "q": f"A sound file has a sample rate of {sr:,} Hz, a bit depth of {bd} bits, and a duration of {dur} seconds.\nCalculate the file size in megabytes. Show your working. [3 marks]",
        "answer": f"Step 1: {sr:,} × {bd} = {sr*bd:,} bits per second\nStep 2: {sr*bd:,} × {dur} = {bits:,} bits\nStep 3: {bits:,} ÷ 8 = {bytez:,} bytes\nStep 4: {bytez:,} ÷ 1,000,000 = {mb:.3f} MB",
        "explanation": "1 mark: sample rate × bit depth. 1 mark: × duration. 1 mark: ÷8 and convert to MB."
    }

def gen_image_filesize():
    w = random.choice([640, 800, 1024, 1200, 1920])
    h = random.choice([480, 600, 768, 800, 1080])
    cd = random.choice([4, 8, 16, 24])
    bits = w * h * cd
    bytez = bits // 8
    kb = bytez / 1000
    return {
        "topic": "Image Representation", "paper": 1, "tier": 2, "type": "self_mark",
        "q": f"An image has a resolution of {w} × {h} pixels and a colour depth of {cd} bits.\nCalculate the file size in kilobytes. Show your working. [2 marks]",
        "answer": f"Step 1: {w} × {h} × {cd} = {bits:,} bits\nStep 2: {bits:,} ÷ 8 = {bytez:,} bytes\nStep 3: {bytez:,} ÷ 1,000 = {kb:.1f} KB",
        "explanation": "1 mark: correct bits calculation (w × h × colour depth). 1 mark: correct KB."
    }

def gen_min_bits_colours():
    colours = random.choice([8, 16, 32, 64, 100, 150, 200, 250, 300, 500, 1000])
    bits = 1
    while 2**bits < colours:
        bits += 1
    return {
        "topic": "Image Representation", "paper": 1, "tier": 2, "type": "self_mark",
        "q": f"State the minimum number of bits needed to represent {colours} different colours. [1 mark]",
        "answer": f"{bits} bits (2^{bits} = {2**bits} which is ≥ {colours})",
        "explanation": f"Find the smallest power of 2 ≥ {colours}. 2^{bits-1}={2**(bits-1)} is too small, 2^{bits}={2**bits} is enough."
    }

def gen_storage_calc():
    count = random.choice([100, 200, 500, 1000, 2000])
    size = random.choice([2, 3, 4, 5, 8, 10])
    total_mb = count * size
    total_gb = total_mb / 1000
    return {
        "topic": "Secondary Storage", "paper": 1, "tier": 1, "type": "self_mark",
        "q": f"A user stores {count} files. Each file is {size} MB. Calculate the total storage needed in GB. Show your working. [2 marks]",
        "answer": f"{count} × {size} = {total_mb} MB\n{total_mb} ÷ 1000 = {total_gb} GB",
        "explanation": "1 mark: correct multiplication. 1 mark: correct GB value."
    }

def gen_p2_trace():
    start = random.randint(2, 6)
    questions = []
    for _ in range(3):
        a = random.randint(1, 9); b = random.randint(1, 9)
        questions.append((a, b, a + b))
    q_text = "\n".join([f"    Q{i+1}: {q[0]} + {q[1]}" for i, q in enumerate(questions)])
    score = sum(1 for q in questions if q[2] > 5)
    trace_rows = []
    s = 0
    for i, q in enumerate(questions):
        s += (1 if q[2] > 5 else 0)
        trace_rows.append(f"i={i+1}: answer={q[2]}, score={s}")
    return {
        "topic": "Trace Tables", "paper": 2, "tier": 1, "type": "self_mark",
        "q": f"Trace through this algorithm and complete the trace table.\n\nscore = 0\nfor i = 1 to 3\n    answer = input(\"Answer: \")\n    if answer > 5 then\n        score = score + 1\n    endif\nnext i\nprint(score)\n\nInputs entered: {', '.join([str(q[2]) for q in questions])}\n\nTrace the values of i, answer, and score for each iteration. State the output. [4 marks]",
        "answer": "\n".join(trace_rows) + f"\nOutput: {score}",
        "explanation": "1 mark per correctly traced iteration (up to 3) + 1 mark correct output."
    }

def gen_sql():
    scenarios = [
        ("TblStudents", ["StudentID", "Name"], "YearGroup", random.randint(7, 13), False),
        ("TblProducts", ["ProductName", "Price"], "Category", "Electronics", True),
        ("TblBookings", ["BookingID", "RoomType"], "Nights", random.randint(1, 7), False),
        ("TblActors", ["Name", "Age"], "Genre", "Comedy", True),
        ("TblResults", ["StudentID", "Score"], "Score", random.randint(50, 90), False),
    ]
    t, fields, col, val, is_str = random.choice(scenarios)
    f_str = ", ".join(fields)
    val_str = f'"{val}"' if is_str else str(val)
    op = random.choice(["=", ">", "<", ">=", "<="]) if not is_str else "="
    return {
        "topic": "SQL", "paper": 2, "tier": 1, "type": "self_mark",
        "q": f"Write an SQL statement to display {f_str} from the table {t} where {col} is {op} {val_str}. [3 marks]",
        "answer": f"SELECT {f_str}\nFROM {t}\nWHERE {col} {op} {val_str}",
        "explanation": f"1 mark: SELECT {f_str} | 1 mark: FROM {t} | 1 mark: WHERE {col} {op} {val_str}"
    }

def gen_logic_expression():
    expressions = [
        ("(A AND B) OR NOT C", [(0,0,0,0),(0,0,1,0),(0,1,0,0),(0,1,1,0),(1,0,0,0),(1,0,1,0),(1,1,0,1),(1,1,1,0)]),
        ("A OR (B AND C)",     [(0,0,0,0),(0,0,1,0),(0,1,0,0),(0,1,1,1),(1,0,0,1),(1,0,1,1),(1,1,0,1),(1,1,1,1)]),
        ("NOT A AND B",        [(0,0,0),(0,1,1),(1,0,0),(1,1,0)]),
        ("A AND NOT B AND C",  [(0,0,0,0),(0,0,1,0),(0,1,0,0),(0,1,1,0),(1,0,0,0),(1,0,1,1),(1,1,0,0),(1,1,1,0)]),
    ]
    expr, rows = random.choice(expressions)
    inputs = len(rows[0]) - 1
    header = "A B C P" if inputs == 3 else "A B P"
    table_rows = "\n".join([" ".join(map(str, r)) for r in rows])
    return {
        "topic": "Logic Gates", "paper": 2, "tier": 1, "type": "self_mark",
        "q": f"Complete the truth table for the expression P = {expr}. [4 marks]\n\n{header}\n" + "\n".join([" ".join(map(str, r[:-1])) + " ?" for r in rows]),
        "answer": f"P = {expr}\n\n{header}\n{table_rows}",
        "explanation": "1 mark per 2 correct P values. Full marks for all correct."
    }

# Pool of generators — called fresh each time to produce unique questions
GENERATORS = [
    gen_denary_to_binary, gen_denary_to_binary, gen_denary_to_binary,
    gen_binary_to_denary, gen_binary_to_denary, gen_binary_to_denary,
    gen_hex_to_denary, gen_hex_to_denary,
    gen_binary_to_hex, gen_binary_to_hex,
    gen_left_shift, gen_left_shift,
    gen_right_shift, gen_right_shift,
    gen_binary_addition, gen_binary_addition, gen_binary_addition,
    gen_sound_filesize, gen_sound_filesize,
    gen_image_filesize, gen_image_filesize,
    gen_min_bits_colours,
    gen_storage_calc, gen_storage_calc,
    gen_p2_trace, gen_p2_trace,
    gen_sql, gen_sql, gen_sql,
    gen_logic_expression, gen_logic_expression,
]

# ─────────────────────────────────────────────────────────────────────────────
# STATIC QUESTION BANK
# ─────────────────────────────────────────────────────────────────────────────

STATIC = [

    # ══ PAPER 1 — NUMBER SYSTEMS ══════════════════════════════════════════════
    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"What is 1 nibble equal to?",
     "options":["2 bits","4 bits","8 bits","16 bits"],"answer":1,
     "explanation":"1 nibble = 4 bits. 1 byte = 8 bits (2 nibbles). Common in hex since one nibble = one hex digit."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"A left binary shift of 3 places multiplies a number by...",
     "options":["3","6","8","16"],"answer":2,
     "explanation":"Left shift n places = × 2^n. 2^3 = 8."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"A right binary shift of 2 places divides a number by...",
     "options":["2","4","6","8"],"answer":1,
     "explanation":"Right shift n places = ÷ 2^n. 2^2 = 4."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"Which is the largest file size?",
     "options":["5,000,000 bytes","4,800 KB","4.9 MB","0.005 GB"],"answer":3,
     "explanation":"0.005 GB = 5 MB = 5,000,000 bytes. 4,800 KB = 4.8 MB. 4.9 MB < 5 MB. 0.005 GB is largest."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"How many bytes are in 1 kilobyte (using the standard 1000-based definition)?",
     "options":["512","1000","1024","2000"],"answer":1,
     "explanation":"OCR uses 1 KB = 1,000 bytes (decimal). Note: 1 KiB = 1,024 bytes (binary) — both are accepted in OCR mark schemes."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"Which hex digit represents the denary value 13?",
     "options":["B","C","D","E"],"answer":2,
     "explanation":"A=10, B=11, C=12, D=13, E=14, F=15. D = 13."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"What is hexadecimal FF in denary?",
     "options":["128","240","254","255"],"answer":3,
     "explanation":"F=15. FF = 15×16 + 15×1 = 240 + 15 = 255. Maximum value of one byte."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"How many unique values can be represented by 4 bits?",
     "options":["4","8","16","32"],"answer":2,
     "explanation":"2^4 = 16. n bits → 2^n unique values."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"How many unique values can 8 bits represent?",
     "options":["128","256","512","1024"],"answer":1,
     "explanation":"2^8 = 256. This is why one byte can store values 0–255."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"What is 3 GB in megabytes?",
     "options":["300 MB","3,000 MB","30,000 MB","3,000,000 MB"],"answer":1,
     "explanation":"1 GB = 1,000 MB. 3 GB = 3 × 1,000 = 3,000 MB."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"What is 0.5 TB in gigabytes?",
     "options":["5 GB","50 GB","500 GB","5,000 GB"],"answer":2,
     "explanation":"1 TB = 1,000 GB. 0.5 × 1,000 = 500 GB."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"Which of the following binary additions is correct?\n  01100011\n+ 00011100",
     "options":["10001111","01111111","10000001","01111110"],"answer":1,
     "explanation":"99 + 28 = 127 = 01111111. Check: 64+32+16+8+4+2+1 = 127."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"What is binary 10000000 in denary?",
     "options":["64","128","192","256"],"answer":1,
     "explanation":"10000000: only the 128 column is 1. Answer = 128."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"Which describes a right binary shift of 1 place?",
     "options":["Multiplies by 2","Divides by 2","Adds 1 to each bit","Subtracts 1 from each bit"],"answer":1,
     "explanation":"Right shift 1 place = ÷ 2. Left shift 1 place = × 2."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"What is the hexadecimal equivalent of binary 11001010?",
     "options":["C9","CA","CB","DA"],"answer":1,
     "explanation":"Split: 1100 = C, 1010 = A. Answer: CA."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"self_mark",
     "q":"Describe how to convert the denary number 47 into 8-bit binary using the column method. [2 marks]",
     "answer":"Columns: 128 64 32 16 8 4 2 1\n47 = 32+8+4+2+1 = 00101111",
     "explanation":"1 mark: working shown with column headers or subtraction method. 1 mark: 00101111."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"Tick two file sizes that are EQUAL to each other:\n A: 1,000 KB   B: 1 MB   C: 1,024 KB   D: 0.001 GB",
     "options":["A and B (1000 KB = 1 MB)","B and D (1 MB = 0.001 GB)","A and D","C and D"],"answer":0,
     "explanation":"1,000 KB = 1 MB (using 1000-based units). A and B are equal."},

    {"topic":"Number Systems","paper":1,"tier":1,"type":"mc",
     "q":"An IPv4 address consists of how many octets?",
     "options":["2","4","6","8"],"answer":1,
     "explanation":"IPv4 has 4 octets (e.g. 192.168.1.1), each 0–255, separated by full stops."},

    # ══ PAPER 1 — NETWORKING ══════════════════════════════════════════════════
    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"What makes a network a LAN rather than a WAN?",
     "options":["It uses fibre optic cables","It covers a small/single geographical area","It connects more than 100 devices","It uses the TCP/IP protocol"],"answer":1,
     "explanation":"LAN = Local Area Network. It covers a small geographical area. Hardware is owned by the organisation."},

    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"What is the role of a SWITCH in a network?",
     "options":["Connects the LAN to the internet","Assigns IP addresses","Connects devices within a LAN and directs data using MAC addresses","Converts digital to analogue signals"],"answer":2,
     "explanation":"A switch operates within a LAN. It reads MAC addresses to direct data only to the intended device."},

    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"What is the role of a ROUTER in a network?",
     "options":["Connects devices in a LAN using MAC addresses","Connects different networks together and routes packets between them","Stores web pages for faster access","Converts URL to IP address"],"answer":1,
     "explanation":"A router connects networks (e.g. your LAN to the internet) and determines the best path for data packets."},

    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"Which is a benefit of a MESH topology over a star topology?",
     "options":["Cheaper to install (fewer cables)","Easier to manage centrally","No single point of failure — multiple routes exist","Requires a central switch"],"answer":2,
     "explanation":"Mesh: if one connection fails, data re-routes. Star: if the switch fails, all devices lose connection."},

    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"Which is a DRAWBACK of a mesh topology?",
     "options":["Single point of failure","Requires more cables and connections — expensive","Harder to add new devices","All devices must be in the same room"],"answer":1,
     "explanation":"Mesh requires many cables (every device potentially connected to every other). High installation cost."},

    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"Which is a drawback of STAR topology?",
     "options":["Hard to find faults","All devices share one cable","If the central switch fails the whole network goes down","Very expensive to cable"],"answer":2,
     "explanation":"The switch is a single point of failure in a star topology. If it fails, no device can communicate."},

    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"Which protocol is used to SEND an email?",
     "options":["IMAP","HTTP","SMTP","FTP"],"answer":2,
     "explanation":"SMTP = Simple Mail Transfer Protocol — sends email. IMAP/POP = receive email. HTTP = webpages. FTP = file transfer."},

    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"Which protocol is used to SECURELY view a webpage?",
     "options":["HTTP","FTP","POP","HTTPS"],"answer":3,
     "explanation":"HTTPS = HTTP Secure. Uses encryption (SSL/TLS). HTTP is unsecured. FTP transfers files. POP receives email."},

    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"Which protocol is used to DOWNLOAD a file from a server?",
     "options":["SMTP","HTTP","FTP","IMAP"],"answer":2,
     "explanation":"FTP = File Transfer Protocol. Used to upload/download files between client and server."},

    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"How does BANDWIDTH affect network performance?",
     "options":["More bandwidth = slower, more secure","More bandwidth = faster data transfer (more data per second)","Less bandwidth = less congestion","Bandwidth only affects wireless networks"],"answer":1,
     "explanation":"Higher bandwidth means more data can flow simultaneously — faster network performance."},

    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"How does a larger NUMBER OF USERS affect network performance?",
     "options":["Makes it faster — more devices sharing processing","Makes it slower — bandwidth is shared, causing congestion","Has no effect","Only affects wired networks"],"answer":1,
     "explanation":"More users = more data competing for the same bandwidth = congestion = slower performance."},

    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"Which of these IPv4 addresses is INVALID?",
     "options":["192.168.1.1","10.0.0.255","256.100.1.1","172.16.254.1"],"answer":2,
     "explanation":"Each octet must be 0–255. 256 exceeds this limit, so 256.100.1.1 is invalid."},

    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"Why is HTTPS preferred over HTTP for online banking?",
     "options":["HTTPS is faster","HTTPS encrypts the data — prevents interception","HTTP is deprecated","HTTPS uses less bandwidth"],"answer":1,
     "explanation":"HTTPS uses SSL/TLS encryption. Data is scrambled in transit so attackers cannot read intercepted packets."},

    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"A student connects a new laptop to the school Wi-Fi. Which device directs the laptop's data to the correct destination on the internet?",
     "options":["Switch","Hub","Router","DNS server"],"answer":2,
     "explanation":"The router connects the school LAN to the internet and routes packets to the correct destination."},

    {"topic":"Networking","paper":1,"tier":1,"type":"self_mark",
     "q":"Describe the FIRST THREE steps that happen when a user types a URL into a browser. [3 marks]",
     "answer":"1. Browser checks its CACHE for a stored IP address for that URL.\n2. If not found, the URL is sent to a DNS server.\n3. The DNS server looks up the URL in its database to find the matching IP address.",
     "explanation":"1 mark per step (max 3). Steps must be in order. Partial credit for correct steps out of order."},

    {"topic":"Networking","paper":1,"tier":1,"type":"self_mark",
     "q":"Describe TWO benefits of changing a wired-only school network to also include wireless connections. [4 marks]",
     "answer":"1. Students with mobile devices (phones/tablets) that lack wired ports can connect to the network.\n   Expansion: Without Wi-Fi these devices could not access school resources at all.\n2. Devices are no longer fixed to one location — students and teachers can move around freely.\n   Expansion: This is useful for lessons that take place in different rooms.",
     "explanation":"2 marks per benefit: 1 mark for stating the benefit, 1 mark for expanding linked to the scenario."},

    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"Which step happens FIRST in the DNS process?",
     "options":["URL is sent to a DNS server","Browser checks its local cache","IP address is returned","Higher-level DNS server is contacted"],"answer":1,
     "explanation":"Step 1: browser checks its OWN cache. Only if not found does it contact a DNS server."},

    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"What is the purpose of a protocol in networking?",
     "options":["To encrypt all data on the network","To set agreed rules for how devices communicate","To assign IP addresses","To connect the LAN to the WAN"],"answer":1,
     "explanation":"A protocol is a set of agreed rules/standards that allow different devices to communicate with each other."},

    {"topic":"Networking","paper":1,"tier":1,"type":"mc",
     "q":"What does IMAP allow you to do?",
     "options":["Send emails","Access and manage emails on the mail server without downloading them","Download files","Browse websites securely"],"answer":1,
     "explanation":"IMAP (Internet Message Access Protocol) lets you read emails stored on the server. POP3 downloads them to your device."},

    # ══ PAPER 1 — SECONDARY STORAGE ══════════════════════════════════════════
    {"topic":"Secondary Storage","paper":1,"tier":1,"type":"mc",
     "q":"Which type of secondary storage has NO MOVING PARTS?",
     "options":["Magnetic (HDD)","Optical (DVD)","Solid-state (SSD)","All secondary storage has moving parts"],"answer":2,
     "explanation":"SSDs use flash memory — no moving parts. HDDs have spinning disks. Optical drives have spinning discs and a moving laser."},

    {"topic":"Secondary Storage","paper":1,"tier":1,"type":"mc",
     "q":"Why is solid-state storage more suitable than magnetic for a portable laptop?",
     "options":["Cheaper per GB","Slower access speed","More durable — no moving parts so less easily damaged","Larger capacity"],"answer":2,
     "explanation":"SSDs have no moving parts — more resistant to shocks and drops. Crucial for portable devices."},

    {"topic":"Secondary Storage","paper":1,"tier":1,"type":"mc",
     "q":"Which type of secondary storage has the LOWEST cost per GB?",
     "options":["Solid-state (SSD)","Magnetic (HDD)","Optical (Blu-ray)","USB flash drive"],"answer":1,
     "explanation":"Magnetic HDDs are cheapest per GB. SSDs cost more per GB. Optical is cheap per disc but low capacity."},

    {"topic":"Secondary Storage","paper":1,"tier":1,"type":"mc",
     "q":"Which type of secondary storage is most suitable for a music streaming service storing millions of songs?",
     "options":["Optical (DVD)","USB flash drive","Magnetic (HDD) — large capacity, low cost per GB","Solid-state — fastest access"],"answer":2,
     "explanation":"For massive storage needs, magnetic HDDs offer the best capacity per pound. Optical is too slow and fragile at scale."},

    {"topic":"Secondary Storage","paper":1,"tier":1,"type":"mc",
     "q":"Why might optical storage (DVD) be chosen to distribute a software game?",
     "options":["Fastest access speed","Cheapest overall, read-only prevents tampering, portable","Largest capacity","Most durable"],"answer":1,
     "explanation":"DVDs are cheap, portable, and read-only (which can prevent unauthorised copying). Suitable for physical distribution."},

    {"topic":"Secondary Storage","paper":1,"tier":1,"type":"self_mark",
     "q":"A hospital needs to store 10,000 patient records. Each record is 5 MB. Identify the most suitable type of secondary storage and justify your choice. [4 marks]",
     "answer":"Magnetic (HDD)\nJustification:\n- Very large capacity needed: 10,000 × 5 MB = 50,000 MB = 50 GB\n- Magnetic storage offers large capacity at low cost per GB\n- Records need to be read and updated frequently — magnetic HDDs support fast read/write\n- Data is not being transported so durability of moving parts is not a concern",
     "explanation":"0 marks for choice alone. 1–2 marks for each justified reason linked to the scenario. Must link reason to the specific context."},

    {"topic":"Secondary Storage","paper":1,"tier":1,"type":"mc",
     "q":"State the THREE types of secondary storage.",
     "options":["RAM, ROM, Cache","Magnetic, Solid-state, Optical","HDD, SSD, USB","Flash, Disc, Drive"],"answer":1,
     "explanation":"The three types are: Magnetic (HDD), Solid-state (SSD/USB flash), Optical (CD/DVD/Blu-ray)."},

    # ══ PAPER 1 — SOUND REPRESENTATION ═══════════════════════════════════════
    {"topic":"Sound Representation","paper":1,"tier":1,"type":"mc",
     "q":"What is SAMPLING in the context of digital audio?",
     "options":["Converting digital sound to analogue","Measuring the amplitude of a sound wave at regular time intervals","Reducing the bit depth of a sound file","Playing sound through speakers"],"answer":1,
     "explanation":"Sampling measures the amplitude of the analogue sound wave at set intervals. Each measurement is stored as a binary number."},

    {"topic":"Sound Representation","paper":1,"tier":1,"type":"mc",
     "q":"What is SAMPLE RATE measured in?",
     "options":["Bits","Bytes","Hertz (Hz)","Megabytes"],"answer":2,
     "explanation":"Sample rate = number of samples per second, measured in Hertz (Hz). e.g. 44,100 Hz = 44,100 samples per second."},

    {"topic":"Sound Representation","paper":1,"tier":1,"type":"mc",
     "q":"What is BIT DEPTH in digital audio?",
     "options":["The number of samples per second","The number of bits used to represent each sample's amplitude","The file size in megabytes","The frequency of the sound wave"],"answer":1,
     "explanation":"Bit depth = bits per sample. More bits = more possible amplitude values = more accurate recording."},

    {"topic":"Sound Representation","paper":1,"tier":1,"type":"mc",
     "q":"What effect does INCREASING the sample rate have?",
     "options":["Decreases file size, increases quality","Increases file size, decreases quality","Increases file size, increases quality","Decreases file size, decreases quality"],"answer":2,
     "explanation":"More samples per second = more data stored = larger file. More samples also captures the wave more accurately = better quality."},

    {"topic":"Sound Representation","paper":1,"tier":1,"type":"mc",
     "q":"What effect does DECREASING the bit depth have?",
     "options":["Larger file, better quality","Smaller file, lower quality","Smaller file, better quality","No effect on quality"],"answer":1,
     "explanation":"Fewer bits per sample = fewer possible amplitude values = less accurate = lower quality. Fewer bits also means smaller file."},

    {"topic":"Sound Representation","paper":1,"tier":1,"type":"mc",
     "q":"Which formula gives the file size of a sound file in BITS?",
     "options":["Sample rate + bit depth + duration","Sample rate × bit depth × duration","Sample rate × duration","Bit depth × duration"],"answer":1,
     "explanation":"File size (bits) = sample rate × bit depth × duration. Divide by 8 for bytes, by 1000 for KB, etc."},

    {"topic":"Sound Representation","paper":1,"tier":1,"type":"mc",
     "q":"An analogue sound wave must be converted to digital for storage. What is this conversion process called?",
     "options":["Sampling","Encryption","Compression","Rendering"],"answer":0,
     "explanation":"The process is called sampling (or Analogue-to-Digital Conversion / ADC). The amplitude is measured at regular intervals."},

    # ══ PAPER 1 — CPU REGISTERS ═══════════════════════════════════════════════
    {"topic":"CPU Registers","paper":1,"tier":2,"type":"mc",
     "q":"What does the PROGRAM COUNTER (PC) store?",
     "options":["The result of the last calculation","The data fetched from memory","The address of the NEXT instruction to be fetched","The address of data being written"],"answer":2,
     "explanation":"PC holds the address of the next instruction. After each fetch, PC increments to point to the instruction after."},

    {"topic":"CPU Registers","paper":1,"tier":2,"type":"mc",
     "q":"What does the ACCUMULATOR (ACC) store?",
     "options":["The next instruction address","The address of data in memory","The result of calculations performed by the ALU","Instructions waiting to be executed"],"answer":2,
     "explanation":"The ACC holds the result of arithmetic/logic operations performed by the ALU (Arithmetic Logic Unit)."},

    {"topic":"CPU Registers","paper":1,"tier":2,"type":"mc",
     "q":"What does the MEMORY DATA REGISTER (MDR) store?",
     "options":["Address of the next instruction","Address of data in memory","Data fetched from memory OR data about to be written to memory","Result of calculations"],"answer":2,
     "explanation":"MDR is a buffer holding data either just fetched from memory or about to be written to it."},

    {"topic":"CPU Registers","paper":1,"tier":2,"type":"mc",
     "q":"What does the MEMORY ADDRESS REGISTER (MAR) store?",
     "options":["Data fetched from RAM","The address in memory to read from or write to","The result of the last operation","The current instruction being decoded"],"answer":1,
     "explanation":"MAR holds the memory address where data or an instruction needs to be fetched from or written to."},

    {"topic":"CPU Registers","paper":1,"tier":2,"type":"mc",
     "q":"Which CPU characteristic has the GREATEST effect on how many instructions can be processed per second?",
     "options":["RAM size","Cache size","Clock speed","Number of USB ports"],"answer":2,
     "explanation":"Clock speed (GHz) = cycles per second. More cycles = more instructions executed per second."},

    {"topic":"CPU Registers","paper":1,"tier":2,"type":"mc",
     "q":"Why does a CPU with MORE CORES generally perform better?",
     "options":["More cores = higher clock speed","More cores can execute multiple tasks simultaneously","More cores = more cache","More cores reduces heat"],"answer":1,
     "explanation":"Each core can handle a separate task independently. More cores = more parallelism = faster overall performance."},

    {"topic":"CPU Registers","paper":1,"tier":2,"type":"mc",
     "q":"Why does a larger CACHE SIZE improve CPU performance?",
     "options":["Cache runs at a higher clock speed than the CPU","Frequently needed data is stored close to the CPU — less time fetching from slower RAM","Cache holds more programs in memory","Cache replaces the need for secondary storage"],"answer":1,
     "explanation":"Cache is much faster than RAM. Frequently accessed data in cache is retrieved quickly, reducing wait times."},

    # ══ PAPER 1 — CHARACTER SETS ══════════════════════════════════════════════
    {"topic":"Character Sets","paper":1,"tier":2,"type":"mc",
     "q":"How many bits does ASCII use to represent each character?",
     "options":["4 bits","7 or 8 bits","16 bits","32 bits"],"answer":1,
     "explanation":"ASCII uses 7 bits (128 characters) or 8 bits (extended ASCII, 256 characters)."},

    {"topic":"Character Sets","paper":1,"tier":2,"type":"mc",
     "q":"What is a benefit of Unicode over ASCII?",
     "options":["Smaller file size","Faster processing","Can represent characters from ALL languages and emojis","Uses fewer bits per character"],"answer":2,
     "explanation":"Unicode supports 100,000+ characters including all world languages and emoji. ASCII only covers 128/256 characters."},

    {"topic":"Character Sets","paper":1,"tier":2,"type":"mc",
     "q":"What is a DRAWBACK of Unicode compared to ASCII?",
     "options":["Cannot represent numbers","Requires more bits per character — larger file size","Only supports English","Cannot represent emojis"],"answer":1,
     "explanation":"Unicode uses 16+ bits per character vs ASCII's 7/8. Files using Unicode are larger."},

    {"topic":"Character Sets","paper":1,"tier":2,"type":"mc",
     "q":"In ASCII, if the letter M has binary code 01001101, what is the binary code for N?",
     "options":["01001100","01001110","01010000","01000001"],"answer":1,
     "explanation":"ASCII letters are sequential. N is one after M: 01001101 + 1 = 01001110."},

    {"topic":"Character Sets","paper":1,"tier":2,"type":"mc",
     "q":"Why are letters in ASCII represented in sequential binary order?",
     "options":["To save space","To allow computers to sort and compare text alphabetically","Because binary is base-2","For historical reasons only"],"answer":1,
     "explanation":"Sequential codes mean alphabetical order = numerical order. Sorting text is just sorting numbers."},

    # ══ PAPER 1 — IMAGE REPRESENTATION ═══════════════════════════════════════
    {"topic":"Image Representation","paper":1,"tier":2,"type":"mc",
     "q":"What is a PIXEL?",
     "options":["A row of binary data","The smallest unit of a digital image — a single square with one colour","The resolution of an image","The colour depth setting"],"answer":1,
     "explanation":"Pixel = picture element. It's the smallest individual unit of a bitmap image, each storing one colour value."},

    {"topic":"Image Representation","paper":1,"tier":2,"type":"mc",
     "q":"What effect does INCREASING colour depth have on an image?",
     "options":["Smaller file, fewer colours","Larger file, better quality (more colours possible)","Smaller file, better quality","No effect"],"answer":1,
     "explanation":"More bits per pixel = more possible colours = better image quality. More bits also means larger file size."},

    {"topic":"Image Representation","paper":1,"tier":2,"type":"mc",
     "q":"What is RESOLUTION in the context of digital images?",
     "options":["The number of colours in the image","The number of pixels wide × pixels tall","The file size in kilobytes","The colour depth setting"],"answer":1,
     "explanation":"Resolution = width × height in pixels (e.g. 1920×1080). Higher resolution = more pixels = more detail."},

    {"topic":"Image Representation","paper":1,"tier":2,"type":"mc",
     "q":"An image is 100×100 pixels with a colour depth of 8 bits. What is its file size in bytes?",
     "options":["800 bytes","8,000 bytes","10,000 bytes","80,000 bytes"],"answer":2,
     "explanation":"100 × 100 × 8 = 80,000 bits. 80,000 ÷ 8 = 10,000 bytes."},

    {"topic":"Image Representation","paper":1,"tier":2,"type":"mc",
     "q":"How many bits are needed to represent exactly 64 different colours?",
     "options":["5","6","7","8"],"answer":1,
     "explanation":"2^6 = 64. So 6 bits exactly covers 64 colours."},

    # ══ PAPER 1 — ENCRYPTION ══════════════════════════════════════════════════
    {"topic":"Encryption","paper":1,"tier":2,"type":"mc",
     "q":"What does encryption DO to data?",
     "options":["Compresses it to reduce file size","Scrambles it using an algorithm and key so it is unreadable without the correct key","Deletes it from storage","Converts it from analogue to digital"],"answer":1,
     "explanation":"Encryption uses an algorithm + key to transform data into ciphertext. Only the correct key can decrypt it back."},

    {"topic":"Encryption","paper":1,"tier":2,"type":"mc",
     "q":"Why should a network use encryption when transmitting sensitive data?",
     "options":["To speed up data transfer","To prevent intercepted data from being read by unauthorised parties","To reduce file sizes","To back up data automatically"],"answer":1,
     "explanation":"If encrypted data is intercepted, it appears as meaningless ciphertext. The attacker cannot read it without the key."},

    {"topic":"Encryption","paper":1,"tier":2,"type":"mc",
     "q":"What is needed to DECRYPT encrypted data?",
     "options":["The original file","The algorithm only","The correct decryption key","The username and password"],"answer":2,
     "explanation":"Data is decrypted using the correct key (and algorithm). Without the key, the ciphertext is meaningless."},

    {"topic":"Encryption","paper":1,"tier":2,"type":"self_mark",
     "q":"Explain the purpose and function of encryption software. [3 marks]",
     "answer":"Purpose: To protect data from being read if it is intercepted during transmission across a network.\nFunction:\n- The data is scrambled/encoded using an algorithm and a key\n- This makes the data unreadable/meaningless to anyone who intercepts it\n- Only someone with the correct key can decrypt it and read the original data",
     "explanation":"1 mark: purpose (protect data in transit). 1 mark: uses algorithm/key to scramble. 1 mark: only correct key decrypts."},

    # ══ PAPER 1 — OS FUNCTIONS ════════════════════════════════════════════════
    {"topic":"OS Functions","paper":1,"tier":2,"type":"mc",
     "q":"Renaming a folder is managed by which OS function?",
     "options":["Memory management","Peripheral management","User management","File management"],"answer":3,
     "explanation":"File management handles creating, renaming, moving, and deleting files and folders."},

    {"topic":"OS Functions","paper":1,"tier":2,"type":"mc",
     "q":"Installing a printer driver is managed by which OS function?",
     "options":["Memory management","Peripheral management","User management","File management"],"answer":1,
     "explanation":"Peripheral management handles communication with I/O devices using device drivers."},

    {"topic":"OS Functions","paper":1,"tier":2,"type":"mc",
     "q":"Multitasking (running multiple applications simultaneously) is managed by which OS function?",
     "options":["Memory management","Peripheral management","User management","File management"],"answer":0,
     "explanation":"Memory management allocates RAM to programs and enables multitasking by swapping data in/out of RAM."},

    {"topic":"OS Functions","paper":1,"tier":2,"type":"mc",
     "q":"Creating a new user account is managed by which OS function?",
     "options":["Memory management","Peripheral management","User management","File management"],"answer":2,
     "explanation":"User management handles user accounts, access permissions, and login authentication."},

    {"topic":"OS Functions","paper":1,"tier":2,"type":"mc",
     "q":"What is the purpose of VIRTUAL MEMORY?",
     "options":["To speed up the CPU","To store the OS permanently","To use part of secondary storage as extra RAM when RAM is full","To encrypt RAM contents"],"answer":2,
     "explanation":"When RAM is full, the OS uses a section of the hard drive as virtual memory. It's slower than RAM but allows more programs to run."},

    {"topic":"OS Functions","paper":1,"tier":2,"type":"mc",
     "q":"What is RAM?",
     "options":["Permanent storage that keeps data without power","Temporary storage that loses its contents when power is removed","Read-only storage that cannot be changed","Secondary storage for long-term files"],"answer":1,
     "explanation":"RAM (Random Access Memory) is volatile — it stores currently running programs and data but loses everything when powered off."},

    {"topic":"OS Functions","paper":1,"tier":2,"type":"mc",
     "q":"What is ROM used for in a computer?",
     "options":["Storing user files permanently","Running currently open applications","Storing firmware/boot instructions — non-volatile","Acting as fast cache memory"],"answer":2,
     "explanation":"ROM (Read-Only Memory) is non-volatile — it keeps its contents without power. Stores the boot sequence/BIOS/firmware."},

    # ══ PAPER 1 — UTILITY SOFTWARE ════════════════════════════════════════════
    {"topic":"Utility Software","paper":1,"tier":2,"type":"mc",
     "q":"What is the purpose of DEFRAGMENTATION software?",
     "options":["Removes viruses from the hard drive","Rearranges file fragments so they are stored contiguously — speeds up access","Compresses files to save space","Backs up files to the cloud"],"answer":1,
     "explanation":"Files become fragmented across the disk over time. Defragmentation brings all parts of each file together, reducing seek time."},

    {"topic":"Utility Software","paper":1,"tier":2,"type":"mc",
     "q":"Why do magnetic hard drives become fragmented?",
     "options":["Because they have no moving parts","Files are stored in separate pieces across the disk as space becomes available","Viruses move file parts around","Because of power cuts"],"answer":1,
     "explanation":"As files grow and are deleted, gaps appear. New data fills gaps where it fits, scattering file fragments across the disk."},

    {"topic":"Utility Software","paper":1,"tier":2,"type":"mc",
     "q":"What type of software performs housekeeping tasks to keep a computer running efficiently?",
     "options":["Application software","System software","Utility software","Productivity software"],"answer":2,
     "explanation":"Utility software performs maintenance tasks: antivirus, defragmentation, backup, compression, encryption tools."},

    # ══ PAPER 1 — LEGISLATION ═════════════════════════════════════════════════
    {"topic":"Legislation","paper":1,"tier":2,"type":"mc",
     "q":"Which law protects personal data held by organisations?",
     "options":["Computer Misuse Act 1990","Copyright Designs and Patents Act 1988","Data Protection Act 2018","Freedom of Information Act"],"answer":2,
     "explanation":"The Data Protection Act 2018 (implementing GDPR) governs how organisations collect, store, and use personal data."},

    {"topic":"Legislation","paper":1,"tier":2,"type":"mc",
     "q":"A hacker gains unauthorised access to a bank's servers. Which law has been broken?",
     "options":["Data Protection Act 2018","Computer Misuse Act 1990","Copyright Designs and Patents Act 1988","Consumer Rights Act"],"answer":1,
     "explanation":"The Computer Misuse Act 1990 criminalises: unauthorised access, unauthorised modification, and spreading malware."},

    {"topic":"Legislation","paper":1,"tier":2,"type":"mc",
     "q":"A student downloads a film from a torrent site without paying. Which law does this break?",
     "options":["Computer Misuse Act 1990","Data Protection Act 2018","Copyright Designs and Patents Act 1988","None — torrenting is legal"],"answer":2,
     "explanation":"CDPA 1988 protects intellectual property. Copying/distributing copyrighted content without permission is illegal."},

    {"topic":"Legislation","paper":1,"tier":2,"type":"mc",
     "q":"Under the Data Protection Act, which of these is a legal requirement for organisations?",
     "options":["They must share data freely with other companies","They must keep data only as long as necessary","They can store any data they want about anyone","They must always encrypt data using government-approved methods"],"answer":1,
     "explanation":"DPA principles include: only keep data as long as needed, keep it accurate, secure it, and only use it for the stated purpose."},

    {"topic":"Legislation","paper":1,"tier":2,"type":"mc",
     "q":"Someone copies a piece of commercial software without a licence. Which act does this violate?",
     "options":["Computer Misuse Act 1990","Data Protection Act 2018","Copyright Designs and Patents Act 1988","GDPR"],"answer":2,
     "explanation":"Copying software without a licence violates CDPA 1988. Software code is protected intellectual property."},

    # ══ PAPER 1 — CYBER SECURITY ══════════════════════════════════════════════
    {"topic":"Cyber Security","paper":1,"tier":2,"type":"mc",
     "q":"What is PHISHING?",
     "options":["Software that replicates itself across a network","Fraudulent emails/websites that trick users into revealing passwords or personal data","Automated password guessing","Intercepting data on a network"],"answer":1,
     "explanation":"Phishing uses deceptive emails or fake websites mimicking legitimate ones to steal credentials or personal data."},

    {"topic":"Cyber Security","paper":1,"tier":2,"type":"mc",
     "q":"What is a BRUTE FORCE attack?",
     "options":["Physically breaking into a server room","Automated software trying every possible password combination","Sending thousands of requests to crash a server","Fake emails pretending to be from banks"],"answer":1,
     "explanation":"Brute force systematically tries all possible passwords/keys until the correct one is found. Defeated by strong, long passwords."},

    {"topic":"Cyber Security","paper":1,"tier":2,"type":"mc",
     "q":"What does a FIREWALL do?",
     "options":["Scans files for viruses","Monitors and filters network traffic to block unauthorised access","Encrypts data during transmission","Backs up important files"],"answer":1,
     "explanation":"A firewall monitors incoming and outgoing network traffic and blocks packets that don't meet security rules."},

    {"topic":"Cyber Security","paper":1,"tier":2,"type":"mc",
     "q":"What is SQL INJECTION?",
     "options":["Physically inserting a device into a USB port","Inserting malicious SQL code into input fields to manipulate a database","A virus spread via email attachments","Guessing database passwords"],"answer":1,
     "explanation":"SQL injection tricks a database by inserting SQL commands through input fields (e.g. login forms). Can expose or delete data."},

    {"topic":"Cyber Security","paper":1,"tier":2,"type":"mc",
     "q":"Which defence BEST protects against data interception on a network?",
     "options":["Firewall","Strong passwords","Encryption","Two-factor authentication"],"answer":2,
     "explanation":"Encryption makes intercepted data unreadable without the key. Even if attackers capture packets, they see only ciphertext."},

    # ══ PAPER 1 — COMPRESSION ═════════════════════════════════════════════════
    {"topic":"Compression","paper":1,"tier":2,"type":"mc",
     "q":"What is the key difference between LOSSY and LOSSLESS compression?",
     "options":["Lossy is faster; lossless is slower","Lossy permanently removes data; lossless can fully restore the original","Lossless removes more data","They are the same — both permanently reduce file size"],"answer":1,
     "explanation":"Lossy permanently discards data (MP3, JPEG). Lossless encodes patterns — original can be fully reconstructed (ZIP, PNG)."},

    {"topic":"Compression","paper":1,"tier":2,"type":"mc",
     "q":"Why is LOSSY compression NOT suitable for a text document?",
     "options":["Text files are too small to compress","Text documents need every character to be exact — losing data would corrupt the content","Lossy compression is only for images","Text cannot be compressed"],"answer":1,
     "explanation":"Lossy permanently removes data. In text, even one changed character changes meaning. Only lossless is suitable for text/executables."},

    {"topic":"Compression","paper":1,"tier":2,"type":"mc",
     "q":"Which file type typically uses LOSSY compression?",
     "options":["ZIP","PNG","MP3","DOCX"],"answer":2,
     "explanation":"MP3 uses lossy compression — removes audio frequencies humans barely notice. ZIP and PNG are lossless. DOCX is not compressed by default."},

    {"topic":"Compression","paper":1,"tier":2,"type":"mc",
     "q":"What is a benefit of compressing a file before sending it by email?",
     "options":["Improves image quality","Reduces file size — faster to send and uses less bandwidth","Makes the file more secure","Converts it to a more compatible format"],"answer":1,
     "explanation":"Smaller files transfer faster and use less network bandwidth. Useful when email attachment size limits are tight."},

    # ══ PAPER 1 — CLOUD STORAGE ═══════════════════════════════════════════════
    {"topic":"Cloud Storage","paper":1,"tier":2,"type":"mc",
     "q":"What is a DRAWBACK of cloud storage?",
     "options":["Files can only be accessed from one device","Requires an internet connection — no access when offline","Data is automatically deleted after 30 days","Cannot store more than 1 GB"],"answer":1,
     "explanation":"Cloud storage is only accessible when online. No internet = no access to your files."},

    {"topic":"Cloud Storage","paper":1,"tier":2,"type":"mc",
     "q":"What is a BENEFIT of cloud storage?",
     "options":["No subscription cost","Data can be accessed from any device with internet access","More secure than local storage — guaranteed","Faster access than local SSD"],"answer":1,
     "explanation":"Cloud storage is accessible from any device anywhere with internet. Enables easy sharing and collaboration."},

    {"topic":"Cloud Storage","paper":1,"tier":2,"type":"mc",
     "q":"Which is a security concern with cloud storage?",
     "options":["Files automatically compress","You lose full control over your data's security — reliant on the provider's security","Data is always encrypted by default","Cloud providers are legally required to share data"],"answer":1,
     "explanation":"You must trust the cloud provider's security. If they're breached, your data is compromised. You have no direct control."},

    # ══ PAPER 2 — SELECTION / ITERATION ══════════════════════════════════════
    {"topic":"Selection vs Iteration","paper":2,"tier":1,"type":"mc",
     "q":"Which keyword opens a SELECTION statement in OCR pseudocode?",
     "options":["for","while","if","do"],"answer":2,
     "explanation":"if/then/else/endif is selection. for/while/do-until are iteration."},

    {"topic":"Selection vs Iteration","paper":2,"tier":1,"type":"mc",
     "q":"A `while` loop checks its condition at which point?",
     "options":["At the end of each iteration","Before each iteration — may never run","In the middle of each iteration","Only once at the start"],"answer":1,
     "explanation":"while checks BEFORE executing. If the condition is false from the start, the loop body never runs. do-until always runs at least once."},

    {"topic":"Selection vs Iteration","paper":2,"tier":1,"type":"mc",
     "q":"A `do...until` loop is different from `while` because...",
     "options":["It runs a fixed number of times","It always executes at least once, then checks the condition at the end","It can only be used inside a function","It uses a counter variable"],"answer":1,
     "explanation":"do-until executes first, then checks the condition. while checks first, so may execute zero times."},

    {"topic":"Selection vs Iteration","paper":2,"tier":1,"type":"mc",
     "q":"In OCR pseudocode, which keyword ends a `for` loop?",
     "options":["endfor","endif","next","loop"],"answer":2,
     "explanation":"OCR ERL uses: for x = 1 to 10 ... next x. The `next` keyword closes the for loop."},

    {"topic":"Selection vs Iteration","paper":2,"tier":1,"type":"mc",
     "q":"What does `elseif` do in OCR pseudocode?",
     "options":["Ends the if block","Creates a second condition to check if the first was false","Starts a loop","Declares a variable"],"answer":1,
     "explanation":"elseif adds additional conditions: if ... then / elseif ... then / else / endif."},

    {"topic":"Selection vs Iteration","paper":2,"tier":1,"type":"mc",
     "q":"What operator is used to check if two values are EQUAL in OCR pseudocode?",
     "options":["=","==","!=","<="],"answer":1,
     "explanation":"== is comparison (is A equal to B?). = is assignment (set A to equal B). Common error: using = instead of == in conditions."},

    {"topic":"Selection vs Iteration","paper":2,"tier":1,"type":"mc",
     "q":"What does the != operator mean in OCR pseudocode?",
     "options":["Less than","Greater than","Not equal to","Approximately equal"],"answer":2,
     "explanation":"!= means 'not equal to'. e.g. while answer != \"quit\" — keep looping until user types quit."},

    {"topic":"Selection vs Iteration","paper":2,"tier":1,"type":"mc",
     "q":"How many times does this loop run?\nfor i = 1 to 5\n    print(i)\nnext i",
     "options":["4","5","6","0"],"answer":1,
     "explanation":"for i = 1 to 5 runs with i = 1, 2, 3, 4, 5. That's 5 iterations."},

    {"topic":"Selection vs Iteration","paper":2,"tier":1,"type":"mc",
     "q":"Which of these is a COUNT-CONTROLLED loop?",
     "options":["while score < 100","do ... until done","for i = 1 to 10","if x > 0 then"],"answer":2,
     "explanation":"for is count-controlled — runs a fixed, predetermined number of times. while/do-until are condition-controlled."},

    # ══ PAPER 2 — LOGIC GATES ════════════════════════════════════════════════
    {"topic":"Logic Gates","paper":2,"tier":1,"type":"mc",
     "q":"An AND gate outputs 1 ONLY when...",
     "options":["At least one input is 1","The inputs are different","ALL inputs are 1","Neither input is 1"],"answer":2,
     "explanation":"AND: output 1 only when ALL inputs are 1. Any input being 0 makes output 0."},

    {"topic":"Logic Gates","paper":2,"tier":1,"type":"mc",
     "q":"An OR gate outputs 0 ONLY when...",
     "options":["Both inputs are 1","At least one input is 0","ALL inputs are 0","The inputs are equal"],"answer":2,
     "explanation":"OR outputs 0 only when ALL inputs are 0. Any input being 1 gives output 1."},

    {"topic":"Logic Gates","paper":2,"tier":1,"type":"mc",
     "q":"For P = NOT A AND (B OR C), what is P when A=1, B=1, C=0?",
     "options":["0","1","Same as B","Error"],"answer":0,
     "explanation":"NOT A = NOT 1 = 0. B OR C = 1. 0 AND 1 = 0. P = 0."},

    {"topic":"Logic Gates","paper":2,"tier":1,"type":"mc",
     "q":"For P = (A AND B) OR C, what is P when A=0, B=1, C=1?",
     "options":["0","1","Same as A","Error"],"answer":1,
     "explanation":"A AND B = 0. 0 OR C = 0 OR 1 = 1. P = 1."},

    {"topic":"Logic Gates","paper":2,"tier":1,"type":"mc",
     "q":"How many rows does a truth table with ONE input need?",
     "options":["1","2","4","8"],"answer":1,
     "explanation":"2^1 = 2 rows. Input can only be 0 or 1."},

    {"topic":"Logic Gates","paper":2,"tier":1,"type":"mc",
     "q":"A logic gate outputs 1 when inputs are DIFFERENT (0,1 or 1,0) but 0 when same (0,0 or 1,1). Which gate is this?",
     "options":["AND","OR","NAND","XOR"],"answer":3,
     "explanation":"XOR (Exclusive OR) outputs 1 when inputs differ. Used in half-adder circuits."},

    {"topic":"Logic Gates","paper":2,"tier":1,"type":"self_mark",
     "q":"Complete the truth table for P = NOT (A AND B). [4 marks]\n\nA B | A AND B | P\n0 0 |    ?    | ?\n0 1 |    ?    | ?\n1 0 |    ?    | ?\n1 1 |    ?    | ?",
     "answer":"A B | A AND B | P\n0 0 |    0    | 1\n0 1 |    0    | 1\n1 0 |    0    | 1\n1 1 |    1    | 0\n\n(This is a NAND gate)",
     "explanation":"1 mark per 2 correct P values. P is the opposite of AND."},

    {"topic":"Logic Gates","paper":2,"tier":1,"type":"self_mark",
     "q":"Describe the purpose of a truth table. [2 marks]",
     "answer":"A truth table shows all possible combinations of input values for a Boolean expression or logic circuit, along with the resulting output for each combination.",
     "explanation":"1 mark: shows all possible input combinations. 1 mark: shows the corresponding output."},

    # ══ PAPER 2 — TRACE TABLES ════════════════════════════════════════════════
    {"topic":"Trace Tables","paper":2,"tier":1,"type":"mc",
     "q":"What is a trace table used for?",
     "options":["To show how long a program takes to run","To manually track variable values line by line to check an algorithm is correct","To draw a flowchart of an algorithm","To count the number of lines in a program"],"answer":1,
     "explanation":"A trace table manually simulates executing code, recording how each variable's value changes line by line."},

    {"topic":"Trace Tables","paper":2,"tier":1,"type":"mc",
     "q":"What is the output of this algorithm?\nx = 10\nwhile x > 4\n    x = x - 3\nendwhile\nprint(x)",
     "options":["4","1","7","10"],"answer":1,
     "explanation":"x=10 (>4, continue), x=7 (>4), x=4 (NOT >4, stop). Output: 4."},

    {"topic":"Trace Tables","paper":2,"tier":1,"type":"mc",
     "q":"After this runs, what is the value of `total`?\ntotal = 0\nfor i = 1 to 4\n    total = total + i\nnext i",
     "options":["4","10","16","0"],"answer":1,
     "explanation":"total: 0+1=1, +2=3, +3=6, +4=10. Final total = 10."},

    {"topic":"Trace Tables","paper":2,"tier":1,"type":"mc",
     "q":"What does a do...until loop guarantee?",
     "options":["It always runs exactly once","It runs at least once before checking the condition","It never runs if the condition is true at the start","It must use a counter variable"],"answer":1,
     "explanation":"do-until always executes the body at least once, then checks the condition. while checks first."},

    {"topic":"Trace Tables","paper":2,"tier":1,"type":"self_mark",
     "q":"Trace this algorithm with input values 7, 3, 9, 4:\n\ncount = 0\ntotal = 0\nfor i = 1 to 4\n    num = input(\"Enter: \")\n    if num > 5 then\n        count = count + 1\n    endif\n    total = total + num\nnext i\nprint(count)\nprint(total)\n\nState the two outputs. [4 marks]",
     "answer":"i=1: num=7 (>5 → count=1), total=7\ni=2: num=3 (not >5), total=10\ni=3: num=9 (>5 → count=2), total=19\ni=4: num=4 (not >5), total=23\nOutput 1: 2\nOutput 2: 23",
     "explanation":"1 mark per correctly traced iteration. 1 mark correct count output (2). 1 mark correct total (23)."},

    # ══ PAPER 2 — LOGIC ERRORS ════════════════════════════════════════════════
    {"topic":"Logic Errors","paper":2,"tier":1,"type":"mc",
     "q":"What type of error does this code have?\ntotal = 0\nfor i = 1 to 5\n    total = 0\n    total = total + scores[i]\nnext i",
     "options":["Syntax error","Runtime error","Logic error","No error"],"answer":2,
     "explanation":"total = 0 inside the loop resets it every iteration. The program runs but total only ever contains the last score."},

    {"topic":"Logic Errors","paper":2,"tier":1,"type":"mc",
     "q":"A programmer writes `if x = 10 then` intending to CHECK if x equals 10. What type of error is this likely to cause?",
     "options":["Syntax error (won't compile)","Logic error (assignment instead of comparison)","Runtime error","No error"],"answer":0,
     "explanation":"In many languages, = in a condition is a syntax error. In OCR ERL specifically, == is comparison and = is assignment."},

    {"topic":"Logic Errors","paper":2,"tier":1,"type":"mc",
     "q":"This loop `for count = 1 to scores.length` accesses a 0-indexed array. What logic error occurs?",
     "options":["Loop runs too many times","scores[0] is skipped — first element is never processed","Loop runs infinitely","A runtime crash on last element"],"answer":1,
     "explanation":"0-indexed arrays start at 0 but loop starts at 1. scores[0] is never accessed. Fix: for count = 0 to scores.length - 1."},

    {"topic":"Logic Errors","paper":2,"tier":1,"type":"self_mark",
     "q":"Identify the logic error in this algorithm and write the corrected line:\n\nline 01: for i = 0 to names.length - 1\nline 02:     found = False\nline 03:     if names[i] == target then\nline 04:         found = True\nline 05:     endif\nline 06: next i",
     "answer":"Logic error: Line 02 — found = False is inside the loop, resetting it every iteration. Even if target is found, found gets reset to False on the next iteration.\nCorrected line 02: Move found = False BEFORE the loop (before line 01).",
     "explanation":"1 mark: identify line 02 as the error. 1 mark: correct fix (move before loop)."},

    # ══ PAPER 2 — DATA TYPES ══════════════════════════════════════════════════
    {"topic":"Data Types","paper":2,"tier":1,"type":"mc",
     "q":"A program stores whether a door is open or closed. What data type for the `isOpen` variable?",
     "options":["Integer","String","Boolean","Real"],"answer":2,
     "explanation":"Open/closed is a binary state (True/False) — Boolean."},

    {"topic":"Data Types","paper":2,"tier":1,"type":"mc",
     "q":"A program stores a temperature like -3.5°C. What data type?",
     "options":["Boolean","Integer","Real","Char"],"answer":2,
     "explanation":"Temperatures can be negative and decimal — Real (Float)."},

    {"topic":"Data Types","paper":2,"tier":1,"type":"mc",
     "q":"A student's name like 'Mohammed Al-Rashid'. What data type?",
     "options":["Char","Integer","Boolean","String"],"answer":3,
     "explanation":"Names are text of variable length — String."},

    {"topic":"Data Types","paper":2,"tier":1,"type":"mc",
     "q":"A program stores a year (e.g. 2024). What data type?",
     "options":["Real","Boolean","String","Integer"],"answer":3,
     "explanation":"A year is a whole number — Integer. No decimals needed."},

    {"topic":"Data Types","paper":2,"tier":1,"type":"mc",
     "q":"Why should a postcode like 'SW1A 2AA' be stored as String, not Integer?",
     "options":["It is too long for an integer","It contains letters and spaces — cannot be stored as a number","Integers cannot be used for addresses","Strings are more efficient"],"answer":1,
     "explanation":"Postcodes contain letters, numbers, and spaces. They must be String. Also, arithmetic on postcodes makes no sense."},

    # ══ PAPER 2 — SQL ══════════════════════════════════════════════════════════
    {"topic":"SQL","paper":2,"tier":1,"type":"mc",
     "q":"In SQL, which keyword retrieves specific fields?",
     "options":["RETRIEVE","GET","SELECT","FETCH"],"answer":2,
     "explanation":"SELECT specifies which fields (columns) to return. SELECT * returns all fields."},

    {"topic":"SQL","paper":2,"tier":1,"type":"mc",
     "q":"In SQL, how do you combine TWO conditions in a WHERE clause?",
     "options":["WHERE x AND y (using AND keyword)","WHERE x, y","WHERE x + y","WHERE (x)(y)"],"answer":0,
     "explanation":"Use AND or OR to combine conditions: WHERE SensorType = \"Door\" AND Length > 20."},

    {"topic":"SQL","paper":2,"tier":1,"type":"mc",
     "q":"What does WHERE Price <= 10 mean?",
     "options":["Price equals 10","Price is less than 10","Price is 10 or less","Price is not 10"],"answer":2,
     "explanation":"<= means 'less than or equal to'. Price <= 10 returns records where Price is 10 or below."},

    {"topic":"SQL","paper":2,"tier":1,"type":"mc",
     "q":"Which SQL returns ALL fields from TblStudents?",
     "options":["SELECT ALL FROM TblStudents","SELECT TblStudents.*","SELECT * FROM TblStudents","FROM TblStudents SELECT *"],"answer":2,
     "explanation":"SELECT * FROM TblStudents — the asterisk (*) means all fields, then FROM specifies the table."},

    # ══ PAPER 2 — TESTING ════════════════════════════════════════════════════
    {"topic":"Testing","paper":2,"tier":1,"type":"mc",
     "q":"A program accepts ages from 13 to 17. What is ERRONEOUS test data?",
     "options":["14","13","17","12"],"answer":3,
     "explanation":"12 is outside the valid range (13–17) and should be rejected. 13 and 17 are boundary, 14 is normal."},

    {"topic":"Testing","paper":2,"tier":1,"type":"mc",
     "q":"For a field accepting 0–100, which value is BOUNDARY test data?",
     "options":["50","0 and 100","−1 and 101","'Hello'"],"answer":1,
     "explanation":"Boundary test data tests the exact limits: 0 (lower boundary) and 100 (upper boundary)."},

    {"topic":"Testing","paper":2,"tier":1,"type":"mc",
     "q":"What is BLACK BOX testing?",
     "options":["Testing done in the dark","Testing without knowledge of the internal code — only testing inputs and outputs","Testing only error-handling","Testing only the database"],"answer":1,
     "explanation":"Black box testing validates outputs for given inputs without looking at the code. White box testing uses knowledge of the code."},

    {"topic":"Testing","paper":2,"tier":1,"type":"mc",
     "q":"What is an INTERPRETER's advantage during testing/development?",
     "options":["Creates a faster executable","Reports all errors at once","Stops at the first error — easier to find and fix during development","Requires no translation"],"answer":2,
     "explanation":"Interpreters execute line by line and stop immediately on an error, making it clear exactly where the fault is."},

    {"topic":"Testing","paper":2,"tier":1,"type":"self_mark",
     "q":"Complete the test plan for a field that accepts integers between 1 and 10 inclusive. Include: one normal, one boundary, one erroneous test value. State the expected result for each. [3 marks]",
     "answer":"Normal: e.g. 5 → Accepted\nBoundary: 1 (or 10) → Accepted\nErroneous: 0 (or 11, or 'Hello') → Rejected",
     "explanation":"1 mark per row: correct test data + correct expected result for that type."},

    # ══ PAPER 2 — FUNCTIONS & PROCEDURES ═════════════════════════════════════
    {"topic":"Functions & Procedures","paper":2,"tier":1,"type":"mc",
     "q":"What does a function RETURN?",
     "options":["Nothing","Control to the calling code","A value to the calling code","An error message"],"answer":2,
     "explanation":"A function returns a value using the `return` keyword. A procedure performs actions but returns nothing."},

    {"topic":"Functions & Procedures","paper":2,"tier":1,"type":"mc",
     "q":"What is the difference between a PARAMETER and an ARGUMENT?",
     "options":["They are the same thing","A parameter is in the definition; an argument is the actual value passed when calling","An argument is in the definition; a parameter is the value passed","Parameters are only used in procedures"],"answer":1,
     "explanation":"Parameter: variable in the function definition. Argument: actual value passed when calling. e.g. function add(a,b): a,b are parameters. add(3,5): 3,5 are arguments."},

    {"topic":"Functions & Procedures","paper":2,"tier":1,"type":"mc",
     "q":"In OCR pseudocode, which keyword closes a procedure definition?",
     "options":["endfunction","return","endprocedure","next"],"answer":2,
     "explanation":"Procedures use: procedure name(params) ... endprocedure. Functions use: function name(params) ... return value ... endfunction."},

    {"topic":"Functions & Procedures","paper":2,"tier":1,"type":"self_mark",
     "q":"Write a procedure in OCR pseudocode called `greet` that takes a parameter `name` and prints 'Hello, ' followed by the name. Then write the call to greet with the argument 'Alice'. [3 marks]",
     "answer":"procedure greet(name)\n    print(\"Hello, \" + name)\nendprocedure\n\ngreet(\"Alice\")",
     "explanation":"1 mark: procedure with correct parameter. 1 mark: correct print. 1 mark: correct call with argument."},

    # ══ PAPER 2 — SORTING ALGORITHMS ══════════════════════════════════════════
    {"topic":"Sorting Algorithms","paper":2,"tier":2,"type":"mc",
     "q":"After ONE complete pass of bubble sort on [5, 3, 8, 1, 9], what is the list?",
     "options":["[1, 3, 5, 8, 9]","[3, 5, 1, 8, 9]","[3, 5, 8, 1, 9]","[1, 3, 8, 5, 9]"],"answer":1,
     "explanation":"Compare pairs: (5,3)→swap=[3,5,8,1,9], (5,8)→ok=[3,5,8,1,9], (8,1)→swap=[3,5,1,8,9], (8,9)→ok=[3,5,1,8,9]. After 1 pass: [3,5,1,8,9]."},

    {"topic":"Sorting Algorithms","paper":2,"tier":2,"type":"mc",
     "q":"Why is merge sort generally more efficient than bubble sort for large lists?",
     "options":["Merge sort uses less memory","Merge sort has fewer comparisons overall — O(n log n) vs O(n²)","Merge sort doesn't need swaps","Merge sort only works on small lists"],"answer":1,
     "explanation":"Bubble sort is O(n²) — comparisons grow rapidly with size. Merge sort is O(n log n) — much faster for large datasets."},

    {"topic":"Sorting Algorithms","paper":2,"tier":2,"type":"self_mark",
     "q":"Explain what the `temp` variable is used for during a swap in a sorting algorithm. [2 marks]",
     "answer":"temp temporarily stores the value of one variable before it is overwritten, so the swap can be completed without losing data.\ne.g. temp=a, a=b, b=temp",
     "explanation":"1 mark: prevents data loss during overwrite. 1 mark: correct example of 3-step swap using temp."},

    # ══ PAPER 2 — SEARCHING ════════════════════════════════════════════════════
    {"topic":"Searching Algorithms","paper":2,"tier":2,"type":"mc",
     "q":"Binary search on a list of 32 items needs at most how many comparisons?",
     "options":["5","10","16","32"],"answer":0,
     "explanation":"log₂(32) = 5. After 5 halvings, only one item remains. Max 5 comparisons."},

    {"topic":"Searching Algorithms","paper":2,"tier":2,"type":"mc",
     "q":"Which searching algorithm works on UNSORTED lists?",
     "options":["Binary search","Linear search","Both work on unsorted","Neither works on unsorted"],"answer":1,
     "explanation":"Linear search checks every element in order — works on any list. Binary search REQUIRES a sorted list."},

    {"topic":"Searching Algorithms","paper":2,"tier":2,"type":"mc",
     "q":"Binary search on [2, 5, 8, 12, 16, 23, 38, 56]. Looking for 23. What is the first element checked?",
     "options":["2","12","16","23"],"answer":1,
     "explanation":"Middle of 8 items = index 3 = 12. 12 < 23, so search right half [16, 23, 38, 56]. Next middle = 23. Found!"},

    # ══ PAPER 2 — VALIDATION ══════════════════════════════════════════════════
    {"topic":"Validation","paper":2,"tier":2,"type":"mc",
     "q":"Which type of check verifies that a field has not been left empty?",
     "options":["Range check","Type check","Presence check","Format check"],"answer":2,
     "explanation":"A presence check ensures required fields are not blank. e.g. username cannot be empty string."},

    {"topic":"Validation","paper":2,"tier":2,"type":"mc",
     "q":"A format check on a date field (DD/MM/YYYY) would reject which input?",
     "options":["01/01/2024","25/12/2023","2024-01-01","31/10/2025"],"answer":2,
     "explanation":"2024-01-01 does not match the DD/MM/YYYY format. Format checks verify the structure/pattern of data."},

    {"topic":"Validation","paper":2,"tier":2,"type":"self_mark",
     "q":"Write OCR pseudocode to validate that an age entered by a user is between 0 and 120 inclusive. Keep asking until a valid age is entered. [3 marks]",
     "answer":"age = int(input(\"Enter age: \"))\nwhile age < 0 OR age > 120\n    print(\"Invalid age. Enter 0-120.\")\n    age = int(input(\"Enter age: \"))\nendwhile",
     "explanation":"1 mark: input before loop. 1 mark: while loop with correct condition. 1 mark: re-prompt inside loop."},

    # ══ PAPER 2 — ARRAYS ══════════════════════════════════════════════════════
    {"topic":"Arrays","paper":2,"tier":2,"type":"mc",
     "q":"An array `prices` contains [4.99, 12.50, 0.75, 8.00]. What does `prices[2]` return?",
     "options":["12.50","0.75","4.99","8.00"],"answer":1,
     "explanation":"0-indexed: prices[0]=4.99, prices[1]=12.50, prices[2]=0.75, prices[3]=8.00. prices[2] = 0.75."},

    {"topic":"Arrays","paper":2,"tier":2,"type":"mc",
     "q":"How do you declare an array of 5 items in OCR pseudocode?",
     "options":["array scores[5]","scores = [1, 2, 3, 4, 5]","scores = array(5)","array scores = new[5]"],"answer":1,
     "explanation":"OCR ERL: scores = [val1, val2, ...] or declared as array scores[5]. Either form is accepted."},

    {"topic":"Arrays","paper":2,"tier":2,"type":"self_mark",
     "q":"Write OCR pseudocode to loop through an array called `marks` and print each element. [3 marks]",
     "answer":"for i = 0 to marks.length - 1\n    print(marks[i])\nnext i",
     "explanation":"1 mark: loop from 0 to length-1. 1 mark: accessing marks[i] inside loop. 1 mark: correct loop syntax."},

    # ══ PAPER 2 — FILE HANDLING ═══════════════════════════════════════════════
    {"topic":"File Handling","paper":2,"tier":2,"type":"mc",
     "q":"In OCR pseudocode, what does `myFile.readLine()` do?",
     "options":["Writes a line to the file","Reads and returns the next line from the file","Closes the file","Checks if the file exists"],"answer":1,
     "explanation":"readLine() reads one line at a time from an open file. Usually used inside a while NOT endOfFile() loop."},

    {"topic":"File Handling","paper":2,"tier":2,"type":"mc",
     "q":"Why must you always call `.close()` after working with a file?",
     "options":["To free memory","To ensure all data is saved and the file is properly released by the OS","To encrypt the file","To compress it"],"answer":1,
     "explanation":"Closing a file ensures any buffered writes are flushed and the file handle is released back to the operating system."},

    # ══ PAPER 2 — COMPILER VS INTERPRETER ════════════════════════════════════
    {"topic":"Compiler vs Interpreter","paper":2,"tier":2,"type":"mc",
     "q":"A compiled program reports all errors. An interpreter reports errors...",
     "options":["All at once before running","One at a time — stops at the first error during execution","Never — interpreters cannot detect errors","After all correct lines have run"],"answer":1,
     "explanation":"Interpreter: translates one line, executes, if error → stop and report. Compiler: translates all first, then lists all errors found."},

    {"topic":"Compiler vs Interpreter","paper":2,"tier":2,"type":"mc",
     "q":"Which statement about compilers is TRUE?",
     "options":["Compiled programs always run slower","The compiler must be present each time the program runs","A compiled executable can run without the original compiler or source code","Compilers only work with Python"],"answer":2,
     "explanation":"Compiled programs become standalone executables. The compiler is only needed during development, not when running the final program."},

    # ══ PAPER 2 — HIGH/LOW LEVEL LANGUAGES ═══════════════════════════════════
    {"topic":"High vs Low Level Languages","paper":2,"tier":2,"type":"mc",
     "q":"Which language is closest to machine code (binary)?",
     "options":["Python","Java","Assembly language","Scratch"],"answer":2,
     "explanation":"Assembly uses mnemonics (LDA, STA, ADD) that map directly to machine code instructions. Python/Java are high-level."},

    {"topic":"High vs Low Level Languages","paper":2,"tier":2,"type":"mc",
     "q":"What is a disadvantage of writing in assembly language?",
     "options":["Very fast execution","Full hardware control","Harder to read, write, and maintain — processor-specific","Direct memory access"],"answer":2,
     "explanation":"Assembly is processor-specific (code for one CPU won't run on another) and much harder to read/debug than high-level code."},

    # ══ PAPER 2 — COMPUTATIONAL THINKING ═════════════════════════════════════
    {"topic":"Computational Thinking","paper":2,"tier":2,"type":"mc",
     "q":"A teacher wants to build a school timetabling system. They break it into: room booking, teacher allocation, class scheduling. This is an example of...",
     "options":["Abstraction","Pattern recognition","Decomposition","Algorithmic thinking"],"answer":2,
     "explanation":"Breaking a complex problem into smaller, manageable sub-problems is decomposition."},

    {"topic":"Computational Thinking","paper":2,"tier":2,"type":"mc",
     "q":"A map of the London Underground doesn't show street-level geography — just station connections. This is an example of...",
     "options":["Decomposition","Abstraction","Pattern recognition","Algorithmic thinking"],"answer":1,
     "explanation":"Abstraction removes unnecessary detail. The tube map abstracts away real geography to show only what matters: station connections and line colours."},

    # ══ PAPER 2 — MAINTAINABILITY ═════════════════════════════════════════════
    {"topic":"Maintainability","paper":2,"tier":2,"type":"mc",
     "q":"Which variable name is MOST maintainable?",
     "options":["x","n1","numberOfStudentsInClass","NSOIC"],"answer":2,
     "explanation":"Meaningful names like numberOfStudentsInClass make code self-documenting. Future developers (or you in 6 months) understand instantly."},

    {"topic":"Maintainability","paper":2,"tier":2,"type":"mc",
     "q":"Why are COMMENTS in code important for maintainability?",
     "options":["They make the program run faster","They explain what sections of code do — making it easier for others to understand and modify","They prevent bugs","They are required by OCR"],"answer":1,
     "explanation":"Comments document the intent and function of code. Essential when code is maintained by different developers over time."},

    # ══ PAPER 2 — STRING MANIPULATION ════════════════════════════════════════
    {"topic":"String Manipulation","paper":2,"tier":2,"type":"mc",
     "q":'What does "Computing".substring(0, 4) return in OCR pseudocode?',
     "options":['"ting"','"Comp"','"ompu"','"Compu"'],"answer":1,
     "explanation":'substring(start, length): start at index 0, take 4 characters: "Comp".'},

    {"topic":"String Manipulation","paper":2,"tier":2,"type":"mc",
     "q":'What does "Hello World".length return?',
     "options":["10","11","5","12"],"answer":1,
     "explanation":'"Hello World" has 11 characters (including the space). .length returns 11.'},

    {"topic":"String Manipulation","paper":2,"tier":2,"type":"mc",
     "q":'What is the result of "Hello" + " " + "World" in OCR pseudocode?',
     "options":['"HelloWorld"','"Hello World"','"Hello+World"','Error'],"answer":1,
     "explanation":'String concatenation with + joins strings. "Hello" + " " + "World" = "Hello World".'},

    # ══ PAPER 2 — CASTING ════════════════════════════════════════════════════
    {"topic":"Casting","paper":2,"tier":2,"type":"mc",
     "q":"What is the result of int(\"42\") in OCR pseudocode?",
     "options":['The string "42"',"The integer 42","An error","The float 42.0"],"answer":1,
     "explanation":'int() converts a String to Integer. int("42") → 42 (integer). Needed before arithmetic on user input.'},

    {"topic":"Casting","paper":2,"tier":2,"type":"mc",
     "q":"What does str(100) return?",
     "options":["The integer 100","A Boolean","The string \"100\"","An error"],"answer":2,
     "explanation":'str() converts to String. str(100) → "100". Needed to concatenate numbers with strings: "Score: " + str(score).'},

    # ══ PAPER 2 — IDE FEATURES ════════════════════════════════════════════════
    {"topic":"IDE Features","paper":2,"tier":2,"type":"mc",
     "q":"What does AUTO-COMPLETE in an IDE do?",
     "options":["Runs the code automatically","Suggests and completes variable names, keywords, and function names as you type","Checks for logical errors","Formats code automatically"],"answer":1,
     "explanation":"Auto-complete reduces typing errors and speeds up coding by suggesting valid completions as you type."},

    {"topic":"IDE Features","paper":2,"tier":2,"type":"mc",
     "q":"What is a RUN-TIME ENVIRONMENT in an IDE?",
     "options":["A second monitor","The environment that executes the program and displays output","A version of the language that runs faster","Automatic test generation"],"answer":1,
     "explanation":"The run-time environment in an IDE executes the program and typically shows output in a console/terminal pane."},

    # ══ PAPER 2 — FLOWCHARTS ═════════════════════════════════════════════════
    {"topic":"Flowcharts","paper":2,"tier":2,"type":"mc",
     "q":"In a flowchart, which shape represents a PROCESS (e.g. a calculation)?",
     "options":["Diamond","Oval","Rectangle","Parallelogram"],"answer":2,
     "explanation":"Rectangle = process. Diamond = decision. Oval = start/end. Parallelogram = input/output."},

    {"topic":"Flowcharts","paper":2,"tier":2,"type":"mc",
     "q":"A DECISION symbol in a flowchart has how many exits?",
     "options":["1","2","3","4"],"answer":1,
     "explanation":"A decision diamond has 2 exits: Yes and No (or True and False). Each leads to a different path."},

    # ══ PAPER 2 — VARIABLES (LOCAL/GLOBAL) ═══════════════════════════════════
    {"topic":"Variables","paper":2,"tier":2,"type":"mc",
     "q":"A variable declared inside a subroutine is...",
     "options":["Available to the whole program","Local — only accessible within that subroutine","Faster than global variables","Automatically deleted after 10 seconds"],"answer":1,
     "explanation":"Local variables exist only within the subroutine they're declared in. They are created when called and destroyed when the subroutine ends."},

    {"topic":"Variables","paper":2,"tier":2,"type":"mc",
     "q":"Why are global variables generally considered bad practice?",
     "options":["They use more memory","Any part of the program can modify them — hard to track bugs and unintended side effects","They run slower","They can only store integers"],"answer":1,
     "explanation":"Any subroutine can change a global variable unexpectedly, making bugs hard to trace. Local variables are safer and more predictable."},
]

# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
class Session:
    def __init__(self):
        self.score = 0
        self.total = 0
        self.streak = 0
        self.topic_stats = {}     # topic -> [correct, attempted]
        self.used_ids = set()     # tracks static question indices used this session
        self.gen_count = {}       # tracks how many times each generator used

    def record(self, topic, correct):
        if correct is None:
            self.streak = 0
            return
        if topic not in self.topic_stats:
            self.topic_stats[topic] = [0, 0]
        self.topic_stats[topic][1] += 1
        self.total += 1
        if correct:
            self.score += 1
            self.streak += 1
            self.topic_stats[topic][0] += 1
        else:
            self.streak = 0

# ─────────────────────────────────────────────────────────────────────────────
# QUESTION SELECTION (anti-repeat)
# ─────────────────────────────────────────────────────────────────────────────
def pick_question(pool_indices, session, paper_filter=None, topic_filter=None):
    """
    50% chance: use a generator (always fresh/unique)
    50% chance: pick from static pool (avoid recently seen)
    """
    # filter generators for the right paper
    gen_pool = GENERATORS[:]
    if paper_filter == 1:
        gen_pool = [g for g in GENERATORS if g().get("paper", 1) == 1]
    elif paper_filter == 2:
        gen_pool = [g for g in GENERATORS if g().get("paper", 2) == 2]
    # re-check generators properly
    if paper_filter is not None or topic_filter is not None:
        filtered_gens = []
        for g in GENERATORS:
            q = g()
            if paper_filter and q.get("paper") != paper_filter:
                continue
            if topic_filter and q.get("topic") != topic_filter:
                continue
            filtered_gens.append(g)
        gen_pool = filtered_gens if filtered_gens else GENERATORS

    # filter static pool
    available_static = [i for i in pool_indices
                        if i not in session.used_ids or len(session.used_ids) >= len(pool_indices)]
    if not available_static:
        session.used_ids.clear()
        available_static = pool_indices[:]

    # 50/50 split or all-generator if no static available
    if gen_pool and (not available_static or random.random() < 0.5):
        gen = random.choice(gen_pool)
        return gen(), None  # no index to track
    else:
        idx = random.choice(available_static)
        session.used_ids.add(idx)
        return STATIC[idx], idx

# ─────────────────────────────────────────────────────────────────────────────
# DISPLAY
# ─────────────────────────────────────────────────────────────────────────────
def header(session, paper_label):
    pct = f"{round(session.score/session.total*100)}%" if session.total else "—"
    streak_str = f"  🔥{session.streak}" if session.streak >= 3 else f"  Streak: {session.streak}"
    print(f"{B}{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{X}")
    print(f"{B}  OCR J277 — {paper_label}{X}  {D}(Q=quit  S=skip  T=change topic){X}")
    print(f"  Score: {G}{B}{session.score}/{session.total} ({pct}){X}{Y}{B}{streak_str}{X}")
    print(f"{B}{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{X}\n")

def tier_col(tier):
    return R if tier == 1 else Y if tier == 2 else D

def ask_mc(q):
    tc = tier_col(q["tier"])
    print(f"  {tc}{B}[{q['topic']} — Tier {q['tier']}]{X}\n")
    # wrap long question text
    for line in q["q"].split("\n"):
        print(f"  {B}{line}{X}")
    print()
    for i, opt in enumerate(q["options"]):
        print(f"    {B}{chr(65+i)}.{X}  {opt}")
    print()
    while True:
        ans = input("  Answer (A/B/C/D) S=skip Q=quit: ").strip().upper()
        if ans in ['A','B','C','D','S','Q']:
            break
        print("  Enter A, B, C, D, S, or Q.")
    if ans == 'Q':
        return 'quit'
    if ans == 'S':
        print(f"\n  {D}Skipped. Answer: {B}{chr(65+q['answer'])}: {q['options'][q['answer']]}{X}")
        print(f"  {Y}→ {q['explanation']}{X}")
        return None
    correct = (ord(ans)-65) == q["answer"]
    if correct:
        print(f"\n  {G}{B}✓  Correct!{X}")
    else:
        print(f"\n  {R}{B}✗  Incorrect.{X}  Answer: {B}{chr(65+q['answer'])}: {q['options'][q['answer']]}{X}")
    print(f"  {Y}→ {q['explanation']}{X}")
    return correct

def ask_self_mark(q):
    tc = tier_col(q["tier"])
    print(f"  {tc}{B}[{q['topic']} — Tier {q['tier']}  |  Open-ended]{X}\n")
    for line in q["q"].split("\n"):
        print(f"  {B}{line}{X}")
    print(f"\n  {D}Write your answer, then press Enter twice to reveal the model answer.{X}")
    ans = input("  Your answer (Q to quit): ").strip().upper()
    if ans == 'Q':
        return 'quit'
    print(f"\n  {C}{B}Model Answer:{X}")
    for line in q["answer"].split("\n"):
        print(f"    {line}")
    print(f"\n  {Y}→ Mark scheme: {q['explanation']}{X}\n")
    while True:
        m = input("  Did you get it? (Y/N): ").strip().upper()
        if m in ['Y','N']:
            return m == 'Y'

# ─────────────────────────────────────────────────────────────────────────────
# MENUS
# ─────────────────────────────────────────────────────────────────────────────
def paper_menu():
    clr()
    print(f"\n{B}{C}")
    print("  ╔══════════════════════════════════════════════════════════╗")
    print("  ║      OCR J277 GCSE Computer Science — Question Bank     ║")
    print("  ║      Built from 2022–2025 past papers + AI-generated   ║")
    print("  ╚══════════════════════════════════════════════════════════╝")
    print(f"{X}")
    print(f"  {R}{B}Tier 1{X} = guaranteed every year   {Y}{B}Tier 2{X} = very likely   {D}Tier 3{X} = rotates\n")
    print(f"  {B}Select a paper:{X}\n")
    print(f"  {B}1.{X}  Paper 1 — Computer Systems  {D}(networking, binary, storage, CPU, OS){X}")
    print(f"  {B}2.{X}  Paper 2 — Programming & Algorithms  {D}(SQL, logic, sorting, pseudocode){X}")
    print(f"  {B}3.{X}  Mixed — Both papers  {D}(full revision){X}\n")
    while True:
        c = input("  Enter 1, 2 or 3: ").strip()
        if c in ['1','2','3']:
            return int(c)
        print("  Enter 1, 2, or 3.")

def topic_menu(pool_indices, paper_filter):
    topics = sorted(set(STATIC[i]["topic"] for i in pool_indices
                        if paper_filter is None or STATIC[i]["paper"] == paper_filter or paper_filter == 3))
    print(f"\n  {B}Select a topic (or 0 for all):{X}\n")
    for i, t in enumerate(topics):
        relevant = [STATIC[j] for j in pool_indices
                    if STATIC[j]["topic"] == t and
                    (paper_filter is None or STATIC[j]["paper"] == paper_filter or paper_filter == 3)]
        if not relevant:
            continue
        min_tier = min(q["tier"] for q in relevant)
        count = len(relevant)
        tc = R if min_tier==1 else Y if min_tier==2 else D
        print(f"  {i+1:3}.  {tc}[T{min_tier}]{X}  {t}  {D}({count} questions + fresh generated){X}")
    print(f"\n  {B}  0.{X}  All topics\n")
    while True:
        c = input("  Enter number: ").strip()
        if c == '0' or c == '':
            return None
        try:
            idx = int(c) - 1
            if 0 <= idx < len(topics):
                return topics[idx]
        except ValueError:
            pass
        print("  Invalid.")

def show_stats(session):
    clr()
    print(f"\n{B}{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{X}")
    print(f"{B}  SESSION RESULTS{X}")
    print(f"{B}{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{X}\n")
    if session.total == 0:
        print("  No questions completed.\n"); return
    pct = round(session.score / session.total * 100)
    col = G if pct >= 70 else Y if pct >= 50 else R
    print(f"  Final: {col}{B}{session.score}/{session.total}  ({pct}%){X}\n")
    if session.topic_stats:
        print(f"  {B}By topic:{X}\n")
        for topic, (correct, attempted) in sorted(
                session.topic_stats.items(),
                key=lambda x: x[1][0]/x[1][1] if x[1][1] > 0 else 0):
            if attempted == 0:
                continue
            tp = round(correct / attempted * 100)
            bar = "█"*(tp//10) + "░"*(10-tp//10)
            tc = G if tp>=70 else Y if tp>=50 else R
            print(f"  {topic:<32} {tc}{bar}  {tp:3}%{X}  {D}({correct}/{attempted}){X}")
    print()
    advice = {
        range(0, 50): f"{R}Review the red topics — revisit the spec and try again.{X}",
        range(50, 70): f"{Y}Good effort — target the topics below 70%.{X}",
        range(70, 101): f"{G}Excellent session! Keep the daily practice going.{X}",
    }
    for r, msg in advice.items():
        if pct in r:
            print(f"  {msg}\n"); break

# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────
def main():
    paper_choice = paper_menu()
    paper_labels = {1:"Paper 1 — Computer Systems", 2:"Paper 2 — Programming", 3:"Mixed Mode"}
    paper_label = paper_labels[paper_choice]
    paper_filter = None if paper_choice == 3 else paper_choice

    # Build index of static questions for chosen paper
    pool_indices = [i for i, q in enumerate(STATIC)
                    if paper_filter is None or q["paper"] == paper_filter]

    clr()
    topic_filter = topic_menu(pool_indices, paper_filter)
    if topic_filter:
        pool_indices = [i for i in pool_indices if STATIC[i]["topic"] == topic_filter]

    session = Session()

    while True:
        clr()
        header(session, paper_label)

        q, idx = pick_question(pool_indices, session, paper_filter, topic_filter)

        if q["type"] == "mc":
            result = ask_mc(q)
        else:
            result = ask_self_mark(q)

        if result == 'quit':
            break

        session.record(q["topic"], result)

        print()
        cmd = input("  Enter=next  T=change topic  P=change paper  Q=quit: ").strip().upper()
        if cmd == 'Q':
            break
        if cmd == 'P':
            paper_choice = paper_menu()
            paper_label = paper_labels[paper_choice]
            paper_filter = None if paper_choice == 3 else paper_choice
            pool_indices = [i for i, q in enumerate(STATIC)
                            if paper_filter is None or q["paper"] == paper_filter]
            clr()
            topic_filter = topic_menu(pool_indices, paper_filter)
            if topic_filter:
                pool_indices = [i for i in pool_indices if STATIC[i]["topic"] == topic_filter]
            session.used_ids.clear()
        if cmd == 'T':
            pool_indices = [i for i, q in enumerate(STATIC)
                            if paper_filter is None or q["paper"] == paper_filter]
            clr()
            topic_filter = topic_menu(pool_indices, paper_filter)
            if topic_filter:
                pool_indices = [i for i in pool_indices if STATIC[i]["topic"] == topic_filter]
            session.used_ids.clear()

    show_stats(session)

if __name__ == "__main__":
    main()
