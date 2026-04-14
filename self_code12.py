pc_builds=[
    {"name":"my pc","gpu":"rtx 5060ti"},
    {"name":"my friends pc","gpu":"rtx 3060"}
]
for i in range(len(pc_builds)):
    print(f"{pc_builds[i]["name"]} uses {pc_builds[i]["gpu"]}")