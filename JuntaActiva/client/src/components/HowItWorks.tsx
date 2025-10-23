import { CheckCircle2 } from "lucide-react";

export default function HowItWorks() {
  const steps = [
    {
      title: "Registro",
      description: "Los vecinos se registran en la plataforma y solicitan su inscripción en la junta."
    },
    {
      title: "Aprobación",
      description: "El directorio revisa y aprueba las solicitudes desde el panel administrativo."
    },
    {
      title: "Acceso",
      description: "Una vez aprobados, los vecinos acceden a todos los servicios disponibles."
    },
    {
      title: "Gestión",
      description: "Solicitan certificados, proponen proyectos, reservan espacios y participan en actividades."
    }
  ];

  return (
    <section className="py-16 md:py-20">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-semibold mb-4">
            ¿Cómo funciona?
          </h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            Proceso simple y transparente para toda la comunidad
          </p>
        </div>

        <div className="max-w-4xl mx-auto">
          <div className="relative">
            <div className="absolute left-4 md:left-1/2 top-0 bottom-0 w-0.5 bg-primary/20 md:-ml-px" />
            
            {steps.map((step, index) => (
              <div key={index} className="relative mb-12 last:mb-0">
                <div className="flex items-start gap-6 md:gap-8">
                  <div className="relative z-10 flex-shrink-0">
                    <div className="w-8 h-8 rounded-full bg-primary flex items-center justify-center">
                      <CheckCircle2 className="h-5 w-5 text-primary-foreground" />
                    </div>
                  </div>
                  <div className="flex-1 md:w-1/2 pb-8">
                    <h3 className="text-xl font-semibold mb-2" data-testid={`step-title-${index}`}>
                      {index + 1}. {step.title}
                    </h3>
                    <p className="text-muted-foreground leading-relaxed" data-testid={`step-description-${index}`}>
                      {step.description}
                    </p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
