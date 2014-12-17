import webapp2


class {{ cookiecutter.repo_name|capitalize }}Main(webapp2.RequestHandler):
    def get(self):
        return self.response.out.write('Hello, {{ cookiecutter.project_name }}!')


app = webapp2.WSGIApplication([
    ('/_{{ cookiecutter.repo_name }}/?', {{ cookiecutter.repo_name|capitalize }}Main)
])
