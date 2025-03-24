import re
def assess_password_strength(password):
    strength = 0
    feedback = []
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Use at least one special character (!@#$%^&* etc.).")
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong", "Extremely Strong"]
    return strength_levels[min(strength, len(strength_levels) - 1)], feedback
  
if __name__ == "__main__":
    password = input("Enter a password to assess: ")
    strength, feedback = assess_password_strength(password)
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions:")
        for suggestion in feedback:
            print(f"- {suggestion}")
