import os
import sys

dir_path = sys.argv[1]
tool_name = sys.argv[2] if len(sys.argv) == 3 else None

if not os.path.exists(dir_path):
    print(f"'{dir_path}' is not a valid directory.")
    sys.exit()

list_of_files = os.listdir(dir_path)

if (len(sys.argv) != 3):
    print("Usage: generate_html.py <path_to_the_source_directory> <name_of_the_tool>")
    sys.exit()

html_file = open(f'{tool_name}.html', 'w')

html_file.write('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Quicksand&display=swap");

      body {
        background-color: #d0d0d0;
        font-family: "Quicksand", sans-serif;
        margin: 10px;
        padding: 10px;
      }

      img {
        background-color: #e0e0e0;
        border: 1px solid #000;
        background-image: linear-gradient(0deg, #a0a0a0 0%, #c0c0c0 100%);
        padding: 2px;
        margin: 10px;
      }

      .center {
        margin: auto;
        text-align: center;
      }
    </style>''')


html_file.write(f'''
    <title>Fuzzing Data for {tool_name}</title>''')

html_file.write(f'''
  </head>
  <body>
    <div class="center">
      <h1>Fuzzing Data for {tool_name}</h1>''')

for file in list_of_files:
    html_file.write(f'''
      <img src="{dir_path}{file}" height="64" width="64" />''')

html_file.write('''
    </div>
  </body>
</html>

''')
