import { Users, Mail, Phone, MapPin } from "lucide-react";
import { Link } from "wouter";

export default function Footer() {
  return (
    <footer className="border-t bg-muted/30">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div>
            <div className="flex items-center gap-2 mb-4">
              <Users className="h-6 w-6 text-primary" />
              <span className="text-lg font-semibold">Sistema UT</span>
            </div>
            <p className="text-sm text-muted-foreground leading-relaxed">
              Plataforma digital para la gestión eficiente de juntas de vecinos en Chile.
            </p>
          </div>

          <div>
            <h3 className="font-semibold mb-4">Servicios</h3>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li><Link href="/services" className="hover:text-primary transition-colors" data-testid="link-footer-registration">Inscripción de Vecinos</Link></li>
              <li><Link href="/services" className="hover:text-primary transition-colors" data-testid="link-footer-certificates">Certificados</Link></li>
              <li><Link href="/services" className="hover:text-primary transition-colors" data-testid="link-footer-projects">Proyectos</Link></li>
              <li><Link href="/services" className="hover:text-primary transition-colors" data-testid="link-footer-reservations">Reservas</Link></li>
            </ul>
          </div>

          <div>
            <h3 className="font-semibold mb-4">Recursos</h3>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li><Link href="/help" className="hover:text-primary transition-colors" data-testid="link-footer-help">Centro de Ayuda</Link></li>
              <li><Link href="/docs" className="hover:text-primary transition-colors" data-testid="link-footer-docs">Documentación</Link></li>
              <li><Link href="/privacy" className="hover:text-primary transition-colors" data-testid="link-footer-privacy">Privacidad</Link></li>
              <li><Link href="/terms" className="hover:text-primary transition-colors" data-testid="link-footer-terms">Términos</Link></li>
            </ul>
          </div>

          <div>
            <h3 className="font-semibold mb-4">Contacto</h3>
            <ul className="space-y-3 text-sm text-muted-foreground">
              <li className="flex items-center gap-2">
                <Mail className="h-4 w-4" />
                <span>contacto@sistemaut.cl</span>
              </li>
              <li className="flex items-center gap-2">
                <Phone className="h-4 w-4" />
                <span>+56 2 2345 6789</span>
              </li>
              <li className="flex items-center gap-2">
                <MapPin className="h-4 w-4" />
                <span>Santiago, Chile</span>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t mt-8 pt-8 text-center text-sm text-muted-foreground">
          <p>© 2025 Sistema Unidad Territorial. Todos los derechos reservados.</p>
        </div>
      </div>
    </footer>
  );
}
