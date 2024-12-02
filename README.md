<br>

<p align="center">
    <img src="https://i.imgur.com/owsuq6w.png"></img>
</p>

<br>

<p align="justify">
<strong>PagePulse</strong> is a user-friendly online eBook platform that enables users to manage their libraries, create and share books, and engage with a vibrant community of readers and writers. The platform offers essential features such as book creation, commenting, bookmarking, and following other users.
</p>

<br>

## Table of Contents

- [Key Features](#key-features)
- [Installation](#installation)
- [Developers](#developers)
- [Project Documents](#project-documents)

<br>

## Key Features

1. **User Authentication**  
   - Secure Registration
   - Login System
   - Password Recovery for Account Security.

2. **Library Management**  
   - Add books from personal library
   - Remove books form personal library

3. **Book Creation**  
   - Create and Publish your own books.

4. **Commenting**  
   - Leave comments on specific sections of a book

5. **Bookmarking**  
   - Save your reading progress by bookmarking chapters or entire books.

6. **Follow/Unfollow**  
   - Follow other users to stay updated on their new books and activities.
   - Unfollow users at any time.

<br>

## Installation

#### Clone the Repository

- Clone the repository to your local machine using Git:

```bash
git clone https://github.com/PagePulse.git
cd PagePulse
```

#### Installing the Dependencies and Setting up the Database

- Use pip to install the required dependencies listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```

- Before running the application, set up the database by running the following migrations:

```bash
python manage.py makemigrations

python manage.py migrate
```

#### Accessing the Admin Panel

- To access the admin panel, you need to create a superuser. Run the following command and follow the prompts to create an admin user:
```bash
python manage.py createsuperuser
```

#### Running the Application

- To start the application, run the development server:
```bash
python manage.py runserver
```

<br>

## Developers

  <a href="#developers">
    <a href="https://github.com/cabadany"><img width="64" title="Cabana, Danisse" src="https://avatars.githubusercontent.com/u/170840848" alt="cabadany" /></a>
    <a href="https://github.com/gianneA"><img width="64" title="Garcia, Gianne Andrea" src="https://avatars.githubusercontent.com/u/182353906" alt="gianneA" /></a>
    <a href="https://github.com/ezzeljan"><img width="64" title="Francisco, Ezzel Jan" src="https://avatars.githubusercontent.com/u/168334933" alt="ezzeljan" /></a>
  </a>


<br>

## Project Documents

- [Functional Requirements](https://docs.google.com/document/d/1kCOF8eaMmoPbc_Flg5Wyz1586ZgGdN8v/edit?usp=drive_link&ouid=106838395546630797936&rtpof=true&sd=true)
- [Gantt Chart](https://cebuinstituteoftechnology-my.sharepoint.com/:x:/r/personal/danisse_cabana_cit_edu/_layouts/15/Doc.aspx?sourcedoc=%7B24263AC0-B7D5-42D5-BA7F-000ED30C46B8%7D&file=Gantt%20Chart.xlsx&fromShare=true&action=default&mobileredirect=true)
- [Entity-Relationship Diagram (ERD)](https://lucid.app/lucidchart/9a68a5e4-805f-4e29-aa13-aa46d94d94ab/edit?viewport_loc=-383%2C-595%2C2994%2C1477%2C0_0&invitationId=inv_e5f0e3f7-03e3-4882-8cbc-7e4e31f5d868)
- [UI/UX Design](https://www.figma.com/design/YhCYsIirxaR18FPDfc6e0b/eBook-System-UI%2FUX?node-id=0-1&t=dYsUffctSePePzPq-1)
