from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),
    
    # Autenticación
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Recuperación de contraseña
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='gestion/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='gestion/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='gestion/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='gestion/password_reset_complete.html'), name='password_reset_complete'),
    
    # URLs públicas - Vecinos
    path('vecinos/registrar/', views.registrar_vecino, name='registrar_vecino'),
    
    # URLs administrativas - Vecinos
    path('vecinos/', views.lista_vecinos, name='lista_vecinos'),
    path('vecinos/cambiar-miembro/<int:id>/', views.cambiar_estado_miembro, name='cambiar_estado_miembro'),
    
    # URLs públicas - Certificados
    path('certificados/solicitar/', views.solicitar_certificado, name='solicitar_certificado'),
    
    # URLs administrativas - Certificados
    path('certificados/', views.listar_certificados, name='listar_certificados'),
    path('certificados/aprobar/<int:id>/', views.aprobar_certificado, name='aprobar_certificado'),
    path('certificados/rechazar/<int:id>/', views.rechazar_certificado, name='rechazar_certificado'),
    path('certificados/descargar/<int:id>/', views.descargar_certificado_pdf, name='descargar_certificado_pdf'),
    
    # URLs públicas - Proyectos
    path('proyectos/postular/', views.postular_proyecto, name='postular_proyecto'),
    
    # URLs administrativas - Proyectos
    path('proyectos/', views.listar_proyectos, name='listar_proyectos'),
    path('proyectos/cambiar-estado/<int:id>/', views.cambiar_estado_proyecto, name='cambiar_estado_proyecto'),
    
    # URLs públicas - Actividades
    path('actividades/', views.listar_actividades, name='listar_actividades'),
    path('actividades/inscribirse/<int:id>/', views.inscribirse_actividad, name='inscribirse_actividad'),
    path('actividades/desinscribirse/<int:id>/', views.desinscribirse_actividad, name='desinscribirse_actividad'),
    
    # URLs públicas - Noticias
    path('noticias/', views.listar_noticias, name='listar_noticias'),
    
    # URLs administrativas - Noticias
    path('noticias/crear/', views.crear_noticia, name='crear_noticia'),
    
    # URLs públicas - Reservas de Espacios
    path('reservas/espacios/', views.listar_espacios, name='listar_espacios'),
    path('reservas/solicitar/', views.solicitar_reserva, name='solicitar_reserva'),
    path('reservas/mis-reservas/', views.mis_reservas, name='mis_reservas'),
    path('reservas/cancelar/<int:id>/', views.cancelar_reserva, name='cancelar_reserva'),
    path('reservas/calendario/', views.calendario_reservas, name='calendario_reservas'),
    
    # URLs administrativas - Reservas de Espacios
    path('reservas/gestionar/', views.gestionar_reservas, name='gestionar_reservas'),
    path('reservas/aprobar/<int:id>/', views.aprobar_reserva, name='aprobar_reserva'),
    path('reservas/rechazar/<int:id>/', views.rechazar_reserva, name='rechazar_reserva'),
]
