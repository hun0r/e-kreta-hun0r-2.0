from __future__ import annotations

from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, Field, computed_field

from ..models import SubjectDescriptor, UidNameStructure, UidStructure, ValueDescriptor


class AnnouncedTest(BaseModel):
    subjectName: Optional[str] = Field(alias="TantargyNeve", frozen=True)
    announcedAt: Optional[datetime] = Field(alias="BejelentesDatuma", frozen=True)
    classScheduleNumber: Optional[int] = Field(alias="OrarendiOraOraszama", frozen=True)
    date: Optional[datetime] = Field(alias="Datum", frozen=True)
    group: Optional[UidStructure] = Field(alias="OsztalyCsoport", frozen=True)
    mode: Optional[ValueDescriptor] = Field(alias="Modja", frozen=True)
    subject: Optional[SubjectDescriptor] = Field(alias="Tantargy", frozen=True)
    teacher: Optional[str] = Field(alias="RogzitoTanarNeve", frozen=True)
    theme: Optional[str] = Field(alias="Temaja", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class ClassAverage(BaseModel):
    average: Optional[float] = Field(alias="TanuloAtlag", frozen=True)
    classAverageNumber: Optional[float] = Field(
        alias="OsztalyCsoportAtlag", frozen=True
    )
    differenceFromClassAverage: Optional[float] = Field(
        alias="OsztalyCsoportAtlagtolValoElteres", frozen=True
    )
    subject: Optional[SubjectDescriptor] = Field(alias="Tantargy", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class ClassMaster(BaseModel):
    listOfClass: Optional[list[SchoolClass]] = Field(alias="Osztalyai", frozen=True)
    teacher: Optional[Teacher] = Field(alias="Tanar", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class Email(BaseModel):
    email: Optional[str] = Field(alias="Email", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class Employee(BaseModel):
    email: Optional[list[Email]] = Field(alias="Emailek", frozen=True)
    name: Optional[str] = Field(alias="Nev", frozen=True)
    phoneList: Optional[list[Phone]] = Field(alias="Telefonok", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class Phone(BaseModel):
    phone: Optional[str] = Field(alias="Telefonszam", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class Teacher(BaseModel):
    employee: Optional[Employee] = Field(alias="Alkalmazott", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class ConsultingHour(BaseModel):
    classroomDescriptor: Optional[UidNameStructure] = Field(alias="Terem", frozen=True)
    consultingHourTimeSlots: Optional[list[ConsultingHourTimeSlot]] = Field(
        alias="Idopontok", frozen=True
    )
    deadline: Optional[datetime] = Field(alias="JelentkezesHatarido", frozen=True)
    endTime: Optional[datetime] = Field(alias="VegIdopont", frozen=True)
    isReservationEnabled: Optional[bool] = Field(
        alias="IsJelentkezesFeatureEnabled", frozen=True
    )
    startTime: Optional[datetime] = Field(alias="KezdoIdopont", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class Evaluation(BaseModel):
    creatingTime: Optional[datetime] = Field(alias="KeszitesDatuma", frozen=True)
    form: Optional[str] = Field(alias="Jelleg", frozen=True)
    formType: Optional[ValueDescriptor] = Field(alias="ErtekFajta", frozen=True)
    group: Optional[UidStructure] = Field(alias="OsztalyCsoport", frozen=True)
    mode: Optional[ValueDescriptor] = Field(alias="Mod", frozen=True)
    numberValue: Optional[int] = Field(alias="SzamErtek", frozen=True)
    recordDate: Optional[datetime] = Field(alias="RogzitesDatuma", frozen=True)
    seenByTutelary: Optional[datetime] = Field(alias="LattamozasDatuma", frozen=True)
    shortValue: Optional[str] = Field(alias="SzovegesErtekelesRovidNev", frozen=True)
    sortIndex: Optional[int] = Field(alias="SortIndex", frozen=True)
    subject: Optional[SubjectDescriptor] = Field(alias="Tantargy", frozen=True)
    teacher: Optional[str] = Field(alias="ErtekeloTanarNeve", frozen=True)
    theme: Optional[str] = Field(alias="Tema", frozen=True)
    type: Optional[ValueDescriptor] = Field(alias="Tipus", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)
    value: Optional[str] = Field(alias="SzovegesErtek", frozen=True)
    weight: Optional[str] = Field(alias="SulySzazalekErteke", frozen=True)


class Group(BaseModel):
    category: Optional[ValueDescriptor] = Field(
        alias="OktatasNevelesiKategoria", frozen=True
    )
    classMaster: Optional[UidStructure] = Field(alias="OsztalyFonok", frozen=True)
    classMasterAssistant: Optional[UidStructure] = Field(
        alias="OsztalyFonokHelyettes", frozen=True
    )
    educationType: Optional[ValueDescriptor] = Field(
        alias="OktatasNevelesiFeladat", frozen=True
    )
    isActive: Optional[bool] = Field(alias="IsAktiv", frozen=True)
    name: Optional[str] = Field(alias="Nev", frozen=True)
    sortIndex: Optional[int] = Field(
        alias="OktatasNevelesiFeladatSortIndex", frozen=True
    )
    type: Optional[str] = Field(alias="Tipus", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class Guardian4T(BaseModel):
    dateOfBirth: Optional[datetime] = Field(alias="SzuletesiDatum", frozen=True)
    firstname: Optional[str] = Field(alias="Utonev", frozen=True)
    firstnameOfBirth: Optional[str] = Field(alias="SzuletesiUtonev", frozen=True)
    mothersFirstname: Optional[str] = Field(alias="AnyjaUtonev", frozen=True)
    mothersSurname: Optional[str] = Field(alias="AnyjaVezeteknev", frozen=True)
    namePrefix: Optional[str] = Field(alias="Elotag", frozen=True)
    placeOfBirth: Optional[str] = Field(alias="SzuletesiHely", frozen=True)
    surname: Optional[str] = Field(alias="Vezeteknev", frozen=True)
    surnameOfBirth: Optional[str] = Field(alias="SzuletesiVezeteknev", frozen=True)


class Homework(BaseModel):
    subjectName: Optional[str] = Field(alias="TantargyNeve", frozen=True)
    attachmentList: Optional[list[Attachment]] = Field(
        alias="Csatolmanyok", frozen=True
    )
    createDate: Optional[datetime] = Field(alias="RogzitesIdopontja", frozen=True)
    deadlineDate: Optional[datetime] = Field(alias="HataridoDatuma", frozen=True)
    group: Optional[UidStructure] = Field(alias="OsztalyCsoport", frozen=True)
    isAllowToAttachFile: Optional[bool] = Field(
        alias="IsCsatolasEngedelyezes", frozen=True
    )
    isDone: Optional[bool] = Field(alias="IsMegoldva", frozen=True)
    isStudentHomeworkEnabled: Optional[bool] = Field(
        alias="IsTanuloHaziFeladatEnabled", frozen=True
    )
    isTeacherRecorded: Optional[bool] = Field(alias="IsTanarRogzitette", frozen=True)
    recordDate: Optional[datetime] = Field(alias="FeladasDatuma", frozen=True)
    recorderTeacherName: Optional[str] = Field(alias="RogzitoTanarNeve", frozen=True)
    subject: Optional[SubjectDescriptor] = Field(alias="Tantargy", frozen=True)
    submitable: Optional[bool] = Field(alias="IsBeadhato", frozen=True)
    text: Optional[str] = Field(alias="Szoveg", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class Attachment(BaseModel):
    name: Optional[str] = Field(alias="Nev", frozen=True)
    type: Optional[str] = Field(alias="Tipus", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class LepEvent(BaseModel):
    address: Optional[str] = Field(alias="Helyszin", frozen=True)
    creationDate: Optional[datetime] = Field(alias="Datum", frozen=True)
    eventEndTime: Optional[datetime] = Field(alias="EloadasVege", frozen=True)
    eventStartTime: Optional[datetime] = Field(alias="EloadasKezdete", frozen=True)
    eventTitle: Optional[str] = Field(alias="EloadasNev", frozen=True)
    hasGuardianPermission: Optional[bool] = Field(
        alias="GondviseloElfogadas", frozen=True
    )
    hasStudentAppeared: Optional[bool] = Field(alias="Megjelent", frozen=True)
    organizationName: Optional[str] = Field(alias="SzervezetNev", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class Lesson(BaseModel):
    announcedTestUid: Optional[str] = Field(
        alias="BejelentettSzamonkeresUid", frozen=True
    )
    attachments: Optional[list[Attachment]] = Field(alias="Csatolmanyok", frozen=True)
    classGroup: Optional[UidNameStructure] = Field(alias="OsztalyCsoport", frozen=True)
    classScheduleNumber: Optional[int] = Field(alias="Oraszam", frozen=True)
    classroom: Optional[str] = Field(alias="TeremNeve", frozen=True)
    classworkGroupId: Optional[str] = Field(alias="FeladatGroupUid", frozen=True)
    digitalInstrumentType: Optional[str] = Field(
        alias="DigitalisEszkozTipus", frozen=True
    )
    digitalPlatformType: Optional[str] = Field(
        alias="DigitalisPlatformTipus", frozen=True
    )
    endTime: Optional[datetime] = Field(alias="VegIdopont", frozen=True)
    homeWorkUid: Optional[str] = Field(alias="HaziFeladatUid", frozen=True)
    homeworkEditedByStudentEnabled: Optional[bool] = Field(
        alias="IsTanuloHaziFeladatEnabled", frozen=True
    )
    isDigitalLesson: Optional[bool] = Field(alias="IsDigitalisOra", frozen=True)
    languageTaskGroupId: Optional[str] = Field(
        alias="NyelviFeladatGroupUid", frozen=True
    )
    lessonNumber: Optional[int] = Field(alias="OraEvesSorszama", frozen=True)
    name: Optional[str] = Field(alias="Nev", frozen=True)
    presence: Optional[ValueDescriptor] = Field(alias="TanuloJelenlet", frozen=True)
    startTime: Optional[datetime] = Field(alias="KezdetIdopont", frozen=True)
    state: Optional[ValueDescriptor] = Field(alias="Allapot", frozen=True)
    subject: Optional[SubjectDescriptor] = Field(alias="Tantargy", frozen=True)
    supplyTeacher: Optional[str] = Field(alias="HelyettesTanarNeve", frozen=True)
    supportedDigitalInstrumentTypes: Optional[list[str]] = Field(
        alias="DigitalisTamogatoEszkozTipusList", frozen=True
    )
    teacher: Optional[str] = Field(alias="TanarNeve", frozen=True)
    topic: Optional[str] = Field(alias="Tema", frozen=True)
    type: Optional[ValueDescriptor] = Field(alias="Tipus", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class Note(BaseModel):
    content: Optional[str] = Field(alias="Tartalom", frozen=True)
    creatingTime: Optional[datetime] = Field(alias="KeszitesDatuma", frozen=True)
    date: Optional[datetime] = Field(alias="Datum", frozen=True)
    group: Optional[UidStructure] = Field(alias="OsztalyCsoport", frozen=True)
    seenByTutelary: Optional[datetime] = Field(alias="LattamozasDatuma", frozen=True)
    teacher: Optional[str] = Field(alias="KeszitoTanarNeve", frozen=True)
    title: Optional[str] = Field(alias="Cim", frozen=True)
    type: Optional[ValueDescriptor] = Field(alias="Tipus", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class NoticeBoardItem(BaseModel):
    content: Optional[str] = Field(alias="Tartalom", frozen=True)
    expireEndTime: Optional[datetime] = Field(alias="ErvenyessegVege", frozen=True)
    expireStartTime: Optional[datetime] = Field(alias="ErvenyessegKezdete", frozen=True)
    madeBy: Optional[str] = Field(alias="RogzitoNeve", frozen=True)
    title: Optional[str] = Field(alias="Cim", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class Omission(BaseModel):
    creatingTime: Optional[datetime] = Field(alias="KeszitesDatuma", frozen=True)
    date: Optional[datetime] = Field(alias="Datum", frozen=True)
    delayTimeMinutes: Optional[int] = Field(alias="KesesPercben", frozen=True)
    group: Optional[UidStructure] = Field(alias="OsztalyCsoport", frozen=True)
    justificationState: Optional[str] = Field(alias="IgazolasAllapota", frozen=True)
    justificationType: Optional[ValueDescriptor] = Field(
        alias="IgazolasTipusa", frozen=True
    )
    lesson: Optional[Lesson] = Field(alias="Ora", frozen=True)
    mode: Optional[ValueDescriptor] = Field(alias="Mod", frozen=True)
    subject: Optional[SubjectDescriptor] = Field(alias="Tantargy", frozen=True)
    teacher: Optional[str] = Field(alias="RogzitoTanarNeve", frozen=True)
    type: Optional[ValueDescriptor] = Field(alias="Tipus", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class SchoolYearCalendarEntry(BaseModel):
    date: Optional[datetime] = Field(alias="Datum", frozen=True)
    dayType: Optional[ValueDescriptor] = Field(alias="Naptipus", frozen=True)
    group: Optional[UidStructure] = Field(alias="OsztalyCsoport", frozen=True)
    irregularDay: Optional[ValueDescriptor] = Field(
        alias="ElteroOrarendSzerintiTanitasiNap", frozen=True
    )
    uid: Optional[str] = Field(alias="Uid", frozen=True)
    weekTypeSchedule: Optional[ValueDescriptor] = Field(
        alias="OrarendiNapHetirendje", frozen=True
    )


class Student(BaseModel):
    addressDataList: Optional[list[str]] = Field(alias="Cimek", frozen=True)
    bankAccount: Optional[BankAccount] = Field(alias="Bankszamla", frozen=True)
    dayOfBirth: Optional[int] = Field(alias="SzuletesiNap", frozen=True)
    emailAddress: Optional[str] = Field(alias="EmailCim", frozen=True)
    guardianList: Optional[list[Guardian]] = Field(alias="Gondviselok", frozen=True)
    instituteCode: Optional[str] = Field(alias="IntezmenyAzonosito", frozen=True)
    instituteName: Optional[str] = Field(alias="IntezmenyNev", frozen=True)
    institution: Optional[Institution] = Field(alias="Intezmeny", frozen=True)
    monthOfBirth: Optional[int] = Field(alias="SzuletesiHonap", frozen=True)
    mothersName: Optional[str] = Field(alias="AnyjaNeve", frozen=True)
    name: Optional[str] = Field(alias="Nev", frozen=True)
    nameOfBirth: Optional[str] = Field(alias="SzuletesiNev", frozen=True)
    phoneNumber: Optional[str] = Field(alias="Telefonszam", frozen=True)
    placeOfBirth: Optional[str] = Field(alias="SzuletesiHely", frozen=True)
    schoolYearUID: Optional[float] = Field(alias="TanevUid", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)
    yearOfBirth: Optional[int] = Field(alias="SzuletesiEv", frozen=True)
    @computed_field
    @property
    def dateOfBirth(self) -> date:
        return date(self.year, self.month, self.day)


class BankAccount(BaseModel):
    accountNumber: Optional[str] = Field(alias="BankszamlaSzam", frozen=True)
    isReadOnly: Optional[str] = Field(alias="IsReadOnly", frozen=True)
    ownerName: Optional[str] = Field(alias="BankszamlaTulajdonosNeve", frozen=True)
    ownerType: Optional[str] = Field(alias="BankszamlaTulajdonosTipusId", frozen=True)


class SubjectAverage(BaseModel):
    averageNumber: Optional[float] = Field(alias="Atlag", frozen=True)
    averagesInTime: Optional[list[AverageWithTime]] = Field(
        alias="AtlagAlakulasaIdoFuggvenyeben", frozen=True
    )
    sortIndex: Optional[int] = Field(alias="SortIndex", frozen=True)
    subject: Optional[SubjectDescriptor] = Field(alias="Tantargy", frozen=True)
    sumOfWeightedEvaluations: Optional[float] = Field(
        alias="SulyozottOsztalyzatOsszege", frozen=True
    )
    sumOfWeights: Optional[float] = Field(alias="SulyozottOsztalyzatSzama", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class AverageWithTime(BaseModel):
    average: Optional[float] = Field(alias="Atlag", frozen=True)
    date: Optional[datetime] = Field(alias="Datum", frozen=True)


class TimeTableWeek(BaseModel):
    endDate: Optional[datetime] = Field(alias="VegNapDatuma", frozen=True)
    numberOfWeek: Optional[int] = Field(alias="HetSorszama", frozen=True)
    startDate: Optional[datetime] = Field(alias="KezdoNapDatuma", frozen=True)
    type: Optional[ValueDescriptor] = Field(alias="Tipus", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class BankAccountNumberPost(BaseModel):
    bankAccountNumber: Optional[str] = Field(alias="BankszamlaSzam", frozen=True)
    bankAccountOwnerName: Optional[str] = Field(
        alias="BankszamlaTulajdonosNeve", frozen=True
    )
    bankAccountOwnerType: Optional[int] = Field(
        alias="BankszamlaTulajdonosTipusId", frozen=True
    )
    bankName: Optional[str] = Field(alias="SzamlavezetoBank", frozen=True)


class Guardian4TPost(BaseModel):
    dateOfBirth: Optional[datetime] = Field(alias="SzuletesiDatum", frozen=True)
    firstname: Optional[str] = Field(alias="Utonev", frozen=True)
    firstnameOfBirth: Optional[str] = Field(alias="SzuletesiUtonev", frozen=True)
    isAszfAccepted: Optional[bool] = Field(alias="IsElfogadottAszf", frozen=True)
    mothersFirstname: Optional[str] = Field(alias="AnyjaUtonev", frozen=True)
    mothersSurname: Optional[str] = Field(alias="AnyjaVezeteknev", frozen=True)
    namePrefix: Optional[str] = Field(alias="Elotag", frozen=True)
    placeOfBirth: Optional[str] = Field(alias="SzuletesiHely", frozen=True)
    surname: Optional[str] = Field(alias="Vezeteknev", frozen=True)
    surnameOfBirth: Optional[str] = Field(alias="SzuletesiVezeteknev", frozen=True)


class LepEventGuardianPermissionPost(BaseModel):
    eventId: Optional[int] = Field(alias="EloadasId", frozen=True)
    isPermitted: Optional[bool] = Field(alias="Dontes", frozen=True)


class SchoolClass(BaseModel):
    category: Optional[ValueDescriptor] = Field(
        alias="OktatasNevelesiKategoria", frozen=True
    )
    name: Optional[str] = Field(alias="Nev", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class ConsultingHourTimeSlot(BaseModel):
    endTime: Optional[datetime] = Field(alias="VegIdopont", frozen=True)
    isReservedByMe: Optional[bool] = Field(alias="IsJelentkeztem", frozen=True)
    startTime: Optional[datetime] = Field(alias="KezdoIdopont", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class Guardian(BaseModel):
    email: Optional[str] = Field(alias="EmailCim", frozen=True)
    isLegalRepresentative: Optional[bool] = Field(
        alias="IsTorvenyesKepviselo", frozen=True
    )
    name: Optional[str] = Field(alias="Nev", frozen=True)
    phoneNumber: Optional[str] = Field(alias="Telefonszam", frozen=True)
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class Institution(BaseModel):
    customizationSettings: Optional[CustomizationSettings] = Field(
        alias="TestreszabasBeallitasok", frozen=True
    )
    shortName: Optional[str] = Field(alias="RovidNev", frozen=True)
    systemModuleList: Optional[list[SystemModule]] = Field(
        alias="Rendszermodulok", frozen=True
    )
    uid: Optional[str] = Field(alias="Uid", frozen=True)


class CustomizationSettings(BaseModel):
    delayOfNotifications: Optional[int] = Field(
        alias="ErtekelesekMegjelenitesenekKesleltetesenekMerteke", frozen=True
    )
    isClassAverageVisible: Optional[bool] = Field(
        alias="IsOsztalyAtlagMegjeleniteseEllenorzoben", frozen=True
    )
    isLessonsThemeVisible: Optional[bool] = Field(
        alias="IsTanorakTemajaMegtekinthetoEllenorzoben", frozen=True
    )
    nextServerDeploy: Optional[datetime] = Field(
        alias="KovetkezoTelepitesDatuma", frozen=True
    )


class SystemModule(BaseModel):
    isActive: Optional[bool] = Field(alias="IsAktiv", frozen=True)
    type: Optional[str] = Field(alias="Tipus", frozen=True)
    url: Optional[str] = Field(alias="Url", frozen=True)
