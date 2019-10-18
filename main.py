import webapp2


class arun(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('He is the hero we deserve but not the one we need right now')


app = webapp2.WSGIApplication([
    ('/', arun),
], debug=True)
