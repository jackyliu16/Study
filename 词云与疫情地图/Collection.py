import json
import Jan
# import Feb
# import Mar
# import Apr
# import May
# import Jun
# import Jul
# import Aug
# import Sep
# import Oct
# import Nov
# import Dec
import importlib

month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
with open("Data.json", "w") as File:
    total_data = []
    for mon in month:
        DataForMonth = {
            "time": mon,
            "Data": importlib.import_module(mon).Province_Confirmed
        }
        print(importlib.import_module(mon).Province_Confirmed)
        total_data.append(DataForMonth)

    File.write(json.dumps(total_data))
