from pyscript import document

def generate_message(event):
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    output = f"""
        🧑‍🎓 Student Profile
        Name : {name}
        Age : {age}
        School : {school}
        
        📚 Notes:
        {name} is currently {age} and is studying at {school}. They do very well
        in their academics."""
    
    document.getElementById("output").innerText = output