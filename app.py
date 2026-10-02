
from flask import Flask, render_template, jsonify, Response
from xml.etree.ElementTree import Element, SubElement, tostring

app = Flask(__name__)

PAGES = {
    "home": {
        "title": "Pixelora Digital Works | We Create. You Grow.",
        "active": "home"
    },
    "about": {
        "title": "About | Pixelora Digital Works",
        "active": "about"
    },
    "services": {
        "title": "Services | Pixelora Digital Works",
        "active": "services"
    },
    "portfolio": {
        "title": "Selected Work | Pixelora Digital Works",
        "active": "portfolio"
    },
    "contact": {
        "title": "Start a Project | Pixelora Digital Works",
        "active": "contact"
    },
}


def page(name):
    return render_template(f"{name}.html", page=PAGES[name])


# Home Page
@app.get("/")
def home():
    return page("home")


# About Page
@app.get("/about")
def about():
    return page("about")


# Services Page
@app.get("/services")
def services():
    return page("services")


# Portfolio Page
@app.get("/portfolio")
def portfolio():
    return page("portfolio")


# Contact Page
@app.get("/contact")
def contact():
    return page("contact")


# XML Sitemap for Google Search Console
@app.get("/sitemap.xml")
def sitemap():
    base_url = "https://pixelorads.in"

    pages = [
        "",
        "/about",
        "/services",
        "/portfolio",
        "/contact",
    ]

    urlset = Element(
        "urlset",
        {
            "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9"
        }
    )

    for path in pages:
        url = SubElement(urlset, "url")
        SubElement(url, "loc").text = base_url + path

    xml_content = tostring(
        urlset,
        encoding="utf-8",
        xml_declaration=True
    )

    return Response(
        xml_content,
        mimetype="application/xml"
    )


# Robots.txt for Search Engines
@app.get("/robots.txt")
def robots():
    content = """User-agent: *
Allow: /

Sitemap: https://pixelorads.in/sitemap.xml
"""

    return Response(
        content,
        mimetype="text/plain"
    )


# Website Health Check
@app.get("/health")
def health():
    return jsonify(
        status="ok",
        app="Pixelora Digital Works"
    )


if __name__ == "__main__":
    app.run(debug=True)