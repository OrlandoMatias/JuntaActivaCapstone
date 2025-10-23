import Contact from "../../pages/Contact";
import { ThemeProvider } from "../ThemeProvider";

export default function ContactExample() {
  return (
    <ThemeProvider>
      <Contact />
    </ThemeProvider>
  );
}
