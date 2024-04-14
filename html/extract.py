from bs4 import BeautifulSoup

# Specify the path to your HTML file
html_file_path = './output.html'

with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
tables = soup.find_all('table')

with open('final.html', 'a', encoding='utf-8') as output_file:
  for table in tables:
      parent_tag = table.find_parent('p')
      next_p_tag = parent_tag.find_next_sibling('p')
      

      print(parent_tag)
      print(next_p_tag)

      # Remove the img tag from the parent_tag
      img_tag = parent_tag.find('img')
      if img_tag:
          img_tag.decompose()

      output_file.write(f"{parent_tag}\n")
      output_file.write(f"{next_p_tag}\n")
      output_file.write("\n")

# from bs4 import BeautifulSoup

# # Replace 'your_file.html' with the path to your HTML file
# file_path = 'output.html'

# # Read the content of the HTML file
# with open(file_path, 'r', encoding='utf-8') as file:
#     html_content = file.read()

# # Create a BeautifulSoup object
# soup = BeautifulSoup(html_content, 'html.parser')

# # Find all parent <p> tags without an <img> tag
# entries_without_img = [entry.find_parent('p') for entry in soup.find_all('img')]

# # Print the prettified version of each parent <p> tag without an <img> tag
# for entry in entries_without_img:
#     print("==============================================")
#     print()
#     print(entry)
#     print()

# from bs4 import BeautifulSoup

# # Replace 'your_file.html' with the path to your HTML file
# file_path = './output.html'

# # Read the content of the HTML file
# with open(file_path, 'r', encoding='utf-8') as file:
#     html_content = file.read()

# # Create a BeautifulSoup object
# soup = BeautifulSoup(html_content, 'html.parser')

# # Find all <g> tags that contain <image> tags
# result = soup.find_all(lambda tag: tag.name == 'g' and tag.find('image'))

# # Print the entire <g> tag for each result
# for element in result:
#     print("==============================================")
#     print()
#     print(element)
#     print()



# from bs4 import BeautifulSoup

# # Replace 'your_file.html' with the path to your HTML file
# file_path = './output.html'

# # Read the content of the HTML file
# with open(file_path, 'r', encoding='utf-8') as file:
#     html_content = file.read()

# # Create a BeautifulSoup object
# soup = BeautifulSoup(html_content, 'html.parser')

# # Find all <g> tags that contain <image> tags
# result = soup.find_all(lambda tag: tag.name == 'g' and tag.find('image'))

# # Print the result
# for element in result:
#     print(element)

# from bs4 import BeautifulSoup

# # Read the content of the HTML file
# with open('index.html', 'r', encoding='utf-8') as file:
#     html_content = file.read()

# # Parse the HTML content with BeautifulSoup
# soup = BeautifulSoup(html_content, 'html.parser')

# # Find all <tr> tags that contain an anchor tag with class "text_2"
# target_tr_tags = soup.find_all(lambda tag: tag.name == 'tr' and tag.find('a', class_='text_2') is not None)

# # Print or process the extracted <tr> tags
# for tr_tag in target_tr_tags:
#     print(tr_tag)

# from bs4 import BeautifulSoup

# # Read HTML content from a file
# with open('./output.html', 'r', encoding='utf-8') as file:
#     html_content = file.read()

# # Create a BeautifulSoup object
# soup = BeautifulSoup(html_content, 'html.parser')

# print("^^^^^^^^^^^^^^^^^^^^^^")
# # Find all elements with list-style-image: url('output.004.png');
# elements = soup.select('[style*="list-style-image: url(\'output.004.png\')"]')

# # Print the elements
# for element in elements:
#     print(element)

# print("*********************")
# # Find all elements with list-style-image: url('output.032.png');
# elements = soup.select('[style*="list-style-image: url(\'output.032.png\')"]')

# # Print the elements
# for element in elements:
#     print(element)


# print("@@@@@@@@@@@@@@@@@@@@@@@")
# # Find all elements with list-style-image: url('output.038.png');
# elements = soup.select('[style*="list-style-image: url(\'output.038.png\')"]')

# # Print the elements
# for element in elements:
#     print(element)




# from bs4 import BeautifulSoup

# def extract_tr_with_img(html_path):
#     with open(html_path, 'r', encoding='utf-8') as html_file:
#         soup = BeautifulSoup(html_file, 'html.parser')
    
#     # Find all <tr> tags
#     tr_tags = soup.find_all('tr')

#     # Filter <tr> tags that contain an <img> tag
#     tr_with_img_list = [tr_tag for tr_tag in tr_tags if tr_tag.find('img') is not None]
    
#     return tr_with_img_list

# if __name__ == "__main__":
#     html_path = "merged.html"  # Replace with the path to your HTML file

#     tr_with_img_list = extract_tr_with_img(html_path)

#     # Print the extracted <tr> tags
#     for tr_tag in tr_with_img_list:
#         print(tr_tag)
# from bs4 import BeautifulSoup

# # Read HTML content from the file
# file_path = './merged.html'
# with open(file_path, 'r', encoding='utf-8') as file:
#     html_content = file.read()

# soup = BeautifulSoup(html_content, 'html.parser')

# # Find all <tr> tags
# all_trs = soup.find_all('tr')

# # Extract the content of <tr> tags that contain an <img> tag
# extracted_content = []
# for tr in all_trs:
#     if tr.find('img') is not None:
#         extracted_content.append(str(tr))

# # Print or use the extracted content as needed
# for content in extracted_content:
#     print(content)