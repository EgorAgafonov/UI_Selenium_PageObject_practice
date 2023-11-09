from dotenv import load_dotenv
import os

photo_1_jpg = os.path.abspath \
    ("C:\\Users\\agafo\\PycharmProjects\\pythonProject15_PageObjects_tests\\photos\\1.jpg")
photo_2_jpg = os.path.abspath \
    ("C:\\Users\\agafo\\PycharmProjects\\pythonProject15_PageObjects_tests\\photos\\2.jpg")

pf_cookies = "C:\\Users\\agafo\\PycharmProjects\\pythonProject15_PageObjects_tests\\my_cookies.pkl"

load_dotenv()
email = os.getenv('email')
password = os.getenv('pass')
invalid_email = os.getenv('invalid_email')
invalid_password = os.getenv('invalid_pass')
