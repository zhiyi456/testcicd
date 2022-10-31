from invokes import invoke_http, all_route


course_route = "http://127.0.0.1:5000/skill"
skills = invoke_http(course_route, method='GET')
print(skills)