# import all dependencies
from csv import get_dialect
from tkinter import *
from tkinter import messagebox, ttk

import easygui
from PIL import Image, ImageTk
from tkcalendar import Calendar
from  datetime import datetime
import mysql.connector as sqlcon
import pyglet
import random

# config main window
pyglet.font.add_file(r"Data\\Miscs\\Evogria.otf")
pyglet.font.load("evogria")

root = Tk()
root.title("DYPIT Hospital")
root.iconbitmap(r"Data\\Images\\Icons\\plus.ico")
root.config(bg = "#FFFFFF")
root.state("zoomed")
root.resizable(False, False)

# top frame (constant)
top_frame = LabelFrame(root)
top_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 8)
top_frame.grid_propagate(0)

# title
title = Label(top_frame, text = "DYPIT Hospital", font = "evogria 45", 
    bg = "#FFE2E2", width = 42, anchor = CENTER)
title.pack()

# left frame (constant)
left_frame = LabelFrame(root, bg = "#FFE2E2")
left_frame.grid(row = 2, column = 0, padx = 4, pady = 4, columnspan = 3, ipady = 40)

# right frame (varies)
right_frame = LabelFrame(root, width = 979, height = 700, bg = "#FFE2E2")
right_frame.grid(row = 2, column = 4, columnspan = 4)
right_frame.grid_propagate(0)


# define all functions
# clean right frame - use in every button
def clean_right_frame():
    global right_frame

    main_window()

    right_frame.grid_forget()
    right_frame = LabelFrame(root, width = 979, height = 700, bg = "#FFE2E2")
    right_frame.grid(row = 2, column = 4, columnspan = 4)
    right_frame.grid_propagate(0)


# clean left and top frame (for services offered window)
def clean_left_frame():
    global left_frame

    main_window()

    left_frame.grid_forget()
    left_frame = LabelFrame(root, bg = "#FFE2E2")
    left_frame.grid(row = 2, column = 0, padx = 4, pady = 4, columnspan = 3, ipady = 40)
    left_frame.grid_propagate(0)


def clean_top_frame():
    global top_frame

    main_window()

    top_frame.grid_forget()
    top_frame = LabelFrame(root, bg = "#FFE2E2")
    top_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 8)
    top_frame.grid_propagate(0)


# registration main window
def registration_window():
    global registration
    clean_right_frame()

    # highlight clicked button
    registration.grid_forget()
    registration = Button(left_frame, text = "Registration", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#2A363B", 
                    fg = "#FF847C", anchor = CENTER, relief = SUNKEN, command = registration_window)
    registration.grid(row = 0, column = 0, columnspan = 3, pady = 5, padx = 20)

    global name_entry
    global age_entry
    global gender_entry
    global contact_entry
    global address_entry
    global blood_group_entry

    # labels
    name_label = Label(right_frame, text = "Name", font = "consolas 25 bold", bg = "#FFE2E2")
    age_label = Label(right_frame, text = "Age", font = "consolas 25 bold", bg = "#FFE2E2")
    gender_label = Label(right_frame, text = "Gender", font = "consolas 25 bold", bg = "#FFE2E2")
    contact_label = Label(right_frame, text = "Contact No.", font = "consolas 25 bold", bg = "#FFE2E2")
    address_label = Label(right_frame, text = "Address", font = "consolas 25 bold", bg = "#FFE2E2")
    blood_group_label = Label(right_frame, text = "Blood Group", font = "consolas 25 bold", bg = "#FFE2E2")

    name_label.grid(row = 0, column = 0, padx = 10, sticky = W)
    age_label.grid(row = 1, column = 0, padx = 10, sticky = W)
    gender_label.grid(row = 2, column = 0, padx = 10, sticky = W)
    contact_label.grid(row = 3, column = 0, padx = 10, sticky = W)
    address_label.grid(row = 4, column = 0, padx = 10, sticky = W)
    blood_group_label.grid(row = 5, column = 0, padx = 10, sticky = W)

    for i in range(6):
        colon = Label(right_frame, text = ":", font = "consolas 25 bold", bg = "#FFE2E2")
        colon.grid(row = i, column = 1, sticky = W)

    # entry fields
    name_entry = Entry(right_frame, font = "consolas 20")
    age_entry = Entry(right_frame, font = "consolas 20")
    gender_entry = Entry(right_frame, font = "consolas 20")
    contact_entry = Entry(right_frame, font = "consolas 20")
    address_entry = Entry(right_frame, font = "consolas 20")
    blood_group_entry = Entry(right_frame, font = "consolas 20")

    name_entry.grid(row = 0, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)
    age_entry.grid(row = 1, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)
    gender_entry.grid(row = 2, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)
    contact_entry.grid(row = 3, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)
    address_entry.grid(row = 4, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)
    blood_group_entry.grid(row = 5, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)

    # submit button
    submit_button = Button(right_frame, text = "Register", font = "consolas 20 bold", 
                    bg = "#FF847C", borderwidth = 7, padx = 10, pady = 4, command = registration_submit)
    submit_button.grid(row = 6, column = 0, columnspan = 4, padx = 10, pady = 54, ipadx = 350)
    submit_button.update()

def doctor_registration_window():
    global doctor_registration
    clean_right_frame()

    # highlight clicked button
    doctor_registration.grid_forget()
    doctor_registration = Button(left_frame, text = "Doctor Registration", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#2A363B", 
                    fg = "#FF847C", anchor = CENTER, relief = SUNKEN, command = doctor_registration_window)
    doctor_registration.grid(row = 6, column = 0, columnspan = 3, pady = 5, padx = 20)

    global doc_name_entry
    global doc_age_entry
    global doc_contact_entry
    global doc_specialisation_entry
    global doc_qualification_entry

    # labels
    doc_name_label = Label(right_frame, text = "Doctor Name", font = "consolas 25 bold", bg = "#FFE2E2")
    doc_age_label = Label(right_frame, text = "Age", font = "consolas 25 bold", bg = "#FFE2E2")
    doc_contact_label = Label(right_frame, text = "Contact No.", font = "consolas 25 bold", bg = "#FFE2E2")
    doc_specialisation_label = Label(right_frame, text = "specialisation", font = "consolas 25 bold", bg = "#FFE2E2")
    doc_qualification_label = Label(right_frame, text = "qualification", font = "consolas 25 bold", bg = "#FFE2E2")

    doc_name_label.grid(row = 0, column = 0, padx = 10, sticky = W)
    doc_age_label.grid(row = 1, column = 0, padx = 10, sticky = W)
    doc_contact_label.grid(row = 2, column = 0, padx = 10, sticky = W)
    doc_specialisation_label.grid(row = 3, column = 0, padx = 10, sticky = W)
    doc_qualification_label.grid(row = 4, column = 0, padx = 10, sticky = W)

    for i in range(5):
        colon = Label(right_frame, text = ":", font = "consolas 25 bold", bg = "#FFE2E2")
        colon.grid(row = i, column = 1, sticky = W)

    # entry fields
    doc_name_entry = Entry(right_frame, font = "consolas 20")
    doc_age_entry = Entry(right_frame, font = "consolas 20")
    doc_contact_entry = Entry(right_frame, font = "consolas 20")
    doc_specialisation_entry = Entry(right_frame, font = "consolas 20")
    doc_qualification_entry = Entry(right_frame, font = "consolas 20")

    doc_name_entry.grid(row = 0, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)
    doc_age_entry.grid(row = 1, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)
    doc_contact_entry.grid(row = 2, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)
    doc_specialisation_entry.grid(row = 3, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)
    doc_qualification_entry.grid(row = 4, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)

    # submit button
    submit_button = Button(right_frame, text = "Register", font = "consolas 20 bold", 
                    bg = "#FF847C", borderwidth = 7, padx = 10, pady = 4, command = doctor_registration_submit)
    submit_button.grid(row = 5, column = 0, columnspan = 4, padx = 10, pady = 54, ipadx = 350)
    submit_button.update()

