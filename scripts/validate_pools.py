#!/usr/bin/env python3
"""
Validate exercise pools have sufficient exercises for assignment logic.

Checks that each pool has at least 2 exercises (minimum needed for 2 rounds).
For production use, you may want at least 5 exercises per pool for variety.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EX_DIR = ROOT / "exercises"


def discover(pool_name: str) -> list[str]:
    """Discover exercises in a pool."""
    pool_dir = EX_DIR / pool_name
    if not pool_dir.exists():
        return []
    # Filter out placeholder directories
    exercises = []
    for p in pool_dir.iterdir():
        if p.is_dir() and p.name != "placeholder":
            # Check if it has required files
            if (p / "task.py").exists() and (p / "tests").exists():
                exercises.append(p.name)
    return sorted(exercises)


def validate_exercise(exercise_path: Path) -> list[str]:
    """Validate an exercise has required structure."""
    errors = []
    if not (exercise_path / "task.py").exists():
        errors.append(f"Missing task.py")
    if not (exercise_path / "tests").exists():
        errors.append(f"Missing tests/ directory")
    else:
        test_files = list((exercise_path / "tests").glob("test_*.py"))
        if not test_files:
            errors.append(f"No test_*.py files in tests/")
    return errors


def main():
    """Validate all exercise pools."""
    pools = ["easy", "medium", "hard"]
    min_required = 2  # Minimum for 2 rounds
    recommended = 5   # Recommended for variety
    
    all_valid = True
    pool_counts = {}
    
    print("Validating exercise pools...")
    print("=" * 60)
    
    for pool_name in pools:
        exercises = discover(pool_name)
        pool_counts[pool_name] = len(exercises)
        
        print(f"\n{pool_name.upper()} pool: {len(exercises)} exercises")
        
        if len(exercises) < min_required:
            print(f"  ❌ ERROR: Need at least {min_required} exercises, found {len(exercises)}")
            all_valid = False
        elif len(exercises) < recommended:
            print(f"  ⚠️  WARNING: Recommended {recommended}+ exercises, found {len(exercises)}")
        else:
            print(f"  ✅ OK: {len(exercises)} exercises")
        
        # Validate each exercise structure
        pool_dir = EX_DIR / pool_name
        for ex_name in exercises:
            ex_path = pool_dir / ex_name
            errors = validate_exercise(ex_path)
            if errors:
                print(f"    ❌ {ex_name}: {', '.join(errors)}")
                all_valid = False
            else:
                test_count = len(list((ex_path / "tests").glob("test_*.py")))
                print(f"    ✅ {ex_name} ({test_count} test file(s))")
    
    print("\n" + "=" * 60)
    
    # Check assignment feasibility
    print("\nAssignment feasibility check:")
    print("-" * 60)
    
    # Experienced: needs 2 medium + 2 hard
    if pool_counts["medium"] >= 2 and pool_counts["hard"] >= 2:
        print("✅ Experienced participants: OK (need 2 medium + 2 hard)")
    else:
        print(f"❌ Experienced participants: Need 2 medium + 2 hard")
        print(f"   Current: {pool_counts['medium']} medium, {pool_counts['hard']} hard")
        all_valid = False
    
    # Inexperienced: needs 2 easy + 2 medium
    if pool_counts["easy"] >= 2 and pool_counts["medium"] >= 2:
        print("✅ Inexperienced participants: OK (need 2 easy + 2 medium)")
    else:
        print(f"❌ Inexperienced participants: Need 2 easy + 2 medium")
        print(f"   Current: {pool_counts['easy']} easy, {pool_counts['medium']} medium")
        all_valid = False
    
    print("\n" + "=" * 60)
    
    if all_valid:
        print("✅ All checks passed! Pools are ready for assignment.")
        return 0
    else:
        print("❌ Validation failed. Please add more exercises or fix issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

