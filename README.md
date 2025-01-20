
# BandKamp Project

The BandKamp Project is a music management platform built with the powerful Django framework and the Django Rest Framework (DRF) library. This project provides a RESTful API that allows users to create, list, update, and delete music albums and their respective songs. Additionally, users can register, log in, and manage their user profiles.

## Description

The BandKamp Project was developed to meet the needs of music enthusiasts, artists, and music lovers who want to manage their album and song collections effectively and organized. With the API provided by the BandKamp Project, users can perform the following actions:

- **Registration and Authentication**: Users can register by creating a user profile with information such as username, email, and password. They can also log in with their credentials.

- **Album Management**: Users can create, update, list, and delete music albums. Each album has a name and a release year associated.

- **Song Management**: For each album, users can add songs, specifying a title and the song's duration.

- **User Profile**: Users can view and update their user profile, including information like username and email.

- **API Documentation**: The API is well-documented and can be accessed via Swagger, providing detailed information about all available routes, request parameters, and examples of requests and responses.

## Technologies Used

The BandKamp Project uses the following technologies:

- Python 3.11.5
- Django 4.2.6
- Django REST framework 3.14.0
- Gunicorn 21.2.0
- Whitenoise 6.6.0
- IPython 8.16.1
- ipdb 0.13.13
- python-dotenv 1.0.0
- drf-spectacular 0.26.5
- djangorestframework-simplejwt 5.3.0


## Index

1. [Route: Authentication](#route-authentication)
   - [User Login](#1-user-login)
2. [Route: Users](#route-users)
   - [Create User](#2-create-user)
   - [List Users](#3-list-users)
   - [User Details](#4-user-details)
   - [Update User](#5-update-user)
   - [Delete User](#6-delete-user)
3. [Route: Albums](#route-albums)
   - [Create Album](#7-create-album)
   - [List Albums](#8-list-albums)
4. [Route: Songs](#route-songs)
   - [Create Song](#9-create-song)
   - [List Songs of an Album](#10-list-songs-of-an-album)

### Route: Authentication

#### 1. User Login

- **URL:** /api/users/login/
- **Method:** POST
- **Request Body:**

```json
  {
      "username": "username",
      "password": "password"
  }
```

- **Description:** Authenticates a user and provides a JWT token for use in other parts of the application.

### Route: Users

#### 2. Create User

- **URL:** /api/users/
- **Method:** POST
- **Request Body:**

```json
  {
      "username": "username",
      "password": "password",
      "email": "email@example.com",
      "full_name": "Full Name (optional)",
      "artistic_name": "Artistic Name"
  }
```

- **Description:** Creates a new user with information such as username, password, email, and artistic name.

#### 3. List Users

- **URL:** /api/users/
- **Method:** GET
- **Description:** Returns a list of all registered users.

#### 4. User Details

- **URL:** /api/users/<int:pk>/
- **Method:** GET
- **Description:** Returns details of a specific user based on the provided ID.

#### 5. Update User

- **URL:** /api/users/<int:pk>/
- **Method:** PUT
- **Request Body:**

```json
  {
      "username": "new_username",
      "password": "new_password",
      "email": "new_email@example.com",
      "full_name": "New Full Name (optional)",
      "artistic_name": "New Artistic Name"
  }
```

- **Description:** Updates information for a specific user based on the provided ID.

#### 6. Delete User

- **URL:** /api/users/<int:pk>/
- **Method:** DELETE
- **Description:** Removes a specific user based on the provided ID.

### Route: Albums

#### 7. Create Album

- **URL:** /api/albums/
- **Method:** POST
- **Request Body:**

```json
  {
      "name": "Album Name",
      "year": 2023
  }
```

- **Description:** Creates a new album with information such as name and year.

#### 8. List Albums

- **URL:** /api/albums/
- **Method:** GET
- **Description:** Returns a list of all registered albums.

### Route: Songs

#### 9. Create Song

- **URL:** /api/albums/<int:pk>/songs/
- **Method:** POST
- **Request Body:**

```json
  {
      "title": "Song Title",
      "duration": "3:45"
  }
```

- **Description:** Creates a new song in a specific album with information such as title and duration.

#### 10. List Songs of an Album

- **URL:** /api/albums/<int:pk>/songs/
- **Method:** GET
- **Description:** Returns a list of all songs in a specific album based on the provided album ID.
