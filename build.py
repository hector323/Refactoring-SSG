# list of all content files
pages = [
  {
  "filename": "content/blog.html", "output": "/docs/index.html", "title": "My Personal Blogs"
  },
  {
  "filename": "content/projects.html", "output": "/docs/index.html", "title": "Projects"
  },
  {
  "filename": "content/contact.html", "output": "/docs/index.html", "title": "About Me"
  }
]


def content():
  for page in pages:
      content = page['filename']
      return content

content()

def apply_template(content):
  for page in pages:
      page_title = page['filename']
      template = open("./templates/base.html").read()
    # Read in the content of the index HTML page
      index_content = open(page_title).read()
      finished_index_page = template.replace("{{content}}", index_content)
      results = open("./docs/index.html", "w+").write(finished_index_page)

  return results

apply_template(content)

def main():
  for page in pages:
    page_title = page['filename']
    # Read in the entire template
    template = open("./templates/base.html").read()
    # Read in the content of the index HTML page
    index_content = open(page_title).read()
    finished_index_page = template.replace("{{content}}", index_content)

    return finished_index_page

main()




# First, get the template files
template = open('/templates/base.html').read()

# Read in index HTML code
content = open('middle_index.html').read()

# Combine template HTML code with content HTML code
index_html = top_template + content
open('index.html', 'w+').write(index_html)

# Rinse and repeat, but with blog HTML code
content = open('middle_blog.html').read()
blog_html = top_template + content + bottom_template
open('blog.html', 'w+').write(blog_html)

# And again, this time with art HTML code
content = open('middle_art.html').read()
art_html = top_template + content + bottom_template
open('art.html', 'w+').write(art_html)
















# def content():
#   for page in pages:
#     page_title = page['filename']
#     template = open("./templates/base.html").read()
#     # Read in the content of the index HTML page
#     index_content = open(page_title).read()
#     finished_index_page = template.replace("{{content}}", index_content)

#     return finished_index_page

# content()

# def apply_template(content):
#   for page in pages:
#     page['output'].replace(x, y)
#   results = open("docs/index.html", "w+").write(content)
#   # print(results)
#   return results


# def main():
#   content = open("docs/index.html").read()
#   resulting_html_for_index = apply_template(content)
#   return resulting_html_for_index

# main()

