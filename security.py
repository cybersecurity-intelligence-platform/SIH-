# =========================================
# CRIMINAL INTELLIGENCE - SECURITY MODULE
# =========================================

from cryptography.fernet import Fernet
import hashlib
from datetime import datetime


# =========================================
# 1. RBAC - ROLE BASED ACCESS CONTROL
# =========================================

ROLES = {
    "Admin": ["view", "add", "update", "delete"],
    "Investigator": ["view", "add", "update"],
    "Viewer": ["view"]
}


def check_access(role, action):
    if role not in ROLES:
        return False

    return action in ROLES[role]


print("\n=== RBAC ===")

roles_to_test = [
    ("Admin", "delete"),
    ("Investigator", "update"),
    ("Viewer", "delete")
]

for role, action in roles_to_test:
    if check_access(role, action):
        print(f"{role}: {action} -> ACCESS GRANTED")
    else:
        print(f"{role}: {action} -> ACCESS DENIED")


# =========================================
# 2. ENCRYPTION - SENSITIVE DATA PROTECTION
# =========================================

print("\n=== ENCRYPTION ===")

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

sensitive_data = "Confidential Criminal Investigation Data"

# Encrypt
encrypted_data = cipher.encrypt(sensitive_data.encode())

print("Original Data :", sensitive_data)
print("Encrypted Data:", encrypted_data.decode())

# Decrypt
decrypted_data = cipher.decrypt(encrypted_data).decode()

print("Decrypted Data:", decrypted_data)


# =========================================
# 3. AUDIT LOG
# =========================================

print("\n=== AUDIT LOG ===")

audit_logs = []


def add_audit_log(user, action, resource):
    log = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user": user,
        "action": action,
        "resource": resource
    }

    audit_logs.append(log)


add_audit_log("Admin", "UPDATE", "Case C001")
add_audit_log("Investigator", "VIEW", "Evidence E001")
add_audit_log("Viewer", "VIEW", "Case C002")

for log in audit_logs:
    print(log)


# =========================================
# 4. EVIDENCE INTEGRITY - HASHING
# =========================================

print("\n=== EVIDENCE INTEGRITY ===")

evidence = "Fingerprint Evidence E001"

# Create SHA-256 hash
original_hash = hashlib.sha256(
    evidence.encode()
).hexdigest()

print("Evidence:", evidence)
print("Original Hash:", original_hash)

# Verify unchanged evidence
current_hash = hashlib.sha256(
    evidence.encode()
).hexdigest()

if original_hash == current_hash:
    print("Evidence Status: INTEGRITY VERIFIED")
else:
    print("Evidence Status: EVIDENCE MODIFIED")


# =========================================
# FINAL STATUS
# =========================================

print("\n=========================================")
print("SECURITY MODULE COMPLETED")
print("=========================================")