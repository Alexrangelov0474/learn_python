chemical_compounds = set()

for _ in range(int(input())):
    chemical_compounds.update(input().split())
    # for element in elements:
    #     chemical_compounds.add(element)

# for element in chemical_compounds:
#     print(element)
print(*chemical_compounds, sep='\n')
