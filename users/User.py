class User:
    def __init__(self, user_dict):
        self.id = user_dict["id"]
        self.email = user_dict["email"]
        self.login = user_dict["login"]
        self.first_name = user_dict["first_name"]
        self.last_name = user_dict["last_name"]
        self.usual_full_name = user_dict["usual_full_name"]
        self.usual_first_name = user_dict["usual_first_name"]
        self.url = user_dict["url"]
        self.phone = user_dict["phone"]
        self.displayname = user_dict["displayname"]
        self.image_url = user_dict["image_url"]
        self.new_image_url = user_dict["new_image_url"]
        self.staff = user_dict["staff?"]
        self.correction_point = user_dict["correction_point"]
        self.pool_month = user_dict["pool_month"]
        self.pool_year = user_dict["pool_year"]
        self.location = user_dict["location"]
        self.wallet = user_dict["wallet"]
        self.anonymize_date = user_dict["anonymize_date"]
        self.data_erasure_date = user_dict["data_erasure_date"]
        self.created_at = user_dict["created_at"]
        self.updated_at = user_dict["updated_at"]
        self.alumnized_at = user_dict["alumnized_at"]
        self.alumni = user_dict["alumni?"]
    