# patient details main window
def patient_details_window():
    clean_right_frame()

    global right_frame
    global patient_details
    global field_to_search
    global search_detail_entry
    global submit_button

    # highlight clicked button
    patient_details.grid_forget()
    patient_details = Button(left_frame, text = "Patient Details", font = "consolas 19 bold", 
                width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#2A363B", fg = "#FF847C", 
                anchor = CENTER, relief = SUNKEN, command = patient_details_window)
    patient_details.grid(row = 1, column = 0, columnspan = 3, pady = 5, padx = 20)

    # search button
    submit_button = Button(right_frame, text = "Search", font = "consolas 17 bold", bg = "#FF847C", 
                borderwidth = 7, padx = 10, pady = 4, command = patient_details_search_submit)
    submit_button.grid(row = 2, column = 0, columnspan = 4, padx = 10, pady = 54, ipadx = 375)

    # select a field to search
    field_to_search_label = Label(right_frame, text = "Field", font = "consolas 19 bold", bg = "#FFE2E2")
    search_detail_label = Label(right_frame, text = "Details", font = "consolas 19 bold", bg = "#FFE2E2")

    field_to_search_label.grid(row = 0, column = 0, padx = 5, sticky = W)
    search_detail_label.grid(row = 1, column = 0, padx = 5, sticky = W)

    for j in range(2):
        colon = Label(right_frame, text = ":", font = "consolas 20 bold", bg = "#FFE2E2")
        colon.grid(row = j, column = 1, sticky = W)

    field_to_search_options = ["PID", "Name", "Age", "Gender", "Contact", "Address", "Blood Group"]

    field_to_search = StringVar()
    field_to_search.set("Name")

    field_to_search_menu = OptionMenu(right_frame, field_to_search, *field_to_search_options)
    field_to_search_menu.config(width = 62, height = 1, font = "consolas 15 bold")
    field_to_search_menu.grid(row = 0, column = 2, columnspan = 3, padx = 15, pady = 5, sticky = W)

    search_detail_entry = Entry(right_frame, font = "consolas 17")
    search_detail_entry.grid(row = 1, column = 2, ipadx = 230, ipady = 5, padx = 15, pady = 10)
    submit_button.update()


# display patient details after search
def display_patient_details_after_search():
    global searched_patient_details
    global patient_details
    global resized_profile_pic_final
    global display_profile_pic

    clean_right_frame()

    # highlight clicked button
    patient_details.grid_forget()
    patient_details = Button(left_frame, text = "Patient Details", font = "consolas 19 bold", 
                width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#2A363B", fg = "#FF847C", 
                anchor = CENTER, relief = SUNKEN, command = patient_details_window)
    patient_details.grid(row = 1, column = 0, columnspan = 3, pady = 5, padx = 20)

    # select a random image for profile pic
    profile_pic_1 = Image.open(r"Data\\Images\\Profile Pics\\dp1.png")
    profile_pic_2 = Image.open(r"Data\\Images\\Profile Pics\\dp2.png")
    profile_pic_3 = Image.open(r"Data\\Images\\Profile Pics\\dp3.png")
    profile_pic_4 = Image.open(r"Data\\Images\\Profile Pics\\dp4.png")
    profile_pic_5 = Image.open(r"Data\\Images\\Profile Pics\\dp5.png")

    profile_pics = [profile_pic_1, profile_pic_2, profile_pic_3, profile_pic_4, profile_pic_5]

    random_profile_pic = random.choice(profile_pics)

    resized_profile_pic = random_profile_pic.resize((100, 100), Image.ANTIALIAS)
    resized_profile_pic_final = ImageTk.PhotoImage(resized_profile_pic)

    display_profile_pic = Label(right_frame, image = resized_profile_pic_final, 
                width = 100, bd = 2, relief = SOLID, anchor = CENTER)
    display_profile_pic.grid(row = 0, column = 0, padx = 5, pady = 5, columnspan = 4)

    # display details
    name_label = Label(right_frame, text = searched_patient_details[1], font = "evogria 30", bg = "#FFE2E2", 
                width = 40, anchor = CENTER)
    pid_label = Label(right_frame, text = searched_patient_details[0], font = "evogria 22", bg = "#FFE2E2", 
                width = 47, anchor = CENTER)

    name_label.grid(row = 1, column = 0, padx = 5, pady = 3, columnspan = 4)
    pid_label.grid(row = 2, column = 0, padx = 5, pady = 3, columnspan = 4)

    # blank label
    blank_label = Label(right_frame, text = "", bg = "#FFE2E2")
    blank_label.grid(row = 3, pady = 5)

    for i in range(6):
        blank_label = Label(right_frame, text = "", bg = "#FFE2E2")
        blank_label.grid(row = i + 4, column = 0, padx = 20)

    # labels
    age_label = Label(right_frame, text = "Age", font = "consolas 19 bold", 
            bg = "#FFE2E2", width = 13, anchor = E)

    gender_label = Label(right_frame, text = "Gender", font = "consolas 19 bold", 
            bg = "#FFE2E2", width = 13, anchor = E)

    contact_label = Label(right_frame, text = "Contact", font = "consolas 19 bold", 
            bg = "#FFE2E2", width = 13, anchor = E)

    address_label = Label(right_frame, text = "Address", font = "consolas 19 bold", 
            bg = "#FFE2E2", width = 13, anchor = E)

    blood_group_label = Label(right_frame, text = "Blood Group", font = "consolas 19 bold", 
            bg = "#FFE2E2", width = 13, anchor = E)

    appointment_label = Label(right_frame, text = "Appointment", font = "consolas 19 bold", 
            bg = "#FFE2E2", width = 13, anchor = E)

    age_label.grid(row = 4, column = 1, pady = 3, sticky = W)
    gender_label.grid(row = 5, column = 1, pady = 3, sticky = W)
    contact_label.grid(row = 6, column = 1, pady = 3, sticky = W)
    address_label.grid(row = 7, column = 1, pady = 3, sticky = W)
    blood_group_label.grid(row = 8, column = 1, pady = 3, sticky = W)
    appointment_label.grid(row = 9, column = 1, pady = 3, sticky = W)

    for i in range(6):
        colon = Label(right_frame, text = ":", font = "consolas 20 bold", bg = "#FFE2E2")
        colon.grid(row = i + 4, column = 2, sticky = W)

    # get appointment details
    if (len(searched_patient_details) == 7):
        details = "No appointments yet"
    else:
        details = "You have an appointment with {} on {}".format(searched_patient_details[7],
                                                                 searched_patient_details[8])

    # display details
    patient_details_age_label = Label(right_frame, text = searched_patient_details[2], 
            font = "consolas 19 bold", bg = "#FFE2E2", width = 15, anchor = W)

    patient_details_gender_label = Label(right_frame, text = searched_patient_details[3], 
            font = "consolas 19 bold", bg = "#FFE2E2", width = 15, anchor = W)

    patient_details_contact_label = Label(right_frame, text = searched_patient_details[4], 
            font = "consolas 19 bold", bg = "#FFE2E2", width = 15, anchor = W)

    patient_details_address_label = Label(right_frame, text = searched_patient_details[5], 
            font = "consolas 19 bold", bg = "#FFE2E2", width = 15, anchor = W)

    patient_details_blood_group_label = Label(right_frame, text = searched_patient_details[6],
            font = "consolas 19 bold", bg = "#FFE2E2", width = 15, anchor = W)

    patient_details_appointment_label = Label(right_frame, text = details, font = "consolas 19 bold", 
            bg = "#FFE2E2", width = 15, anchor = W, wraplength = 225, justify = LEFT)

    patient_details_age_label.grid(row = 4, column = 2, padx = 5, pady = 3)
    patient_details_gender_label.grid(row = 5, column = 2, padx = 5, pady = 3)
    patient_details_contact_label.grid(row = 6, column = 2, padx = 5, pady = 3)
    patient_details_address_label.grid(row = 7, column = 2, padx = 5, pady = 3)
    patient_details_blood_group_label.grid(row = 8, column = 2, padx = 5, pady = 3)
    patient_details_appointment_label.grid(row = 9, column = 2, padx = 5, pady = 3)


