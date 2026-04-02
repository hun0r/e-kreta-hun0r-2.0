from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Optional

from ..utils.utils import filter_params, Router, week_dates
from .models import (
    AnnouncedTest,
    ClassAverage,
    ClassMaster,
    ConsultingHour,
    Evaluation,
    Group,
    Guardian4T,
    Homework,
    LepEvent,
    Lesson,
    Note,
    NoticeBoardItem,
    Omission,
    SchoolYearCalendarEntry,
    Student,
    SubjectAverage,
    TimeTableWeek,
)

if TYPE_CHECKING:
    from datetime import datetime

    from ..idp.auth_session_protocol import Auth_Session_Protocol
        

class Mobile(Router):
    BASE_URL: str = "https://{institute_code}.e-kreta.hu/ellenorzo/v3/"

    def delete_bank_account_number(
        self,
    ) -> None:
        self.request(
            "DELETE",
            "sajat/Bankszamla",
        )


    def delete_reservation(
        self,
        uid: str,
    ) -> None:
        self.request(
            "DELETE",
            f"sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}",
        )


    def download_attachment(
        self,
        uid: str,
    ) -> bytes:
        return self.request(
            "GET",
            f"sajat/Csatolmany/{uid}",
            model=bytes
        )


    def get_announced_tests(
        self,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
    ) -> list[AnnouncedTest]:
        params: dict[str, str] = filter_params(
            datumTol=from_date,
            datumIg=to_date,
        )

        return self.request(
            "GET",
            "sajat/BejelentettSzamonkeresek",
            model=list[AnnouncedTest],
            params=params,
        )


    def get_class_average(
        self,
        educationalTaskUid: str,
        subjectUid: Optional[str] = None,
    ) -> list[ClassAverage]:
        params: dict[str, str] = filter_params(
            oktatasiNevelesiFeladatUid=educationalTaskUid,
            tantargyUid=subjectUid,
        )

        return self.request(
            "GET",
            "sajat/Ertekelesek/Atlagok/OsztalyAtlagok",
            model=list[ClassAverage],
            params=params,
        )


    def get_class_master(
        self,
        Uids: Optional[list[str]] = None,
    ) -> list[ClassMaster]:
        params = filter_params(
            Uids=" ".join(Uids),
        )

        return self.request(
            "GET",
            "felhasznalok/Alkalmazottak/Tanarok/Osztalyfonokok",
            model=list[ClassMaster],
            params=params,
        )


    def get_consulting_hour(
        self,
        Uid: str,
    ) -> ConsultingHour:
        return self.request(
            "GET",
            f"sajat/Fogadoorak/{Uid}",
            model=ConsultingHour,
        )


    def get_consulting_hours(
        self,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
    ) -> list[ConsultingHour]:
        params: dict[str, str] = filter_params(
            datumTol=from_date,
            datumIg=to_date,
        )

        return self.request(
            "GET",
            "sajat/Fogadoorak",
            model=ConsultingHour,
            params=params,
        )


    def get_device_state(
        self,
    ) -> bool:
        return self.request(
            "GET",
            "TargyiEszkoz/IsEszkozKiosztva",
        ).json()


    def get_evaluations(
        self,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
    ) -> list[Evaluation]:
        params: dict[str, str] = filter_params(
            datumTol=from_date,
            datumIg=to_date,
        )

        return self.request(
            "GET",
            "sajat/Ertekelesek",
            model=list[Evaluation],
            params=params,
        )


    def get_groups(
        self,
    ) -> list[Group]:
        return self.request(
            "GET",
            "sajat/OsztalyCsoportok",
            model=list[Group],
        )


    def get_guardian4t(
        self,
    ) -> Guardian4T:
        return self.request(
            "GET",
            "sajat/GondviseloAdatlap",
            model=Guardian4T,
        )


    def get_homework(
        self,
        id: str,
    ) -> Homework:
        return self.request(
            "GET",
            f"sajat/HaziFeladatok/{id}",
            model=Homework,
        )


    def get_homeworks(
        self,
        from_date: datetime,
        to_date: Optional[datetime] = None,
    ) -> list[Homework]:
        params: dict[str, str] = filter_params(
            datumTol=from_date,
            datumIg=to_date,
        )

        return self.request(
            "GET",
            "sajat/HaziFeladatok",
            model=list[Homework],
            params=params,
        )


    def get_lep_events(
        self,
    ) -> list[LepEvent]:
        return self.request(
            "GET",
            "Lep/Eloadasok",
            model=LepEvent,
        )


    def get_lesson(
        self,
        LessonUid: str,
    ) -> Lesson:
        params: dict[str, str] = filter_params(
            ororendElemUid=LessonUid,
        )

        return self.request(
            "GET",
            "sajat/OrarendElem",
            model=Lesson,
            params=params,
        )


    def get_lessons(
        self,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
    ) -> list[Lesson]:
        params: dict[str, str] = filter_params(
            datumTol=from_date,
            datumIg=to_date,
        )

        return self.request(
            "GET",
            "sajat/OrarendElem",
            model=list[Lesson],
            params=params,
        )


    def get_notes(
        self,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
    ) -> list[Note]:
        params: dict[str, str] = filter_params(
            datumTol=from_date,
            datumIg=to_date,
        )

        return self.request(
            "GET",
            "sajat/Feljegyzesek",
            model=list[Note],
            params=params,
        )


    def get_noticeboard_items(
        self,
    ) -> list[NoticeBoardItem]:
        return self.request(
            "GET",
            "sajat/FaliujsagElemek",
            model=list[NoticeBoardItem],
        )


    def get_ommissions(
        self,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
    ) -> list[Omission]:
        params: dict[str, str] = filter_params(
            datumTol=from_date,
            datumIg=to_date,
        )

        return self.request(
            "GET",
            "sajat/Mulasztasok",
            model=list[Omission],
            params=params,
        )


    def get_registration_state(
        self,
    ) -> dict | str | int | list:
        return self.request(
            "GET",
            "TargyiEszkoz/IsRegisztralt",
        ).json()


    def get_schoolyear_calendar(
        self,
    ) -> list[SchoolYearCalendarEntry]:
        return self.request(
            "GET",
            "Intezmenyek/TanevRendjeElemek",
            model=list[SchoolYearCalendarEntry],
        )


    def get_student(
        self,
    ) -> Student:
        return self.request(
            "GET",
            "sajat/TanuloAdatlap",
            model=Student,
        )


    def get_subject_average(
        self,
        educationalTaskUid: str,
    ) -> list[SubjectAverage]:
        params: dict[str, str] = filter_params(
            oktatasiNevelesiFeladatUid=educationalTaskUid,
        )

        return self.request(
            "GET",
            "sajat/Ertekelesek/Atlagok/OsztalyAtlagok",
            model=list[SubjectAverage],
            params=params,
        )


    def get_timetable_weeks(
        self,
        date_in_first_week: datetime,
        weeks: Literal[1, 2, 3],
    ) -> list[TimeTableWeek]:
        start, end = week_dates(date_in_first_week, weeks)
        params: dict[str, str] = filter_params(
            orarendElemKezdoNapDatuma=start,
            orarendElemVegNapDatuma=end,
        )

        return self.request(
            "GET",
            "Intezmenyek/Hetirendek/Orarendi",
            model=list[TimeTableWeek],
            params=params,
        )


    def post_bank_account_number(
        self,
        bankAccountNumber: str,
        bankAccountOwnerName: str,
        bankAccountOwnerType: int,
        bankName: str,
    ) -> None:
        json = {
            "BankszamlaSzam": bankAccountNumber,
            "BankszamlaTulajdonosNeve": bankAccountOwnerName,
            "BankszamlaTulajdonosTipusId": bankAccountOwnerType,
            "SzamlavezetoBank": bankName,
        }

        self.request(
            "POST",
            "sajat/Bankszamla",
            json=json,
        )
        return None


    def post_contact(self, email: str, phone_number: str) -> None:
        data = {
            "email": email,
            "telefonszam": phone_number,
        }

        self.request(
            "POST",
            "sajat/Elerhetoseg",
            data=data,
        )
        return None


    def post_covid_form(self) -> None:
        self.request(
            "POST",
            "Bejelentes/Covid",
        )
        return None


    def post_reservation(self, uid: str) -> None:
        self.request(
            "POST",
            f"Fogadoorak/Idopontok/Jelentkezesek/{uid}",
        )
        return None


    def post_teszek_registration(
        self,
        dateOfBirth: datetime,
        firstname: str,
        firstnameOfBirth: str,
        isAszfAccepted: bool,
        mothersFirstname: str,
        mothersSurname: str,
        namePrefix: str,
        placeOfBirth: str,
        surname: str,
        surnameOfBirth: str,
    ) -> None:
        data = {
            "SzuletesiDatum": dateOfBirth,
            "Utonev": firstname,
            "SzuletesiUtonev": firstnameOfBirth,
            "IsElfogadottAszf": isAszfAccepted,
            "AnyjaUtonev": mothersFirstname,
            "AnyjaVezeteknev": mothersSurname,
            "Elotag": namePrefix,
            "SzuletesiHely": placeOfBirth,
            "Vezeteknev": surname,
            "SzuletesiVezeteknev": surnameOfBirth,
        }

        self.request(
            "POST",
            "TargyiEszkoz/Regisztracio",
            data=data,
        )
        return None


    def update_guardian4T(
        self,
        dateOfBirth: datetime,
        firstname: str,
        firstnameOfBirth: str,
        isAszfAccepted: bool,
        mothersFirstname: str,
        mothersSurname: str,
        namePrefix: str,
        placeOfBirth: str,
        surname: str,
        surnameOfBirth: str,
    ) -> None:
        data = {
            "SzuletesiDatum": dateOfBirth,
            "Utonev": firstname,
            "SzuletesiUtonev": firstnameOfBirth,
            "IsElfogadottAszf": isAszfAccepted,
            "AnyjaUtonev": mothersFirstname,
            "AnyjaVezeteknev": mothersSurname,
            "Elotag": namePrefix,
            "SzuletesiHely": placeOfBirth,
            "Vezeteknev": surname,
            "SzuletesiVezeteknev": surnameOfBirth,
        }

        self.request(
            "PUT",
            "sajat/GondviseloAdatlap",
            data=data,
        )
        return None


    def update_LEP_event_permission(
        self,
        eventId: int,
        isPermitted: bool,
    ) -> None:
        json = {
            "EloadasId": eventId,
            "Dontes": isPermitted,
        }

        self.request(
            "POST",
            "Lep/Eloadasok/GondviseloEngedelyezes",
            json=json,
        )
        return None
