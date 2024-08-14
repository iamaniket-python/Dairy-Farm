from . import views
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from . forms import LoginForm, MyPasswordChangeFrom, MyPasswordResetForm, MysetPasswordForm
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('',views.Home,name="Home"),
   
    path("about/",views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('category/<slug:val>',views.Categoryview.as_view(),name="category"),
    path('category-title/<val>',views.CategoryTitle.as_view(),name="category-title"),
    path('product-detail/<int:pk>',views.ProductDetail.as_view(),name="product-detail"),
    path('registration/',views. CutomerRegistrationView.as_view(),name="customerregistration"),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='main/login.html',authentication_form=LoginForm),name='login'),
   
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(), name="updateAddress"),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),

    path('add-to-cart/',views.add_to_cart, name="add-to-cart"),
    path('cart/',views.show_cart, name="showcart"),
    path('checkout/',views.show_cart, name="checkout"),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    path('paymentdone/',views.payment_done, name="paymentdone"),
    path('orders/', views.orders, name='orders'),


    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='main/password_reset.html',form_class=MyPasswordResetForm),name="password_reset"),
 
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='main/changepassword.html',form_class=MyPasswordChangeFrom,success_url='/passwordchangedone'),name="passwordchange"),

    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='main/passwordchangedone.html'),name="passwordchangedone"),

    path ('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'), name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='main/password_reset_confirm.html',form_class=MysetPasswordForm),name='password_reset_confirm'),

    path('password-reser-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'), name='password_reset_complete')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
