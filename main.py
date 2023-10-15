from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_objects.append(post)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    post_image = f"/static/{index}.jpg"
    for blog_post in post_objects:
        if int(blog_post["id"]) == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, image=post_image)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
