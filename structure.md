ROOT
|   .env
|   .gitignore
|   board.sqlite
|   create_docker.py
|   Dockerfile
|   entrypoint.sh
|   README.md
|   requirements.txt
|   setup.py
|   structure.md
|   structure.txt          
+---board
|   |   database.py
|   |   pages.py
|   |   posts.py
|   |   schema.sql
|   |   __init__.py
|   |   
|   +---static
|   |       styles.css
|   |       
|   +---templates
|   |   |   base.html
|   |   |   _navigation.html
|   |   |   
|   |   +---pages
|   |   |       about.html
|   |   |       home.html
|   |   |       
|   |   +---posts
|   |           create.html
|   |           posts.html