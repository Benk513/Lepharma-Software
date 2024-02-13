
class UserModel:
    def __init__(self,username,password,role):
        self.username = username
        self.password = password
        self.role = role
    
    def displayUserInfo(self):
        print(f'user username:{self.username} ,password:{self.password} and role : {self.role}')
        

    @staticmethod
    def authenticate(username, password):
        # Example: Authenticate user based on username and password
        # In a real-world scenario, you would validate credentials against a database
        # For simplicity, this example uses hardcoded credentials
        users = [
            {"username": "admin", "password": "admin123", "role": "admin"},
            {"username": "pharmacist", "password": "pharma456", "role": "pharmacist"},
            # Add more users as needed
        ]

        for user in users:
            if user["username"] == username and user["password"] == password:
                return UserModel(username=user["username"], password=user["password"], role=user["role"])

        return print("not matching")

    def has_permission(self, required_role):
        # Check if the user has the required role
        return self.role == required_role



c = UserModel("admin","admin123","admin")

c.displayUserInfo()
c.authenticate("admin","admin123")
print(c.has_permission("admin"))