# doctor"s details main window
def doctors_details_window():
    doctor_id_values, doctor_name_values, doctor_age_values, \
    doctor_contact_values, doctor_specialisation_values, \
    doctor_qualification_values = doctor_details_values()

    global doctor_details
    clean_right_frame()

    # highlight clicked button
    doctor_details.grid_forget()
    doctor_details = Button(left_frame, text = "Doctor Details", font = "consolas 19 bold", 
            width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#2A363B", fg = "#FF847C", 
            anchor = CENTER, relief = SUNKEN, command = patient_details_window)
    doctor_details.grid(row = 2, column = 0, columnspan = 3, pady = 5, padx = 20)

    # Doctors details
    sno_id = 1
    doctor_id_attribute = Label(right_frame, text = "ID", font = "evogria 17", width = 4, 
            anchor = CENTER, bg = "#FFE2E2")
    doctor_id_attribute.grid(row = 0, column = 0)
    for i in doctor_id_values:
        value = Label(right_frame, text = i, font = "consolas 14", bg = "#FFE2E2")
        value.grid(row = sno_id, column = 0)
        sno_id += 1

    sno_name = 1
    doctor_name_attribute = Label(right_frame, text = "Name", font = "evogria 17", width = 10, 
            anchor = CENTER, bg = "#FFE2E2")
    doctor_name_attribute.grid(row = 0, column = 1)
    for i in doctor_name_values:
        value = Label(right_frame, text = i, font = "consolas 14", bg = "#FFE2E2")
        value.grid(row = sno_name, column = 1)
        sno_name += 1

    sno_age = 1
    doctor_age_attribute = Label(right_frame, text = "Age", font = "evogria 17", width = 4, 
            anchor = CENTER, bg = "#FFE2E2")
    doctor_age_attribute.grid(row = 0, column = 2)
    for i in doctor_age_values:
        value = Label(right_frame, text = i, font = "consolas 14", bg = "#FFE2E2")
        value.grid(row = sno_age, column = 2)
        sno_age += 1

    sno_contact = 1
    doctor_contact_attribute = Label(right_frame, text = "Contact Number", font = "evogria 17", 
            width = 15, anchor = CENTER, wraplength = 100, justify = "center", bg = "#FFE2E2")
    doctor_contact_attribute.grid(row = 0, column = 3)
    for i in doctor_contact_values:
        value = Label(right_frame, text = i, font = "consolas 14", bg = "#FFE2E2")
        value.grid(row = sno_contact, column = 3)
        sno_contact += 1

    sno_specialisation = 1
    doctor_specialisation_attribute = Label(right_frame, text = "Specialistaion", font = "evogria 17", 
            width = 15, anchor = CENTER, bg = "#FFE2E2")
    doctor_specialisation_attribute.grid(row = 0, column = 4)
    for i in doctor_specialisation_values:
        value = Label(right_frame, text = i, font = "consolas 14", anchor = W, bg = "#FFE2E2")
        value.grid(row = sno_specialisation, column = 4)
        sno_specialisation += 1

    sno_qualification = 1
    doctor_qualification_attribute = Label(right_frame, text = "Qualification", font = "evogria 17", 
            width = 15, anchor = CENTER, bg = "#FFE2E2")
    doctor_qualification_attribute.grid(row = 0, column = 5)
    for i in doctor_qualification_values:
        value = Label(right_frame, text = i, font = "consolas 14", anchor = W, wraplength = 200, 
            justify = "center", bg = "#FFE2E2")
        value.grid(row = sno_qualification, column = 5)
        sno_qualification += 1

    doctor_qualification_attribute.update()
  


# modify details main window
def modify_details_window():
    global modify_details
    global check_pid_modify

    # get back to main menu
    home_submit()

    # check patient id
    check_pid_modify = easygui.enterbox(title = "Modify Details", msg = "Enter your PID")

    operation = """SELECT *
				FROM patient_details"""
    cursor.execute(operation)
    data = cursor.fetchall()
    existing_pid = []
    for i in data:
        existing_pid.append(str(i[0]))

    if (check_pid_modify in existing_pid):
        clean_right_frame()

        # highlight clicked button
        modify_details.grid_forget()
        modify_details = Button(left_frame, text = "Modify Details", font = "consolas 19 bold", width = 27, 
                    padx = 10, pady = 4, borderwidth = 7, bg = "#2A363B", fg = "#FF847C", anchor = CENTER, 
                    relief = SUNKEN, command = modify_details_window) 
        modify_details.grid(row = 4, column = 0, columnspan = 3, pady = 5, padx = 20)

        modify_details_after_verification()

    else:
        messagebox.showerror("Modify Details", "PID given is wrong")
        return ()


