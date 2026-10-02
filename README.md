# Pixelora Digital Works — Flask Website

A multi-page, responsive creative studio website built with Python Flask, HTML and CSS, with a small amount of JavaScript for mobile navigation and the WhatsApp enquiry form.

## Run on Windows

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000. Pages: `/`, `/about`, `/services`, `/portfolio`, `/contact`.

The contact form opens WhatsApp with the visitor's message ready to send; it does not store enquiries. Project interface imagery is illustrative. Replace it with approved project screenshots before publishing. Update the contact number in `templates/base.html` and `templates/contact.html` if needed.
