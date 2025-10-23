import { Card, CardContent, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Calendar } from "lucide-react";

interface NewsCardProps {
  title: string;
  excerpt: string;
  category: string;
  date: string;
  image?: string;
}

export default function NewsCard({ title, excerpt, category, date, image }: NewsCardProps) {
  return (
    <Card className="overflow-hidden hover-elevate active-elevate-2 transition-all duration-200" data-testid="card-news">
      {image && (
        <div className="aspect-video overflow-hidden">
          <img 
            src={image} 
            alt={title}
            className="w-full h-full object-cover"
          />
        </div>
      )}
      <CardHeader className="space-y-3">
        <div className="flex items-center gap-2">
          <Badge variant="secondary" data-testid="badge-category">{category}</Badge>
          <span className="text-sm text-muted-foreground flex items-center gap-1" data-testid="text-date">
            <Calendar className="h-3 w-3" />
            {date}
          </span>
        </div>
        <h3 className="text-xl font-semibold line-clamp-2" data-testid="text-title">{title}</h3>
      </CardHeader>
      <CardContent>
        <p className="text-muted-foreground line-clamp-3 leading-relaxed" data-testid="text-excerpt">
          {excerpt}
        </p>
      </CardContent>
    </Card>
  );
}