# modify details after verifying
def modify_details_after_verification():
    global old_details_frame
    global update_frame
    global field_to_update
    global updated_detail_entry
    global old_details

    # fetch old details of the patient
    operation = """SELECT *
				FROM patient_details
				WHERE pid = {}""".format(check_pid_modify)
    cursor.execute(operation)
    data = cursor.fetchone()

    old_details = [str(i) for i in data]
    for i in old_details[3]:
        if (i == "M"):
            old_details[1] = "Mr. " + old_details[1]
        else:
            old_details[1] = "Miss. " + old_details[1]

    # define frame
    # old details frame
    old_details_frame = LabelFrame(right_frame, height = 362, width = 1000, text = "Old Records", bg = "#FFE2E2")
    old_details_frame.grid(row = 0, column = 0, rowspan = 7, columnspan = 3, padx = 7)
    old_details_frame.grid_propagate(0)

    # update frame
    update_frame = LabelFrame(right_frame, height = 283, width = 1000, text = "Update Record", bg = "#FFE2E2")
    update_frame.grid(row = 8, column = 0, rowspan = 3, columnspan = 3, pady = 5, padx = 7)
    update_frame.grid_propagate(0)

    # old details
    # labels
    pid_label = Label(old_details_frame, text = "PID", font = "consolas 19 bold", bg = "#FFE2E2")
    name_label = Label(old_details_frame, text = "Name", font = "consolas 19 bold", bg = "#FFE2E2")
    age_label = Label(old_details_frame, text = "Age", font = "consolas 19 bold", bg = "#FFE2E2")
    gender_label = Label(old_details_frame, text = "Gender", font = "consolas 19 bold", bg = "#FFE2E2")
    contact_label = Label(old_details_frame, text = "Contact No.", font = "consolas 19 bold", bg = "#FFE2E2")
    address_label = Label(old_details_frame, text = "Address", font = "consolas 19 bold", bg = "#FFE2E2")
    blood_group_label = Label(old_details_frame, text = "Blood Group", font = "consolas 19 bold", bg = "#FFE2E2")

    pid_label.grid(row = 0, column = 0, padx = 5, pady = 3, sticky = W)
    name_label.grid(row = 1, column = 0, padx = 5, pady = 3, sticky = W)
    age_label.grid(row = 2, column = 0, padx = 5, pady = 3, sticky = W)
    gender_label.grid(row = 3, column = 0, padx = 5, pady = 3, sticky = W)
    contact_label.grid(row = 4, column = 0, padx = 5, pady = 3, sticky = W)
    address_label.grid(row = 5, column = 0, padx = 5, pady = 3, sticky = W)
    blood_group_label.grid(row = 6, column = 0, padx = 5, pady = 3, sticky = W)

    for i in range(7):
        colon = Label(old_details_frame, text = ":", font = "consolas 20 bold", bg = "#FFE2E2")
        colon.grid(row = i, column = 1, sticky = W)

    # old details
    display_old_pid = Button(old_details_frame, text = old_details[0], font = "consolas 19 bold", 
                    width = 27, padx = 10, borderwidth = 1, bg = "#FFE2E2", relief = GROOVE, anchor = W)

    display_name_pid = Button(old_details_frame, text = old_details[1], font = "consolas 19 bold", 
                    width = 27, padx = 10, borderwidth = 1, bg = "#FFE2E2", relief = GROOVE, anchor = W)

    display_age_pid = Button(old_details_frame, text = old_details[2], font = "consolas 19 bold", 
                    width = 27, padx = 10, borderwidth = 1, bg = "#FFE2E2", relief = GROOVE, anchor = W)

    display_gender_pid = Button(old_details_frame, text = old_details[3], font = "consolas 19 bold", 
                    width = 27, padx = 10, borderwidth = 1, bg = "#FFE2E2", relief = GROOVE, anchor = W)

    display_contact_pid = Button(old_details_frame, text = old_details[4], font = "consolas 19 bold", 
                    width = 27, padx = 10, borderwidth = 1, bg = "#FFE2E2", relief = GROOVE, anchor = W)

    display_address_pid = Button(old_details_frame, text = old_details[5], font = "consolas 19 bold", 
                    width = 27, padx = 10, borderwidth = 1, bg = "#FFE2E2", relief = GROOVE, anchor = W)

    display_blood_group_pid = Button(old_details_frame, text = old_details[6], 
                    font = "consolas 19 bold", width = 27, padx = 10, borderwidth = 1, 
                    bg = "#FFE2E2", relief = GROOVE, anchor = W)

    display_old_pid.grid(row = 0, column = 2, columnspan = 3, padx = 20, ipadx = 120)
    display_name_pid.grid(row = 1, column = 2, columnspan = 3, padx = 20, ipadx = 120)
    display_age_pid.grid(row = 2, column = 2, columnspan = 3, padx = 20, ipadx = 120)
    display_gender_pid.grid(row = 3, column = 2, columnspan = 3, padx = 20, ipadx = 120)
    display_contact_pid.grid(row = 4, column = 2, columnspan = 3, padx = 20, ipadx = 120)
    display_address_pid.grid(row = 5, column = 2, columnspan = 3, padx = 20, ipadx = 120)
    display_blood_group_pid.grid(row = 6, column = 2, columnspan = 3, padx = 20, ipadx = 120)

    # update details
    field_to_update_label = Label(update_frame, text = "Field", font = "consolas 19 bold", bg = "#FFE2E2")
    updated_detail_label = Label(update_frame, text = "New Details", font = "consolas 19 bold", bg = "#FFE2E2")

    field_to_update_label.grid(row = 0, column = 0, padx = 5, sticky = W)
    updated_detail_label.grid(row = 1, column = 0, padx = 5, sticky = W)

    for i in range(2):
        colon = Label(update_frame, text = ":", font = "consolas 20 bold", bg = "#FFE2E2")
        colon.grid(row = i, column = 1, sticky = W)

    field_to_update_options = ["Name", "Age", "Gender", "Contact", "Address", "Blood Group"]
    field_to_update = StringVar()
    field_to_update.set("Name")

    field_to_update_menu = OptionMenu(update_frame, field_to_update, *field_to_update_options)
    field_to_update_menu.config(width = 55, height = 1, font = "consolas 15 bold")
    field_to_update_menu.grid(row = 0, column = 2, columnspan = 3, padx = 15, pady = 5, sticky = W)

    updated_detail_entry = Entry(update_frame, font = "consolas 17")
    updated_detail_entry.grid(row = 1, column = 2, ipadx = 193, ipady = 5, padx = 15, pady = 10)

    # update button
    submit_button = Button(update_frame, text = "Update", font = "consolas 17 bold", bg = "#FF847C", 
                        borderwidth = 7, padx = 10, pady = 4, command = modify_submit)
    submit_button.grid(row = 5, column = 0, columnspan = 4, padx = 10, pady = 54, ipadx = 360)

    submit_button.update()
    #speak("Please select the field that you want to change")


