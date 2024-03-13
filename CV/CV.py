import tkinter as tk

class CVWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("CV")

        header_frame = tk.Frame(root, bg="lightblue", pady=10)
        header_frame.pack(fill=tk.X)
       # self.photo = tk.PhotoImage(file="\photo.jpg")
        self.header_label = tk.Label(header_frame, text="Atakan Adalı", font=("Helvetica", 18, "bold"), pady=5)
        self.header_label.pack()
        self.role_label = tk.Label(header_frame, text="Junior Developer", font=("Helvetica", 12), pady=5)
        self.role_label.pack()
        # self.photo_label = tk.Label(header_frame, image=self.photo)
        # self.photo_label.pack()

        main_frame = tk.Frame(root)
        main_frame.pack(padx=10, pady=10)

        contact_frame = tk.LabelFrame(main_frame, text="İletişim Bilgileri")
        contact_frame.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        contact_labels = ["Adres: Tekirdağ/Ergene, Türkiye",
                          "Telefon: 0535 052 02 53",
                          "E-posta: atakan_adali@hotmail.com.tr",
                          "Linkedin: Atakan Adalı",
                          "Github: PISTIN22",
                          "Website: atakan-adali.com.tr"]
        for i, label_text in enumerate(contact_labels):
            label = tk.Label(contact_frame, text=label_text, anchor="w", justify="left")
            label.grid(row=i, column=0, sticky="w")

        education_frame = tk.LabelFrame(main_frame, text="Eğitim")
        education_frame.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        education_labels = ["Lise",
                            "Mezun Olduğu Okul: Deri Sanayicilieri Mesleki Teknik Anadolu Lisesi",
                            "Bölüm: Bilişim",
                            "Mezuniyet Yılı: 2019",
                            "Üniversite",
                            "Öğrenim Durumu: Devam Etmekte",
                            "Ortalama: 3,42",
                            "Okul: Mehmet Âkif Ersoy Üniversitesi Ağlasun Meslek Yüksekolulu",
                            "Bölüm: Bilişim Güvenliği Teknolojisi"]
        for i, label_text in enumerate(education_labels):
            label = tk.Label(education_frame, text=label_text, anchor="w", justify="left")
            label.grid(row=i, column=0, sticky="w")

        personal_frame = tk.LabelFrame(main_frame, text="Kişisel Bilgiler")
        personal_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        personal_labels = ["Doğum Tarihi: 02/05/2001",
                           "Cinsiyet: Erkek",
                           "Ehliyet: B2"]
        for i, label_text in enumerate(personal_labels):
            label = tk.Label(personal_frame, text=label_text, anchor="w", justify="left")
            label.grid(row=i, column=0, sticky="w")

        skills_frame = tk.LabelFrame(main_frame, text="Beceriler")
        skills_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        skills_labels = ["Python: 70%",
                         "JavaScript: 75%",
                         "HTML/CSS: 90%",
                         "C#: 85%",
                         "SQL: 75%",
                         "Unity: 50%"]
        for i, label_text in enumerate(skills_labels):
            label = tk.Label(skills_frame, text=label_text, anchor="w", justify="left")
            label.grid(row=i, column=0, sticky="w")

        language_frame = tk.LabelFrame(main_frame, text="Diller")
        language_frame.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        language_labels = ["İngilizce: B1",
                           "Bulgarca: A2"]
        for i, label_text in enumerate(language_labels):
            label = tk.Label(language_frame, text=label_text, anchor="w", justify="left")
            label.grid(row=i, column=0, sticky="w")

        interests_frame = tk.LabelFrame(main_frame, text="İlgi Alanları")
        interests_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        interests_labels = ["Oyun Oynamak & Tasarlamak",
                            "Film izlemek",
                            "Kitap okumak",
                            "Kahve",
                            "Elektronik cihaz tamir etmek"]
        for i, label_text in enumerate(interests_labels):
            label = tk.Label(interests_frame, text=label_text, anchor="w", justify="left")
            label.grid(row=i, column=0, sticky="w")

        internship_frame = tk.LabelFrame(main_frame, text="Staj Dönemi")
        internship_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        internship_label = tk.Label(internship_frame, text="16 Temmuz 2024 - 26 Ağustos 2024")
        internship_label.grid(row=0, column=0, sticky="w")

        social_frame = tk.LabelFrame(root, text="Sosyal Medya", pady=10)
        social_frame.pack(fill=tk.X)
        social_labels = ["Instagram", "Twitter", "Facebook", "Youtube", "Steam", "Spotify", "Github"]
        # social_icons = ["instagram.png", "twitter.png", "facebook.png", "youtube.png", "steam.png", "spotify.png", "github.png"]
        # for label_text, icon in zip(social_labels, social_icons):
        #     icon_image = tk.PhotoImage(file=icon)
        #     label = tk.Label(social_frame, image=icon_image)
        #     label.image = icon_image
        #     label.pack(side="left", padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    cv_window = CVWindow(root)
    root.mainloop()
