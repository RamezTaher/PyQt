import csv
import re
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication,QDialog,QMainWindow,QMessageBox
from PyQt5.uic import *
import datetime
from datetime import timedelta


etudiant={}
matiere={}
note={}


class main(QMainWindow):

    def __init__(self):
        super(main, self).__init__()
        loadUi("essai_nouvelle_interface.ui", self)
        self.onAddStudent.triggered.connect(self.ajout_window)
        self.onAddNewSubject.triggered.connect(self.ajout_matiere_window)
        self.onAddNewMark.triggered.connect(self.ajout_note_window)
        self.onDeleteStudentDone.triggered.connect(self.supprimer_etudiantwindow)
        self.onDeleteStudentBySectionDone.triggered.connect(self.supprimer_sectionwindow)
        self.onDeleteStudentByLevelDone.triggered.connect(self.supprimer_niveauwindow)
        self.onDeleteStudentByLevelAndSectionDone.triggered.connect(self.supprimer_niveau_sectionwindow)
        self.onDeleteSubject.triggered.connect(self.supprimer_matieretwindow)
        self.onDeleteMark.triggered.connect(self.supprimer_notetwindow)
        self.onPhone.triggered.connect(self.modifier_num_telephonewindow)
        self.onMail.triggered.connect(self.modifier_mailwindow)
        self.onAddress.triggered.connect(self.modifier_adressewindow)
        self.onName.triggered.connect(self.modifier_nom_matierewindow)
        self.OnCoefficient.triggered.connect(self.modifier_coefficient_matierewindow)
        self.onModifyDataMark.triggered.connect(self.modifier_notewindow)
        self.onShowStudents.triggered.connect(self.dic_etudiantwindow)
        self.onShowSubjects.triggered.connect(self.dic_matierewindow)
        self.onShowMarks.triggered.connect(self.dic_notewindow)
        self.onSearchBySection.triggered.connect(self.recherche_sectionwindow)
        self.onSearchByLevel.triggered.connect(self.recherche_niveauwindow)
        self.onSearchById.triggered.connect(self.recherche_num_inscriptionwindow)
        self.onSearchBySectionAndLevel.triggered.connect(self.recherche_niveau_sectionwindow)
        self.onSearchByCode.triggered.connect(self.recherche_codewindow)
        self.onSearchBySection2.triggered.connect(self.recherche_sectionmatierewindow)
        self.onSeachByTermAndSection.triggered.connect(self.recherche_sectionsemestrewindow)
        self.onSearchMarkByID.triggered.connect(self.recherche_num_note)
        self.onSearchBySectionAndLevel2.triggered.connect(self.recherche_sec_niv_note)
        self.onSearchMarkByIDAndTerm.triggered.connect(self.recherche_num_sem_note)
        self.onSaveStudents.triggered.connect(self.enregistrement_etudiants)
        self.onBackupStudents.triggered.connect(self.recuperation_etudiant)
        self.onSaveSubjects.triggered.connect(self.enregistrement_matiere)
        self.onBackUpSubjects.triggered.connect(self.recuperation_matiere)
        self.onSaveMarks.triggered.connect(self.enregistrement_notes)
        self.onBackUpMarks.triggered.connect(self.recuperation_note)
        self.onBillByStudent.triggered.connect(self.bulletin_etudiantwindow)
        self.onBillByTerm.triggered.connect(self.bulletin_etudiant_semestrewindow)
        self.onSuccBySection.triggered.connect(self.etudiant_admis_sectionwindow)
        self.onFailBySection.triggered.connect(self.etudiant_redoublant_sectionwindow)
        self.onSuccByISIMM.triggered.connect(self.etudiant_admis_isimmwindow)
        self.onFailByISIMM.triggered.connect(self.etudiant_redoublant_isimmwindow)
        self.onAverageBySEction.triggered.connect(self.moyenne_window)
        self.onWork.triggered.connect(self.open_filewindow)
        self.onClose.triggered.connect(self.closeEvent)


    def ajout_window(self):
            ajoutetudiant = ajout_etudiant()
            widget.addWidget(ajoutetudiant)
            widget.setCurrentWidget(ajoutetudiant)
    def ajout_matiere_window(self):
            ajoutematiere = ajout_matiere()
            widget.addWidget(ajoutematiere)
            widget.setCurrentWidget(ajoutematiere)
    def ajout_note_window(self):
            ajoutenote = ajout_note()
            widget.addWidget(ajoutenote)
            widget.setCurrentWidget(ajoutenote)
    def supprimer_etudiantwindow(self):
        supprimeretudiant = supprimer_etudiant()
        widget.addWidget(supprimeretudiant)
        widget.setCurrentWidget(supprimeretudiant)
    def supprimer_sectionwindow(self):
        supprimersection=supprimer_section()
        widget.addWidget(supprimersection)
        widget.setCurrentWidget(supprimersection)
    def supprimer_niveauwindow(self):
        supprimerniveau=supprimer_niveau()
        widget.addWidget(supprimerniveau)
        widget.setCurrentWidget(supprimerniveau)

    def supprimer_niveau_sectionwindow(self):
        supprimerniveau_section=supprimer_niveau_section()
        widget.addWidget(supprimerniveau_section)
        widget.setCurrentWidget(supprimerniveau_section)
    def supprimer_matieretwindow(self):
        supprimermatiere = supprimer_matiere()
        widget.addWidget(supprimermatiere)
        widget.setCurrentWidget(supprimermatiere)
    def supprimer_notetwindow(self):
        supprimernote = supprimer_note()
        widget.addWidget(supprimernote)
        widget.setCurrentWidget(supprimernote)
    def modifier_num_telephonewindow(self):
        modifiernumtele = modifier_tel()
        widget.addWidget(modifiernumtele)
        widget.setCurrentWidget(modifiernumtele)
    def modifier_mailwindow(self):
        modifiermail = modifier_mail()
        widget.addWidget(modifiermail)
        widget.setCurrentWidget(modifiermail)
    def modifier_adressewindow(self):
        modifieradresse = modifier_adresse()
        widget.addWidget(modifieradresse)
        widget.setCurrentWidget(modifieradresse)
    def modifier_nom_matierewindow(self):
        modifiernom = modifier_nommatiere()
        widget.addWidget(modifiernom)
        widget.setCurrentWidget(modifiernom)
    def modifier_coefficient_matierewindow(self):
        modifiercoe=modifier_coefficientmatiere()
        widget.addWidget(modifiercoe)
        widget.setCurrentWidget(modifiercoe)
    def modifier_notewindow(self):
        modifiernote=modifier_note()
        widget.addWidget(modifiernote)
        widget.setCurrentWidget(modifiernote)
    def dic_etudiantwindow(self):
        dicetud = dic_etudiant()
        widget.addWidget(dicetud)
        widget.setCurrentWidget(dicetud)
    def dic_matierewindow(self):
        dicmat = dic_matiere()
        widget.addWidget(dicmat)
        widget.setCurrentWidget(dicmat)
    def dic_notewindow(self):
        dicnote = dic_note()
        widget.addWidget(dicnote)
        widget.setCurrentWidget(dicnote)


    def recherche_num_inscriptionwindow(self):
        recherchenum = recherche_num_inscription()
        widget.addWidget(recherchenum)
        widget.setCurrentWidget(recherchenum)
    def recherche_sectionwindow(self):
        recherchesec = recherche_sect()
        widget.addWidget(recherchesec)
        widget.setCurrentWidget(recherchesec)
    def recherche_niveauwindow(self):
        rechercheniv = recherche_niv()
        widget.addWidget(rechercheniv)
        widget.setCurrentWidget(rechercheniv)
    def recherche_niveau_sectionwindow(self):
        rechercheniv_sec = recherche_niv_sec()
        widget.addWidget(rechercheniv_sec)
        widget.setCurrentWidget(rechercheniv_sec)
    def recherche_codewindow(self):
        recherchecode = recherche_code_matiere()
        widget.addWidget(recherchecode)
        widget.setCurrentWidget(recherchecode)

    def recherche_sectionmatierewindow(self):
        recherchesecmat = recherche_sec_matiere()
        widget.addWidget(recherchesecmat)
        widget.setCurrentWidget(recherchesecmat)
    def recherche_sectionsemestrewindow(self):
        recherchesecsemestre = recherche_sec_semestre_matiere()
        widget.addWidget(recherchesecsemestre)
        widget.setCurrentWidget(recherchesecsemestre)

    def recherche_num_note(self):
        recherchenum_note = recherche_num_inscription_note()
        widget.addWidget(recherchenum_note)
        widget.setCurrentWidget(recherchenum_note)
    def recherche_sec_niv_note(self):
        recherchesec_niv_note = recherche_niveau_section_note()
        widget.addWidget(recherchesec_niv_note)
        widget.setCurrentWidget(recherchesec_niv_note)

    def recherche_num_sem_note(self):
        recherchenum_sem_note = recherche_num_inscription_semestre_note()
        widget.addWidget(recherchenum_sem_note)
        widget.setCurrentWidget(recherchenum_sem_note)

