from src.gcp.VisWax import VisWax


v = VisWax()
viswax_combo_result = v.get_viswax_combo(True)

if "error" not in viswax_combo_result:
    print(viswax_combo_result)
else:
    print("There was an error fetching the viswax details..")


