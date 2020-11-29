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

