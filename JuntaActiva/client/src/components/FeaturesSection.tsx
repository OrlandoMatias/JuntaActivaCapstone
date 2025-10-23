import FeatureCard from "./FeatureCard";
import { FileCheck, Users, Calendar, Megaphone, FolderKanban, Award } from "lucide-react";

export default function FeaturesSection() {
  const features = [
    {
      icon: Users,
      title: "Gestión de Vecinos",
      description: "Inscripción y administración de vecinos con proceso de aprobación digital y notificaciones automáticas."
    },
    {
      icon: FileCheck,
      title: "Certificados de Residencia",
      description: "Solicitud y emisión digital de certificados de residencia con descarga en PDF."
    },
    {
      icon: FolderKanban,
      title: "Proyectos Comunitarios",
      description: "Postulación y gestión de proyectos vecinales con flujo de aprobación transparente."
    },
    {
      icon: Calendar,
      title: "Reserva de Espacios",
      description: "Sistema de calendario para reservar canchas, salas y espacios comunitarios."
    },
    {
      icon: Megaphone,
      title: "Comunicación Efectiva",
      description: "Envío de avisos, notificaciones y noticias a toda la comunidad vía email."
    },
    {
      icon: Award,
      title: "Actividades Vecinales",
      description: "Organización de eventos con inscripción y gestión de cupos automática."
    }
  ];

  return (
    <section className="py-16 md:py-20 bg-muted/30">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-semibold mb-4">
            Todo lo que necesitas
          </h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            Herramientas completas para la gestión moderna de tu junta de vecinos
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((feature, index) => (
            <FeatureCard key={index} {...feature} />
          ))}
        </div>
      </div>
    </section>
  );
}