# appointment window
def appointment_window():
    global appointment
    global check_pid

    # get back to main menu
    home_submit()

    # check patient id
    check_pid = easygui.enterbox(title = "Check PID", msg = "Enter your PID")
    operation = """SELECT * FROM PATIENT_DETAILS"""
    cursor.execute(operation)
    data = cursor.fetchall()
    existing_pid = []
    for i in data:
        existing_pid.append(str(i[0]))
        
    if (check_pid in existing_pid):
        clean_right_frame()
        # highlight clicked button
        appointment.grid_forget()
        appointment = Button(left_frame, text = "Appointment", font = "consolas 19 bold", 
                width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#2A363B", fg = "#FF847C", 
                anchor = CENTER, relief = SUNKEN, command = appointment_window)
        appointment.grid(row = 3, column = 0, columnspan = 3, pady = 5, padx = 20)
        appointing_the_doctor()

    else:
        messagebox.showerror("Modify Details", "PID given is wrong")
      
        return ()


date = "Pick Date"


# appointing the doctor
def appointing_the_doctor():
    global existing_doctors
    global doctor_frame
    global field_to_update
    global date_entry
    global date_pick
    global doctor_name

    # selecting doctor
    doctor_frame = LabelFrame(right_frame, height = 372, width = 1000, 
        text = "Doctor and Date select", bg = "#FFE2E2")
    doctor_frame.grid(row = 0, column = 0, rowspan = 7, columnspan = 3, padx = 7)
    doctor_frame.grid_propagate(0)

    # collecting doctors names
    operation = """SELECT * FROM doctor_details"""
    cursor.execute(operation)
    data = cursor.fetchall()

    existing_doctors = {}

    for i in data:
        existing_doctors[i[0]] = i[1]

    doctor_name = StringVar()
    doctor_name.set("Doctors")

    doctor_label = Label(doctor_frame, text = "Doctor", font = "consolas 25 bold", bg = "#FFE2E2")
    date_label = Label(doctor_frame, text = "Date", font = "consolas 25 bold", bg = "#FFE2E2")
    doctor_label.grid(row = 0, column = 0, columnspan = 3, padx = 10, sticky = W)
    date_label.grid(row = 1, column = 0, columnspan = 3, padx = 10, sticky = W)

    for i in range(2):
        colon = Label(doctor_frame, text = ":", font = "consolas 20 bold", bg = "#FFE2E2")
        colon.grid(row = i, column = 3, sticky = W)

    date_pick = Button(doctor_frame, text = date, font = "consolas 15 bold", width = 57, command = get_date)
    date_pick.grid(row = 1, column = 4, columnspan = 3, padx = 15, pady = 20, sticky = W)

    doctor_select = OptionMenu(doctor_frame, doctor_name, *list(existing_doctors.values()))
    doctor_select.config(width = 54, height = 1, font = "consolas 15 bold")
    doctor_select.grid(row = 0, column = 4, columnspan = 3, padx = 15, pady = 20, sticky = W)

    submit_button = Button(doctor_frame, text = "Submit", font = "consolas 20 bold", bg = "#FF847C", width = 55,
                           borderwidth = 7, padx = 10, pady = 4, command = appointment_submit)
    submit_button.grid(row = 6, column = 0, columnspan = 7, padx = 10, pady = 54)

    submit_button.update()
   


# date picker
def get_date():
    global date
    global date_pick

    def cal_done():
        top.withdraw()
        root.quit()

    root = Tk()
    root.withdraw()  # keep the root window from appearing

    top = Toplevel(root)
    style = ttk.Style(top)
    style.theme_use("alt")
    style.configure("style.TButton", font = "evogria 20 bold", background = "#FF847C", width = 20)
    style.map("TButton", background = [("active", "#2A363B")], foreground = [("active", "#FF847C")])
    # dt = date.today()
    # dt1=date(2022,13,5)
    cal = Calendar(top, font = "Arial 14", selectmode = "day", cursor = "hand2", mindate=datetime.now())
    cal.pack(fill = "both", expand = True)
    ttk.Button(top, text = "ok", style = "style.TButton", command = cal_done).pack()

    root.mainloop()

    date = cal.selection_get()

    date_pick.grid_forget()
    date_pick = Button(doctor_frame, text = date, font = "consolas 15 bold", width = 57, command = get_date)
    date_pick.grid(row = 1, column = 4, columnspan = 3, padx = 15, pady = 20, sticky = W)

    return date





# forward and backward button for image carousel
def forward_button(n):
    global num
    global display_img
    global status_bar
    global resized_images
    global right_frame

    if (num == 1):
        return

    display_img.grid_forget()
    display_img = Label(right_frame, image = resized_images[n + 1])
    display_img.grid(row = 0, column = 0, rowspan = 3, columnspan = 3)

    status_bar.grid_forget()
    status_bar = Label(right_frame, text = ("Image " + str(n + 2) + " of " + str(len(resized_images))), bd = 2,
                       relief = SUNKEN, anchor = E)
    status_bar.grid(row = 5, column = 0, columnspan = 3, sticky = W + E)
    num += 1


def backward_button(n):
    global display_img
    global status_bar
    global num
    global resized_images
    global right_frame

    if (num == 0):
        return

    display_img.grid_forget()
    display_img = Label(right_frame, image = resized_images[n - 1])
    display_img.grid(row = 0, column = 0, rowspan = 3, columnspan = 3)

    status_bar = Label(right_frame, text = ("Image " + str(n) + " of " + str(len(resized_images))), bd = 2,
                       relief = SUNKEN, anchor = E)
    status_bar.grid(row = 5, column = 0, columnspan = 3, sticky = W + E)

    num -= 1


# return to main menu
def home_submit():
    global right_frame
    global resized_logo_main
    clean_right_frame()

    # display logo in main window
    logo_main = Image.open(r"Data\\Images\\Icons\\logo6.png")
    resized_main = logo_main.resize((970, 492), Image.ANTIALIAS)
    resized_logo_main = ImageTk.PhotoImage(resized_main)

    display_logo_main = Label(right_frame, image = resized_logo_main)
    display_logo_main.pack()


