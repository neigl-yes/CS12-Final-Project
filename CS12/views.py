import cherrypy

class FormSubmission(object):
    @cherrypy.expose
    def index(self):
        return """<html>
        <head>
            <title>FORM RAHHH</title>
        </head>
        <body>
            <form action="formsubmission" method="POST" onsubmit="return formValidation()" novalidate>
                <div>
                <label for="studentno">Student Number</label> <br>
                <input type="text" id="studentno" name="studentno"> <br>
                <label for="firstname">First Name</label> <br>
                <input type="text" id="firstname" name="firstname"> <br>
                <label for="lastname">Last Name</label> <br>
                <input type="text" id="lastname" name="lastname"> <br>
                <label for="age">Age</label> <br>
                <input type="number" id="age" name="age"> <br>
                <label for="email">Email</label> <br>
                <input type="email" id="email" name="email"> <br>
                <br>
                <button type="submit">Submit Data</button>
                </div>
            </form>

            <script src="public/script.js"></script>
        </body>
        </html>"""
    
    @cherrypy.expose
    def formsubmission(self, studentno, firstname, lastname, age, email):
        return f"""
            <h1>Submission Successful!</h1>
            <p>Student No: {studentno}</p>
            <p>Name: {firstname} {lastname}</p>
            <p>Age: {age}</p>
            <p>Email: {email}</p>
        """