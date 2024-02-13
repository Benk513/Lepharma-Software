# app/controllers/authentication_controller.py

from app.models.user_model import UserModel

class AuthenticationController:
    @staticmethod
    def authenticate_user(username, password):
        try:
            user = UserModel.authenticate(username, password)
            if user:
                return {"success": True, "message": "Authentication successful", "user": user.__dict__}
            else:
                return {"success": False, "message": "Invalid username or password"}
        except ValueError as e:
            return {"success": False, "message": str(e)}
