"""
seed.py
"""
import model

db = model.connect_db()
user_id = model.new_user(db, "chriszf@gmail.com", "securepassword", "Christian")
task = model.new_task(db, "Brush hair", user_id)
task = model.new_task(db, "Complete this task list", user_id)
task = model.new_task(db, "Sleep", user_id)

user_id = model.new_user(db, "laura@gmail.com", "securepassword", "Laura")
task = model.new_task(db, "Tweet", user_id)
task = model.new_task(db, "Blog", user_id)
task = model.new_task(db, "Caltrain to San Jose", user_id)

user_id = model.new_user(db, "elle@gmail.com", "securepassword", "Elle")
task = model.new_task(db, "Tweet", user_id)
task = model.new_task(db, "Blog", user_id)
task = model.new_task(db, "Caltrain to San Jose", user_id)

user_id = model.new_user(db, "meggie@gmail.com", "securepassword", "Meggie")
task = model.new_task(db, "Bike to Berkeley", user_id)
task = model.new_task(db, "Write swimming exercises", user_id)
task = model.new_task(db, "Sew stockings", user_id)
task = model.new_task(db, "Blog", user_id)
