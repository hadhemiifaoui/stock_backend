from ..models.stock import Stock
from ..models.stock_history import StockHistory
from datetime import date, timedelta


def get_current_week_code():
    today = date.today()
    year, week_num, _ = today.isocalendar()
    return f"{year}-W{week_num}"

#
# def update_stock_quantity(stock_id, quantity_added=0, quantity_removed=0,
#                           quantity_produced=0, quantite_consume=0 , quantity_transacted=0, quantity_cmd=0):
#
#     stock = Stock.objects.get(id=stock_id)
#
#     quantity_start = stock.virtual_stock
#
#     if quantity_added:
#         stock.quantity += quantity_added
#     if quantity_removed:
#         stock.quantity -= quantity_removed
#     if quantity_produced:
#         stock.virtual_stock -= quantity_produced
#     if quantite_consume:
#         stock.virtual_stock -= quantite_consume
#     if quantity_transacted:
#         stock.virtual_stock -= quantity_transacted
#
#     if quantity_cmd:
#         stock.virtual_stock += quantity_cmd
#
#     stock.total_quantity_used += (
#             quantity_removed + quantity_produced + quantite_consume + quantity_transacted
#     )
#     stock.save()
#
#     week_code = get_current_week_code()
#
#     StockHistory.objects.create(
#         stock=stock,
#         week=week_code,
#         starting_quantity=quantity_start,
#         recieved_commands=quantity_cmd,
#         totale_quatity_used=quantity_removed + quantity_produced + quantite_consume + quantity_transacted,
#         ending_quantity=stock.quantity,
#         virtual_stock=stock.virtual_stock,
#         ecart_stock=stock.ecart_stock
#     )


def update_stock_quantity(stock_id, quantity_added=0, quantity_removed=0,
                          quantity_produced=0, quantite_consume=0,
                          quantity_transacted=0, quantity_cmd=0):

    stock = Stock.objects.get(id=stock_id)

    quantity_start = stock.virtual_stock

    if quantity_added:
        stock.quantity += quantity_added
    if quantity_removed:
        stock.quantity -= quantity_removed
    if quantity_produced:
        stock.virtual_stock -= quantity_produced
    if quantite_consume:
        stock.virtual_stock -= quantite_consume
    if quantity_transacted:
        stock.virtual_stock -= quantity_transacted

    if quantity_cmd:
        stock.virtual_stock += quantity_cmd
        stock.received_commands += quantity_cmd

    stock.total_quantity_used += (
        quantity_removed + quantity_produced + quantite_consume + quantity_transacted
    )

    stock.save()

    week_code = get_current_week_code()

    StockHistory.objects.create(
        stock=stock,
        week=week_code,
        starting_quantity=quantity_start,
        recieved_commands=quantity_cmd,
        totale_quatity_used=quantity_removed + quantity_produced + quantite_consume + quantity_transacted,
        ending_quantity=stock.quantity,
        virtual_stock=stock.virtual_stock,
        ecart_stock=stock.ecart_stock
    )


def get_previous_week_code():
    today = date.today()
    last_week_date = today - timedelta(weeks=1)
    year, week_num, _ = last_week_date.isocalendar()
    return f"{year}-W{week_num}"


def calculate_virtual_stock(stock_id):
    try:
        stock = Stock.objects.get(id=stock_id)
        last_week_code = get_previous_week_code()
        last_week_history = StockHistory.objects.filter(
            stock=stock,
            week=last_week_code
        ).first()

        if last_week_history:
            virtual_stock = (
                last_week_history.starting_quantity + last_week_history.recieved_commands - last_week_history.totale_quatity_used
            )
            stock.virtual_stock = virtual_stock
            stock.save()
            return virtual_stock
        else:
            print("auccune historique pour la semaine dernière")
            return None

    except Stock.DoesNotExist:
        print("Stock n'est pas trouvé")
        return None




















#
# from ..models.stock import Stock
# from ..models.stock_history import StockHistory
# from datetime import date, timedelta
#
#
# def get_current_week_code():
#     today = date.today()
#     year, week_num, _ = today.isocalendar()
#     return f"{year}-W{week_num}"
#
#
# def update_stock_quantity(stock_id, quantity_added=0, quantity_removed=0,
#                           quantity_produced=0, quantite_consume=0 , quantity_transacted=0, quantity_cmd=0):
#
#     stock = Stock.objects.get(id=stock_id)
#
#     quantity_start = stock.quantity
#
#     if quantity_added:
#         stock.quantity += quantity_added
#     if quantity_removed:
#         stock.quantity -= quantity_removed
#     if quantity_produced:
#         stock.quantity -= quantity_produced
#     if quantite_consume:
#         stock.quantity -= quantite_consume
#     if quantity_transacted:
#         stock.quantity -= quantity_transacted
#     if quantity_cmd:
#             stock.quantity += quantity_cmd
#
#     stock.total_quantity_used += (
#             quantity_removed + quantity_produced + quantite_consume + quantity_transacted
#     )
#     stock.save()
#
#     week_code = get_current_week_code()
#
#     StockHistory.objects.create(
#         stock=stock,
#         week=week_code,
#         starting_quantity=quantity_start,
#         recieved_commands=quantity_added,
#         totale_quatity_used=quantity_removed + quantity_produced + quantite_consume + quantity_transacted,
#         ending_quantity=stock.quantity,
#         virtual_stock=stock.virtual_stock,
#         ecart_stock=stock.ecart_stock
#     )
#
# def get_previous_week_code():
#     today = date.today()
#     last_week_date = today - timedelta(weeks=1)
#     year, week_num, _ = last_week_date.isocalendar()
#     return f"{year}-W{week_num}"
#
#
# def calculate_virtual_stock(stock_id):
#     try:
#         stock = Stock.objects.get(id=stock_id)
#         last_week_code = get_previous_week_code()
#         last_week_history = StockHistory.objects.filter(
#             stock=stock,
#             week=last_week_code
#         ).first()
#
#         if last_week_history:
#             virtual_stock = (
#                 last_week_history.starting_quantity + last_week_history.recieved_commands - last_week_history.totale_quatity_used
#             )
#             stock.virtual_stock = virtual_stock
#             stock.save()
#             return virtual_stock
#         else:
#             print("auccune historique pour la semaine dernière")
#             return None
#
#     except Stock.DoesNotExist:
#         print("Stock n'est pas trouvé")
#         return None