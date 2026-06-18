import os

# =========================
# SAVE UPLOADED PDF
# =========================

def save_uploaded_file(uploaded_file):

    # Create folder if it does not exist
    upload_dir = "uploaded_pdfs"

    os.makedirs(
        upload_dir,
        exist_ok=True
    )

    # Create complete save path
    save_path = os.path.join(
        upload_dir,
        uploaded_file.name
    )

    # Save uploaded PDF
    with open(save_path, "wb") as f:

        f.write(
            uploaded_file.getbuffer()
        )

    return save_path