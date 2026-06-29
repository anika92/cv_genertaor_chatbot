class CVData:
    def __init__(self, personal_info, summary, experience,
                 education, skills, projects):
        self.personal_info = personal_info
        self.summary = summary
        self.experience = experience
        self.education = education
        self.skills = skills
        self.projects = projects

    @staticmethod
    def parse_experience(text):
        """Parse multi-line text into list of experience dicts."""
        experiences = []
        blocks = text.strip().split("\n\n")
        for block in blocks:
            lines = [l.strip() for l in block.strip().split("\n") if l.strip()]
            if len(lines) >= 2:
                exp = {
                    "position": lines[0],
                    "company": lines[1] if len(lines) > 1 else "",
                    "period": lines[2] if len(lines) > 2 else "",
                    "responsibilities": [
                        l.lstrip("•-* ").strip()
                        for l in lines[3:]
                    ] if len(lines) > 3 else []
                }
                experiences.append(exp)
        return experiences

    @staticmethod
    def parse_education(text):
        educations = []
        blocks = text.strip().split("\n\n")
        for block in blocks:
            lines = [l.strip() for l in block.strip().split("\n") if l.strip()]
            if len(lines) >= 2:
                edu = {
                    "degree": lines[0],
                    "school": lines[1] if len(lines) > 1 else "",
                    "year": lines[2] if len(lines) > 2 else "",
                    "gpa": lines[3] if len(lines) > 3 else ""
                }
                educations.append(edu)
        return educations

    @staticmethod
    def parse_list(text):
        """Split comma-separated or newline-separated list."""
        if "," in text:
            return [s.strip() for s in text.split(",") if s.strip()]
        return [s.strip() for s in text.split("\n") if s.strip()]

    @staticmethod
    def parse_projects(text):
        projects = []
        blocks = text.strip().split("\n\n")
        for block in blocks:
            lines = [l.strip() for l in block.strip().split("\n") if l.strip()]
            if len(lines) >= 2:
                proj = {
                    "name": lines[0],
                    "tech": lines[1] if len(lines) > 1 else "",
                    "description": " ".join(lines[2:]) if len(lines) > 2 else ""
                }
                projects.append(proj)
        return projects