# starting window
def main_window():
    global registration
    global patient_details
    global doctor_details
    global appointment
    global modify_details
    global doctor_registration
    

    # define buttons in left frame
    registration = Button(left_frame, text = "Registration", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                    anchor = CENTER, command = registration_window)

    patient_details = Button(left_frame, text = "Patient Details", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                    anchor = CENTER, command = patient_details_window)

    doctor_details = Button(left_frame, text = "Doctor Details", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                    anchor = CENTER, command = doctors_details_window)

    appointment = Button(left_frame, text = "Appointment", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                    anchor = CENTER, command = appointment_window)

    modify_details = Button(left_frame, text = "Modify Details", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                    anchor = CENTER, command = modify_details_window)


    home = Button(left_frame, text = "Home", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                    anchor = CENTER, command = home_submit)
    
    doctor_registration = Button(left_frame, text = "Doctor Registration", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                    anchor = CENTER, command = doctor_registration_window)

    registration.grid(row = 0, column = 0, columnspan = 3, pady = 5, padx = 20)
    patient_details.grid(row = 1, column = 0, columnspan = 3, pady = 5, padx = 20)
    doctor_details.grid(row = 2, column = 0, columnspan = 3, pady = 5, padx = 20)
    appointment.grid(row = 3, column = 0, columnspan = 3, pady = 5, padx = 20)
    modify_details.grid(row = 4, column = 0, columnspan = 3, pady = 5, padx = 20)
    home.grid(row = 6, column = 0, columnspan = 3, pady = 5, padx = 20)
    doctor_registration.grid(row = 7, column = 0, columnspan = 3, pady = 5, padx = 20)

main_window()


# home button for services offered
def home_submit_services_offered():
    global left_frame
    global top_frame
    global right_frame

    left_frame.grid_forget()
    top_frame.grid_forget()

    # top frame (constant)
    top_frame = LabelFrame(root)
    top_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 8)
    top_frame.grid_propagate(0)

    # title
    title = Label(top_frame, text = "DYPIT Hospital", font = "evogria 45", 
        bg = "#FFE2E2", width = 42, anchor = CENTER)
    title.pack()

    # left frame (constant)
    left_frame = LabelFrame(root, bg = "#FFE2E2")
    left_frame.grid(row = 2, column = 0, padx = 4, pady = 4, columnspan = 3, ipady = 40)

    home_submit()


# display logo in main window
logo_main = Image.open(r"Data\\Images\\Icons\\logo6.png")
resized_main = logo_main.resize((970, 492), Image.ANTIALIAS)
resized_logo_main = ImageTk.PhotoImage(resized_main)

display_logo_main = Label(right_frame, image = resized_logo_main)
display_logo_main.pack()


# ask MySQL username and password
def ask_MySQL_username_password():
    global MySQL_username
    global MySQL_password

    username_confirm = messagebox.askokcancel("MySQL Username", 
        "Please click on OK if your MySQL username is root")

    if (username_confirm == 0):
        #speak("Please enter your MySQL username")
        MySQL_username = easygui.enterbox(title = "MySQL Username", msg = "ENTER YOUR MY-SQL USERNAME: ")

    else:
        MySQL_username = "root"

 
    MySQL_password = easygui.passwordbox(title = "MySQL Password", msg = "ENTER YOUR MySQL PASSWORD: ")


ask_MySQL_username_password()


# connect to database
def connect_with_database():
    global dbcon
    global cursor
    dbcon = sqlcon.connect(
        host = "localhost",
        user = MySQL_username,
        password = MySQL_password,
    )
    cursor = dbcon.cursor()

    #speak("Successfully established connection with Database")


try:
    connect_with_database()
except:
    #("Your MySQL username or password is incorrect. Please try again")
    ask_MySQL_username_password()
    connect_with_database()


def create_database_and_table():
    operation = """CREATE DATABASE IF NOT EXISTS chase_hospitals"""
    cursor.execute(operation)

    operation = """USE chase_hospitals"""
    cursor.execute(operation)

    operation = """CREATE TABLE IF NOT EXISTS patient_details(
					pid            BIGINT          NOT NULL  AUTO_INCREMENT    PRIMARY KEY,
					name           VARCHAR(50)     NOT NULL,
					age            INTEGER         NOT NULL,
					gender         VARCHAR(20)     NOT NULL,
					contact        BIGINT          NOT NULL,
					address        VARCHAR(99)     NOT NULL,
					blood_group    VARCHAR(20)     NOT NULL)"""
    cursor.execute(operation)

    operation = """CREATE TABLE IF NOT EXISTS doctor_details(
					did             BIGINT         NOT NULL  AUTO_INCREMENT    PRIMARY KEY,
					name            VARCHAR(50)    NOT NULL,
					age             INTEGER        NOT NULL,
					contact         BIGINT         NOT NULL,
					specialisation  VARCHAR(99)    NOT NULL,
					qualification   VARCHAR(99)    NOT NULL)"""
    cursor.execute(operation)

    operation = """CREATE TABLE IF NOT EXISTS appointment(
					pid                BIGINT      NOT NULL  PRIMARY KEY,
					did                BIGINT      NOT NULL,
					appointment_date   VARCHAR(20) NOT NULL)"""
    cursor.execute(operation)


create_database_and_table()


def insert_bydefault_data():
    operation = """INSERT INTO patient_details VALUES
					(313570101, "Udit Pati", 17, "M", 8375054875, "Delhi", "O+"),
					(313570102, "Robin Vats", 17, "M", 7567563156, "Delhi", "O+"),
					(313570103, "Rahul Roy", 18, "M", 8345671848, "Mumbai", "A+"),
					(313570104, "Aditya Manas", 16, "M", 7534586798, "Jaipur", "B+")"""
    cursor.execute(operation)
    # dbcon.commit()

    operation = """INSERT INTO doctor_details VALUES
                    (101, "Dr. Abhijeet Sangle", 24, 7658424743,"Dentist", "Bachelor of Dental Surgery"),
                    (102, "Dr. Rushi Ladane", 87, 9427365092, "Ayurveda", 
                    "Bachelor of Ayurvedic Medicine and Surgery"),
                    (103, "Dr. Akshay Petkar", 22, 7248743423, "Medicine", "MBBS Ph.D"),
                    (104, "Dr. Arshad Shirgave", 23, 8493883433, "Cardiologists", "MBBS M.Phil M.D"),
                    (105, "Dr. Sojwal Lakade", 25, 7839478943, "Surgeon", "MBBS")"""
    cursor.execute(operation)

    dbcon.commit()


#speak("Do you want to insert some by default data in the database?")
by_default_data_confirm = messagebox.askyesno("Database",
                        "Do you want to insert some BY - DEFAULT DATA in the database?")

if (by_default_data_confirm == 1):
    try:
        insert_bydefault_data()
        #speak("Data inserted successfully")
        #speak("Welcome to DYPIT Hospital. How can I help you?")
    except:
        #speak("Data already inserted in the Database")
        #speak("Welcome to DYPIT Hospitals. How can I help you?")
        pass


