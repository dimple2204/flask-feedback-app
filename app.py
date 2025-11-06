from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    # show the feedback form by default
    return render_template("feedback.html")


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        # get form values (provide defaults if missing)
        name = request.form.get("username", "Anonymous")
        message = request.form.get("message", "")
        # render thank you page with submitted values
        return render_template("thankyou.html", user=name, message=message)
    # GET -> show form
    return render_template("feedback.html")


if __name__ == "__main__":
    app.run(debug=True)
