"""
Install shared packages before audience job runs.
Called as first task in every audience Databricks job.
"""
import subprocess
import sys


def install(audience: str):
    print(f"Installing shared packages for {audience}...")

    packages = [
        "shared/insights_framework",
        "shared/insights_drift",
    ]

    for pkg in packages:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-e", pkg, "--quiet"],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"ERROR installing {pkg}: {result.stderr}")
            sys.exit(1)
        print(f"  ✓ {pkg} installed")

    print(f"All packages installed for {audience}")


if __name__ == "__main__":
    audience = sys.argv[1] if len(sys.argv) > 1 else "unknown"
    install(audience)