#***************enregistrements et recuperations********************
    def enregistrement_etudiants(self):
        global etudiant
        with open("enregistrement et recuperation etudiants.csv", 'w', newline="") as file:
            l = []
            csv_writer = csv.writer(file)
            csv_writer.writerow(["num_inscription", "nom", "prenom", "date_naissance", "adresse", "mail", "telephne", "section","niveau_etude"])
            for key in etudiant.keys():
                l.append(key)
                l.append(etudiant[key][0])
                l.append(etudiant[key][1])
                l.append(etudiant[key][2])
                l.append(etudiant[key][3])
                l.append(etudiant[key][4])
                l.append(etudiant[key][5])
                l.append(etudiant[key][6])
                l.append(etudiant[key][7])
                csv_writer.writerow(l)
                l = []

        msge = QtWidgets.QMessageBox()
        msge.setWindowTitle("SUCCEE")
        msge.setText(" ")
        msge.setInformativeText("SAVED SUCCESSFULLY")
        #msge.setts.QMessageBox.Critical)Icon(QtWidge
        x = msge.exec_()


    def recuperation_etudiant(self):
        global etudiant
        with open("enregistrement et recuperation etudiants.csv", 'r') as file:
            f = csv.reader(file, delimiter=',')
            next(f)
            for line in f:
                l = []
                l.append(line[1])
                l.append(line[2])
                l.append(line[3])
                l.append(line[4])
                l.append(line[5])
                l.append(line[6])
                l.append(line[7])
                l.append(line[8])
                etudiant[line[0]] = l
        msge = QtWidgets.QMessageBox()
        msge.setWindowTitle("SUCCEE")
        msge.setText(" ")
        msge.setInformativeText("BACKUP SUCCESSFULLY")
        # msge.setts.QMessageBox.Critical)Icon(QtWidge
        x = msge.exec_()
        print(etudiant)


    def enregistrement_matiere(self):
        global matiere
        with open("enregistrement et recuperation matieres.csv", 'w', newline="") as file:
            l = []
            csv_writer = csv.writer(file)


            csv_writer.writerow(["code_matiere", "coefficient", "designation", "section", "semestre"])
            for key in matiere.keys():
                l.append(key)
                l.append(matiere[key][0])
                l.append(matiere[key][1])
                l.append(matiere[key][2])
                l.append(matiere[key][3])
                csv_writer.writerow(l)
                l = []
        msge = QtWidgets.QMessageBox()
        msge.setWindowTitle("SUCCESS")
        msge.setText(" ")
        msge.setInformativeText("SAVED SUCCESSFULLY")
        #msge.setts.QMessageBox.Critical)Icon(QtWidge
        x = msge.exec_()

    def recuperation_matiere(self):
        global matiere
        with open("enregistrement et recuperation matieres.csv", 'r') as file:
            f = csv.reader(file, delimiter=',')
            next(f)
            for line in f:
                l = []
                l.append(line[1])
                l.append(line[2])
                l.append(line[3])
                l.append(line[4])
                matiere[line[0]] = l
        msge = QtWidgets.QMessageBox()
        msge.setWindowTitle("SUCCESS")
        msge.setText(" ")
        msge.setInformativeText("BACKUP SUCCESSFULLY")
        # msge.setts.QMessageBox.Critical)Icon(QtWidge
        x = msge.exec_()
        print(matiere)

    def enregistrement_notes(self):
        global note
        with open("enregistrement et recuperation notes.csv", 'a', newline="") as file:
            l = []
            csv_writer = csv.writer(file)
            #csv_writer.writerow(["code_note", "nom", "coefficient", "section", "semestre", "code_matiere", "note_ds", "note_ex","num_inscription"])
            for key in note.keys():
                l.append(key)
                l.append(note[key][0])
                l.append(note[key][1])
                l.append(note[key][2])
                l.append(note[key][3])
                l.append(note[key][4])
                l.append(note[key][5])
                l.append(note[key][6])
                l.append(note[key][7])
                csv_writer.writerow(l)
                l = []
        msge = QtWidgets.QMessageBox()
        msge.setWindowTitle("SUCCESS")
        msge.setText(" ")
        msge.setInformativeText("SAVED SUCCESSFULLY")
        #msge.setts.QMessageBox.Critical)Icon(QtWidge
        x = msge.exec_()

    def recuperation_note(self):
        global note
        with open("enregistrement et recuperation notes.csv", 'r') as file:
            f = csv.reader(file, delimiter=',')
            next(f)
            for line in f:
                l = []
                l.append(line[1])
                l.append(line[2])
                l.append(line[3])
                l.append(line[4])
                l.append(line[5])
                l.append(line[6])
                l.append(line[7])
                l.append(line[8])
                note[line[0]] = l
        msge = QtWidgets.QMessageBox()
        msge.setWindowTitle("SUCCESS")
        msge.setText(" ")
        msge.setInformativeText("BACKUP SUCCESSFULLY")
        # msge.setts.QMessageBox.Critical)Icon(QtWidge
        x = msge.exec_()
        print(note)

    def open_filewindow(self):
        import subprocess
        path = 'projet-2.pdf'
        subprocess.Popen([path], shell=True)
    #**********CALCUL ET AFFICHAGE***********************
    def bulletin_etudiantwindow(self):
        bulletinetudiant = bulletin_etudiant()
        widget.addWidget(bulletinetudiant)
        widget.setCurrentWidget(bulletinetudiant)
    def bulletin_etudiant_semestrewindow(self):
        bulletinetudiant_sem = bulletin_etudiant_semestre()
        widget.addWidget(bulletinetudiant_sem)
        widget.setCurrentWidget(bulletinetudiant_sem)

    def etudiant_admis_sectionwindow(self):
        etudiantadmis_sec = etudiant_admis_section()
        widget.addWidget(etudiantadmis_sec)
        widget.setCurrentWidget(etudiantadmis_sec)

    def etudiant_redoublant_sectionwindow(self):
        etudiantredoublant_sec=etudiant_redoublant_section()
        widget.addWidget(etudiantredoublant_sec)
        widget.setCurrentWidget(etudiantredoublant_sec)
    def etudiant_admis_isimmwindow(self):
        etudiantadmis_isimm = etudiant_admis_isimm()
        widget.addWidget(etudiantadmis_isimm)
        widget.setCurrentWidget(etudiantadmis_isimm)
    def etudiant_redoublant_isimmwindow(self):
        etudiantredoublant_isimm = etudiant_redoublant_isimm()
        widget.addWidget(etudiantredoublant_isimm)
        widget.setCurrentWidget(etudiantredoublant_isimm)

    def moyenne_window(self):
        moyennesection = moyenne_section()
        widget.addWidget(moyennesection)
        widget.setCurrentWidget(moyennesection)

    def closeEvent(self, event):
        close = QMessageBox()
        close.setText("WANNA QUIT ?")
        close.setInformativeText("DO NOT FORGOT TO SAVE")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close.setIcon(QtWidgets.QMessageBox.Critical)
        close = close.exec()

        if close == QMessageBox.Yes:
            sys.exit()
        else:
            pass




