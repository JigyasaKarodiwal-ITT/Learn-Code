import socket
import threading
import json
from database_handler import DatabaseHandler
from login_handler import LoginHandler
from recomendation import Recommendation
import datetime

class Server:
    def __init__(self, host, port, db_host, db_user, db_password, db_name):
        self.host = host
        self.port = port
        self.db_handler = DatabaseHandler(db_host, db_user, db_password, db_name)
        self.login_handler = LoginHandler(self.db_handler)
        self.recomendation_engine = Recommendation(self.db_handler)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_server(self):
        self.db_handler.connect()
        if not self.db_handler.conn:
            print("Failed to connect to the database. Exiting...")
            return
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                raise ValueError("No data received")
            request = json.loads(data)
            endpoint = request.get("endpoint")
            if endpoint == "/login":
                self.login_handler.login(request, client_socket)
            elif endpoint == "/food_menu":
                self.view_food_menu(client_socket, request)
            elif endpoint == "/delete-menu-item":
                self.delete_menu_item(client_socket, request)
            elif endpoint == "/add-menu-item":
                self.add_menu_item(client_socket, request)
            elif endpoint == "/update-menu-item":
                self.update_menu_item(client_socket, request)
            elif endpoint == "/roll-out":
                self.roll_out_menu(client_socket, request)
            elif endpoint == "/view-recomendation":
                self.view_recomendation(client_socket, request)
            elif endpoint == "/view-feedback":
                self.view_feedback(client_socket, request)
            elif endpoint == "/give-feedback":
                self.give_feedback(client_socket, request)    
            elif endpoint == "/update-availablity":
                self.update_availabilty(client_socket, request) 
            elif endpoint == "/voting":
                self.vote_for_menu(client_socket, request)
            elif endpoint == "/voting-items":
                self.view_voting_items(client_socket, request)   
            elif endpoint == "/send-notification":
                self.send_notification(client_socket, request)
            elif endpoint == "/get-notification":
                self.get_notification(client_socket)              
            elif endpoint == "/update-user-profile":
                self.update_user_profile(client_socket, request)    
            elif endpoint == "/view-low-rating-items":
                self.view_low_rating_items(client_socket, request)  
            elif endpoint == "/add-moms-recipe":
                self.moms_recipe(client_socket,request)   
            elif endpoint == "/view-moms-recipe":
                self.view_moms_recipe(client_socket,request)    
            else:
                response = {"status": "failure", "message": "Invalid endpoint"}
                client_socket.sendall(json.dumps(response).encode())
        except ValueError as ve:
            print(f"ValueError: {ve}")
            response = {"status": "failure", "message": "Invalid request format or no data received"}
            client_socket.sendall(json.dumps(response).encode())
        except Exception as e:
            print(f"Error: {e}")
            response = {"status": "failure", "message": "An error occurred"}
            client_socket.sendall(json.dumps(response).encode())
        finally:
            client_socket.close()


    def moms_recipe(self, client_socket, request):
        user_id = request.get("UserID")
        moms_recipe = request.get("Recipe")
        print(request)
        try:
            response = self.db_handler.add_moms_recipe(user_id, moms_recipe)
            if response == "success":
                response = {"status": "success", "message": "Mom's recipe successfully added"}
            else:
                response = {"status": "failure", "message": "Failed to add Mom's recipe"}
        except Exception as e:
            print(f"Error in moms_recipe: {e}")
            response = {"status": "failure", "message": "An error occurred while adding Mom's recipe"}
        client_socket.sendall(json.dumps(response).encode())

    def view_low_rating_items(self, client_socket, request):
        role_name = request.get("role_name")
        if role_name in ["Admin", "Chef"]:
            low_rating_items = self.db_handler.get_low_rating_items()
            print(low_rating_items)
            response = {"status": "success", "low_rating_items": low_rating_items}
        else:
            response = {"status": "failure", "message": "Access denied"}
        client_socket.sendall(json.dumps(response).encode())
        


    def send_notification(self, client_socket, request):
        message = request.get("message")
        try:
            self.db_handler.send_notification(message)
            response = {"status": "success", "message": "Notification sent successfully"}
        except Exception as e:
            print(f"Error sending notification: {e}")
            response = {"status": "failure", "message": "Failed to send notification"}
        client_socket.sendall(json.dumps(response).encode())

    def get_notification(self, client_socket):
        try:
            notifications = self.db_handler.get_notification()
            # Convert date objects to string
            notifications = [
                (notification_id, message, date.isoformat() if isinstance(date, datetime.date) else date)
                for notification_id, message, date in notifications
            ]
            response = {"status": "success", "notifications": notifications}
        except Exception as e:
            print(f"Error fetching notifications: {e}")
            response = {"status": "failure", "message": "Failed to fetch notifications"}
        client_socket.sendall(json.dumps(response).encode())            

    def roll_out_menu(self, client_socket, request):
        data = request.get("data")
       
        truncate_result = self.db_handler.truncate_recommended_menu_item_table()
        if truncate_result == "failure":
            response = {"status": "failure", "message": "Failed to truncate recommendedmenuitem table"}
            client_socket.sendall(json.dumps(response).encode())
            return
        self.db_handler.reset_form_filled_status_for_all_user()
        results = []
        try:
            for meal, menu_items in data.items():
                for item in menu_items:
                    menu_item_id = int(item)
                    result = self.db_handler.add_recommended_menu_item(menu_item_id, 0)  # Initial votes set to 0
                    results.append(result)
            if all(result == "success" for result in results):
                self.db_handler.send_notification("Tomorrow's Menu Rolled Out, Fill your choice(If not).")
                response = {"status": "success", "message": "Menu items are rolled out successfully"}
            else:
                response = {"status": "failure", "message": "An error occurred while adding menu items"}
        except Exception as e:
            print(f"Error in roll_out_menu: {e}")
            response = {"status": "failure", "message": "An error occurred while adding menu items"}
        client_socket.sendall(json.dumps(response).encode())
    
    def view_recomendation(self, client_socket, request):
        role_name = request.get("RoleName")
        if role_name == "Chef":
            response = self.recomendation_engine.recommend_food_items()
            response = {"status": "success", "recomendations": response}
            client_socket.sendall(json.dumps(response).encode())
    
    def view_feedback(self, client_socket, request):
        role_name = request.get("role_name")
        feedback = self.db_handler.get_feedback_details()
        print(feedback)
        response = {"status": "success", "feedback": feedback}
        client_socket.sendall(json.dumps(response).encode())

    def view_moms_recipe(self, client_socket, request):
        role_name = request.get("role_name")
        recipe = self.db_handler.get_moms_recipe()
        print(recipe)
        response = {"status": "success", "feedback": recipe}
        client_socket.sendall(json.dumps(response).encode())        

    def give_feedback(self, client_socket, request):
        role_name = request.get("RoleName")
        if role_name == "Employee":
            response = self.db_handler.give_menuItemfeedback(request)
            if "success" in response:
                response = {"status": "success", "message": "Successfully given feedback"}
            else:
                response = {"status": "failure", "message": "There is an error"}
        else:
            response = {"status": "failure", "message": "Invalid role for giving feedback"}

        client_socket.sendall(json.dumps(response).encode())
      
    def update_availabilty(self, client_socket, request):
        role_name = request.get("RoleName")
        menuitemid = request.get("MenuItemID")
        new_availability = request.get("AvailabilityStatus")
        if role_name == "Chef":
            response = self.db_handler.update_menuItemavailabilty(menuitemid, new_availability)
            if "success" in response:
                response = {"status": "success", "message": "Item successfully Updated"}
            else:
                response = {"status": "failure", "message": "There is an error"}
            client_socket.sendall(json.dumps(response).encode())      

    def update_menu_item(self, client_socket, request):
        role_name = request.get("RoleName")
        menuitemid = request.get("MenuItemID")
        new_price = request.get("Price")
        new_availability = request.get("AvailabilityStatus")
        if role_name == "Admin":
            response = self.db_handler.update_menuItem(menuitemid, new_price, new_availability)
            if "success" in response:
                response = {"status": "success", "message": "Item successfully Updated"}
            else:
                response = {"status": "failure", "message": "There is an error"}
            client_socket.sendall(json.dumps(response).encode())

    def update_user_profile(self, client_socket, request):
        role_name = request.get("RoleName")
        user_id = request.get("UserId")
        new_dietpreference = request.get("DietPreference")
        new_spicelevel = request.get("SpiceLevel")
        new_cuisinepreference = request.get("CuisinePreference")
        new_sweettooth = request.get("SweetTooth")
        print(request)
        if role_name == "Employee":
            response = self.db_handler.update_userprofile(user_id, new_dietpreference, new_spicelevel, new_cuisinepreference, new_sweettooth)
            if "success" in response:
                response = {"status": "success", "message": "Profile successfully Updated"}
            else:
                response = {"status": "failure", "message": "There is an error"}
            client_socket.sendall(json.dumps(response).encode())        

    def add_menu_item(self, client_socket, request):
        role_name = request.get("RoleName")
        if role_name == "Admin":
            response = self.db_handler.add_menuItem(request)
            if "success" in response:
                response = {"status": "success", "message": "Item successfully added"}
            else:
                response = {"status": "failure", "message": "There is an error"}
            client_socket.sendall(json.dumps(response).encode())

    def delete_menu_item(self, client_socket, request):
        role_name = request.get("RoleName")
        menuitemid = request.get("MenuItemID")
        if role_name == "Admin":
            response = self.db_handler.delete_menuItem(menuitemid)
            if "success" in response:
                response = {"status": "success", "message": "Item successfully Deleted"}
            else:
                response = {"status": "failure", "message": "There is an error"}
            client_socket.sendall(json.dumps(response).encode())

    def view_food_menu(self, client_socket, request):
        role_name = request.get("role_name")
        if role_name in ["Admin", "Chef","Employee"]:
            menu = self.db_handler.get_food_menu()
            response = {"status": "success", "menu": menu}
        else:
            response = {"status": "failure", "message": "Access denied"}
        client_socket.sendall(json.dumps(response).encode())

    def view_voting_items(self, client_socket, request):
        user_id = request.get("UserID")
        try:
            diet_preference = self.db_handler.get_diet_preference(user_id)
            voting_items = self.db_handler.get_voting_items(diet_preference)
            categorized_items = {"Breakfast": [], "Lunch": [], "Dinner": []}

            for item in voting_items:
                meal_type = item[2]
                categorized_items[meal_type].append({
                    "MenuItemID": item[0],
                    "MenuItemName": item[1],
                    "Votes": item[3]
                })

            response = {"status": "success", "data": categorized_items}
            client_socket.sendall(json.dumps(response).encode())
        except Exception as e:
            print(f"Error in view_voting_items: {e}")
            response = {"status": "failure", "message": "An error occurred while fetching voting items"}
            client_socket.sendall(json.dumps(response).encode())

    def vote_for_menu(self, client_socket, request):
        data = request.get("data")
        if not data:
            raise ValueError("No data provided")
        try:
            for meal_type, menu_item_id in data.items():
                menu_item_id = int(menu_item_id)
                result = self.db_handler.add_vote(menu_item_id)
                if result != "success":
                    response = {"status": "failure", "message": f"Failed to cast vote for {meal_type}"}
                    client_socket.sendall(json.dumps(response).encode())
                    return

            response = {"status": "success", "message": "Votes successfully cast"}
        except Exception as e:
            print(f"Error in vote_for_menu: {e}")
            response = {"status": "failure", "message": "An error occurred while casting votes"}
        client_socket.sendall(json.dumps(response).encode())


if __name__ == "__main__":
    server = Server('localhost', 12345, 'localhost', 'root', '12345678', 'cafeteria_db')
    server.start_server()
