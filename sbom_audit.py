import json
import sys

def audit_sbom(file_path):
    print(f"[*] Analyzing Software Bill of Materials: {file_path}")
    
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"[-] Error loading SBOM: {e}")
        return

    artifacts = data.get('artifacts', [])
    print(f"[*] Total artifacts found: {len(artifacts)}")
    
    malicious_found = False
    
    print("\n--- SECURITY REPORT ---")
    
    for item in artifacts:
        name = item.get('name', 'unknown')
        version = item.get('version', '0.0.0')
        purl = item.get('purl', '') # Package URL (откуда скачано)

        # ЛОГИКА ДЕТЕКТИРОВАНИЯ (Наши правила)
        
        # 1. Поиск конкретного пакета с аномальной версией
        if name == 'auth-utils-core':
            if version == '1.1.0' or version.startswith('99.'):
                print(f"[!!!] CRITICAL: Malicious package version detected!")
                print(f"      Package: {name}")
                print(f"      Version: {version}")
                print(f"      Reason: Known IOC for Supply Chain Attack (Dependency Confusion)")
                malicious_found = True

        # 2. Поиск пакетов из недоверенных источников (Localhost/IP)
        # Если в PURL или метаданных есть IP-адрес вместо registry.npmjs.org
        if 'localhost' in str(item) or '192.168.' in str(item):
             print(f"[!] WARNING: Package installed from untrusted registry")
             print(f"      Package: {name} @ {version}")
             print(f"      Source: Local/Private Registry detected")
             malicious_found = True

    if malicious_found:
        print("\n[FAIL] Build rejected. Compromised dependencies detected.")
        sys.exit(1)
    else:
        print("\n[PASS] No known threats detected.")

if __name__ == "__main__":
    audit_sbom("sbom.json")
