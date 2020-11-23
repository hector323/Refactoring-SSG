# You should have a “pages” list in the following format:4

# Your list must contain dictionaries. Each dictionary has information3 about a page on your site. It must also contain a file path that can be used to read the contents of the page, and a file path of where you will eventually output the combined version of this page.
pages = [
  {
  "filename": "content/about.html", "output": "docs/about.html", "title": "About Me"
  },
  {
  "filename": "content/blog.html", "output": "docs/blog.html", "title": "My programming blog"
  },
  {
  "filename": "content/blog.html", "output": "docs/blog.html", "title": "My programming blog"
  }
]

for page in pages:
  # print(page['filename'])
  # To access data within a dictionary, consider the following code as a clue:
  # Where "page" is a dictionary with a key "title"
  print(page) # Replace this line eventually with other stuff...

# Where "page" is a dictionary with a key "title"
  page_title = page['filename']
  print(page_title)

# def apply_template(content):
#   # TODO: Read in template, do string replacing, and return result
#   return results

# def main():
#   content = open(’docs/index.html’).read()
#   resulting_html_for_index = apply_template(content)

# def main():
#   base_html = open('./templates/base.html').read()
#   middle_html = open('./content/blog.html').read()
#   combined_html = base_html + middle_html
#   open('blog.html', 'w+').write(combined_html)

#   middle_html = open('./content/projects.html').read()
#   combined_html = base_html + middle_html
#   open('projects.html', 'w+').write(combined_html)

#   middle_html = open('./content/contact.html').read()
#   combined_html = base_html + middle_html
#   open('contact.html', 'w+').write(combined_html)

# main()



