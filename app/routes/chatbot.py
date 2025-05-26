from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user

chatbot = Blueprint('chatbot', __name__)

@chatbot.route('/chatbot')
@login_required
def chatbot_page():
    # Restrict admins from accessing chatbot page
    if current_user.role == 'admin':
        return "Admins cannot access the chatbot.", 403
    return render_template('chatbot.html')

@chatbot.route('/chatbot/api', methods=['POST'])
@login_required
def chatbot_api():
    # Restrict admins from using chatbot API
    if current_user.role == 'admin':
        return jsonify({'reply': 'Admins do not have chatbot access.'})

    data = request.get_json()
    user_msg = data.get('message', '').lower()

    # Simple keyword-based response logic
    if 'hello' in user_msg or 'hi' in user_msg:
        reply = "Hello! How can I assist you with your CloudVault files today?"
    elif 'upload' in user_msg:
        reply = "To upload a file, go to the 'Files' page and use the upload form."
    elif 'download' in user_msg:
        reply = "You can download your files from the 'Files' page by clicking the Download button."
    elif 'delete' in user_msg or 'remove' in user_msg:
        reply = "To delete a file, go to the 'Files' page and click the Delete button next to the file."
    elif 'help' in user_msg:
        reply = "I can help you upload, download, or delete files. Try asking me!"
    else:
        reply = "Sorry, I didn't understand that. You can ask about uploading, downloading, or deleting files."

    return jsonify({'reply': reply})
