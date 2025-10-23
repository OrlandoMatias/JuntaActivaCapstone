import { Link } from "wouter";
import { Button } from "@/components/ui/button";
import { Menu, Users } from "lucide-react";
import ThemeToggle from "./ThemeToggle";
import { useState } from "react";

export default function Header() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <header className="sticky top-0 z-50 border-b bg-background/95 backdrop-blur">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          <Link href="/" className="flex items-center gap-2 hover-elevate active-elevate-2 rounded-md px-3 py-2" data-testid="link-home">
            <Users className="h-6 w-6 text-primary" />
            <span className="text-xl font-semibold">Sistema Unidad Territorial</span>
          </Link>

          <nav className="hidden md:flex items-center gap-6">
            <Link href="/" className="text-sm font-medium hover:text-primary transition-colors" data-testid="link-nav-home">
              Inicio
            </Link>
            <Link href="/services" className="text-sm font-medium hover:text-primary transition-colors" data-testid="link-nav-services">
              Servicios
            </Link>
            <Link href="/news" className="text-sm font-medium hover:text-primary transition-colors" data-testid="link-nav-news">
              Noticias
            </Link>
            <Link href="/contact" className="text-sm font-medium hover:text-primary transition-colors" data-testid="link-nav-contact">
              Contacto
            </Link>
          </nav>

          <div className="flex items-center gap-2">
            <ThemeToggle />
            <Button variant="ghost" className="hidden md:inline-flex" data-testid="button-login">
              Iniciar Sesión
            </Button>
            <Button className="hidden md:inline-flex" data-testid="button-register">
              Registrarse
            </Button>
            <Button
              variant="ghost"
              size="icon"
              className="md:hidden"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              data-testid="button-mobile-menu"
            >
              <Menu className="h-5 w-5" />
            </Button>
          </div>
        </div>

        {mobileMenuOpen && (
          <div className="md:hidden border-t py-4 space-y-2" data-testid="mobile-menu">
            <Link href="/" className="block px-3 py-2 rounded-md hover-elevate active-elevate-2" data-testid="link-mobile-home">
              Inicio
            </Link>
            <Link href="/services" className="block px-3 py-2 rounded-md hover-elevate active-elevate-2" data-testid="link-mobile-services">
              Servicios
            </Link>
            <Link href="/news" className="block px-3 py-2 rounded-md hover-elevate active-elevate-2" data-testid="link-mobile-news">
              Noticias
            </Link>
            <Link href="/contact" className="block px-3 py-2 rounded-md hover-elevate active-elevate-2" data-testid="link-mobile-contact">
              Contacto
            </Link>
            <div className="flex gap-2 pt-2">
              <Button variant="ghost" className="flex-1" data-testid="button-mobile-login">
                Iniciar Sesión
              </Button>
              <Button className="flex-1" data-testid="button-mobile-register">
                Registrarse
              </Button>
            </div>
          </div>
        )}
      </div>
    </header>
  );
}