class ajout_etudiant(QDialog):
    def __init__(self):
        super(ajout_etudiant,self).__init__()
        loadUi("ajout_etudiant1.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.ajouter.clicked.connect(self.button_ajouter)
    def Return(self):
        widget.setCurrentIndex(0)
    def button_ajouter(self):
        global etudiant
        num_inscription=self.num_inscription.text()
        ok=1

        for key in etudiant.keys():
            if key==num_inscription:
                ok=0
        if (not(num_inscription.isnumeric())):
            self.num_inscription_2.setText("Subscription ID False")
            self.num_inscription.clear()
        else:
            self.num_inscription_2.setText("")
        nom=self.nom.text()
        if(not(nom.isalpha())):
            self.nom_2.setText("First Name False")
            self.nom.clear()
        else:
            self.nom_2.setText("")
        prenom = self.prenom.text()
        if (not(prenom.isalpha() )):
            self.prenom_2.setText("Last Name False")
            self.prenom.clear()
        else:
            self.prenom_2.setText("")
        telephone = self.telephone.text()
        if not(telephone.isnumeric()):
            self.telephone_2.setText("Phone Number False")
            self.telephone.clear()
        elif len(telephone)==0 or len(telephone)>8:
            self.telephone_2.setText("Phone Number False")
            self.telephone.clear()

        else:
            self.telephone_2.setText("")

        self.adresse_3.setText("")
        self.mail_2.setText("")
        mail=self.mail.text()

        regex=r'\b[A-Za-z0-9._%+-]+@[A-Aa-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(not(re.fullmatch(regex,mail))):
            self.mail_2.setText("Email False")
            self.mail.clear()


        section=self.section.currentText()
        date_naissance=self.date_naissance.text()
        adresse=self.adresse.text()
        mail=self.mail.text()
        niveau_etude=self.niveauetude.text()
        if (not (niveau_etude.isnumeric())):
            self.niveau_etude.setText("Level False")
            self.niveauetude.clear()
        else:
            self.niveau_etude.setText("")
        if(not(niveau_etude.isnumeric)):
            self.niveau_etude.setText("Level False")


        num_inscr = self.num_inscription_2.text()
        n = self.nom_2.text()
        p = self.prenom_2.text()
        ad= self.adresse_3.text()
        ma = self.mail_2.text()
        tele= self.telephone_2.text()
        niv = self.niveau_etude.text()
        if (n == p == num_inscr == ad == ma ==tele==niv and ok == 1):
            L = [nom, prenom, date_naissance, adresse, mail, telephone,section,niveau_etude]
            etudiant[num_inscription] = [nom, prenom, date_naissance, adresse, mail, telephone,section,niveau_etude]
            print(etudiant)
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Success")
            msge.setText("Data Saved Successfully")
            msge.setInformativeText("Wanna ADD another Student ?")
            msge.setIcon(QtWidgets.QMessageBox.Question)
            msge.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msge.buttonClicked.connect(self.fate)
            x = msge.exec_()
        else:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("ERROR :D")
            #msge.setInformativeText("Validate your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        if ok == 0:
            self.num_inscription_2.setText("This Student Already Exists")
        
    def fate(self,i):
        if i.text()=="&Yes":
            self.num_inscription.clear()
            self.nom.clear()
            self.prenom.clear()
            self.telephone.clear()
            self.adresse.clear()
            self.mail.clear()
            self.niveauetude.clear()

        else:
            widget.setCurrentIndex(0)
#***********************************************************************
class ajout_matiere(QDialog):
    def __init__(self):
        super(ajout_matiere,self).__init__()
        loadUi("ajout_matiere1.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.ajouter.clicked.connect(self.button_ajouter)
    def Return(self):
        widget.setCurrentIndex(0)
    def button_ajouter(self):
        global matiere
        code = self.code.text()
        ok = 1
        for key in matiere.keys():
            if key == code:
                ok = 0
        if (code== ""):
            self.code_2.setText("Code False")
            self.code.clear()
        elif(not(code.isnumeric)):
            self.code_2.setText("Code False")
        else:
            self.code_2.setText("")

        coefficient= self.coefficient.text()
        if (coefficient==""):
            self.coefficient_2.setText("coefficient False")
            self.coefficient.clear()
        elif(not(coefficient.isnumeric)):
            self.coefficient_2.setText("coefficient False")
        else:
            self.coefficient_2.setText("")


        designation = self.designation.text()
        if (designation==""):
            self.designation_2.setText("designation False")
            self.designation.clear()
        elif(designation.isnumeric()):
            self.designation_2.setText("designation False")
        else:
            self.designation_2.setText("")

        section = self.section.currentText()
        semestre = self.semestre.currentText()

        cod = self.code_2.text()
        coe = self.coefficient_2.text()
        desig= self.designation_2.text()

        if (cod == coe == desig  and ok == 1):
            L = [ coefficient, designation, section, semestre]
            matiere[code] =[ coefficient, designation, section, semestre]
            print(matiere)
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Success")
            msge.setText("Data Saved Successfully")
            msge.setInformativeText("Wanna ADD Another Subject ?")
            msge.setIcon(QtWidgets.QMessageBox.Question)
            msge.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msge.buttonClicked.connect(self.fate)
            x = msge.exec_()
        else:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("ERROR :D")
            msge.setInformativeText("Validate your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        if ok == 0:
            self.code_2.setText("This Subject Already Exists")

    def fate(self, i):
        if i.text() == "&Yes":
            self.code.clear()
            self.coefficient.clear()
            self.designation.clear()

        else:
            widget.setCurrentIndex(0)


#*****************************************************
class ajout_note(QDialog):
    def __init__(self):
        super(ajout_note,self).__init__()
        loadUi("ajout_note.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.ajouter.clicked.connect(self.button_ajouter)
    def Return(self):
        widget.setCurrentIndex(0)
    def button_ajouter(self):
        global note
        code_note = self.code_note.text()
        ok = 1
        for key in note.keys():
            if key == code_note:
                ok = 0
        if (code_note== ""):
            self.code_note_2.setText("code False")
            self.code_note.clear()
        elif (not(code_note.isnumeric)):
            self.code_note_2.setText("code False")
            self.code_note.clear()

        else:
            self.code_note_2.setText("")
        coefficient= self.coefficient.text()
        if (coefficient==""):
            self.coefficient_2.setText("coefficient False")
            self.coefficient.clear()
        elif(not(coefficient.isnumeric)):
            self.coefficient_2.setText("coefficient False")
            self.coefficient.clear()
        else:
            self.coefficient_2.setText("")
        nom = self.nom.text()
        if (nom==""):
            self.nom_2.setText("First Name False")
            self.nom.clear()
        elif (not(nom.isalpha)):
            self.nom_2.setText("First Name False")
            self.nom.clear()
        else:
            self.nom_2.setText("")
        code_matiere=self.code_matiere.text()
        if (code_matiere== ""):
            self.code_matiere_2.setText("Code False")
            self.code_matiere.clear()
        elif (not(code_matiere.isnumeric)):
            self.code_matiere_2.setText("Code False")
            self.code_matiere.clear()
        else:
            self.code_matiere_2.setText("")
        num_inscription = self.num_inscription.text()

        if (num_inscription==""):
            self.num_inscr.setText("Subscription ID False")
            self.num_inscription.clear()
        elif(not(num_inscription.isnumeric())):
            self.num_inscr.setText("Subscription ID False")
            self.num_inscription.clear()
        else:
            self.num_inscr.setText("")
        note_ds=self.note_ds.text()

        if(note_ds==""):
            self.note_ds_2.setText(" Mark False")
            self.note_ds.clear()
        elif(note_ds.isalpha()):
            self.note_ds_2.setText(" Mark False")
            self.note_ds.clear()
        elif(float(note_ds)>20):
            self.note_ds_2.setText(" Mark False")
            self.note_ds.clear()

        else:
            self.note_ds_2.setText("")
        note_ex = self.note_ex.text()
        if (note_ex == ""):
            self.note_ex_2.setText(" Mark False")
            self.note_ex.clear()
        elif (note_ex.isalpha()) :
            self.note_ex_2.setText(" Mark False")
            self.note_ex.clear()
        elif float(note_ex)>20:
            self.note_ex_2.setText(" Mark False")
            self.note_ex.clear()

        else:
            self.note_ex_2.setText("")


        section = self.section.currentText()
        semestre = self.semestre.currentText()

        cod_note = self.code_note_2.text()
        no = self.nom_2.text()
        coe= self.coefficient_2.text()
        cod_mat=self.code_matiere_2.text()
        not_ds = self.note_ds_2.text()
        not_ex=self.note_ex_2.text()
        inscr=self.num_inscr.text()
        if (cod_note==no==coe==cod_mat==not_ds==not_ex==inscr  and ok == 1):
            L = [ nom, coefficient, section, semestre,code_matiere,note_ds,note_ex,num_inscription]
            note[code_note] =[ nom, coefficient, section, semestre,code_matiere,note_ds,note_ex,num_inscription]
            print(note)
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Success")
            msge.setText("Data Saved Successfully")
            msge.setInformativeText("Wanna ADD Another Mark ?")
            msge.setIcon(QtWidgets.QMessageBox.Question)
            msge.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msge.buttonClicked.connect(self.fate)
            x = msge.exec_()
        else:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("ERROR :D")
            msge.setInformativeText("Validate your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        if ok == 0:
            self.code_2.setText("This MArk is ALready Exists")

    def fate(self, i):
        if i.text() == "&Yes":
            self.code_note.clear()
            self.coefficient.clear()
            self.nom.clear()
            self.code_matiere.clear()
            self.note_ds.clear()
            self.note_ex.clear()
            self.num_inscription.clear()

        else:
            widget.setCurrentIndex(0)

#***************************************************
class supprimer_etudiant(QDialog):
    def __init__(self):
        super(supprimer_etudiant,self).__init__()
        loadUi("supprimer.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.supprimer.clicked.connect(self.button_supprimer)
    def Return(self):
        widget.setCurrentIndex(0)

    def button_supprimer(self):
        global etudiant
        ok = 0
        num_inscription = self.num_inscription.text()
        for key in etudiant.keys():
            if key == num_inscription:
                ok = 1
                break

        if (num_inscription==""):
            self.num_inscription_2.setText("Subscription ID False")
            self.num_inscription.clear()
        elif ok == 0:
            self.num_inscription_2.setText("this Student is Already Exists")
            self.num_inscription.clear()
        else:
            self.num_inscription_2.setText("")
        m = self.num_inscription_2.text()
        if etudiant=={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText(" ")
            msge.setInformativeText("You Must BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

        elif (m == ""):
            for key in etudiant.keys():
                if num_inscription == key:
                    etudiant.pop(key)
                    print(etudiant)
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("Success")
                    msge.setText("Deleted Successfully")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x = msge.exec_()
                    break
        else:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText(" ")
            msge.setInformativeText("Validate ur Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

#********************suppression section donnee***********************************
class supprimer_section(QDialog):
    def __init__(self):
        super(supprimer_section, self).__init__()
        loadUi("supprimer_section.ui", self)
        self.annuler.clicked.connect(self.Return)
        self.supprimer.clicked.connect(self.button_supprimer)

    def Return(self):
        widget.setCurrentIndex(0)

    def button_supprimer(self):
        global etudiant
        ok = 0
        L = []
        section = self.section.currentText()
        for key in etudiant.keys():
            if etudiant[key][6] == section:
                ok = 1
        if (section== ""):
            self.section_2.setText("You Must Choose the Students Section")
            self.section.clear()
        if ok == 0:
            self.section_2.setText("This SEction Doesn't Exists")
            self.section.clear()
        else:
            self.section_2.setText("")
        m = self.section_2.text()
        if etudiant=={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No Content You Must DO The Back UP")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        elif (m == ""):
            for key in etudiant.keys():
                if etudiant[key][6] == section:
                    L.append(key)
            for i in L:
                etudiant.pop(i)
            print(etudiant)
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Success")
            msge.setText("Deleted Successfully")
            msge.setIcon(QtWidgets.QMessageBox.Information)
            x = msge.exec_()
        else:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

#*******************supprimer_niveau*****+*******************
class supprimer_niveau(QDialog):
    def __init__(self):
        super(supprimer_niveau, self).__init__()
        loadUi("supprimer_niveau.ui", self)
        self.annuler.clicked.connect(self.Return)
        self.supprimer.clicked.connect(self.button_supprimer)

    def Return(self):
        widget.setCurrentIndex(0)

    def button_supprimer(self):
        global etudiant
        ok = 0
        L = []
        niveau = self.niveau.text()
        for key in etudiant.keys():
            if etudiant[key][7] == niveau:
                ok = 1
        if (niveau== ""):
            self.niveau_2.setText("You must choose the Studies Level")
            self.niveau.clear()
        if ok == 0:
            self.niveau_2.setText("THis Level Doesn't Exist")
            self.niveau.clear()
        else:
            self.niveau_2.setText("")
        m = self.niveau_2.text()
        if etudiant=={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No content Yoou Must Do The BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        elif (m == ""):
            for key in etudiant.keys():
                if etudiant[key][7] == niveau:
                    L.append(key)
            for i in L:
                etudiant.pop(i)
            print(etudiant)
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Success")
            msge.setText("Deleted Successfully")
            msge.setIcon(QtWidgets.QMessageBox.Information)
            x = msge.exec_()
        else:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

#*******************supprimer_niveau_section*****+*******************
class supprimer_niveau_section(QDialog):
    def __init__(self):
        super(supprimer_niveau_section, self).__init__()
        loadUi("supprimer_section_niveau.ui", self)
        self.annuler.clicked.connect(self.Return)
        self.supprimer.clicked.connect(self.button_supprimer)

    def Return(self):
        widget.setCurrentIndex(0)

    def button_supprimer(self):
        global etudiant
        ok = 0
        L = []
        niveau = self.niveau.text()
        section=self.section.currentText()
        for key in etudiant.keys():
            if etudiant[key][7] == niveau and etudiant[key][6] == section:
                ok = 1
        if (niveau== ""):
            self.niveau_2.setText("You must choose the Studies Level")
            self.niveau.clear()
        if ok == 0:
            self.niveau_2.setText("THis Level Doesn't Exist")
            self.section_3.setText("This Section Doesn't Exist")
            self.niveau.clear()
        else:
            self.niveau_2.setText("")
            self.section_3.setText("")
        m = self.niveau_2.text()
        n=self.section_3.text()
        if etudiant=={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No content Yoou Must Do The BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        elif (m == ""and n==""):
            for key in etudiant.keys():
                if etudiant[key][7] == niveau and etudiant[key][6]==section:
                    L.append(key)
            for i in L:
                etudiant.pop(i)
            print(etudiant)
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Success")
            msge.setText("Deleted Successfully")
            msge.setIcon(QtWidgets.QMessageBox.Information)
            x = msge.exec_()
        else:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
#**********************supprimer matiere***************************************************
class supprimer_matiere(QDialog):
    def __init__(self):
        super(supprimer_matiere,self).__init__()
        loadUi("supprimer_matiere.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.supprimer.clicked.connect(self.button_supprimer)
    def Return(self):
        widget.setCurrentIndex(0)

    def button_supprimer(self):
        global matiere
        ok = 0
        code = self.code.text()
        for key in matiere.keys():
            if key == code:
                ok = 1
                break

        if (code==""):
            self.code_3.setText("Code False")
            self.code.clear()
        elif ok == 0:
            self.code_3.setText("This Subject Doesn't Exist")
            self.code.clear()
        else:
            self.code_3.setText("")
        m = self.code_3.text()
        if matiere=={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No content Yoou Must Do The BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        elif (m == ""):
            for key in matiere.keys():
                if code == key:
                    matiere.pop(key)
                    print(matiere)
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("Success")
                    msge.setText("Deleted Successfully")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x = msge.exec_()
                    break
        else:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText(" ")
            msge.setInformativeText("Validate ur Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
#**************************supprimer-note************************************
class supprimer_note(QDialog):
    def __init__(self):
        super(supprimer_note,self).__init__()
        loadUi("supprimer_note.ui",self)
        self.annuler.clicked.connect(self.Return)
        self.supprimer.clicked.connect(self.button_supprimer)
    def Return(self):
        widget.setCurrentIndex(0)

    def button_supprimer(self):
        global note
        ok = 0
        code = self.code.text()
        for key in note.keys():
            if key == code:
                ok = 1
                break

        if (code==""):
            self.code_3.setText("Code False")
            self.code.clear()
        elif ok == 0:
            self.code_3.setText("This Subject Doesn't Exist")
            self.code.clear()
        else:
            self.code_3.setText("")
        m = self.code_3.text()
        if note=={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No content Yoou Must Do The BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        elif (m == ""):
            for key in note.keys():
                if code == key:
                    note.pop(key)
                    print(note)
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("Success")
                    msge.setText("Deleted Successfully")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x = msge.exec_()
                    break
        else:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText(" ")
            msge.setInformativeText("Validate ur Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
#*******************modifier num de telephone*******************************
class modifier_tel(QDialog):
    def __init__(self):
        super(modifier_tel, self).__init__()
        loadUi("modifier_tel.ui", self)
        self.annuler.clicked.connect(self.Return)
        self.modifier.clicked.connect(self.modification)

    def Return(self):
        widget.setCurrentIndex(0)

    def modification(self):
        global etudiant
        ok = 0
        num_inscription = self.num_inscription.text()
        for key in etudiant.keys():
            if key == num_inscription:
                ok = 1
                break

        if (not(num_inscription.isnumeric)):
           self.num_insc.setText("Subscription Id False")
           self.num_inscription.clear()
        if ok == 0:
            self.num_insc.setText("This Student Doesn't exist")
            self.num_inscription.clear()
        else:
            self.num_insc.setText("")

        num= self.num.text()
        if (num== ""):
            self.num_2.setText("You Must chosoe the Phone Number")
            self.num.clear()
        elif (num.isalpha()):
            self.num_2.setText("Number False")
            self.num.clear()
        else:
            self.num_2.setText("")
        m = self.num_insc.text()
        c = self.num_2.text()
        print(m)
        print(c)
        if etudiant =={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No content Yoou Must Do The BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        elif (m == c == ""):
            for key in etudiant.keys():
                if key == num_inscription:
                    etudiant[key][5] = num
                    print(etudiant)
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("Success")
                    msge.setText("Data Saved Successfully")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x = msge.exec_()

        else:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

#********************modifier_mail********************
class modifier_mail(QDialog):
    def __init__(self):
        super(modifier_mail, self).__init__()
        loadUi("modifier_mail.ui", self)
        self.annuler.clicked.connect(self.Return)
        self.modifier.clicked.connect(self.modification)

    def Return(self):
        widget.setCurrentIndex(0)

    def modification(self):
        global etudiant
        ok = 0
        num_inscription = self.num_inscription.text()
        for key in etudiant.keys():
            if key == num_inscription:
                ok = 1
                break

        if (not(num_inscription.isnumeric)):
           self.num_insc.setText("Subscription Id False")
           self.num_inscription.clear()
        if ok == 0:
            self.num_insc.setText("This Student Doesn't exist")
            self.num_inscription.clear()
        else:
            self.num_insc.setText("")

        mail= self.mail.text()
        if (mail== ""):
            self.mail_2.setText("You Must choose the Email")
            self.mail.clear()
        else:
            self.mail_2.setText("")
        m = self.num_insc.text()
        c = self.mail_2.text()
        print(m)
        print(c)
        if etudiant=={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No content Yoou Must Do The BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

        elif (m == c == ""):
            for key in etudiant.keys():
                if key == num_inscription:
                    etudiant[key][4] = mail
                    print(etudiant)
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("Success")
                    msge.setText("Data Modified Successfully")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x = msge.exec_()

        else:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

class modifier_adresse(QDialog):
    def __init__(self):
        super(modifier_adresse, self).__init__()
        loadUi("modifier_adresse.ui", self)
        self.annuler.clicked.connect(self.Return)
        self.modifier.clicked.connect(self.modification)

    def Return(self):
        widget.setCurrentIndex(0)

    def modification(self):
        global etudiant
        ok = 0
        num_inscription = self.num_inscription.text()
        for key in etudiant.keys():
            if key == num_inscription:
                ok = 1
                break

        if(not(num_inscription.isnumeric)):
           self.num_insc.setText("Subscription Id False")
           self.num_inscription.clear()
        elif ok == 0:
            self.num_insc.setText("This Student Doesn't exist")
            self.num_inscription.clear()
        else:
            self.num_insc.setText("")

        adresse= self.adresse.text()
        if (adresse== ""):
            self.adresse_2.setText("You Must Choose the Adress")
            self.adresse.clear()
        else:
            self.adresse_2.setText("")
        m = self.num_insc.text()
        c = self.adresse_2.text()
        print(m)
        print(c)
        if etudiant=={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No content Yoou Must Do The BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        elif (m == c == ""):
            for key in etudiant.keys():
                if key == num_inscription:
                    etudiant[key][3] = adresse
                    print(etudiant)
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("Success")
                    msge.setText("Data Saved Successfully")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x = msge.exec_()

        else:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

class modifier_nommatiere(QDialog):
    def __init__(self):
        super(modifier_nommatiere, self).__init__()
        loadUi("modifier_nom_matiere.ui", self)
        self.annuler.clicked.connect(self.Return)
        self.modifier.clicked.connect(self.modification)

    def Return(self):
        widget.setCurrentIndex(0)

    def modification(self):
        global matiere
        ok = 0
        code = self.code.text()
        for key in matiere.keys():
            if key == code:
                ok = 1
                break

        if(not(code.isnumeric)):
           self.code_2.setText("Code False")
           self.code.clear()
        elif ok == 0:
            self.code_2.setText("This Subject Doesn't exist")
            self.code.clear()
        else:
            self.code_2.setText("")

        nom= self.nom.text()
        if (nom== ""):
            self.nom_2.setText("You must choose the first name")
            self.nom.clear()
        else:
            self.nom_2.setText("")
        m = self.code_2.text()
        c = self.nom_2.text()
        print(m)
        print(c)
        if matiere=={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No content Yoou Must Do The BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        elif (m == c == ""):
            for key in matiere.keys():
                if key == code:
                    matiere[key][1] = nom
                    print(matiere)
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("Success")
                    msge.setText("Data Saved Successfully")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x = msge.exec_()

        else:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

class modifier_coefficientmatiere(QDialog):
    def __init__(self):
        super(modifier_coefficientmatiere, self).__init__()
        loadUi("modifier_coefficient_matiere.ui", self)
        self.annuler.clicked.connect(self.Return)
        self.modifier.clicked.connect(self.modification)

    def Return(self):
        widget.setCurrentIndex(0)

    def modification(self):
        global matiere
        ok = 0
        code = self.code.text()
        for key in matiere.keys():
            if key == code:
                ok = 1
                break

        if(not(code.isnumeric)):
           self.code_2.setText("Code False")
           self.code.clear()
        elif ok == 0:
            self.code_2.setText("This Subject Doesn't exist")
            self.code.clear()
        else:
            self.code_2.setText("")

        coe= self.coe.text()
        if (coe== ""):
            self.coe_2.setText("You Must Choose the Coefficient ")
            self.coe.clear()
        else:
            self.coe_2.setText("")
        m = self.code_2.text()
        c = self.coe_2.text()
        print(m)
        print(c)
        if matiere=={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No content Yoou Must Do The BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        elif (m == c == ""):
            for key in matiere.keys():
                if key == code:
                    matiere[key][0] = coe
                    print(matiere)
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("Success")
                    msge.setText("Data Saved Successfully")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x = msge.exec_()

        else:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

class modifier_note(QDialog):
    def __init__(self):
        super(modifier_note, self).__init__()
        loadUi("modifier_note.ui", self)
        self.annuler.clicked.connect(self.Return)
        self.modifier.clicked.connect(self.modification)

    def Return(self):
        widget.setCurrentIndex(0)

    def modification(self):
        global note
        ok = 0
        code = self.code.text()
        for key in note.keys():
            if key == code:
                ok = 1
                break

        if(not(code.isnumeric)):
           self.code_2.setText("Code False")
           self.code.clear()
        elif ok == 0:
            self.code_2.setText("This Mark Doesn't Exist")
            self.code.clear()
        else:
            self.code_2.setText("")

        ds= self.ds.text()
        ex=self.ex.text()
        if (ds== "" ):
            self.ds_2.setText("You Must Choose the DS MArk")
            self.ds.clear()
        else:
            self.ds_2.setText("")
        if (ex== "" ):
            self.ex_2.setText("You Must Choose The Exam Mark")
            self.ex.clear()
        else:
            self.ex_2.setText("")
        m = self.code_2.text()
        c = self.ds_2.text()
        b=self.ex_2.text()
        print(m)
        print(c)
        if note=={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No content Yoou Must Do The BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        elif (m == c ==b== ""):
            for key in note.keys():
                if key == code:
                    note[key][5] = ds
                    note[key][6]=ex
                    print(note)
                    msge = QtWidgets.QMessageBox()
                    msge.setWindowTitle("Success")
                    msge.setText("Data Saved Successfully")
                    msge.setIcon(QtWidgets.QMessageBox.Information)
                    x = msge.exec_()

        else:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()


#****************************************
class dic_etudiant(QDialog):
    def __init__(self):
        super(dic_etudiant, self).__init__()
        loadUi("dic_etudiant.ui", self)
        self.affichage()
        self.ok.clicked.connect(self.Return)

    def Return(self):
        widget.setCurrentIndex(0)

    def affichage(self):
        global etudiant
        row = 0
        self.tableWidget.setRowCount(len(etudiant))
        if etudiant=={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No content Yoou Must Do The BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        else:
            for key in etudiant.keys():

                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(etudiant[key][0]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(etudiant[key][1]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(etudiant[key][2]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(etudiant[key][3]))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(etudiant[key][4]))
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(etudiant[key][5]))
                self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(etudiant[key][6]))
                self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(etudiant[key][7]))

                row = row + 1

#****************************************
class dic_matiere(QDialog):
    def __init__(self):
        super(dic_matiere, self).__init__()
        loadUi("dic_matiere.ui", self)
        self.affichage()
        self.ok.clicked.connect(self.Return)

    def Return(self):
        widget.setCurrentIndex(0)

    def affichage(self):
        global matiere
        row = 0
        self.tableWidget.setRowCount(len(matiere))
        if matiere=={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No content Yoou Must Do The BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        else:
            for key in matiere.keys():

                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(matiere[key][0]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(matiere[key][1]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(matiere[key][2]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(matiere[key][3]))


                row = row + 1


#****************************************
class dic_note(QDialog):
    def __init__(self):
        super(dic_note, self).__init__()
        loadUi("dic_note.ui", self)
        self.affichage()
        self.ok.clicked.connect(self.Return)

    def Return(self):
        widget.setCurrentIndex(0)

    def affichage(self):
        global note
        row = 0
        self.tableWidget.setRowCount(len(note))
        if note=={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No content Yoou Must Do The BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        else:
            for key in note.keys():

                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(note[key][0]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(note[key][1]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(note[key][2]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(note[key][3]))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(note[key][4]))
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(note[key][5]))
                self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(note[key][6]))
                self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(note[key][7]))


                row = row + 1

#***************************************************************
class recherche_num_inscription(QDialog):
    def __init__(self):
        super(recherche_num_inscription, self).__init__()
        loadUi("recherche_num_inscr.ui", self)
        self.ok.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.chercher)

    def Return(self):
        widget.setCurrentIndex(0)

    def chercher(self):
        global etudiant
        L = []
        num_inscription= self.num_inscription.text()
        if (num_inscription== ""):
            self.num.setText("You Must Choose The Subscription ID")
            self.num_inscription.clear()
        else:
            self.num.setText("")
            num_inscription = self.num_inscription.text()

        for key in etudiant.keys():
            if key==num_inscription:
                L.append(key)

        if etudiant =={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No content Yoou Must Do The BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        elif (len(L) == 0):
            self.num.setText("This Num Doesn't Exist")
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        row = 0
        self.tableWidget.setRowCount(len(L))
        for i in L:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(etudiant[i][0]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(etudiant[i][1]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(etudiant[i][2]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(etudiant[i][3]))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(etudiant[i][4]))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(etudiant[i][5]))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(etudiant[i][6]))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(etudiant[i][7]))
            row = row + 1

#**********************************************************************

class recherche_sect(QDialog):
    def __init__(self):
        super(recherche_sect, self).__init__()
        loadUi("recherche_section.ui", self)
        self.ok.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.chercher)

    def Return(self):
        widget.setCurrentIndex(0)

    def chercher(self):
        global etudiant
        L = []
        section= self.section.currentText()
        if (section== ""):
            self.section_2.setText("You Must Choose The Section")
            
        else:
            self.section_2.setText("")
            section= self.section.currentText()

        for key in etudiant.keys():
            if etudiant[key][6] == section:
                L.append(key)
        if etudiant =={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No content Yoou Must Do The BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        elif (len(L) == 0):
            self.section_2.setText("This Section Doesn't Exist")
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

        row = 0
        self.tableWidget.setRowCount(len(L))
        for i in L:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(etudiant[i][0]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(etudiant[i][1]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(etudiant[i][2]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(etudiant[i][3]))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(etudiant[i][4]))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(etudiant[i][5]))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(etudiant[i][6]))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(etudiant[i][7]))
            row = row + 1


#***************************************************************
class recherche_niv(QDialog):
    def __init__(self):
        super(recherche_niv, self).__init__()
        loadUi("recherche_niveau.ui", self)
        self.ok.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.chercher)

    def Return(self):
        widget.setCurrentIndex(0)

    def chercher(self):
        global etudiant
        L = []
        niveau= self.niveau.text()
        if (niveau== ""):
            self.niveau_2.setText("You Must Choose The Level")
            self.niveau.clear()
        else:
            self.niveau_2.setText("")
            niveau= self.niveau.text()

        for key in etudiant.keys():
            if etudiant[key][7] == niveau:
                L.append(key)
        if etudiant =={}:
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("EROOR :D")
            msge.setText(" ")
            msge.setInformativeText(" There is No content Yoou Must Do The BackUp")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        elif (len(L) == 0):
            self.niveau_2.setText("THis Level Doesn't Exist")
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

        row = 0

        self.tableWidget.setRowCount(len(L))
        for i in L:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(etudiant[i][0]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(etudiant[i][1]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(etudiant[i][2]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(etudiant[i][3]))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(etudiant[i][4]))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(etudiant[i][5]))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(etudiant[i][6]))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(etudiant[i][7]))
            row = row + 1

    # ***************************************************************
class recherche_niv_sec(QDialog):
        def __init__(self):
            super(recherche_niv_sec, self).__init__()
            loadUi("recherche_section_niveau.ui", self)
            self.ok.clicked.connect(self.Return)
            self.afficher.clicked.connect(self.chercher)

        def Return(self):
            widget.setCurrentIndex(0)

        def chercher(self):
            global etudiant
            L = []
            niveau = self.niveau.text()
            section=self.section.currentText()
            if (niveau == ""):
                self.niveau_2.setText("You Must Choose The Level")
                self.niveau.clear()
            else:
                self.niveau_2.setText("")
                niveau = self.niveau.text()
            if (section == ""):
                self.section_2.setText("You Must Choose The Section")
                self.section.clear()
            else:
                self.section_2.setText("")
                section = self.section.currentText()

            for key in etudiant.keys():
                if etudiant[key][7] == niveau and etudiant[key][6]==section:
                    L.append(key)
            if (len(L) == 0):
                self.niveau_2.setText("Doesn't Exist")
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("Failed")
                msge.setText("Something is Wrong")
                msge.setInformativeText("Validate Your Data")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x = msge.exec_()

            row = 0
            self.tableWidget.setRowCount(len(L))
            for i in L:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(etudiant[i][0]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(etudiant[i][1]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(etudiant[i][2]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(etudiant[i][3]))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(etudiant[i][4]))
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(etudiant[i][5]))
                self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(etudiant[i][6]))
                self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(etudiant[i][7]))
                row = row + 1

#*************************recherche code matiere***********************************************
class recherche_code_matiere(QDialog):
    def __init__(self):
        super(recherche_code_matiere, self).__init__()
        loadUi("recherche_code_matiere.ui", self)
        self.ok.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.chercher)

    def Return(self):
        widget.setCurrentIndex(0)

    def chercher(self):
        global matiere
        L = []
        code= self.code.text()
        if (code== ""):
            self.code_2.setText("You Must Choose the Code")
            self.code.clear()
        else:
            self.code_2.setText("")
            code = self.code.text()

        for key in matiere.keys():
            if key==code:
                L.append(key)
        if (len(L) == 0):
            self.code_2.setText("This Code Doesn't Exist")
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

        row = 0
        self.tableWidget.setRowCount(len(L))
        for i in L:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(matiere[i][0]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(matiere[i][1]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(matiere[i][2]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(matiere[i][3]))
            row = row + 1

#*****************recherche_section matiere******************************
class recherche_sec_matiere(QDialog):
    def __init__(self):
        super(recherche_sec_matiere, self).__init__()
        loadUi("recherche_section_matiere.ui", self)
        self.ok.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.chercher)

    def Return(self):
        widget.setCurrentIndex(0)

    def chercher(self):
        global matiere
        L = []
        section = self.section.currentText()
        if (section == ""):
            self.section_2.setText("You Must Choose The Section")

        else:
            self.section_2.setText("")


        for key in matiere.keys():
            if matiere[key][2] == section:
                L.append(key)
        if (len(L) == 0):
            self.section_2.setText("This Section Doesn't Exist")
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

        row = 0
        self.tableWidget.setRowCount(len(L))
        for i in L:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(matiere[i][0]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(matiere[i][1]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(matiere[i][2]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(matiere[i][3]))
            row = row + 1



#************************recherche section_semestre matiere**************************
class recherche_sec_semestre_matiere(QDialog):
    def __init__(self):
        super(recherche_sec_semestre_matiere, self).__init__()
        loadUi("recherche_section_semestre_matiere.ui", self)
        self.ok.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.chercher)

    def Return(self):
        widget.setCurrentIndex(0)

    def chercher(self):
        global matiere
        L = []
        section = self.section.currentText()
        semestre=self.semestre.currentText()
        if (section == ""):
            self.section_2.setText("You Must Choose The Section")

        else:
            self.section_2.setText("")
        if (semestre == ""):
            self.semestre_2.setText("You Must Choose The Section")

        else:
            self.semestre_2.setText("")

        for key in matiere.keys():
            if matiere[key][2] == section and matiere[key][3]==semestre:
                L.append(key)
        if (len(L) == 0):
            self.section_2.setText("This Section Doesn't Exist")
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

        row = 0
        self.tableWidget.setRowCount(len(L))
        for i in L:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(matiere[i][0]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(matiere[i][1]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(matiere[i][2]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(matiere[i][3]))
            row = row + 1

#******************recherche num inscription note**********************************
class recherche_num_inscription_note(QDialog):
    def __init__(self):
        super(recherche_num_inscription_note, self).__init__()
        loadUi("recherche_num_inscr_note.ui", self)
        self.ok.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.chercher)

    def Return(self):
        widget.setCurrentIndex(0)

    def chercher(self):
        global note
        L = []
        num_inscription= self.num_inscription.text()
        if (num_inscription== ""):
            self.num.setText("You Must Choose The Subscription ID")
            self.num_inscription.clear()
        else:
            self.num.setText("")
            num_inscription = self.num_inscription.text()

        for key in note.keys():
            if note[key][7]==num_inscription:
                L.append(key)
        if (len(L) == 0):
            self.num.setText("This Num Doesn't Exist")
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

        row = 0
        self.tableWidget.setRowCount(len(L))
        for i in L:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(note[i][0]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(note[i][1]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(note[i][2]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(note[i][3]))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(note[i][4]))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(note[i][5]))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(note[i][6]))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(note[i][7]))

            row = row + 1
#*******************recherchesection et niveau*************************************
class recherche_niveau_section_note(QDialog):
    def __init__(self):
        super(recherche_niveau_section_note, self).__init__()
        loadUi("recherche_section_niveau_note.ui", self)
        self.ok.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.chercher)

    def Return(self):
        widget.setCurrentIndex(0)

    def chercher(self):
        global note
        L = []

        section = self.section.currentText()

        if (section == ""):
            self.section_2.setText("You Must Choose The Section")
        else:
            self.section_2.setText("")
            section = self.section.currentText()

        for key in note.keys():
            if  note[key][2] == section:
                L.append(key)
        if (len(L) == 0):
            self.section_2.setText("Doesn't Exist")
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

        row = 0
        self.tableWidget.setRowCount(len(L))
        for i in L:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(note[i][0]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(note[i][1]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(note[i][2]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(note[i][3]))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(note[i][4]))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(note[i][5]))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(note[i][6]))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(note[i][7]))

            row = row + 1
#*******************recherche num inscription et semestre****************************
class recherche_num_inscription_semestre_note(QDialog):
    def __init__(self):
        super(recherche_num_inscription_semestre_note, self).__init__()
        loadUi("recherche_num_semestre_NOTE.ui", self)
        self.ok.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.chercher)

    def Return(self):
        widget.setCurrentIndex(0)

    def chercher(self):
        global note
        L = []
        num_inscription= self.num_inscription.text()
        semestre = self.semestre.currentText()

        if (semestre == ""):
            self.semestre_2.setText("You Must Choose The Section")

        else:
            self.semestre_2.setText("")

        if (num_inscription== ""):
            self.num.setText("You Must Choose The Subscription ID")
            self.num_inscription.clear()
        else:
            self.num.setText("")
            num_inscription = self.num_inscription.text()

        for key in note.keys():
            if note[key][7]==num_inscription and note[key][3]==semestre:
                L.append(key)
        if (len(L) == 0):
            self.num.setText("This Num Doesn't Exist")
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()

        row = 0
        self.tableWidget.setRowCount(len(L))
        for i in L:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(note[i][0]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(note[i][1]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(note[i][2]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(note[i][3]))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(note[i][4]))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(note[i][5]))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(note[i][6]))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(note[i][7]))

            row = row + 1

#*************************bulletin_etudiant**************
class bulletin_etudiant(QDialog):
    def __init__(self):
        super(bulletin_etudiant, self).__init__()
        loadUi("bulletin_note1.ui", self)
        self.ok.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.chercher)
        

    def Return(self):
        widget.setCurrentIndex(0)


    def chercher(self):
        global etudiant
        global matiere
        global note
        L=[]
        num_inscription = self.num_inscription.text()
        if (num_inscription== ""):
            self.num.setText("You Must Choose The Subscription ID")
            self.num_inscription.clear()
        else:
            self.num.setText("")
        for key in note.keys():
            if note[key][7] == num_inscription:
                L.append(key)
        if (len(L) == 0):
            self.num.setText("This Num Doesn't Exist")
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        else:
            row = 0
            self.tableWidget.setRowCount(len(L))
            for i in L:

                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(note[i][0]))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(note[i][5]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(note[i][6]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(note[i][1]))


                row = row + 1

            m=0
            somme_coe=0
            for i in L:
                note_ds=float(note[i][5])
                note_ex=float(note[i][6])
                coefficient=float(note[i][1])

                m=m+(note_ds*0.3+note_ex*0.7)*coefficient
                somme_coe=somme_coe+coefficient

            moy=m/somme_coe
            print(moy)
            self.moyenne.setText("{:5.2f}".format(moy))
            if moy>=10:
                self.a.setText("SUCCEED")
            else:
                self.a.setText("REFUSED")
        for key in etudiant.keys():
                if num_inscription==key:
                    self.nom.setText("{}".format(etudiant[key][0]))
                    self.prenom.setText("{}".format(etudiant[key][1]))
                    self.section.setText("{}".format(etudiant[key][6]))
                    self.niveau.setText("{}".format(etudiant[key][7]))


class bulletin_etudiant_semestre(QDialog):
    def __init__(self):
        super(bulletin_etudiant_semestre, self).__init__()
        loadUi("bulletin_note_semestre.ui", self)
        self.ok.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.chercher)

    def Return(self):
        widget.setCurrentIndex(0)

    def chercher(self):
        global etudiant
        global matiere
        global note
        L = []
        num_inscription = self.num_inscription.text()
        semestre=self.semestre.currentText()
        if (num_inscription == ""):
            self.num.setText("You Must Choose The Subscription ID")
            self.num_inscription.clear()
        else:
            self.num.setText("")
        for key in note.keys():
            if note[key][7] == num_inscription and note[key][3]==semestre:
                L.append(key)
        if (len(L) == 0):
            self.num.setText("This Num Doesn't Exist")
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        else:
            row = 0
            self.tableWidget.setRowCount(len(L))
            for i in L:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(note[i][0]))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(note[i][5]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(note[i][6]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(note[i][1]))

                row = row + 1

            m = 0
            somme_coe = 0
            for i in L:
                note_ds = float(note[i][5])
                note_ex = float(note[i][6])
                coefficient = float(note[i][1])

                m = m + (note_ds * 0.3 + note_ex * 0.7) * coefficient
                somme_coe = somme_coe + coefficient

            moy = m / somme_coe
            print(moy)
            self.moyenne.setText("{:5.2f}".format(moy))
            if moy >= 10:
                self.a.setText("SUCCESS")
            else:
                self.a.setText("REFUSED")
        for key in etudiant.keys():
                if num_inscription==key :
                    self.nom.setText("{}".format(etudiant[key][0]))
                    self.prenom.setText("{}".format(etudiant[key][1]))
                    self.section.setText("{}".format(etudiant[key][6]))
                    self.niveau.setText("{}".format(etudiant[key][7]))

class etudiant_admis_section(QDialog):
    def __init__(self):
        super(etudiant_admis_section, self).__init__()
        loadUi("etudiant_admis_section.ui", self)
        self.ok.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.chercher)

    def Return(self):
        widget.setCurrentIndex(0)

    def chercher(self):
        global etudiant
        global matiere
        global note
        dic={}
        L = []
        section=self.section.currentText()
        if (section == ""):
            self.section_2.setText("You Must Choose The Section")

        else:
            self.section_2.setText("")
        for key in etudiant.keys():
            m = 0
            somme_coe = 0
            for i in note.keys():
                if key == note[i][7]:
                    note_ds = float(note[i][5])
                    note_ex = float(note[i][6])
                    coefficient = float(note[i][1])

                    m = m + (note_ds * 0.3 + note_ex * 0.7) * coefficient
                    somme_coe = somme_coe + coefficient

                if somme_coe>0:
                    moy = m / somme_coe
            print(moy)
            if moy>=10:
                L.append(key)
                dic[key]=moy
            print(etudiant)
        dic1={}
        l1=[]
        for i in L:
            if etudiant[i][6]==section:
                l1.append(i)
        for key in dic.keys():
            if etudiant[key][6]==section:
                dic1[key]=dic[key]
        if (len(l1) == 0):
            self.section_2.setText("This Section Doesn't Exist")
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        else:
            row = 0
            self.tableWidget.setRowCount(len(l1))
            for i in l1:

                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(etudiant[i][0]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(etudiant[i][1]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(etudiant[i][6]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(etudiant[i][7]))
                for key in dic1.keys():
                    if key == i:
                        self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str("{:5.2f}".format(dic1[key]))))

                row = row + 1

                


                row = row + 1


#******************etudiant redoublant d'une section donnee***************************
class etudiant_redoublant_section(QDialog):
    def __init__(self):
        super(etudiant_redoublant_section, self).__init__()
        loadUi("etudiant_redoublant_section.ui", self)
        self.ok.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.chercher)

    def Return(self):
        widget.setCurrentIndex(0)

    def chercher(self):
        global etudiant
        global matiere
        global note
        L = []
        dic={}
        section=self.section.currentText()
        if (section == ""):
            self.section_2.setText("You Must Choose The Section")

        else:
            self.section_2.setText("")
        for key in etudiant.keys():
            
                m = 0
                somme_coe = 0
                for i in note.keys():
                    if key == note[i][7]:
                        note_ds = float(note[i][5])
                        note_ex = float(note[i][6])
                        coefficient = float(note[i][1])

                        m = m + (note_ds * 0.3 + note_ex * 0.7) * coefficient
                        somme_coe = somme_coe + coefficient

                    if somme_coe>0:
                        moy = m / somme_coe
                print(moy)
                if moy<10 :
                    L.append(key)
                    dic[key] = moy

        l1=[]
        dic1={}
        for i in L:
            if etudiant[i][6]==section:
                l1.append(i)
        for key in dic.keys():
            if etudiant[key][6]==section:
                dic1[key]=dic[key]
        if (len(l1) == 0):
            self.section_2.setText("This Section Doesn't Exist")
            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        else:
            row = 0
            self.tableWidget.setRowCount(len(l1))
            for i in l1:

                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(etudiant[i][0]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(etudiant[i][1]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(etudiant[i][6]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(etudiant[i][7]))
                for key in dic1.keys():
                    if key == i:
                        self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str("{:5.2f}".format(dic1[key]))))



                row = row + 1

#*****************etudiant admis l'isimmmm***************************************
class etudiant_admis_isimm(QDialog):
    def __init__(self):
        super(etudiant_admis_isimm, self).__init__()
        loadUi("etudiant_admis_isimm.ui", self)
        self.ok.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.chercher)

    def Return(self):
        widget.setCurrentIndex(0)

    def chercher(self):
        global etudiant
        global matiere
        global note
        L = []
        dic={}

        for key in etudiant.keys():
            m = 0
            somme_coe = 0
            for i in note.keys():
                if key == note[i][7]:
                    note_ds = float(note[i][5])
                    note_ex = float(note[i][6])
                    coefficient = float(note[i][1])

                    m = m + (note_ds * 0.3 + note_ex * 0.7) * coefficient
                    somme_coe = somme_coe + coefficient

                if somme_coe>0:
                    moy = m / somme_coe
            print(moy)
            if moy>=10:
                L.append(key)
                dic[key]=moy
                print(dic)
        if (len(L) == 0):

            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        else:
            row = 0
            self.tableWidget.setRowCount(len(L))
            for i in L:

                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(etudiant[i][0]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(etudiant[i][1]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(etudiant[i][6]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(etudiant[i][7]))
                for key in dic.keys():
                    if key == i:
                        self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str("{:5.2f}".format(dic[key]))))

                row = row + 1

#*****************etudiant redoublant de  l'isimmmm***************************************
class etudiant_redoublant_isimm(QDialog):
    def __init__(self):
        super(etudiant_redoublant_isimm, self).__init__()
        loadUi("etudiant_redoublant_isimm.ui", self)
        self.ok.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.chercher)

    def Return(self):
        widget.setCurrentIndex(0)

    def chercher(self):
        global etudiant
        global matiere
        global note
        L = []
        dic={}

        for key in etudiant.keys():
            m = 0
            somme_coe = 0
            for i in note.keys():
                if key == note[i][7]:
                    note_ds = float(note[i][5])
                    note_ex = float(note[i][6])
                    coefficient = float(note[i][1])

                    m = m + (note_ds * 0.3 + note_ex * 0.7) * coefficient
                    somme_coe = somme_coe + coefficient

                if somme_coe>0:
                    moy = m / somme_coe
            print(moy)
            if moy<10:
                L.append(key)
                dic[key] = moy
                print(dic)


        if (len(L) == 0):

            msge = QtWidgets.QMessageBox()
            msge.setWindowTitle("Failed")
            msge.setText("Something is Wrong")
            msge.setInformativeText("Validate Your Data")
            msge.setIcon(QtWidgets.QMessageBox.Critical)
            x = msge.exec_()
        else:
            row = 0
            self.tableWidget.setRowCount(len(L))
            for i in L:

                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(etudiant[i][0]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(etudiant[i][1]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(etudiant[i][6]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(etudiant[i][7]))
                for key in dic.keys():
                    if key == i:
                        self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str("{:5.2f}".format(dic[key]))))



                row = row + 1

#****************moyenne section************************************
class moyenne_section(QDialog):
    def __init__(self):
        super(moyenne_section, self).__init__()
        loadUi("moyennes_etudiants.ui", self)
        self.ok.clicked.connect(self.Return)
        self.afficher.clicked.connect(self.chercher)

    def Return(self):
        widget.setCurrentIndex(0)

    def chercher(self):
        global etudiant
        global matiere
        global note
        L = []
        dic = {}
        section = self.section.currentText()
        if (section == ""):
            self.section_2.setText("You Must Choose The Section")

        else:
            self.section_2.setText("")

        for key in etudiant.keys():
            m = 0
            somme_coe = 0
            for i in note.keys():
                if key == note[i][7]:
                    note_ds = float(note[i][5])
                    note_ex = float(note[i][6])
                    coefficient = float(note[i][1])

                    m = m + (note_ds * 0.3 + note_ex * 0.7) * coefficient
                    somme_coe = somme_coe + coefficient

                if somme_coe > 0:
                    moy = m / somme_coe
            L.append(key)
            dic[key] = moy
            
        l1 = []
        dic1 = {}
        for i in L:
                if etudiant[i][6] == section:
                    l1.append(i)
        for key in dic.keys():
                if etudiant[key][6] == section:
                    dic1[key] = dic[key]
        if (len(l1) == 0):
                self.section_2.setText("This Section Doesn't Exist")
                msge = QtWidgets.QMessageBox()
                msge.setWindowTitle("Failed")
                msge.setText("Something is Wrong")
                msge.setInformativeText("Validate Your Data")
                msge.setIcon(QtWidgets.QMessageBox.Critical)
                x = msge.exec_()
        else:
                row = 0
                self.tableWidget.setRowCount(len(l1))
                for i in l1:

                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i))
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(etudiant[i][0]))
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(etudiant[i][1]))
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(etudiant[i][6]))
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(etudiant[i][7]))
                    for key in dic.keys():
                        if key == i:
                            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str("{:5.2f}".format(dic1[key]))))

                    row = row + 1


app=QApplication(sys.argv)
mainwindow=main()

widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1200)
widget.setFixedHeight(800)
widget.show()
msge = QtWidgets.QMessageBox()
msge.setWindowTitle("")
msge.setText("FIRST OF ALL DO THE BACKUP ")
#msge.setInformativeText("Validate Your Data")
msge.setIcon(QtWidgets.QMessageBox.Critical)
x = msge.exec_()
app.exec_()





