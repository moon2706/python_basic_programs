email=input("Enter Your Email ID: ").strip()
username=email[:email.index("@")]
domain=email[email.index("@")+1:]
format=(f"Your username is '{username}' and your domain is '{domain}'")
print(format)