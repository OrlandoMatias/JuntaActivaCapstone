import Header from "@/components/Header";
import Footer from "@/components/Footer";
import NewsCard from "@/components/NewsCard";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Search } from "lucide-react";
import { useState } from "react";

export default function News() {
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("Todos");

  // TODO: remove mock functionality
  const categories = ["Todos", "Proyectos", "Actividades", "Avisos", "Comunicados"];
  
  const newsItems = [
    {
      title: "Nueva Plaza Comunitaria Inaugurada",
      excerpt: "Este fin de semana se inauguró la nueva plaza comunitaria resultado del proyecto vecinal aprobado el mes pasado. La comunidad se reunió para celebrar este logro conjunto.",
      category: "Proyectos",
      date: "15 Ene 2025"
    },
    {
      title: "Jornada de Limpieza del Barrio",
      excerpt: "Invitamos a todos los vecinos a participar en la jornada de limpieza este sábado a las 9:00 AM. Punto de encuentro: Plaza Principal.",
      category: "Actividades",
      date: "12 Ene 2025"
    },
    {
      title: "Nuevo Horario de Atención",
      excerpt: "Informamos que el horario de atención de la sede vecinal ha sido modificado para mejor servicio a la comunidad. Ahora: Lunes a Viernes 9:00 - 18:00.",
      category: "Avisos",
      date: "10 Ene 2025"
    },
    {
      title: "Aprobación de Proyecto de Seguridad",
      excerpt: "El directorio aprobó el proyecto de mejora de iluminación pública en el sector norte. Inicio de obras programado para febrero.",
      category: "Proyectos",
      date: "8 Ene 2025"
    },
    {
      title: "Taller de Reciclaje para Vecinos",
      excerpt: "Este jueves se realizará un taller gratuito de reciclaje y compostaje. Inscripciones abiertas hasta el miércoles.",
      category: "Actividades",
      date: "5 Ene 2025"
    },
    {
      title: "Corte de Agua Programado",
      excerpt: "Se informa corte de suministro de agua el próximo martes de 8:00 a 14:00 hrs por mantención de red.",
      category: "Avisos",
      date: "3 Ene 2025"
    }
  ];

  const filteredNews = newsItems.filter(item => {
    const matchesCategory = selectedCategory === "Todos" || item.category === selectedCategory;
    const matchesSearch = item.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         item.excerpt.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-1">
        <section className="py-12 md:py-16 bg-muted/30">
          <div className="container mx-auto px-4 sm:px-6 lg:px-8">
            <div className="max-w-3xl">
              <h1 className="text-4xl md:text-5xl font-bold mb-4">
                Noticias y Comunicados
              </h1>
              <p className="text-lg text-muted-foreground">
                Mantente informado sobre todas las novedades de tu comunidad
              </p>
            </div>
          </div>
        </section>

        <section className="py-8 md:py-12 border-b">
          <div className="container mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex flex-col md:flex-row gap-4 items-start md:items-center justify-between">
              <div className="relative flex-1 max-w-md w-full">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
                <Input
                  placeholder="Buscar noticias..."
                  className="pl-9"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  data-testid="input-search-news"
                />
              </div>
              
              <div className="flex gap-2 flex-wrap">
                {categories.map((category) => (
                  <Badge
                    key={category}
                    variant={selectedCategory === category ? "default" : "outline"}
                    className="cursor-pointer hover-elevate active-elevate-2"
                    onClick={() => setSelectedCategory(category)}
                    data-testid={`badge-category-${category.toLowerCase()}`}
                  >
                    {category}
                  </Badge>
                ))}
              </div>
            </div>
          </div>
        </section>

        <section className="py-12 md:py-16">
          <div className="container mx-auto px-4 sm:px-6 lg:px-8">
            {filteredNews.length > 0 ? (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {filteredNews.map((item, index) => (
                  <NewsCard key={index} {...item} />
                ))}
              </div>
            ) : (
              <div className="text-center py-12">
                <p className="text-lg text-muted-foreground">
                  No se encontraron noticias con los criterios seleccionados
                </p>
              </div>
            )}
          </div>
        </section>
      </main>
      <Footer />
    </div>
  );
}
