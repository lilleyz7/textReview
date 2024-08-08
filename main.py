from flask import Flask, request, render_template
from extraction import get_statistics, extract_from_pdf

app = Flask(__name__, template_folder="templates")

app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.secret_key = b'hbf78f332iewfw87fov;;sdfg3rgw56'

@app.route('/', methods=["GET", "POST"])
async def main():
    if request.method == "GET":
        return render_template("main.html")
    
    if request.method == "POST":
        if 'file' in request.files:
            file = request.files['file']
            if file.filename == '':
                return render_template('main.html', error="No file specified")
            if file and file.filename.endswith('.pdf'):
                details = await extract_from_pdf(file)
                return render_template('main.html', details=details)
            if file and file.filename.endswith('.txt'):
                content = file.stream.readlines()
                finalStr = ""
                for line in content:
                    strline = line.decode('utf-8')
                    strline.replace("\n", " ")
                    finalStr += (strline + " ")
                details = await get_statistics(finalStr)
                print(details)
                return render_template('main.html', details=details)
        return render_template('main.html', error="No file uploaded")
    
# @app.route('/upload', methods=["POST"])
# async def upload():
#     if 'file' in request.files:
#         file = request.files['file']
#         if file.filename == '':
#             return render_template('main.html', error="No file specified")
#         if file and file.filename.endswith('.pdf'):
#             details = await extract_from_pdf(file)
#             return render_template('main.html', details=details)
#         if file and file.filename.endswith('.txt'):
#             content = file.stream.readlines()
#             finalStr = ""
#             for line in content:
#                 strline = line.decode('utf-8')
#                 strline.replace("\n", " ")
#                 finalStr += (strline + " ")
#             details = await get_statistics(finalStr)
#             print(details)
#             return render_template('details.html', details=details)
#     return render_template('main.html', error="No file uploaded")

        
if __name__ == "__main__":
    app.run(debug=False)