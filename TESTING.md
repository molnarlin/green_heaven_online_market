# Testing
## Table of Contents

1. [Code Validation](#1-code-validation)
    - [HTML Validation](#11-html-validation)
    - [CSS Validation](#12-css-validation)
    - [JavaScript Validation](#13-javascript-validation)
    - [Python Validation](#14-python-validation)
    - [Lighthouse Reports](#15-lighthouse-reports)
2. [Manual Testing](#2-manual-testing)
    - [Test Cases (User Story Based)](#21-test-cases-user-story-based)
        - [User Account Features](#user-account-features)
        - [Content and Community Features](#content-and-community-features)
        - [E-Commerce Features](#e-commerce-features)
    - [Supported Screens and Browsers](#22-supported-screens-and-browsers)
3. [Stripe Webhook Testing](#3-stripe-webhook-testing)

This document describes the testing approach for the Green Heaven Online Market project. It covers validation tools, manual test cases, device/browser compatibility, and Stripe webhook verification.

## 1. Code Validation

### 1.1 HTML Validation

- Used [W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgreen-heaven-online-garden-cen-2439019d4b13.herokuapp.com%2F).
- No issues found.
- ![HTML validation screenshot](media/testing/html-val.PNG)

### 1.2 CSS Validation

- Used [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fgreen-heaven-online-garden-cen-2439019d4b13.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en).
- No issues found.
- ![CSS validation screenshot](media/testing/css-val.PNG)

### 1.3 JavaScript Validation

All JavaScript scripts were validated using JSHint. Each script passed without issues.

| Script                | Tool    | Result         | Screenshot                                      |
|-----------------------|---------|----------------|-------------------------------------------------|
| base.html             | JSHint  | No issues      | ![base.html](media/testing/base-html.png)        |
| bag.html              | JSHint  | No issues      | ![bag.html](media/testing/bag-js.png)            |
| add_article.html      | JSHint  | No issues      | ![add_article.html](/media/testing/add-article-js.PNG) |
| edit_article.html     | JSHint  | No issues      | ![edit_article.html](media/testing/edit-article-js.PNG) |
| stripe_elements.js    | JSHint  | No issues      | ![stripe_elements.js](media/testing/stripe-elements-js.PNG) |
| subscription_success.html | JSHint | No issues   | ![subscription_success.html](media/testing/subscription-success-html.PNG) |
| quantity_input_script.html | JSHint | No issues | ![quantity_input_script.html](media/testing/quantity-input-script.PNG) |
| add_product.html      | JSHint  | No issues      | ![add_product.html](media/testing/add-product.PNG) |
| products.html         | JSHint  | No issues      | ![products.html](media/testing/products.PNG)      |
| countryfield.js       | JSHint  | No issues      | ![countryfield.js](media/testing/countryfield.PNG) |
| accounts.js           | JSHint  | No issues      | ![accounts.js](media/testing/accounts-js.PNG)     |
| edit_product.html     | JSHint  | No issues      | ![edit_product.html](media/testing/edit-product.PNG) |
| onload.js             | JSHint  | No issues      | ![onload.js](media/testing/onload-js.PNG)         |

### 1.4 Python Validation

- Used Flake8 for linting.
- Installed via `pip install flake8`.
- Excluded `.venv`, migrations, and empty files.
- Some files have long lines or tabs, but these do not affect execution.
- ![Flake8 installation](/media/testing/flake8%20installation.PNG)
- ![Flake8 output](/media/testing/flake8-output.PNG)

### 1.5 Lighthouse Reports

Lighthouse audits were run in Chrome Incognito mode to avoid extension interference. Results for key pages:

- **Home page:** ![Home](media/testing/lighthouse.PNG)
- **Product list:** ![Product list](/media/testing/lighthouse-product-list.PNG)
- **Product page:** ![Product page](media/testing/lighthouse_product.PNG)
- **Checkout:** ![Checkout](media/testing/lighthouse-checkout.PNG)
- **Blog list:** ![Blog list](media/testing/lighthouse_blog_list.PNG)
- **Blog article:** ![Blog article](media/testing/lighthouse_blog_article.PNG)
- **User profile:** ![Profile](media/testing/lighthouse_profile.PNG)
- **Shopping bag:** ![Shopping bag](media/testing/lighthouse_shopping_bag.PNG)
- **Sign up/in:** ![Sign in](media/testing/lighthouse_sign_in.PNG)
- **Order confirmation:** ![Order confirmation](media/testing/lighthouse-order-conf.PNG)
- **Admin product management:** ![Product management](media/testing/lighthouse_product_man.PNG)
- **Admin blog management:** ![Blog management](media/testing/lighthouse_blog_man.PNG)

## 2. Manual Testing

### 2.1 Test Cases (User Story Based)

#### User Account Features

| Feature           | Requirement                                   | Expected Result                                 | Actual Result | Screenshot                                 | Pass/Fail | Date    | Correction |
|-------------------|-----------------------------------------------|-------------------------------------------------|--------------|--------------------------------------------|-----------|---------|------------|
| Sign Up           | Register new users                            | Registration successful, redirected             | As expected  | ![Sign Up](media/readme/Signup.png)        | Pass      | 4/8/25  | None       |
| Sign In           | Authenticate users                            | Login and redirect                              | As expected  | ![Sign In](media/readme/signin.PNG)        | Pass      | 4/8/25  | None       |
| Sign Out          | Log out users                                 | Session ends, redirect to landing page          | As expected  | ![Sign Out](media/readme/Signout.PNG)      | Pass      | 4/8/25  | None       |
| Profile display   | View profile dashboard                        | Details and activity visible                    | As expected  | ![Profile](media/readme/Myprofile.PNG)     | Pass      | 4/8/25  | None       |
| Profile management| Edit details, view orders                     | Changes saved, order history accurate           | As expected  | ![Profile](media/readme/Myprofile.PNG)     | Pass      | 4/8/25  | None       |

#### Content and Community Features

| Feature           | Requirement                                   | Expected Result                                 | Actual Result | Screenshot                                 | Pass/Fail | Date    | Correction |
|-------------------|-----------------------------------------------|-------------------------------------------------|--------------|--------------------------------------------|-----------|---------|------------|
| Blog display      | View blog posts                               | Blog loads with title, content, metadata        | As expected  | ![Blog](media/readme/blog_display.PNG)     | Pass      | 4/8/25  | None       |
| Blog management   | Admin manage posts                            | Changes reflected in real time                  | As expected  | ![Blog mgmt](media/readme/blog-man.PNG)    | Pass      | 4/8/25  | None       |
| Comments display  | View comments                                 | Chronological, usernames shown                  | As expected  | ![Comments](media/readme/comments-display.PNG) | Pass  | 4/8/25  | None       |
| Comments management| Add/edit/delete comments                     | Correct permissions, actions work               | As expected  | ![Comment mgmt](media/readme/comment-man.PNG) | Pass  | 4/8/25  | None       |

#### E-Commerce Features

| Feature           | Requirement                                   | Expected Result                                 | Actual Result | Screenshot                                 | Pass/Fail | Date    | Correction |
|-------------------|-----------------------------------------------|-------------------------------------------------|--------------|--------------------------------------------|-----------|---------|------------|
| Product display   | Show products with details                    | Listings load with images, prices, ratings      | As expected  | ![Product](/media/readme/product-display.PNG) | Pass   | 4/8/25  | None       |
| Product management| Admin add/edit/remove products                | Catalog updates instantly                       | As expected  | ![Add](media/readme/add-product.PNG), ![Edit](media/readme/edit-product.PNG) | Pass | 4/8/25 | None |
| Bag display       | View shopping bag                             | Items and totals visible                        | As expected  | ![Bag](media/readme/shopping-bag.PNG)      | Pass      | 4/8/25  | None       |
| Bag management    | Add/update items in bag                       | Bag updates, correct price/stock                | As expected  | ![Bag mgmt](media/readme/shopping-bag.PNG) | Pass      | 4/8/25  | None       |
| Checkout          | Secure checkout for users                     | Payment and confirmation with email             | As expected  | ![Checkout](/media/readme/checkout.PNG)    | Pass      | 4/8/25  | None       |

### 2.2 Supported Screens and Browsers

| Device/Screen      | Page                | Browser(s)      | Result                                      | Screenshot                                   | Pass/Fail | Date    |
|--------------------|---------------------|-----------------|----------------------------------------------|-----------------------------------------------|-----------|---------|
| iPhone SE          | Homepage            | Chrome          | Menu collapses, navigation works             | ![iPhone SE Home](media/readme/mobile-hp-navbar.png) | Pass      | 4/8/25  |
| iPhone SE          | Product Display     | Chrome          | Info visible, images scale                   | ![iPhone SE Product](media/readme/mobile-pp.png) | Pass      | 4/8/25  |
| iPhone SE          | Checkout            | Chrome          | Fields accessible, payment works             | ![iPhone SE Checkout](media/readme/phone-checkout.png) | Pass      | 4/8/25  |
| iPhone SE          | Blog Page           | Chrome          | Blog readable, comments visible              | ![iPhone SE Blog](media/readme/mobile-blog.png) | Pass      | 4/8/25  |
| Nest Hub           | Homepage            | Chrome, Edge    | Nav bar visible, links work                  | ![Nest Hub Home](media/readme/tablet-hp-navbar.png) | Pass      | 4/8/25  |
| Nest Hub           | Product Display     | Chrome, Edge    | Grid adapts, images clear                    | ![Nest Hub Product](media/readme/tablet-pp.png) | Pass      | 4/8/25  |
| Nest Hub           | Checkout            | Chrome, Edge    | Fields accessible, summary visible           | ![Nest Hub Checkout](media/readme/tablet-checkout.png) | Pass      | 4/8/25  |
| Nest Hub           | Blog Page           | Chrome, Edge    | Blog/comments readable                       | ![Nest Hub Blog](media/readme/tablet-blog.png) | Pass      | 4/8/25  |
| Desktop            | Homepage            | Chrome, Edge    | Full menu, navigation works                  | ![Desktop Home](media/readme/desktop-hp-navbar.png) | Pass      | 4/8/25  |
| Desktop            | Product Display     | Chrome, Edge    | Grid, images sharp                           | ![Desktop Product](media/readme/desktop-pp.png) | Pass      | 4/8/25  |
| Desktop            | Checkout            | Chrome, Edge    | Fields, payment, summary visible             | ![Desktop Checkout](media/readme/desktop-checkout.png) | Pass      | 4/8/25  |
| Desktop            | Blog Page           | Chrome, Edge    | Blog/comments visible, formatted             | ![Desktop Blog](media/readme/desktop-blog.png) | Pass      | 4/8/25  |

## 3. Stripe Webhook Testing

### 3.1 In VS Code

- I opened 3 terminals.\
One for running the server:\
`python manage.py runserver`,\
Second one to listen to Stripe:\
`stripe listen --forward-to localhost:8000/checkout/wh/`,\
Stripe trigger in the third terminal.
- I verified events with success messages in terminal.\
![VS Code webhook terminal](media/testing/webhook-check1.PNG)

### 3.2 In Stripe Dashboard

- I logged in to [Stripe](https://stripe.com/gb).
- Searched for Events.
- Here I could check the status and error messages of the different events.
- I could confirm successful payment processing for orders:\
![Stripe dashboard webhook check](media/testing/webhook-check2.PNG)