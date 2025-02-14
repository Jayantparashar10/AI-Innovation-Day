import re

def format_response(response):
    """Format the chatbot response for better readability"""
    # Split response into sections
    sections = response.split('\n')
    formatted = []
    
    current_section = []
    for line in sections:
        if line.strip():
            if re.match(r'^[A-Z][A-Za-z\s]+:', line):  # New section header
                if current_section:
                    formatted.append('\n'.join(current_section))
                    current_section = []
                formatted.append(f"**{line.strip()}**")
            else:
                current_section.append(line.strip())
    
    if current_section:
        formatted.append('\n'.join(current_section))
    
    return '\n\n'.join(formatted)

def validate_input(user_input):
    """Validate user input"""
    if not user_input:
        return False, "Please enter your symptoms or question"
    if len(user_input.strip()) < 3:
        return False, "Please provide more details about your symptoms"
    if len(user_input.strip()) > 500:
        return False, "Please keep your description under 500 characters"
    return True, ""

def sanitize_input(user_input):
    """Sanitize user input to prevent injection"""
    return re.sub(r'[<>{}]', '', user_input)