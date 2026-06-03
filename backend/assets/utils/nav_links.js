import RideIcon from "../icons/rides-route.svg";
import { CiCalendar, CiClock1, CiMenuKebab, CiMoneyCheck1 } from "react-icons/ci";
import { IoAdd, IoBusOutline, IoDocumentsOutline } from "react-icons/io5";
import { GiGroundbreaker } from "react-icons/gi";
import { CgDanger } from "react-icons/cg";
import { MdOutlineDangerous, MdPeopleOutline } from "react-icons/md";
import { PiTrolleySuitcase } from "react-icons/pi";
import { BsBuilding } from "react-icons/bs";




const nav_links = [
  {
    id: 1,
    title: "Vožnje",
    icon: PiTrolleySuitcase,
    has_sublinks: true,
    sublinkId: 1,
    sublinks: [
      { id: 12, subtitle: "Kalendar", href: "/calendar", icon: CiCalendar },
      {
        id: 13,
        subtitle: "Pregled dana",
        href: "/dashboard",
        icon: CiClock1,
      },
      { id: 14, subtitle: "Pregled vožnji", href: "/rides", icon: CiMenuKebab },
      {
        id: 15,
        subtitle: "Dodaj vožnju",
        href: "/rides-create",
        icon: IoAdd,
      },
    ],
  },
  {
    id: 2,
    title: "Vozila",
    icon: IoBusOutline,
    has_sublinks: true,
    sublinkId: 2,
    sublinks: [
      { id: 21, subtitle: "Sva vozila", href: "/vehicles", icon: IoBusOutline },
      { id: 22, subtitle: "Kvarovi", href: "/defects", icon: GiGroundbreaker },
    ],
  },
  {
    id: 3,
    title: "Vozači",
    icon: MdPeopleOutline,
    has_sublinks: false,
    href: "/drivers",
  },
  {
    id: 4,
    title: "Vodiči",
    icon: MdPeopleOutline,
    has_sublinks: false,
    href: "/guides",
  },
  {
    id: 5,
    title: "Agencije",
    icon: BsBuilding,
    has_sublinks: false,
    href: "/agencies",
  },
  {
    id: 6,
    title: "Dokumenti",
    icon: IoDocumentsOutline,
    has_sublinks: true,
    sublinkId: 6,
    sublinks: [
      { id: 61, subtitle: "Svi dokumenti", href: "/company-documents", icon: IoDocumentsOutline },
      { id: 62, subtitle: "U opasnosti", href: "/expiring-documents", icon: CgDanger },
      { id: 63, subtitle: "Istekli dokumenti", href: "/expired-documents" , icon: MdOutlineDangerous},
    ],
  },
  //{
  //  id: 7,
  //  title: "Financije",
  //  icon: CiMoneyCheck1,
  //  has_sublinks: false,
  //  href: "/finance",
  //},
];

export default nav_links;