# register button in registration window (insert data into the database)
def registration_submit():
    global name_entry
    global age_entry
    global gender_entry
    global address_entry
    global blood_group_entry

    # insert data into the database
    name = str(name_entry.get())
    age = str(age_entry.get())
    gender = str(gender_entry.get()[0]).upper()
    contact = str(contact_entry.get())
    address = str(address_entry.get())
    blood_group = str(blood_group_entry.get()).upper()

    data = [name, age, gender, contact, address, blood_group]
    for i in data:
        if (i == contact):
            if (len(i) != 10):
                messagebox.showerror("Database", "Please enter valid Contact Number")
                return
        elif (i == blood_group):
            valid_blood_group = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
            if (i not in valid_blood_group):
                messagebox.showerror("Database", "PLease enter valid Blood Group")
                return
        elif (len(i) == 0):
            messagebox.showerror("Database", "Please fill all Details")
            return

    operation = """INSERT INTO patient_details(name, age, gender, contact, address, blood_group) VALUES
					("{}", {}, "{}", {}, "{}", "{}")""".format(name, age, gender, contact, 
                        address, blood_group)
    cursor.execute(operation)
    dbcon.commit()

    # clear the entry boxes
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    gender_entry.delete(0, END)
    contact_entry.delete(0, END)
    address_entry.delete(0, END)
    blood_group_entry.delete(0, END)

    # get patient id
    operation = """SELECT *
				FROM patient_details"""
    cursor.execute(operation)
    data = cursor.fetchall()
    pid = str(data[-1][0])

    #speak("Record added successfully!")
    messagebox.showinfo("Database", "Your PID is: {}".format(pid))


# search button in patient details window
num = 3
def doctor_registration_submit():
    global doc_name_entry
    global doc_age_entry
    global doc_contact_entry
    global doc_specialisation_entry
    global doc_qualification_entry

    # insert data into the database
    doc_name = str(doc_name_entry.get())
    doc_age = str(doc_age_entry.get())
    doc_contact = str(doc_contact_entry.get())
    doc_specialisation= str(doc_specialisation_entry.get())
    doc_qualification = str(doc_qualification_entry.get())

    data = [doc_name, doc_age, doc_contact, doc_specialisation, doc_qualification]
    for i in data:
        if (i == doc_contact):
            if (len(i) != 10):
                messagebox.showerror("Database", "Please enter valid Contact Number")
                return
        elif (len(i) == 0):
            messagebox.showerror("Database", "Please fill all Details")
            return

    operation = """INSERT INTO doctor_details(name, age, contact, specialisation, qualification) VALUES
					("{}", {},  {}, "{}", "{}")""".format(doc_name, doc_age, doc_contact, 
                        doc_specialisation, doc_qualification)
    cursor.execute(operation)
    dbcon.commit()

    # clear the entry boxes
    doc_name_entry.delete(0, END)
    doc_age_entry.delete(0, END)
    doc_contact_entry.delete(0, END)
    doc_specialisation_entry.delete(0, END)
    doc_qualification_entry.delete(0, END)
    
    # get  id
    operation = """SELECT *
				FROM doctor_details"""
    cursor.execute(operation)
    data = cursor.fetchall()
    did = str(data[-1][0])
    messagebox.showinfo("Database", "Doctor's DID is: {}".format(did))
   


# search button in patient details window
#num = 3

def patient_details_search_submit():
    global num
    global field_to_search
    global search_detail_entry
    global field_to_search_2
    global search_detail_entry_2
    global field_to_search_3
    global search_detail_entry_3
    global searched_patient_details

    # search details
    field_to_search_value = field_to_search.get()
    search_value = search_detail_entry.get()

    # check if value is empty
    if (search_value == ""):
        return

    # chnage value if field is blood group
    if (field_to_search_value == "Blood Group"):
        field_to_search_value = "blood_group"

    # check if multiple values are present
    if (num == 3):
        # fetch values from database
        operation = """SELECT *
					FROM patient_details
					WHERE {} LIKE "%{}%"
					""".format(field_to_search_value, search_value)
        cursor.execute(operation)
        data = cursor.fetchall()

        if (len(data) == 0):
            #speak("Record Not Found")
            messagebox.showinfo("Database", "Record not found")
            return

        elif (len(data) > 1):
            #speak("{} records found. Please enter additional details to narrow down the search".format(
                #len(data)))
            multiple_fields_search_patient_details(num)
            num += 3
            return

    elif (num == 6):
        # search details
        field_to_search_value_2 = field_to_search_2.get()
        search_value_2 = search_detail_entry_2.get()

        if (field_to_search_value_2 == "Blood Group"):
            field_to_search_value_2 = "blood_group"

        operation = """SELECT *
				FROM patient_details
				WHERE {} LIKE "%{}%"
				AND {} LIKE "%{}%"
				""".format(field_to_search_value, search_value, field_to_search_value_2, search_value_2)
        cursor.execute(operation)
        data = cursor.fetchall()

        if (len(data) == 0):
            #speak("Record Not Found")
            messagebox.showinfo("Database", "Record not found")
            return

        elif (len(data) > 1):
            #speak("{} records found. Please enter additional details to narrow down the search".format(
            #    len(data)))
            multiple_fields_search_patient_details(num)
            num += 3
            return

    else:
        # search details
        field_to_search_value_2 = field_to_search_2.get()
        field_to_search_value_3 = field_to_search_3.get()
        search_value_2 = search_detail_entry_2.get()
        search_value_3 = search_detail_entry_3.get()

        if (field_to_search_value_3 == "Blood Group"):
            field_to_search_value_3 = "blood_group"

        operation = """SELECT *
				FROM patient_details
				WHERE {} LIKE "%{}%"
				AND {} LIKE "%{}%"
				AND {} LIKE "%{}%"
				""".format(field_to_search_value, search_value, field_to_search_value_2, search_value_2,
                           field_to_search_value_3, search_value_3)
        cursor.execute(operation)
        data = cursor.fetchall()

        if (len(data) == 0):
            #speak("Record Not Found")
            messagebox.showinfo("Database", "Record not found")
            return

        elif (len(data) > 1):
            #speak("Numerous records found. Please check your details")
            messagebox.showinfo("Database", "Numerous records found. Please check your details")
            return

    if (len(data) == 1):
        searched_patient_details = [str(i) for i in data[0]]

        # fetch appointment details
        operation = """SELECT did, appointment_date
					FROM appointment
					WHERE pid = {}""".format(searched_patient_details[0])
        cursor.execute(operation)
        records = cursor.fetchall()

        if (len(records) != 0):
            operation = """SELECT name
						FROM doctor_details
						WHERE did = {}""".format(int(records[0][0]))
            cursor.execute(operation)
            doctor_name = cursor.fetchall()
            records = [doctor_name[0][0], records[0][1]]
            searched_patient_details.extend(records)

        display_patient_details_after_search()
        return


