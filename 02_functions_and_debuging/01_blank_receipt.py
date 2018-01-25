def print_headar():
    print('CASH RECEIPT')
    print('------------------------------')


def print_body():
    print('Charged to____________________')
    print('Received by___________________')


def print_footer():
    print('------------------------------')
    print('\u00A9 SoftUni')


def print_receipt():
    print_headar()
    print_body()
    print_footer()

print_receipt()