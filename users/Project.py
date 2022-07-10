class Project:
    def __init__(self, project, client):
        self.client = client
        self.id = project['id']
        self.project_id = project['project']['id']
        self.name = project['project']['name']
        self.slug = project['project']['slug']
        self.final_mark = project['final_mark']
        self.status = project['status']
        self.validated = project['validated?']

    def toJSON(self):
        return {
            "id": self.id,
            "project_id": self.project_id,
            "name": self.name,
            "slug": self.slug,
            "final_mark": self.final_mark,
            "status": self.status,
            "validated": self.validated
        }
