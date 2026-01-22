To fulfill your specific requirements and incorporate the Refresh Token and Cookie logic into your project documentation, you should update your README.md.

This will demonstrate to anyone reviewing your code that you went above and beyond the basic requirements to implement industry-standard security.

Professional README.md Template
You can copy and paste this content into your README.md file:

FastAPI Secure Authentication API
A professional-grade backend authentication system built with FastAPI and MySQL, featuring dual-token security (Access & Refresh tokens) and secure cookie storage.

🚀 Features
Secure Signup: Mandatory field validation and unique email checks.

Password Hashing: Uses bcrypt for one-way password encryption.

JWT Authentication: Implements short-lived Access Tokens for authorization.

Session Management: Implements Refresh Tokens stored in HTTPOnly Cookies.

Enhanced Security: Prevents XSS and CSRF attacks using secure cookie flags (httponly, samesite).

🛠 Tech Stack
Framework: FastAPI

Database: MySQL

ORM: SQLAlchemy

Security: Passlib (Bcrypt), PyJWT

Environment: Python-dotenv

🔒 Security Implementation Logic
Dual-Token System
Access Token (JSON Response):

Payload: Contains user_id and email.

Expiration: 30 minutes (configurable).

Usage: Sent by the client in the Authorization: Bearer <token> header.

Refresh Token (HTTPOnly Cookie):

Payload: Contains user_id.

Expiration: 7 Days.

Storage: Stored in an HttpOnly cookie, meaning it is invisible to JavaScript, protecting it from theft via XSS attacks.

🛣 API Endpoints
1. User Signup
Endpoint: POST /api/auth/signup

Description: Registers a new user and hashes the password.

Status Code: 201 Created

2. User Signin
Endpoint: POST /api/auth/signin

Description: Validates credentials and issues tokens.

Response Body: Returns Access Token and User Profile.

Response Header: Sets a Set-Cookie header containing the Refresh Token.

Status Code: 200 OK

📂 Deliverables
.env.example
Create a .env file based on this template:

Code snippet

DATABASE_URL=mysql+pymysql://user:password@localhost:3306/auth_db
SECRET_KEY=your_generated_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
Final Check for your Deliverables:
Unique Email: Your signup code already checks if the user exists.

No Plain-Text: Ensure your models.py uses the password_hash field.

Mandatory Fields: Pydantic (schemas.py) handles this automatically.

JWT Payload: Your auth_utils.py includes user_id and email.
