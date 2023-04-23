
from django.contrib import admin
from django.urls import path,include
from apple import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__reload__',include('django_browser_reload.urls')),
    path('',views.SignUpPage,name='signup'),
    path('home/results/',views.ResultsPage,name='results'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('classified2/',views.classified2,name='classified2'),
    path('classifiedmul/',views.classifiedmul,name='classifiedmul'),
    path('correlation2/',views.correlation2,name='correlation2'),
    path('correlationmul/',views.correlationmul,name='correlationmul'),
    path('dt/',views.dt,name='dt'),
    path('knn/',views.knn,name='knn'),
    path('lg/',views.lg,name='lg'),
    path('lrg/',views.lrg,name='lrg'),
    path('lsvm/',views.lsvm,name='lsvm'),
    path('rf/',views.rf,name='rf'),
    path('dtm/',views.dtm,name='dtm'),
    path('knnm/',views.knnm,name='knnm'),
    path('lgm/',views.lgm,name='lgm'),
    path('lrgm/',views.lrgm,name='lrgm'),
    path('lsvmm/',views.lsvmm,name='lsvmm'),
    path('rfm/',views.rfm,name='rfm'),
    path('dtr/',views.dtr,name='dtr'),
    path('knnr/',views.knnr,name='knnr'),
    path('lgr/',views.lgr,name='lgr'),
    path('lrgr/',views.lrgr,name='lrgr'),
    path('lsvmr/',views.lsvmr,name='lsvmr'),
    path('rfr/',views.rfr,name='rfr'),

]
