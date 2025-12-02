import json
import sys

def load_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[-] Error: File {path} not found.")
        sys.exit(1)

def analyze_sbom(sbom_path, policy_path):
    print(f"[*] Loading SBOM: {sbom_path}")
    print(f"[*] Loading Policy: {policy_path}")
    
    sbom = load_json(sbom_path)
    policy = load_json(policy_path)
    
    trusted_registries = policy.get("trusted_registries", [])
    pinned_versions = policy.get("pinned_versions", {})
    
    artifacts = sbom.get('artifacts', [])
    issues = []

    print(f"[*] Scanning {len(artifacts)} artifacts...\n")

    for pkg in artifacts:
        name = pkg.get('name')
        version = pkg.get('version')
        purl = pkg.get('purl', '')
        if name in pinned_versions:
            required_version = pinned_versions[name]
            if version != required_version:
                issues.append({
                    "severity": "CRITICAL",
                    "msg": f"Drift detected for '{name}'! Expected: {required_version}, Found: {version}"
                })
        if purl:
            is_trusted = False
            for reg in trusted_registries:
                if reg in purl:
                    is_trusted = True
                    break
            if not is_trusted:
                if "192.168." in str(pkg) or "localhost" in str(pkg):
                     issues.append({
                        "severity": "HIGH",
                        "msg": f"Untrusted source for '{name}'. Origin seems local/private."
                    })

    if issues:
        print("="*60)
        print(f"SECURITY VIOLATION REPORT ({len(issues)} issues)")
        print("="*60)
        for i in issues:
            print(f"[{i['severity']}] {i['msg']}")
        sys.exit(1)
    else:
        print("[OK] All checks passed.")

if __name__ == "__main__":
    analyze_sbom("sbom.json", "security-policy.json")
