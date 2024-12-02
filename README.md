<p align="center">
  📚 <strong>PagePulse</strong> 📚
</p>

**PagePulse** is a user-friendly online eBook platform that enables users to manage their libraries, create and share books, and engage with a vibrant community of readers and writers. The platform offers essential features such as book creation, commenting, bookmarking, and following other users.

---

## Project Documentation

- [Functional Requirements](https://docs.google.com/document/d/1kCOF8eaMmoPbc_Flg5Wyz1586ZgGdN8v/edit?usp=drive_link&ouid=106838395546630797936&rtpof=true&sd=true)
- [Gantt Chart](https://cebuinstituteoftechnology-my.sharepoint.com/:x:/r/personal/danisse_cabana_cit_edu/_layouts/15/Doc.aspx?sourcedoc=%7B24263AC0-B7D5-42D5-BA7F-000ED30C46B8%7D&file=Gantt%20Chart.xlsx&fromShare=true&action=default&mobileredirect=true)
- [Entity-Relationship Diagram (ERD)](https://lucid.app/lucidchart/9a68a5e4-805f-4e29-aa13-aa46d94d94ab/edit?viewport_loc=-383%2C-595%2C2994%2C1477%2C0_0&invitationId=inv_e5f0e3f7-03e3-4882-8cbc-7e4e31f5d868)
- [UI/UX Design](https://www.figma.com/design/YhCYsIirxaR18FPDfc6e0b/eBook-System-UI%2FUX?node-id=0-1&t=dYsUffctSePePzPq-1)

---

## Key Features

- **User Authentication**  
  Secure registration, login system, and password recovery for account security.

- **Library Management**  
  Easily add and remove books from your personal library.

- **Book Creation**  
  Create and publish your own books for others to read and enjoy.

- **Commenting**  
  Leave comments on specific sections of a book to engage in discussions with other readers.

- **Bookmarking**  
  Save your reading progress by bookmarking chapters or entire books.

- **Follow/Unfollow**  
  Follow other users to stay updated on their new books and activities. Unfollow users at any time.

---

## Project Members

- **Cabana, Danisse D.** – Team Leader, Designer, Developer
- **Garcia, Gianne Andrea** – Designer, Developer
- **Francisco, Ezzel Jan** – Designer, Developer

---

## Installation Guide

### 1. Clone the Repository

Clone the repository to your local machine using Git:

```bash
git clone https://github.com/PagePulse.git
cd PagePulse
```

Use pip to install the required dependencies listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```

Before running the application, set up the database by running the following migrations:

```bash
# Make migrations for the application
python manage.py makemigrations

# Apply the migrations to set up the database
python manage.py migrate
```

To access the admin panel, you need to create a superuser. Run the following command and follow the prompts to create an admin user:
```bash
python manage.py createsuperuser
```

To start the application, run the development server:
```bash
python manage.py runserver
```