# display multiple fields to search if multiple values are fetched
def multiple_fields_search_patient_details(num):
    global field_to_search
    global search_detail_entry
    global field_to_search_2
    global search_detail_entry_2
    global field_to_search_3
    global search_detail_entry_3
    global submit_button

    submit_button.grid_forget()

    # select a field to search
    field_to_search_label = Label(right_frame, text = "Field", font = "consolas 19 bold", bg = "#FFE2E2")
    search_detail_label = Label(right_frame, text = "Details", font = "consolas 19 bold", bg = "#FFE2E2")

    field_to_search_label.grid(row = num, column = 0, padx = 5, sticky = W)
    search_detail_label.grid(row = 1 + num, column = 0, padx = 5, sticky = W)

    for j in range(2):
        colon = Label(right_frame, text = ":", font = "consolas 20 bold", bg = "#FFE2E2")
        colon.grid(row = j + num, column = 1, sticky = W)

    field_to_search_options = ["PID", "Name", "Age", "Gender", "Contact", "Address", "Blood Group"]

    if (num == 3):
        field_to_search_2 = StringVar()
        field_to_search_2.set("Name")

        field_to_search_menu_2 = OptionMenu(right_frame, field_to_search_2, *field_to_search_options)
        field_to_search_menu_2.config(width = 62, height = 1, font = "consolas 15 bold")
        field_to_search_menu_2.grid(row = num, column = 2, columnspan = 3, padx = 15, pady = 5, sticky = W)

        search_detail_entry_2 = Entry(right_frame, font = "consolas 17")
        search_detail_entry_2.grid(row = 1 + num, column = 2, ipadx = 230, ipady = 5, padx = 15, pady = 10)

    elif (num == 6):
        field_to_search_3 = StringVar()
        field_to_search_3.set("Name")

        field_to_search_menu_3 = OptionMenu(right_frame, field_to_search_3, *field_to_search_options)
        field_to_search_menu_3.config(width = 62, height = 1, font = "consolas 15 bold")
        field_to_search_menu_3.grid(row = num, column = 2, columnspan = 3, padx = 15, pady = 5, sticky = W)

        search_detail_entry_3 = Entry(right_frame, font = "consolas 17")
        search_detail_entry_3.grid(row = 1 + num, column = 2, ipadx = 230, ipady = 5, padx = 15, pady = 10)

    # search button
    submit_button = Button(right_frame, text = "Search", font = "consolas 17 bold", bg = "#FF847C", 
                    borderwidth = 7, padx = 10, pady = 4, command = patient_details_search_submit)
    submit_button.grid(row = 2 + num, column = 0, columnspan = 4, padx = 10, pady = 54, ipadx = 375)


# backend data for doctor details
def doctor_details_values():
    operation = """SELECT * FROM doctor_details"""
    cursor.execute(operation)
    data = cursor.fetchall()

    doctor_id_values = []
    doctor_name_values = []
    doctor_age_values = []
    doctor_contact_values = []
    doctor_specialisation_values = []
    doctor_qualification_values = []

    for i in data:
        doctor_id_values.append(i[0])
        doctor_name_values.append(i[1])
        doctor_age_values.append(i[2])
        doctor_contact_values.append(i[3])
        doctor_specialisation_values.append(i[4])
        doctor_qualification_values.append(i[5])

    return (
        doctor_id_values, doctor_name_values, doctor_age_values, 
        doctor_contact_values, doctor_specialisation_values,
        doctor_qualification_values)


# update button in modify details window
def modify_submit():
    global resized_logo_main
    global display_logo_main

    # get values
    field_to_update_value = field_to_update.get()
    new_record = updated_detail_entry.get()

    # check if value is empty
    if (new_record == ""):
        #speak("Please enter some value to update")
        return

    # change value if field is blood group or name
    if (field_to_update_value == "Blood Group"):
        field_to_update_value = "blood_group"

    # insert data into the database
    operation = """UPDATE patient_details
					SET {} = "{}"
					WHERE pid = {}
					""".format(field_to_update_value, new_record, check_pid_modify)
    cursor.execute(operation)
    dbcon.commit()

    # return to main menu
    #speak("Record updated successfully")
    messagebox.showinfo("Database", "Record updated successfully")
    clean_right_frame()

    # display logo in main window
    logo_main = Image.open(r"Data\\Images\\Icons\\logo6.png")
    resized_main = logo_main.resize((970, 492), Image.ANTIALIAS)
    resized_logo_main = ImageTk.PhotoImage(resized_main)

    display_logo_main = Label(right_frame, image = resized_logo_main)
    display_logo_main.pack()


# submitting the appointment details
def appointment_submit():
    global doctor_name
    global existing_doctors
    global check_pid
    global date

    doctor_name_value = doctor_name.get()
    for key in existing_doctors:
        if (existing_doctors[key] == doctor_name_value):
            did = key

    # check for existing data
    operation = """SELECT pid FROM appointment"""
    cursor.execute(operation)
    data = cursor.fetchall()

    for i in data:
        if (i[0] == int(check_pid)):
            operation = """DELETE FROM appointment
							WHERE pid = {}""".format(check_pid)
            cursor.execute(operation)
            dbcon.commit()

    operation = """INSERT INTO appointment VALUES
					({}, {}, "{}")""".format(check_pid, did, date)

    cursor.execute(operation)
    dbcon.commit()

    detail_frame = LabelFrame(right_frame, text = "Details of your appointment", height = 275, 
                              width = 1000, bg = "#FFE2E2")
    detail_frame.grid(row = 8, column = 0, rowspan = 5, columnspan = 3, padx = 4, pady = 5)
    detail_frame.grid_propagate(0)

    details = str(
        "Your appointment with {} has been approved on " +
        "{}. You must follow all the norms of the hospital. " +
        "Mask, face shield, gloves and hand santizers are compulsory. " +
        "The health and safety of our patients, families, and staff members is our top priority. " +
        "By following all these essential steps we all can stop corona together"
    ).format(existing_doctors[did], date)

    details_label = Label(detail_frame, text = details, font = "consolas 16 bold", bg = "#FFE2E2", 
                          wraplength = 850, justify = LEFT)
    details_label.grid(row = 0, column = 0, columnspan = 3, rowspan = 4)

    home_button = Button(detail_frame, text = "Home", font = "consolas 20 bold", width = 55, bg = "#FF847C",
                         borderwidth = 7, padx = 10, pady = 4, command = home_submit)
    home_button.grid(row = 5, column = 0, columnspan = 3, pady = 10, padx = 10)
    #speak("Your appointment is fixed")




print(get_date)

root.mainloop()
