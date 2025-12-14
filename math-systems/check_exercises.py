import re

# Read the file
with open('MATHSYS_oefeningen.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all exercises (subsection or subsubsection with "Oefening")
exercises = re.findall(r'\\(?:sub)*section\*?\{[^}]*Oefening\s+([\d.]+):', content)

# Find all solutions (subsubsection with "Oplossing")
solutions = re.findall(r'\\subsubsection\*?\{[^}]*Oplossing\s+([\d.]+):', content)

print("=" * 60)
print(f"Total Exercises Found: {len(exercises)}")
print(f"Total Solutions Found: {len(solutions)}")
print("=" * 60)

# Convert to sets for comparison
exercise_set = set(exercises)
solution_set = set(solutions)

print("\nExercises without solutions:")
missing_solutions = exercise_set - solution_set
if missing_solutions:
    for ex in sorted(missing_solutions, key=lambda x: [int(n) for n in x.split('.')]):
        print(f"  - Oefening {ex}")
else:
    print("  OK - All exercises have solutions!")

print("\nSolutions without corresponding exercises:")
orphan_solutions = solution_set - exercise_set
if orphan_solutions:
    for sol in sorted(orphan_solutions, key=lambda x: [int(n) for n in x.split('.')]):
        print(f"  - Oplossing {sol}")
else:
    print("  OK - All solutions match exercises!")

print("\n" + "=" * 60)
print("Exercise List:")
for ex in sorted(exercise_set, key=lambda x: [int(n) for n in x.split('.')]):
    has_sol = "HAS" if ex in solution_set else "NO"
    print(f"  {has_sol} Oefening {ex}")
