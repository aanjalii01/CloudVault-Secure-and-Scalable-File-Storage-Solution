import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory, abort
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app.extensions import db
from app.models import File
from app.forms import UploadFileForm

files = Blueprint('files', __name__)

UPLOAD_FOLDER = 'uploads'

def allowed_file(filename):
    allowed_extensions = {
        'jpg', 'jpeg', 'png', 'pdf', 'txt', 'doc', 'docx',
        'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'rar', 'csv'
    }
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@files.route('/files', methods=['GET'])
@login_required
def files_page():
    user_files = File.query.filter_by(user_id=current_user.id).order_by(File.uploaded_at.desc()).all()
    form = UploadFileForm()
    return render_template('files.html', files=user_files, form=form)

@files.route('/files/upload', methods=['POST'])
@login_required
def upload_file():
    form = UploadFileForm()
    if form.validate_on_submit():
        uploaded_file = form.file.data
        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = secure_filename(uploaded_file.filename)
            user_folder = os.path.join(UPLOAD_FOLDER, str(current_user.id))
            os.makedirs(user_folder, exist_ok=True)
            filepath = os.path.join(user_folder, filename)

            # Avoid overwrite by renaming if file exists
            if os.path.exists(filepath):
                base, ext = os.path.splitext(filename)
                count = 1
                while os.path.exists(filepath):
                    filename = f"{base}_{count}{ext}"
                    filepath = os.path.join(user_folder, filename)
                    count += 1

            uploaded_file.save(filepath)

            new_file = File(filename=filename, filepath=filepath, user_id=current_user.id)
            db.session.add(new_file)
            db.session.commit()
            flash(f'File "{filename}" uploaded successfully.', 'success')
        else:
            flash('Invalid file type.', 'danger')
    else:
        flash('No file selected or invalid input.', 'danger')

    return redirect(url_for('files.files_page'))

@files.route('/download/<int:file_id>', methods=['GET'])
@login_required
def download_file(file_id):
    file_record = File.query.get_or_404(file_id)
    if file_record.user_id != current_user.id and current_user.role != 'admin':
        abort(403)

    full_path = file_record.filepath

    # Make sure full_path is absolute
    if not os.path.isabs(full_path):
        full_path = os.path.join(os.getcwd(), full_path)

    if not os.path.exists(full_path):
        abort(404, description="File not found on server")

    directory = os.path.dirname(full_path)
    filename = os.path.basename(full_path)

    return send_from_directory(directory, filename, as_attachment=True)



@files.route('/delete/<int:file_id>', methods=['GET', 'POST'])  # fixed route here
@login_required
def delete_file(file_id):
    file_record = File.query.get_or_404(file_id)
    if file_record.user_id != current_user.id and current_user.role != 'admin':
        abort(403)
    try:
        if os.path.exists(file_record.filepath):
            os.remove(file_record.filepath)
        db.session.delete(file_record)
        db.session.commit()
        flash(f'File "{file_record.filename}" deleted.', 'info')
    except Exception:
        flash('Error deleting file.', 'danger')
    return redirect(url_for('files.files_page'))
