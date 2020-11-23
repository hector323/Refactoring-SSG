# # Reads in the top.html
# # print('reading in html variables')
# base_html = open('./templates/base.html').read()
# # print(top_html)

# # Reads in the bottom.html
# # bottom_html = open('./templates/bottom.html').read()
# # print(bottom_html)

# # Reads in the middle index.html
# middle_html = open('./content/blog.html').read()
# # print(middle_html)

# # combining all 3 files
# # Assembles hte new index.html file by combining the top middle and bottom in that order
# combined_html = base_html + middle_html
# # print(combined_html)

# # Writes the new index.html file to a brand new file in the same directory
# open('index.html', 'w+').write(combined_html)


# # Reads in the middle index.html
# middle_html = open('./content/projects.html').read()

# combined_html = base_html + middle_html

# # Writes the new index.html file to a brand new file in the same directory
# open('projects.html', 'w+').write(combined_html)

# # Reads in the middle index.html
# middle_html = open('./content/contact.html').read()

# combined_html = base_html + middle_html

# # Writes the new index.html file to a brand new file in the same directory
# open('blog.html', 'w+').write(combined_html)



def main():
  base_html = open('./templates/base.html').read()
  middle_html = open('./content/blog.html').read()
  combined_html = base_html + middle_html
  open('blog.html', 'w+').write(combined_html)

  middle_html = open('./content/projects.html').read()
  combined_html = base_html + middle_html
  open('projects.html', 'w+').write(combined_html)

  middle_html = open('./content/contact.html').read()
  combined_html = base_html + middle_html
  open('contact.html', 'w+').write(combined_html)

main()



