# proj_fetch_meta_data_Team_84
# ABOUT THE PROJECT
  A platform that allows authenticated users to upload files, so as to extract the metadata of the uploaded file and the metadata is displayed 
### Working Team Name
  - 84Meta
### Team Logo
  ![Logo](https://res.cloudinary.com/issie/image/upload/v1659619070/Logo_1_eeynk2.png)
### Team Members
  - See list Here[^1]
### TABLE OF CONTENTS
  - [FEATURES](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#features)
  - [DESIGN DOCUMENTATION](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#design-documentation)
  - [DEVELOPER DOCUMENTATION](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#developer-documentation)
    - [LANGUAGES](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#languages)
    - [DATABASE](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#database)
    - [DEPENDENCIES](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#dependencies)
    - [FRONTEND FUNCTIONALITIES](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#frontend-functionalities)
    - [BACKEND FUNCTIONALITIES](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#backend-functionalities)
      - [DJANGO](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#django)
      - [ARCHITECTURE](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#architecture) 
      - [DATABASE SCHEMA](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#database-schema)
  - [GETTING STARTED AND USAGE REQUIREMENTS](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#getting-started-and-usage-requirements)
    - [ISSUES](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#issues)
      - [REPORTING AN ISSUE](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#reporting-an-issue)
      - [FIXING AN ISSUE](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#fixing-an-issue)
    - [CONTRIBUTING](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#contributing)
      - [CONNECTING REPOSITORY AND SETTING UPSTREAM](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#connecting-repository-and-setting-upstream)
      - [PULL REQUESTS](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#pull-requests)
      - [CHECKLIST](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#checklist)
      - [REQUIREMENTS](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#requirements)
    - [DEPLOYMENT](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#deployment)
       - [REQUIRED PACKAGES](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#required-packages)
       - [RUNNING ON LOCAL MACHINE](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#running-on-local-machine)
   - [ACKNOWLEDGEMENTS](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#acknowledments)
   - [README CONTRIBUTING AUTHORS](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#readme-contributing-authors)
   - [REFERENCES/FOOTER](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#referencesfooter)

# FEATURES
  - Require User Authentication to perform extraction of metadata
  - Allows File upload
  - Extract metadata from *PDF*,  *Images (Jpeg, Jpg, Png etc.)*,  *JSON*,  *CSV*
  - Validate file type
  - Validate file size
  - Save uploaded files for further use
  - Share to social media
  - Download metadata
  - Export Metadata
# DESIGN DOCUMENTATION
  - [Low fidelity designs](https://www.figma.com/file/JQtpoNpLc7SeBEHpormEqh/Team84_fetch_metadata-collaboration?node-id=0%3A1)
  - [High Fidelity designs](https://www.figma.com/file/JQtpoNpLc7SeBEHpormEqh/Team84_fetch_metadata-collaboration?node-id=2%3A3)
  - [Style guide](https://www.figma.com/file/JQtpoNpLc7SeBEHpormEqh/Team84_fetch_metadata-collaboration?node-id=2%3A2)
  - [Userflow](https://www.figma.com/file/0YyH4VImuyfpTcKR0z6CkF/Userflow%2C-user-story%2C-empathy-map%2C-impact-effort-matrix?node-id=0%3A1)
# DEVELOPER DOCUMENTATION
## LANGUAGES
### FRONTEND
   1. HTML
   2. CSS
   3. JAVASCRIPT
### BACKEND
   1. PYTHON
   2. DJANGO
   
## DATABASE
   1. SQLite offered by Django
 
## SERVER
   1. Digital Ocean provided by Zuri
   
## MODULES
   - PasswordResetTokenGenerator
   - account_activation_token
   - EmailMessage
   - Redirect and Render
   - FileSystemStorage
   
## DEPENDENCIES
   - Pillow Library from PIL
   - Python Magic library
   - Six
   - Twitter share API
   - Facebook share API
   
## FRONTEND FUNCTIONALITIES
  ### PAGES/ TEMPLATES
   - Home page/ Landing page
   - Dashboard [Extraction space]
   - About Us Page
   - Contact us page
   - Login Page
   - Sign up Page
   - Forgot password page
   - Frequently asked questions [FAQ] page

## BACKEND FUNCTIONALITIES
 ### DJANGO
   - User Authentication using Django Authentication Systems
   - Database management for user profile and user uploads
   - File type and size validation
   - File metadata extraction
   - Communication with frontend using Django Templates

 ### ARCHITECTURE 
  - Monolith (Django templating)

 ### DATABASE SCHEMA
 - Link to [Schema](https://miro.com/app/board/uXjVOjcOrRY=/?share_link_id=276742582296)
        
## GETTING STARTED AND USAGE REQUIREMENTS
  ### ISSUES
   #### REPORTING AN ISSUE
    
    1. On noticing any issues with code
        - Search through existing issues to find out if issue has been logged by another contributor
        - Please create a new issue if it doesn't already exist that's detailed for the developers to understand and fix.
        
    2. Label the issue correctly for appropriate handling
    
  #### FIXING AN ISSUE
    1. Search for an issue you can fix
      - Note the tasks that need fixing within the issue
      
    2. Fork repo and work on the issue in order to keep development area secure
    
    3. Create pull request on finished fix and ensure it is linked to corresponding issue by attaching the appropriate keyword
      - If you are a base developer in the project or you're working on the same repository. Reference issue by keyword e.g. resolves #12, closes #13
        - If you are contributing from external repository, reference issue by repository name and issue number e.g. proj_fetch_meta_data_Team_84 closes #13
    
 ### CONTRIBUTING
 #### Project is Open Source
   - Contributions and Feedback are welcome
   
 #### CONNECTING REPOSITORY AND SETTING UPSTREAM
 1. Fork the main branch of the repository
 2. Clone the forked repository to local 

        git clone forked-repo-address
 3. Set this repo as upstream to ensure your repository is up to date

        git remote add upstream https://github.com/zuri-training/proj_fetch_meta_data_Team_84.git
 4. Pull changes from our repo
    
        git fetch upstream
 5. Pull changes from our repo to your remote repo
        
        git pull upstream main
 6. Stage your changes
    - For all files
    
          git add -A 
    - For specific file
        
          git add 'example.html'
 7. Write descriptive commit message

        git commit -m 'example change to example issue on example file'
 8. Push your changes to your remote repo
 
        git push
  
  ### PULL REQUESTS
  1. Create a pull request on our main branch
  2. Give detailed description on your pull request and link to approriate issue [See Fixing an Issue above](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#fixing-an-issue)
  3. Wait for our reviewers to approve pull request for merging
  
  #### CHECKLIST
   - [ ] Ensure you have dependencies installed.
   - [ ] List extra dependencies in branch readMe and create requirements.txt file with dependencies which is pushed along with other files.
   - [ ] Ensure secret keys  are kept secret and virtual environment is placed in git ignore files 
  
  ### REQUIREMENTS
  KNOWLEDGE OF:
   1. HTML5
   2. CSS
   3. Javascript
   4. Django including Class based views and Function based views, Authentication, Forms
   5. Python

  INSTALLATION
  1. An Integrated development environment [IDE]
  - Examples
    - [Visual Studio](https://visualstudio.microsoft.com/)
    - [Sublime Text](https://www.sublimetext.com/3)
  3. Git  
   - [WindowsOS](https://git-scm.com/download/win)
   - [MacOS](https://git-scm.com/download/mac)
  4. Git Desktop for collaboration **Optional** 
   - [WindowsOS](https://central.github.com/deployments/desktop/desktop/latest/win32)
   - [MacOS](https://central.github.com/deployments/desktop/desktop/latest/darwin)
   - [Windows MSI](https://central.github.com/deployments/desktop/desktop/latest/win32?format=msi)
  5. Python 3.10 or higher 
   - [WindowsOS](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe)
   - [MacOS](https://www.python.org/ftp/python/3.10.4/python-3.10.4-macos11.pkg)
  6. Installation of dependencies [See Dependencies above](https://github.com/zuri-training/proj_fetch_meta_data_Team_84/#dependencies)
  7. Virtual Environment
    
    ****
    Latest version(maintained builds) for all installation requirements as at 4/8/2022
    
    Windows versions are for 64bit
    ****

   ## DEPLOYMENT
  ### Required packages
  - asgiref==3.5.2
  - crispy-bootstrap5==0.6
  - Django==4.1
  - django-crispy-forms==1.14.0
  - django-social-share==2.3.0
  - filetype==1.1.0
  - lxml==4.9.1
  - Pillow==9.2.0
  - PyPDF2==2.10.0
  - python-decouple==3.6
  - python-docx==0.8.11
  - python-dotenv==0.20.0
  - sqlparse==0.4.2
  - tinytag==1.8.1

  ### Running on local machine
  *** current working branch is the master branch***
  - Create a virtual environment
  - Install the required packages (pip install <package>)
  - Make migrations (python manage.py makemigrations)
  - Migrate (python manage.py migrate)
  - Run the server (python manage.py runserver)

  
 ### README CONTRIBUTING AUTHORS
  - [Ekwemuka Isioma](https://github.com/Issiedoesit)
  - [Mbugua Wanjiru](https://github.com/mbuguaellen)
  - [Temitope Osifalujo](https://github.com/topnics)
  - [Adesina Aladesae](https://github.com/adesinna)
  
 ### ACKNOWLEDMENTS
 - We'd like to thank the entire [Zuri Team](https://training.zuri.team/) and [Ingressive for Good community](https://ingressive.org/) for this opportunity to learn and grow as developers and designers.
 - It's an honour to work with such a decicated group of mentors.
 - Special Thanks to our project mentor [Tolu Folorunsho](https://www.linkedin.com/in/tolufolorunso/). Thanks for all you do.

### REFERENCES/FOOTER
  
[^1]:
    - Wanjiru Mbugua https://github.com/mbuguaellen TEAM LEAD and DESIGNER
    - Isioma Ekwemuka https://github.com/Issiedoesit ASSISTANT TEAM LEAD and DEVELOPER
    - Temitope Osifalujo https://github.com/topnics ASSISTANT TEAM LEAD and DEVELOPER
    - Samuel Godson https://GitHub.com/samuelgodson55 DEVELOPER
    - Olubunmi Olawoyin https://github.com/olawoyintosin DESIGNER
    - Wuraola Nureni http://github.com/Wuraola-Omotoyosi DESIGNER
    - Oreoluwa Dahunsi https://github.com/OreoluwaDahunsi DESIGNER
    - Chinonso Onyekonwu https://github.com/Nonso-hub DESIGNER
    - Abdulbasit Ajibola https://github.com/Berseet DESIGNER
    - Stanley Ibe https://github.com/ugoostanleyibe DEVELOPER
    - Olayinka Olajumilo https://github.com/olamijulo2 DEVELOPER
    - Victoria Akeju https://GitHub.com/vic-designs DESIGNER
    - Adelaide Banibensu https://github.com/Ade-Bani/ DESIGNER
    - Shalom Onyeukwu https://Github.com/Shalomking DEVELOPER
    - Adesina Aladesae https://github.com/adesinna DEVELOPER
    - George Ogundokun https://github.com/geonerd777 DESIGNER
    - John Fadumiye http://github.com/Enojay DESIGNER
    - Iyanuoluwa Olawoye https://github.com/SirIyanu DEVELOPER
    - Taribor Ajuesi http://GitHub.com/Tarielenz DEVELOPER
    - Oluwashola Adeola https://github.com/sholigezy DESIGNER
    - Precious Nwogu https://github.com/preshwhyte DEVELOPER
    - Olamilekan Ojebowa https://github.com/Lyon689 DEVELOPER
    - Taiyelolu Abiri https://github.com/taiyeabiri DEVELOPER
    - Isaac David https://github.com/Daeveed1 Designer
