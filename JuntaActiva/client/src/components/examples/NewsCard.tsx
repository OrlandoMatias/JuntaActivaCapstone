import NewsCard from "../NewsCard";

export default function NewsCardExample() {
  return (
    <div className="p-6 max-w-sm">
      <NewsCard
        title="Nueva Plaza Comunitaria Inaugurada"
        excerpt="Este fin de semana se inauguró la nueva plaza comunitaria resultado del proyecto vecinal aprobado el mes pasado."
        category="Proyectos"
        date="15 Ene 2025"
      />
    </div>
  );
}
