from flask import Flask, request, send_file, render_template, make_response
import openai
import os

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    return make_response(render_template('aisomm2.html'))

@app.route('/taste/', methods=['GET'])
def process_form_get():
    process_form_post()

@app.route('/taste/', methods=['POST'])
def process_form_post():
    body = request.form['body']
    alcohol = request.form['alcohol']
    acidity = request.form['acidity']
    tannins = request.form['tannins']
    wine_type = request.form['wine-type']
    flavors = request.form.getlist('flavors')
    
    prompt = f"I want you to give me a list of 3 possible wine styles that match these parameters. Acidity (1 to 5): {acidity}, Alcohol (1 to 5):{alcohol}, Tannins (0 to 5):{tannins}, Body (1 to 5): {body}, Wine type (Red, White, Rose, Orange, Sparkling and Fortified):{wine_type}, and a list of flavors: {flavors}. Return a simple list without any introduction or comments.'"
       
    return render_template('result.html', result=sommelAIer(prompt))
    

def sommelAIer(prompt):
    # Set up your OpenAI API key
    openai.api_key = os.environ["OPENAI_API_KEY"]

    # Set up the parameters for the GPT request
    temperature = 0.5
    max_tokens = 50

    # Send the request to the ChatGPT instance
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,)

    # Print the generated text from the ChatGPT instance
    return response.choices[0].text.strip()
    
if __name__ == '__main__':
    app.run(debug=True)
