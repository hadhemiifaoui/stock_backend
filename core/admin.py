from django.contrib import admin
from .models.role import Role
from .models.user import  User
from .models.category import Category
from .models.article import Article
from .models.repport import Report
from .models.stock import Stock
from .models.supplier import Supplier
from .models.planning import Planning
from .models.manifacturation import Manifacturation
from .models.transaction import Transaction
from .models.inventory import Inventory
from .models.setting import Setting
#from .models.stock_history import StockHistory
from .models.order import Order
#from .models.carteAccep import CarteAcceptation
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.forms import UserCreationForm, UserChangeForm

class CustomUserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = ('user_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'role')
    search_fields = ('user_name',)
    ordering = ('user_name',)
    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (None, {'fields': ('user_name', 'password')}),
        ('Profile', {'fields': ('profile_pic', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_name', 'password1', 'password2', 'role', 'profile_pic', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(User, CustomUserAdmin)

#admin.site.register(User)
admin.site.register(Role)

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Report)
admin.site.register(Stock)
admin.site.register(Supplier)
admin.site.register(Planning)
admin.site.register(Manifacturation)
admin.site.register(Transaction)
admin.site.register(Inventory)
admin.site.register(Setting)
#admin.site.regis