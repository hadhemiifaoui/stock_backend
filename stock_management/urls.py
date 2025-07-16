from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categories/' , include('core.urls.categories')),
    path('api/users/', include('core.urls.user')),
    path('api/roles/', include('core.urls.role')),
    path('api/suppliers/' , include('core.urls.suppliers')),
    path('api/articles/', include('core.urls.articles')),
    path('api/stock/', include('core.urls.stock')),
    path('api/inventories/', include('core.urls.inventory')),
    path('api/transactions/', include('core.urls.transaction')),
    path('api/manifacturations/', include('core.urls.manifacturation')),
    path('api/planning/', include('core.urls.planning')),
    path('api/settings/', include('core.urls.setting')),
    path('api/reports/', include('core.urls.report')),
    path('api/stockhistory/' , include('core.urls.stock_history')),
    path('api/tests/', include('core.urls.test')),
    path('api/orders/', include('core.urls.order')),
    path('api/maintenances/', include('core.urls.maintenance')),
    path('api/curatives/', include('core.urls.curative')),
    path('api/preventives/', include('core.urls.preventive')),
    path('api/chefequipes/', include('core.urls.ChefEquipe')),

    # path('api/outillage/references', include('core.urls.outillage')),
    # path('api/outillage/tools', include('core.urls.outillage')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('core.urls.ml_predict')),
    path('api/', include('core.urls.ml_predict1')),
    path('api/', include('core.urls.ml_predict2')),
    path('api/projects/', include('core.urls.project')),
    path('api/references/', include('core.urls.reference')),
    #path('api/carte/', include('core.urls.carteAcc')),


    #path of carte acceptance

    path('api/carte/', include('core.urls.carteAcceptanceUrls.acceptcarte')),
   #path('api/carte/ordercarteaccep/', include('core.urls.carteAcceptanceUrls.ordercarteaccepturl')),
    path('api/carte/validationframechefoutilage/', include('core.urls.carteAcceptanceUrls.validationframechefoutillageurl')),
    path('api/carte/validationframeingqual/', include('core.urls.carteAcceptanceUrls.validationframeingqualityurl')),
    path('api/carte/validationframeserviceoutillage/', include('core.urls.carteAcceptanceUrls.validationframeserviceoutiurl')),
    path('api/carte/validationoutillageingquality/', include('core.urls.carteAcceptanceUrls.validationoutillageingqualityurl')),
    path('api/carte/validationoutillageserviceoutillage/', include('core.urls.carteAcceptanceUrls.validationoutillageservoutiurl')),


    path('api/newoutillage/', include('core.urls.newoutillage')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)