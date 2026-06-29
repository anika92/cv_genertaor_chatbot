import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from cv_data import CVData
from pdf_generator import PDFGenerator


class CVFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CV Generator - Build Your Resume")
        self.root.geometry("700x750")
        self.root.configure(bg="#f0f0f0")

        self._build_ui()

    def _build_ui(self):
        # Title bar
        title = tk.Label(self.root, text="📄 CV Generator",
                         font=("Helvetica", 20, "bold"),
                         bg="#2C3E50", fg="white", pady=10)
        title.pack(fill="x")

        # Main scrollable frame
        container = tk.Frame(self.root, bg="#f0f0f0")
        container.pack(fill="both", expand=True, padx=10, pady=10)

        canvas = tk.Canvas(container, bg="#f0f0f0", highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        self.form_frame = tk.Frame(canvas, bg="#f0f0f0")

        self.form_frame.bind("<Configure>",
                             lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.form_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self._build_form_fields()

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(fill="x", pady=10)

        tk.Button(btn_frame, text="📝 Generate CV",
                  command=self.generate_cv,
                  bg="#27AE60", fg="white",
                  font=("Helvetica", 12, "bold"),
                  padx=20, pady=8).pack(side="left", padx=10)

        tk.Button(btn_frame, text="🗑 Clear Form",
                  command=self.clear_form,
                  bg="#E74C3C", fg="white",
                  font=("Helvetica", 12, "bold"),
                  padx=20, pady=8).pack(side="left", padx=10)

        tk.Button(btn_frame, text="❌ Exit",
                  command=self.root.quit,
                  bg="#7F8C8D", fg="white",
                  font=("Helvetica", 12, "bold"),
                  padx=20, pady=8).pack(side="right", padx=10)

    def _build_form_fields(self):
        f = self.form_frame

        # ===== Personal Info =====
        self._section_label(f, "👤 Personal Information")
        self.name = self._labeled_entry(f, "Full Name *")
        self.title = self._labeled_entry(f, "Professional Title")
        self.email = self._labeled_entry(f, "Email *")
        self.phone = self._labeled_entry(f, "Phone")
        self.address = self._labeled_entry(f, "Address")
        self.linkedin = self._labeled_entry(f, "LinkedIn URL")
        self.github = self._labeled_entry(f, "GitHub URL")

        # ===== Summary =====
        self._section_label(f, "📝 Professional Summary")
        self.summary = self._labeled_text(f, "Write a short summary...", height=4)

        # ===== Experience =====
        self._section_label(f, "💼 Work Experience")
        tk.Label(f, text="Format each entry separated by blank line:\n"
                         "Line 1: Position\nLine 2: Company\n"
                         "Line 3: Period\nLines 4+: Responsibilities (• bullet)",
                 bg="#f0f0f0", fg="#555", font=("Helvetica", 8, "italic"),
                 justify="left").pack(anchor="w", padx=20)
        self.experience = self._labeled_text(f,
                                             "Senior Software Engineer\n"
                                             "Tech Corp\n2021 - Present\n"
                                             "• Led microservices architecture\n"
                                             "• Mentored junior developers",
                                             height=10)

        # ===== Education =====
        self._section_label(f, "🎓 Education")
        tk.Label(f, text="Format each entry separated by blank line:\n"
                         "Line 1: Degree\nLine 2: School\n"
                         "Line 3: Year\nLine 4: GPA (optional)",
                 bg="#f0f0f0", fg="#555", font=("Helvetica", 8, "italic"),
                 justify="left").pack(anchor="w", padx=20)
        self.education = self._labeled_text(f,
                                            "B.Sc. Computer Science\n"
                                            "University of Technology\n"
                                            "2014 - 2018\n3.8/4.0",
                                            height=8)

        # ===== Skills =====
        self._section_label(f, "🛠 Technical Skills")
        self.skills = self._labeled_entry(f,
                                          "Python, Django, JavaScript, React, AWS")

        # ===== Projects =====
        self._section_label(f, "🚀 Projects")
        tk.Label(f, text="Format each entry separated by blank line:\n"
                         "Line 1: Project Name\nLine 2: Tech Stack\n"
                         "Line 3+: Description",
                 bg="#f0f0f0", fg="#555", font=("Helvetica", 8, "italic"),
                 justify="left").pack(anchor="w", padx=20)
        self.projects = self._labeled_text(f,
                                           "E-commerce Platform\n"
                                           "Django, React, PostgreSQL\n"
                                           "Built full-stack platform with payment integration",
                                           height=8)

    def _section_label(self, parent, text):
        lbl = tk.Label(parent, text=text, font=("Helvetica", 13, "bold"),
                       bg="#34495E", fg="white", pady=6, padx=10, anchor="w")
        lbl.pack(fill="x", pady=(15, 5), padx=10)

    def _labeled_entry(self, parent, label_text):
        frame = tk.Frame(parent, bg="#f0f0f0")
        frame.pack(fill="x", padx=20, pady=3)
        tk.Label(frame, text=label_text, bg="#f0f0f0",
                 font=("Helvetica", 10)).pack(anchor="w")
        entry = tk.Entry(frame, font=("Helvetica", 10), relief="solid", bd=1)
        entry.pack(fill="x", ipady=4)
        return entry

    def _labeled_text(self, parent, placeholder, height=5):
        frame = tk.Frame(parent, bg="#f0f0f0")
        frame.pack(fill="x", padx=20, pady=3)
        entry = tk.Text(frame, height=height, font=("Helvetica", 10),
                        relief="solid", bd=1, wrap="word")
        entry.insert("1.0", placeholder)
        entry.pack(fill="x")
        return entry

    def clear_form(self):
        if messagebox.askyesno("Clear Form", "Clear all fields?"):
            for widget in [self.name, self.title, self.email, self.phone,
                           self.address, self.linkedin, self.github, self.skills]:
                widget.delete(0, tk.END)
            for widget in [self.summary, self.experience, self.education, self.projects]:
                widget.delete("1.0", tk.END)

    def generate_cv(self):
        # Validate required fields
        if not self.name.get().strip() or not self.email.get().strip():
            messagebox.showerror("Error", "Name and Email are required!")
            return

        # Gather data
        personal_info = {
            "name": self.name.get().strip(),
            "title": self.title.get().strip(),
            "email": self.email.get().strip(),
            "phone": self.phone.get().strip(),
            "address": self.address.get().strip(),
            "linkedin": self.linkedin.get().strip(),
            "github": self.github.get().strip()
        }

        cv = CVData(
            personal_info=personal_info,
            summary=self.summary.get("1.0", tk.END).strip(),
            experience=CVData.parse_experience(self.experience.get("1.0", tk.END)),
            education=CVData.parse_education(self.education.get("1.0", tk.END)),
            skills=CVData.parse_list(self.skills.get()),
            projects=CVData.parse_projects(self.projects.get("1.0", tk.END))
        )

        # Choose file location
        default_name = personal_info["name"].replace(" ", "_") + "_CV.pdf"
        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialfile=default_name,
            title="Save CV as..."
        )

        if not filename:
            return

        # Generate PDF
        try:
            pdf = PDFGenerator(filename)
            pdf.add_header(cv.personal_info)
            pdf.add_section_title("Professional Summary")
            pdf.add_summary(cv.summary)
            pdf.add_section_title("Work Experience")
            pdf.add_experience(cv.experience)
            pdf.add_section_title("Education")
            pdf.add_education(cv.education)
            pdf.add_section_title("Technical Skills")
            pdf.add_skills(cv.skills)
            if cv.projects:
                pdf.add_section_title("Projects")
                pdf.add_projects(cv.projects)
            pdf.save()

            messagebox.showinfo("Success! 🎉",
                                f"CV generated successfully!\n\nSaved at:\n{filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate CV:\n{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CVFormApp(root)
    root.mainloop()
