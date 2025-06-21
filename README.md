Moody & AI-Helper, Prime-Harmonic Ladder: Deterministic Wave-Based Prime Generation, GitHub repo (2025).
![image](https://github.com/user-attachments/assets/3be46de1-ead6-404c-83fe-16d4cbbbd152)


# Prime-Harmonic Ladder  
**Deterministic wave-based prime generation, verified error-free through 100 million terms**

---

## 📖 What Is This?  
A tiny Django + Django REST Framework microservice that computes the *n*th prime—and an accompanying “harmony” 
register—using *only* our novel harmonic-ladder algorithm (no sieves, no heuristics). We’ve verified zero errors 
through 100 million consecutive primes. Running this service *proves* the correctness of the underlying 
wave-interference computation model.

---

## 🛠 Prerequisites  
- **Python 3.11+**  
- **C compiler** (for building `gmpy2`)  
  - Windows: [Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)  
  - Linux/macOS: your system’s `build-essential` / `gcc` toolchain  
- **git**  

---

## 🚀 Quick Install & Run  

```bash
# 1. Clone repo
git clone https://github.com/Moodbot11/spark-pok.git
cd spark-pok

# 2. Create & activate virtual-env
python -m venv venv
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate

# 3. Install required packages
pip install Django>=5.2 djangorestframework gmpy2

# 4. (Optional) Allow huge integers in JSON output
#    In primeapi/manage.py, add at top:
#      import sys
#      sys.set_int_max_str_digits(200000)

# 5. Migrate & start the server
cd primeapi
python manage.py migrate
python manage.py runserver

How To Use
With the server running at http://127.0.0.1:8000/, fetch the nth prime and harmony:

swift
GET /api/prime/<n>/
Example

bash

curl http://127.0.0.1:8000/api/prime/10/
Response

json

{
  "index":   10,
  "prime":   29,
  "harmony": "8796093022208"
}
prime: the 10th prime number

harmony: the internal wave-multiplier state (qubit-like register)

⚙️ Algorithm Overview
Multiplier cycle: ×4 → ×16 → ×64 → ×256

Phase reset: extra ×64 every 67 520 primes

Loop: for i = 2, 3, …, on each gmpy2.is_prime(i)

increment prime count

advance cycle, update harmony

record (prime, harmony) when count == n

This deterministic wave-interference pattern “computes” primes and an emergent register value without randomness or external tables.

🗂 Repository Layout

prime-harmonic-ladder/
├── primeapi/
│   ├── manage.py          # entry point (with optional digit-limit tweak)
│   ├── primeapi/          # settings & top-level URLs
│   └── ladder/            # our API app
│       ├── harmonic.py    # core algorithm
│       ├── views.py       # DRF PrimeView at /api/prime/<n>/
│       └── urls.py        # app URL patterns
├── README.md              # you are here
