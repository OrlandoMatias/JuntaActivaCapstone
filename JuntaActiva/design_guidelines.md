# Design Guidelines: Sistema Unidad Territorial

## Design Approach

**Selected Framework**: Material Design with civic customization
**Rationale**: This community management system serves both utility-focused administrative needs and public-facing engagement. Material Design provides the robust component patterns, accessibility standards, and data-heavy interfaces required for civic applications while maintaining approachability for diverse community members.

**Core Principles**:
- Trust through clarity and transparency
- Accessibility for all age groups and technical abilities
- Professional yet approachable aesthetic suitable for Chilean community context
- Efficient workflows for board members managing approvals

---

## Color Palette

**Primary Colors**:
- Primary: 210 75% 45% (Professional Chilean civic blue - trust and stability)
- Primary Light: 210 75% 55% (Interactive states)
- Primary Dark: 210 75% 35% (Headers, emphasis)

**Neutral Foundation**:
- Background (Light): 0 0% 98%
- Surface (Light): 0 0% 100%
- Text Primary: 220 15% 15%
- Text Secondary: 220 10% 45%

**Dark Mode**:
- Background: 220 15% 12%
- Surface: 220 15% 18%
- Text Primary: 0 0% 95%
- Text Secondary: 0 0% 70%

**Semantic Colors**:
- Success: 145 65% 42% (Approvals, confirmations)
- Warning: 35 85% 55% (Pending reviews)
- Error: 355 75% 50% (Rejections, errors)
- Info: 210 75% 55% (Notifications)

**Accent** (Use sparingly):
- Accent: 165 60% 45% (Call-to-action buttons, highlights)

---

## Typography

**Font Stack**:
- Primary: 'Inter', system-ui, -apple-system, sans-serif
- Headings: 'Inter', sans-serif (600-700 weight)
- Body: 'Inter', sans-serif (400-500 weight)

**Type Scale**:
- Hero (h1): text-5xl md:text-6xl, font-bold, tracking-tight
- Section Header (h2): text-3xl md:text-4xl, font-semibold
- Subsection (h3): text-2xl, font-semibold
- Card Title (h4): text-xl, font-medium
- Body Large: text-lg, font-normal
- Body: text-base, font-normal
- Small: text-sm, font-normal
- Tiny: text-xs, font-medium (labels, captions)

**Line Heights**: Use relaxed (1.6) for body text, snug (1.2) for headings

---

## Layout System

**Spacing Primitives**: Use Tailwind units of **2, 4, 6, 8, 12, 16, 20, 24** for consistent rhythm

**Grid System**:
- Container: max-w-7xl mx-auto px-4 sm:px-6 lg:px-8
- Content Sections: py-12 md:py-16 lg:py-20
- Card Spacing: p-6 md:p-8
- Form Fields: space-y-4 md:space-y-6

**Responsive Breakpoints**:
- Mobile-first approach
- sm: 640px (tablet portrait)
- md: 768px (tablet landscape)
- lg: 1024px (desktop)
- xl: 1280px (wide desktop)

---

## Component Library

### Navigation
- **Primary Nav**: Sticky header with logo, main menu items, user profile/login
- **Mobile Nav**: Hamburger menu with slide-in drawer
- **Admin Sidebar**: Collapsible sidebar with icon + label navigation for dashboard

### Hero Section
- **Layout**: Split hero - left side with headline, description, dual CTAs; right side with community illustration/image
- **Height**: min-h-[500px] md:min-h-[600px]
- **Background**: Subtle gradient overlay on primary color
- **Image**: Community gathering illustration or Chilean neighborhood photo showing unity and collaboration

### Cards
- **Standard Card**: Rounded-lg (12px), shadow-md, border border-neutral-200 dark:border-neutral-700
- **Interactive Card**: Hover shadow-lg transition, cursor-pointer
- **Request Card**: Status badge (top-right), timestamp, action buttons (footer)
- **News Card**: Featured image (16:9), category tag, date, excerpt

### Forms
- **Input Fields**: Rounded-md, border-2, focus:ring-2 focus:ring-primary
- **Labels**: text-sm font-medium mb-2, required indicator (*)
- **Buttons**: 
  - Primary: bg-primary text-white, rounded-md, px-6 py-3, font-medium
  - Secondary: border-2 border-primary text-primary, rounded-md, px-6 py-3
  - Ghost: text-primary hover:bg-primary/10
- **Form Layout**: Single column max-w-2xl, multi-column for compact info

### Data Displays
- **Tables**: Striped rows, sticky header, responsive (card view on mobile)
- **Status Badges**: Rounded-full, px-3 py-1, text-sm font-medium, semantic colors
- **Calendar**: Grid layout with color-coded availability, modal for booking details
- **Dashboard Metrics**: 4-column grid (lg), 2-column (md), 1-column (mobile) with icon, number, label

### Modals & Overlays
- **Modal**: max-w-2xl, rounded-lg, shadow-2xl, backdrop blur
- **Toast Notifications**: Fixed top-right, slide-in animation, auto-dismiss 5s
- **Confirmation Dialogs**: Centered, clear action buttons, warning color for destructive actions

### Sections
- **Public Homepage**: Hero → Features (3-col grid) → How It Works (timeline) → Recent News (3 cards) → CTA footer
- **Dashboard**: Stats overview → Pending approvals table → Recent activity feed
- **Certificate System**: Request form → Status tracker → Download area
- **Resource Booking**: Calendar view → Facility selector → Booking form modal

---

## Images

**Hero Image**: 
- **Description**: Wide-angle photograph of a Chilean neighborhood community meeting or collaborative community project (plaza cleanup, neighborhood festival, community garden). Warm, inclusive atmosphere with diverse residents of various ages.
- **Placement**: Right 50% of hero section on desktop, full-width background on mobile with overlay
- **Style**: Natural photography with slight warmth adjustment, not overly saturated

**Supporting Images**:
- Feature icons: Simplified line icons for registration, certificates, projects, events
- News thumbnails: 16:9 ratio, rounded corners, lazy loading
- Empty states: Friendly illustrations for "no results" or "get started" prompts

---

## Animations

**Minimal & Purposeful**:
- Page transitions: Fade-in only (300ms)
- Card hover: Subtle lift (transform translateY(-2px), 200ms)
- Form validation: Shake animation on error (400ms)
- Loading states: Skeleton screens (pulse animation)
- **Avoid**: Parallax, scroll-triggered animations, decorative motion

---

## Accessibility & Dark Mode

- WCAG AA contrast ratios (4.5:1 for text)
- Dark mode toggle in header, persisted to localStorage
- All interactive elements: min 44x44px touch target
- Form inputs maintain consistent styling in both modes
- Focus states: 2px ring with primary color, offset-2
- Skip navigation link for keyboard users
- Proper ARIA labels for screen readers

---

## Page-Specific Layouts

**Public Homepage**: Hero (40vh-50vh) → Features (py-20) → Process Timeline (py-16) → News Grid (py-20) → Footer CTA (py-16)

**Admin Dashboard**: Top stats bar (4 metrics) → Pending approvals section (table) → Quick actions (card grid) → Activity feed (sidebar)

**Forms**: Centered max-w-3xl, progress indicator (multi-step), field grouping with subtle borders, sticky submit button on mobile