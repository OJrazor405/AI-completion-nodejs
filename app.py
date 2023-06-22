import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        name = request.form["name"]
        category = request.form["category"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(name, category),
            temperature=0.8,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(name, category):
    # Change this to make the prompt your own!
    prompt = ("""Suggest three names for a {ctg}
                name: Ole
                Names: Captain Ole the {ctg}, Agent-{ctg} Ole, Ole The Incredible {ctg}
                name: Jorgen
                Names: {ctg} Jorgen, Ol' Jorgen the {ctg}, Jorgen the Great {ctg}
                name: Daniel
                Names: {ctg} Daniel, Daniel the Magnificent {ctg}, Daniel Mc{ctg}
                name: {nm}
                Names:""").format(ctg=category, nm=name)
    return prompt
