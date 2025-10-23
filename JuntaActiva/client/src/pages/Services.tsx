import Header from "@/components/Header";
import Footer from "@/components/Footer";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { FileCheck, Users, Calendar, Megaphone, FolderKanban, Award, ChevronRight } from "lucide-react";

export default function Services() {
  const services = [
    {
      icon: Users,
      title: "Inscripción de Vecinos",
      description: "Registra tu solicitud para formar parte de la junta de vecinos. El directorio revisará y aprobará tu inscripción.",
      features: ["Proceso digital completo", "Notificación por email", "Aprobación del directorio"]
    },
    {
      icon: FileCheck,
      title: "Certificados de Residencia",
      description: "Solicita tu certificado de residencia y descárgalo en formato PDF una vez aprobado por el directorio.",
      features: ["Solicitud en línea", "Descarga en PDF", "Validación oficial"]
    },
    {
      icon: FolderKanban,
      title: "Proyectos Comunitarios",
      description: "Propone proyectos para mejorar tu barrio. Solo miembros activos pueden postular proyectos vecinales.",
      features: ["Postulación digital", "Seguimiento de estado", "Aprobación transparente"]
    },
    {
      icon: Calendar,
      title: "Reserva de Espacios",
      description: "Reserva canchas, salas y espacios comunitarios a través de nuestro calendario integrado.",
      features: ["Calendario en tiempo real", "Gestión de disponibilidad", "Confirmación automática"]
    },
    {
      icon: Megaphone,
      title: "Avisos y Notificaciones",
      description: "Recibe comunicados importantes de la junta de vecinos directamente en tu email.",
      features: ["Avisos tipo afiche", "Notificaciones por email", "Historial de comunicados"]
    },
    {
      icon: Award,
      title: "Actividades Vecinales",
      description: "Inscríbete en actividades y eventos comunitarios con gestión automática de cupos.",
      features: ["Inscripción online", "Control de cupos", "Recordatorios automáticos"]
    }
  ];

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-1">
        <section className="py-12 md:py-16 bg-muted/30">
          <div className="container mx-auto px-4 sm:px-6 lg:px-8">
            <div className="max-w-3xl">
              <h1 className="text-4xl md:text-5xl font-bold mb-4">
                Servicios Disponibles
              </h1>
              <p className="text-lg text-muted-foreground">
                Descubre todos los servicios que ofrecemos para mejorar la gestión de tu unidad territorial
              </p>
            </div>
          </div>
        </section>

        <section className="py-12 md:py-16">
          <div className="container mx-auto px-4 sm:px-6 lg:px-8">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              {services.map((service, index) => (
                <Card key={index} className="hover-elevate active-elevate-2 transition-all" data-testid={`card-service-${index}`}>
                  <CardHeader>
                    <div className="w-12 h-12 rounded-md bg-primary/10 flex items-center justify-center mb-4">
                      <service.icon className="h-6 w-6 text-primary" />
                    </div>
                    <CardTitle className="text-2xl">{service.title}</CardTitle>
                    <CardDescription className="text-base">
                      {service.description}
                    </CardDescription>
                  </CardHeader>
                  <CardContent className="space-y-4">
                    <ul className="space-y-2">
                      {service.features.map((feature, idx) => (
                        <li key={idx} className="flex items-center gap-2 text-sm text-muted-foreground">
                          <ChevronRight className="h-4 w-4 text-primary" />
                          {feature}
                        </li>
                      ))}
                    </ul>
                    <Button className="w-full" data-testid={`button-service-${index}`}>
                      Acceder al Servicio
                    </Button>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </section>

        <section className="py-12 md:py-16 bg-muted/30">
          <div className="container mx-auto px-4 sm:px-6 lg:px-8">
            <div className="max-w-3xl mx-auto text-center">
              <h2 className="text-3xl md:text-4xl font-semibold mb-4">
                ¿Necesitas ayuda?
              </h2>
              <p className="text-lg text-muted-foreground mb-8">
                Nuestro equipo está disponible para asistirte con cualquier consulta sobre nuestros servicios.
              </p>
              <Button size="lg" variant="outline" data-testid="button-contact-support">
                Contactar Soporte
              </Button>
            </div>
          </div>
        </section>
      </main>
      <Footer />
    </div>
  );
}
