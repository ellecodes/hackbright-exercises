"""
seed.py
"""
import model

db = model.connect_db()
user_id = model.new_user(db, "chriszf@gmail.com", "securepassword", "Christian")
task = model.new_task(db, "Complete this task list", user_id)

user_id = model.new_user(db, "laura@gmail.com", "securepassword", "Laura")
task = model.new_task(db, "Tweet", user_id)

user_id = model.new_user(db, "elle@gmail.com", "securepassword", "Elle")
task = model.new_task(db, "Blog", user_id)

user_id = model.new_user(db, "meggie@gmail.com", "securepassword", "Meggie")
task = model.new_task(db, "Bike to Berkeley", user_id)