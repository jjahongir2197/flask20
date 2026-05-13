from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def table():

    result = []

    if request.method == "POST":

        number = int(request.form["number"])

        for i in range(1, 11):

            result.append(
                f"{number} x {i} = {number * i}"
            )

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)
