import FeatureCard from "../FeatureCard";
import { Users } from "lucide-react";

export default function FeatureCardExample() {
  return (
    <div className="p-6 max-w-sm">
      <FeatureCard
        icon={Users}
        title="Gestión de Vecinos"
        description="Inscripción y administración de vecinos con proceso de aprobación digital y notificaciones automáticas."
      />
    </div>
  );
}
