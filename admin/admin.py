from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from .models import User, Books

class CustomAdminSite(admin.AdminSite):
    def index(self, request, extra_context=None):
        total_users = User.objects.count()
        total_orders = Books.objects.count()

        html_content = f"""
        <html>
        <head>
            <title>Admin Dashboard</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    display: flex;
                }}
                .dashboard {{
                    padding: 20px;
                    width: 100%;
                }}
                .card {{
                    display: inline-block;
                    width: 200px;
                    margin: 10px;
                    padding: 20px;
                    background-color: #f4f6f9;
                    border-radius: 5px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }}
                .card h3 {{
                    font-size: 18px;
                    color: #333;
                }}
                .card p {{
                    font-size: 24px;
                    font-weight: bold;
                }}
                .logout-btn {{
                    padding: 8px 16px;
                    background-color: #e74c3c;
                    color: white;
                    border: none;
                    cursor: pointer;
                    margin-top: 20px;
                    display: inline-block;
                }}
                .logout-btn:hover {{
                    background-color: #c0392b;
                }}
            </style>
        </head>
        <body>
            <div class="dashboard">
                <h1>Welcome to the Admin Dashboard</h1>
                <div class="card">
                    <h3>Total Users</h3>
                    <p>{total_users}</p>
                </div>
                <div class="card">
                    <h3>Total Orders</h3>
                    <p>{total_orders}</p>
                </div>

                <form action="/admin/logout/" method="POST">
                    {% csrf_token %}
                    <button type="submit" class="logout-btn">Logout</button>
                </form>
            </div>
        </body>
        </html>
        """

        return HttpResponse(html_content)

admin_site = CustomAdminSite(name='custom_admin')
admin.site = admin_site

admin_site.register(User)
admin_site.register(Books)