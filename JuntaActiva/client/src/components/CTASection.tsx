import { Button } from "@/components/ui/button";

export default function CTASection() {
  return (
    <section className="py-16 md:py-20">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="max-w-3xl mx-auto text-center">
          <h2 className="text-3xl md:text-4xl font-semibold mb-4">
            ¿Listo para modernizar tu junta de vecinos?
          </h2>
          <p className="text-lg text-muted-foreground mb-8">
            Únete a las comunidades que ya están mejorando su gestión territorial con nuestra plataforma digital.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button size="lg" data-testid="button-cta-register">
              Registrar mi Junta
            </Button>
            <Button size="lg" variant="outline" data-testid="button-cta-demo">
              Solicitar Demo
            </Button>
          </div>
        </div>
      </div>
    </section>
  );
}
