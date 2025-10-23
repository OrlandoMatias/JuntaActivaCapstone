import News from "../../pages/News";
import { ThemeProvider } from "../ThemeProvider";

export default function NewsExample() {
  return (
    <ThemeProvider>
      <News />
    </ThemeProvider>
  );
}
