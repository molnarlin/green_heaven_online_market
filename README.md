# green_heaven_online_market
This is my fourth milestone project with Code Institute and Runshaw College. I used Django for this project.
# 1. Purpose of the project
The aim of this project is to develop an online garden center for an imaginary company, enabling them to effectively sell gardening products, plants, and seeds. This platform will enhance their marketing reach, providing a convenient 24/7 online presence and allowing customers to browse and shop from the comfort of their homes. The project seeks to streamline the shopping experience by offering easy navigation, personalized account features, and seamless checkout. Additionally, it will empower customers to discover new products, while helping the company attract a broader audience and increase sales.
# 2. User stories
## Epic: As a shopper
- I want to browse a list of available products so I can explore my options.
- I want each product to have a detailed description so I can make informed decisions.
- I want to receive shopping inspirations and recommendations so I can discover new items.
- I want to easily identify deals and discounts so I can save money.
- I want to see the total cost of my purchases at any time so I can manage my budget.
- I want to search for items on the website so I can quickly find what I need.
- I want to select the quantity, color, and size of a product easily so I can customize my order.
- I want to receive an email confirmation after checking out so I can verify my purchase.
## Epic: As a registered user
- I want a navigation bar visible on all pages and screen sizes so I can easily move between sections.
- I want to create an account so I can access exclusive features.
- I want to sign in so I can use functions available to logged-in users.
- I want to sign out so my account remains secure.
- I want clear sign-in, sign-up, and log-out options so I can manage my account.
- I want to update my profile so I can keep my personal information accurate.
- I want to view my shopping history so I can review past purchases.
- I want to recover my password easily so I can regain access if I forget it.
- I want to receive a confirmation email when registering so I can verify my account.
- I want to save my payment information so I can speed up future purchases.
## Epic: As an administrator
- I want to add products to the website so I can sell new inventory.
- I want to edit product details such as image, description, and price so I can keep listings accurate.
- I want to delete products so I can remove items no longer available.
- I want to assist users with profile or order issues so I can provide customer support.
# 3. Features
# 4. Future features
# 5. Typography and color scheme
# 6. Wireframes
- Home page
![Home page wireframe](media/readme/Home%20page.png)
- Product list page
![Product list page wireframe](media/readme/Product%20list.png)
- Product page
![Product page wireframe](media/readme/Product%20page.png)
- Sign up page
![Sign up page wireframe](media/readme/Sign%20up%20page.png)
- Check out page
![Check out page wireframe](media/readme/Check%20out%20page.png)
- List of blog articles page
![List of blog articles page](media/readme/Blog%20articles%20list%20page.png)
- Blog page
![Blog page wireframe](media/readme/Blog%20page.png)
=== 1-6 for planning and then write code ===
# 7. Technology
## 7.1. ERD
I would like to use the django admin pannel for adding and updating product, and I would like to work with a delivery company to arrange deliveries.
![ERD image](media/readme/Database%20ER%20diagram%20(crow's%20foot).png)
# 8. Testing
   ## 8.1 code validation
   ## 8.2 test cases (user story based with screenshots)
   ## 8.3 fixed bugs
   ## 8.4 supported screens and browsers
# 9. Deployment
   ## 9.1 via VS Code
   To deploy this project locally using VS Code:

   - **Clone the repository**  
      Open a terminal and run:  
      ```bash
      git clone https://github.com/your-username/green_heaven_online_market.git
      cd green_heaven_online_market
      ```

   - **Create and activate a virtual environment**  
      ```bash
      python -m venv venv
      # On Windows:
      venv\Scripts\activate
      # On macOS/Linux:
      source venv/bin/activate
      ```

   - **Install dependencies**  
      ```bash
      pip install -r requirements.txt
      ```

   - **Apply migrations**  
      ```bash
      python manage.py migrate
      ```

   - **Create a superuser (optional, for admin access)**  
      ```bash
      python manage.py createsuperuser
      ```

   - **Run the development server**  
      ```bash
      python manage.py runserver
      ```

   - **Open the project**  
      Visit `http://127.0.0.1:8000/` in your browser.

   - **Access the admin panel**  
      Visit `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

   ## 9.2 via Heroku
   To deploy this project to Heroku, follow these steps:

   - **Log in to Heroku**  
      In your terminal, run:  
      ```bash
      heroku login
      ```

   - **Prepare your Django project for Heroku**  
      - Add `gunicorn` and `dj-database-url` to your `requirements.txt`.
      - Create a `Procfile` in your project root with:  
        ```
        web: gunicorn green_heaven_online_market.wsgi
        ```
      - Set `ALLOWED_HOSTS` in `settings.py` to include your Heroku app domain.
      - create .python-version file.

   - **Initialize a git repository (if not already done)**  
      ```bash
      git init
      git add .
      git commit -m "Prepare for Heroku deployment"
      ```

   - **Create a Heroku app**  
     In Heroku create a new app.

   - **Set environment variables**  
      Set any required environment variables in Heroku.

   - **Push your code to Heroku**  
      ```bash
      git push heroku main
      ```

   - **Apply migrations and collect static files**  
      ```bash
      heroku run python manage.py migrate
      heroku run python manage.py collectstatic
      ```

   - **Create a superuser (optional)**  
       ```bash
       heroku run python manage.py createsuperuser
       ```

   - **Change Deployement method**
      In Heroku change the deployment method to GitHub.
      Go to Deploy branch, check build log, if any problem.

   - **Open your deployed app**  
       In Heroku open the new app. (https://green-heaven-online-garden-cen-2439019d4b13.herokuapp.com/)

# 10. Credits
- images from kaggle.com and Microsoft Copilot.
- I used Microsoft Copilot for check and debug code, write articles for the blog, write product descriptions.
- thanks for w3school.com.
- thanks for RHS for the plant description and growing information.
- I used Antonio Melé: Django 5 By Example to create the blog app for this project.