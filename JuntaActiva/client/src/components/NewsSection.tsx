import NewsCard from "./NewsCard";
import { Button } from "@/components/ui/button";

export default function NewsSection() {
  // TODO: remove mock functionality
  const news = [
    {
      title: "Nueva Plaza Comunitaria Inaugurada",
      excerpt: "Este fin de semana se inauguró la nueva plaza comunitaria resultado del proyecto vecinal aprobado el mes pasado.",
      category: "Proyectos",
      date: "15 Ene 2025"
    },
    {
      title: "Jornada de Limpieza del Barrio",
      excerpt: "Invitamos a todos los vecinos a participar en la jornada de limpieza este sábado a las 9:00 AM.",
      category: "Actividades",
      date: "12 Ene 2025"
    },
    {
      title: "Nuevo Horario de Atención",
      excerpt: "Informamos que el horario de atención de la sede vecinal ha sido modificado para mejor servicio a la comunidad.",
      category: "Avisos",
      date: "10 Ene 2025"
    }
  ];

  return (
    <section className="py-16 md:py-20 bg-muted/30">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-semibold mb-4">
            Últimas Noticias
          </h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            Mantente informado sobre las novedades de tu comunidad
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          {news.map((item, index) => (
            <NewsCard key={index} {...item} />
          ))}
        </div>

        <div className="text-center">
          <Button variant="outline" size="lg" data-testid="button-view-all-news">
            Ver Todas las Noticias
          </Button>
        </div>
      </div>
    </section>
  );
}
