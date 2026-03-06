import flet as ft

def main(page: ft.Page):
    # Βασικές ρυθμίσεις
    page.title = "ATM Pin Pad"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 350
    page.window.height = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Ο κωδικός
    SWSTOS_KWDIKOS = "1235"
    trexwn_kwdikos = "" # Εδώ θα αποθηκεύουμε τι πατάει ο χρήστης

    # --- Στήσιμο της "Οθόνης" του ΑΤΜ ---
    othoni_text = ft.Text(value="Εισάγετε PIN", size=24, weight=ft.FontWeight.BOLD, color="white")

    othoni_container = ft.Container(
        content=othoni_text,
        width=280,
        height=80,
        bgcolor="#1e1e1e", # Σκούρο γκρι φόντο
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        margin=ft.margin.only(bottom=30) # Αφήνει κενό από κάτω
    )

    # --- Η Λογική (Τι γίνεται όταν πατάμε ένα κουμπί) ---
    def patithike_koumpi(e):
        nonlocal trexwn_kwdikos 
        koympi_pou_patithike = e.control.data 

        if koympi_pou_patithike == "C":
            # Κουμπί Clear
            trexwn_kwdikos = ""
            othoni_text.value = "Εισάγετε PIN"
            othoni_text.color = "white"

        elif koympi_pou_patithike == "OK":
            # Κουμπί OK
            if trexwn_kwdikos == SWSTOS_KWDIKOS:
                othoni_text.value = "Πρόσβαση Επιτράπηκε!"
                othoni_text.color = "green"
            else:
                othoni_text.value = "Λάθος PIN!"
                othoni_text.color = "red"
                trexwn_kwdikos = "" # Μηδενίζουμε για να ξαναπροσπαθήσει

        else:
            # Αν πάτησε αριθμό (και δεν έχουμε ξεπεράσει τα 4 ψηφία)
            if len(trexwn_kwdikos) < 4:
                trexwn_kwdikos += koympi_pou_patithike
                othoni_text.value = "✱ " * len(trexwn_kwdikos)
                othoni_text.color = "white"

        page.update()

    # --- Το "Εργοστάσιο" Κουμπιών μας ---
    def ftiakse_koumpi(keimeno, xrwma_fontou="#2c3e50"):
        return ft.Container(
            content=ft.Text(keimeno, size=24, weight=ft.FontWeight.BOLD),
            alignment=ft.Alignment(0, 0), 
            width=75,
            height=75,
            bgcolor=xrwma_fontou,
            border_radius=40, 
            data=keimeno, 
            on_click=patithike_koumpi,
            ink=True 
        )

    # --- Χτίζουμε το Πληκτρολόγιο με Γραμμές ---
    grammi_1 = ft.Row([ftiakse_koumpi("1"), ftiakse_koumpi("2"), ftiakse_koumpi("3")], alignment=ft.MainAxisAlignment.CENTER)
    grammi_2 = ft.Row([ftiakse_koumpi("4"), ftiakse_koumpi("5"), ftiakse_koumpi("6")], alignment=ft.MainAxisAlignment.CENTER)
    grammi_3 = ft.Row([ftiakse_koumpi("7"), ftiakse_koumpi("8"), ftiakse_koumpi("9")], alignment=ft.MainAxisAlignment.CENTER)
    grammi_4 = ft.Row([
        ftiakse_koumpi("C", "#c0392b"), 
        ftiakse_koumpi("0"),
        ftiakse_koumpi("OK", "#27ae60") 
    ], alignment=ft.MainAxisAlignment.CENTER)

    # Βάζουμε τα πάντα στη σελίδα
    page.add(othoni_container, grammi_1, grammi_2, grammi_3, grammi_4)

ft.run(main)