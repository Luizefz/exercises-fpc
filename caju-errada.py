def do_harvest(plant_area, rows_harvest, cols_harvest):
    plant_cut = []

    for i in range(len(plant_area)):
        for j in range(len(plant_area[0])):
            holver = []
            for row_slice in plant_area[i:i + rows_harvest]:
                col_slice = row_slice[j:j + cols_harvest]
                holver.extend(col_slice)
            plant_cut.append(holver)
            holver = []

    return plant_cut
    
rows_plant, cols_plant, rows_harvest, cols_harvest = map(int, input().split())
plant_area = [[int(i) for i in input().split()] for _ in range(rows_plant)]

plant_cut = do_harvest(plant_area, rows_harvest, cols_harvest)
print(plant_cut)

bigger_sum = 0

for i in plant_cut:
    if sum(i) > bigger_sum:
        bigger_sum = sum(i)
print(bigger_sum)