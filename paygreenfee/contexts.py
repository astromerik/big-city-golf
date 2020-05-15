

def greenfee_contents(request):

    greenfee_items = []
    total = 0
    greenfee_count = 0

    context = {
        'greenfee_items': greenfee_items,
        'total': total,
        'greenfee_count': greenfee_count,
    }

    return context
