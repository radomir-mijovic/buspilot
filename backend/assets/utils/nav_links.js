const nav_links = [
  {
    id: 1,
    title: "Vožnje",
    has_sublinks: true,
    sublinks: [
      { id: 12, subtitle: "Kalendar", href: "/calendar" },
      { id: 13, subtitle: "Pregled dana", href: "/dashboard" },
      { id: 14, subtitle: "Pregled vožnji", href: "/rides" },
      { id: 15, subtitle: "Dodaj vožnju", href: "/rides-create" },
    ],
  },
  {
    id: 2,
    title: "Vozila",
    has_sublinks: true,
    sublinks: [
      { id: 21, subtitle: "Sva vozila", href: "/vehicles" },
      { id: 22, subtitle: "Kvarovi", href: "/defects" },
    ],
  },
  {
    id: 3,
    title: "Vozači",
    has_sublinks: false,
    href: "/drivers",
  },
  {
    id: 4,
    title: "Vodiči",
    has_sublinks: false,
    href: "/guides",
  },
  {
    id: 5,
    title: "Agencije",
    has_sublinks: false,
    href: "/agencies",
  },
  {
    id: 6,
    title: "Dokumenti",
    has_sublinks: true,
    sublinks: [
      { id: 61, subtitle: "Svi dokumenti", href: "/documents" },
      { id: 62, subtitle: "U opasnosti", href: "/expiring-documents" },
      { id: 63, subtitle: "Istekli dokumenti", href: "/expired-documents" },
    ],
  },
  {
    id: 7,
    title: "Financije",
    has_sublinks: false,
    href: "/finance",
  },
];

export default nav_links;
