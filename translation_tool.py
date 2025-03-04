from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = "1mcfCUMLD6UvnK9NQHf3K908w1iOdUVwlcxYAGydssKyTaM45fdCJQQJ99BCACGhslBXJ3w3AAAbACOGroNN"
REGION = "centralindia"
ENDPOINT = "https://api.cognitive.microsofttranslator.com/translate"


def translate_text_microsoft(text, target_language):

    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Ocp-Apim-Subscription-Region": REGION,
        "Content-Type": "application/json"
    }
    params = {
        "api-version": "3.0",
        "to": target_language
    }
    body = [{"text": text}]


    response = requests.post(ENDPOINT, headers=headers, params=params, json=body)


    if response.status_code == 200:
        return response.json()[0]["translations"][0]["text"]
    else:
        return f"Error: {response.status_code} - {response.text}"


@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = None
    if request.method == "POST":
        text = request.form.get("text")
        target_language = request.form.get("language")
        if text and target_language:
            translated_text = translate_text_microsoft(text, target_language)
    return render_template("index.html", translated_text=translated_text)


if __name__ == "__main__":
    app.run(debug=True)