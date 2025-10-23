import { Button } from "@/components/ui/button";
import heroImage from "@assets/stock_images/diverse_community_gr_f1857826.jpg";

export default function Hero() {
  return (
    <section className="relative min-h-[500px] md:min-h-[600px] overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-r from-background via-background/95 to-background/60 z-10" />
      <img 
        src={heroImage} 
        alt="Comunidad vecinal colaborando" 
        className="absolute inset-0 w-full h-full object-cover"
      />
      
      <div className="relative z-20 container mx-auto px-4 sm:px-6 lg:px-8 h-full min-h-[500px] md:min-h-[600px] flex items-center">
        <div className="max-w-2xl py-12 md:py-20">
          <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight mb-6">
            Gestión Digital para Juntas de Vecinos
          </h1>
          <p className="text-lg md:text-xl text-muted-foreground mb-8 leading-relaxed">
            Moderniza la administración de tu unidad territorial. Gestiona inscripciones, 
            certificados, proyectos comunitarios y más, todo en un solo lugar.
          </p>
          <div className="flex flex-col sm:flex-row gap-4">
            <Button size="lg" className="text-base" data-testid="button-get-started">
              Comenzar Ahora
            </Button>
            <Button size="lg" variant="outline" className="text-base bg-background/80 backdrop-blur" data-testid="button-learn-more">
              Conocer Más
            </Button>
          </div>
        </div>
      </div>
    </section>
  );
}
