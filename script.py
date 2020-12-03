# pages = [
#     {"filename": None,"output":None,"title":None},
#     {"filename": None,"output":None,"title":None},
#     {"filename": None,"output":None,"title":None}
# ]

pages = [
    {"filename": 'blog', "output": "/docs/blog.html", "title": "My Personal Blogs"},
    {"filename": 'projects', "output": "content/projects.html", "title": "Projects"},
    {"filename": "about", "output": "/docs/index.html", "title": "About Me"}
]
def main():
  for page in pages:
    print(page['filename'])
    base = open('./templates/base.html').read()
    middle_html = open('./content/blog.html').read()
    # combining all 3 files
    # Assembles hte new index.html file by combining the top middle and bottom in that order
    combined_html = base + middle_html
    # print(combined_html)
    # Writes the new index.html file to a brand new file in the same directory
    open('index.html', 'w+').write(combined_html)
    # Reads in the middle index.html
    middle_html = open('./content/projects.html').read()
    combined_html = base + middle_html
    # Writes the new index.html file to a brand new file in the same directory
    open('projects.html', 'w+').write(combined_html)
    # Reads in the middle index.html
    middle_html = open('./content/blog.html').read()
    combined_html = base + middle_html
    # Writes the new index.html file to a brand new file in the same directory
    open('blog.html', 'w+').write(combined_html)

main()

# print(pages)


# Bonus solution that only has one template file that it applies templating to
# to insert the right data in the right spots
from string import Template
template = open("./templates/base.html").read()
# template = Template(template_text)

print(template)
# Use "format" feature of Python strings to insert data where needed for the
# index page
index_content = open("./content/contact.html").read()
finished_index_page = template.replace("{{content}}", index_content)
# index_html = template.safe_substitute(
#     title="About Me",
#     index_class="active",
#     content=index_content,
# )
open('about.html', 'w+').write(ind_html)

# Do the same for blog, this time having the page title be Blog, the blog link
# be active, and the using the blog content in the middle
blog_content = open("./content/blog.html").read()
finished_blog_page = template.replace("{{content}}", blog_content)
# blog_html = template.safe_substitute(
#     title="Blog",
#     blog_class="active",
#     content=blog_content,
# )
open('blog.html', 'w+').write(bl_html)


# Finally, do the same for the art page
projects_content = open("content/projects.html").read()
finished_projects_page = template.replace("{{content}}", projects_content)
# art_html = template.safe_substitute(
#     title="Projects",
#     art_class="active",
#     content=art_content,
# )
open('art.html', 'w+').write(pro_html)

