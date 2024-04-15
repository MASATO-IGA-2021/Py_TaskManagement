import requests
import json
from flask import Flask,render_template,request

import line_util
import task

class main:
    # message = "Hello, this is your LINE chatbot!お試しちゃっとボットです！！！"
    # line = line_util.lineUtil()
    # line.send_message(message)
    app = Flask(__name__)
    
    @app.route("/")
    def displayTaskList(name=None):
        return render_template('TaskList.html', name=name)

    
    @app.route("/post", methods = ['POST','GET'])
    def postTask():
        if request.method == "POST" :
            title = request.form["title"]
            due_day = request.form["due_day"]
            comment = request.form["comment"]
            task_ticket = task.Task(title, due_day, comment)
            line = line_util.lineUtil()
            message = "タスク名{}期限日{}内容{}".format(title, due_day, comment)
            line.send_message(message)
            return render_template("TaskList.html")
        else:
            return render_template("MakeTask.html")
        
    
    @app.route("/show/<int:task_id>")
    def showTask(task_id):
        return "Hello World",task_id
    

    if __name__ == "__main__":
        app.run(debug=True)
#     json_load = getJsonFile()
#     access_token = json_load["line_information"]["access_token"]
#     user_id = json_load["line_information"]["user_id"]

#     send_message(access_token, user_id, message)

