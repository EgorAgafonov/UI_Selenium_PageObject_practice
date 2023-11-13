from dotenv import load_dotenv
import os

photo_1_jpg = os.path.abspath("C:\\Users\\agafo\\PycharmProjects\\pythonProject15_PageObjects_tests\\photos\\1.jpg")
photo_2_jpg = os.path.abspath("C:\\Users\\agafo\\PycharmProjects\\pythonProject15_PageObjects_tests\\photos\\2.jpg")

load_dotenv()
email = os.getenv('email')
password = os.getenv('pass')
invalid_email = os.getenv('invalid_email')
invalid_password = os.getenv('invalid_pass')
cookie_value = os.getenv("cookie_value")
