from sqlalchemy import create_engine
# test

# # Connect to db
 engine = create_engine("")

 print(engine)

password = b"secret password"

# Hash password
hashed = bcrypt.hashpw(password, bcrypt.gensalt(14)
print(hashed)

# Check to see if user has got the correct password
if bcrypt.checkpw(password, hashed):
    print("right password")
else:
    print("wrong password")
