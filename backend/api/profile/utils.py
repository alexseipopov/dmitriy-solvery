def prepare_data(request):
    var = ["name", "description", "price"]
    data = {}
    for label in var:
        if request.form.get(label):
            data.setdefault(label, request.form.get(label))
    return data
