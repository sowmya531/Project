from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Sample genre-wise data
story_data = {
    "romcom": [
        {
            "prompt": "A shy barista and a CEO switch bodies.",
            "idea": "They live each other's lives and fall in love through the chaos."
        },
        {
            "prompt": "Two fake lovers on a dating show turn real.",
            "idea": "Childhood enemies are forced to act like a couple — but sparks fly."
        }
    ],
    "horror": [
        {
            "prompt": "A family moves into a silent town.",
            "idea": "They discover everyone vanished after a haunting ritual."
        },
        {
            "prompt": "A girl finds a mirror that shows the dead.",
            "idea": "Each night, the dead get closer to her real world."
        }
    ],
    "thriller": [
        {
            "prompt": "A hacker is trapped in his own AI simulation.",
            "idea": "He must outsmart his own creation to survive."
        },
        {
            "prompt": "A detective keeps reliving the same crime scene.",
            "idea": "The only way to stop it is to catch himself."
        }
    ],
    "suspense": [
        {
            "prompt": "A woman receives letters predicting future murders.",
            "idea": "Each letter leads her deeper into a twisted mystery."
        },
        {
            "prompt": "A student disappears every full moon.",
            "idea": "The truth is hidden in the school’s underground archive."
        }
    ]
}

@app.route("/", methods=["GET", "POST"])
def home():
    selected_stories = []
    selected_genre = ""

    if request.method == "POST":
        selected_genre = request.form.get("genre")
        if selected_genre in story_data:
            selected_stories = random.sample(story_data[selected_genre], k=2)

    return render_template("index.html", stories=selected_stories, genre=selected_genre)

if __name__ == "__main__":
    app.run(debug=True)
