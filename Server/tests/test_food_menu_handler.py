import unittest
from unittest.mock import Mock, MagicMock
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from food_menu_handler import FoodMenuHandler  

class TestFoodMenuHandler(unittest.TestCase):

    def setUp(self):
        self.db_handler = Mock()
        self.food_menu_handler = FoodMenuHandler(self.db_handler)
        self.client_socket = Mock()

    def test_add_menu_item_success(self):
        request = {
            "endpoint": "/add-menu-item",
            "RoleName": "Admin",
            "Name": "hhhh",
            "Price": 12.5
        }

        self.db_handler.menu_item_exists.return_value = False
        self.db_handler.add_menuItem.return_value = "success"

        self.food_menu_handler.endpointHandler(self.client_socket, request)

        expected_response = json.dumps({"status": "success", "message": "Item successfully added"}).encode()
        self.client_socket.sendall.assert_called_with(expected_response)

    def test_add_menu_item_failure_exists(self):
        request = {
          "endpoint": "/add-menu-item",
          "RoleName": "Admin",
          "Name": "hhhh"
        }

        self.db_handler.menu_item_exists.return_value = True
        self.db_handler.add_menuItem.return_value = "failure" 

        self.food_menu_handler.endpointHandler(self.client_socket, request)

        expected_response = json.dumps({"status": "failure", "message": "There is an error"}).encode()
        self.client_socket.sendall.assert_called_with(expected_response)


    def test_update_menu_item_success(self):
        request = {
            "endpoint": "/update-menu-item",
            "RoleName": "Admin",
            "MenuItemID": 1,
            "Price": 15.0,
            "AvailabilityStatus": "Available",
            "DietPreference": "Vegetarian",
            "SpiceLevel": "Medium",
            "CuisinePreference": "Italian",
            "SweetTooth": "No"
        }

        self.db_handler.menu_item_exists_by_id.return_value = True
        
        self.db_handler.update_menuItem.return_value = "success"

        self.food_menu_handler.endpointHandler(self.client_socket, request)

        expected_response = json.dumps({"status": "success", "message": "Item successfully Updated"}).encode()
        self.client_socket.sendall.assert_called_with(expected_response)

    def test_delete_menu_item_success(self):
        request = {
            "endpoint": "/delete-menu-item",
            "RoleName": "Admin",
            "MenuItemID": 1
        }

        self.db_handler.menu_item_exists_by_id.return_value = True
        self.db_handler.delete_menuItem.return_value = "success"

        self.food_menu_handler.endpointHandler(self.client_socket, request)

        expected_response = json.dumps({"status": "success", "message": "Item successfully Deleted"}).encode()
        self.client_socket.sendall.assert_called_with(expected_response)

    def test_view_food_menu_success(self):
        request = {
            "endpoint": "/food_menu",
            "role_name": "Admin"
        }

        self.db_handler.get_food_menu.return_value = [{"Name": "Pasta", "Price": 12.5}]

        self.food_menu_handler.endpointHandler(self.client_socket, request)

        expected_response = json.dumps({"status": "success", "menu": [{"Name": "Pasta", "Price": 12.5}]}).encode()
        self.client_socket.sendall.assert_called_with(expected_response)

    def test_update_availability_success(self):
        request = {
            "endpoint": "/update-availability",
            "RoleName": "Chef",
            "MenuItemID": 1,
            "AvailabilityStatus": "Unavailable"
        }

        self.db_handler.update_menuItemavailabilty.return_value = "success"

        self.food_menu_handler.endpointHandler(self.client_socket, request)

        expected_response = json.dumps({"status": "success", "message": "Item successfully Updated"}).encode()
        self.client_socket.sendall.assert_called_with(expected_response)

    def test_view_low_rating_items_success(self):
        request = {
            "endpoint": "/view-low-rating-items",
            "role_name": "Admin"
        }

        self.db_handler.get_low_rating_items.return_value = [{"Name": "Soup", "Rating": 2.0}]

        self.food_menu_handler.endpointHandler(self.client_socket, request)

        expected_response = json.dumps({"status": "success", "low_rating_items": [{"Name": "Soup", "Rating": 2.0}]}).encode()
        self.client_socket.sendall.assert_called_with(expected_response)

    def test_view_food_menu_failure(self):
        request = {
            "endpoint": "/food_menu",
            "role_name": "Customer"
        }

        self.food_menu_handler.endpointHandler(self.client_socket, request)

        expected_response = json.dumps({"status": "failure", "message": "Access denied"}).encode()
        self.client_socket.sendall.assert_called_with(expected_response)

if __name__ == "__main__":
    unittest.main()
