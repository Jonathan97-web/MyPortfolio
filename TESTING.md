# Testing

Return back to the [README.md](README.md) file.

## Code Validation


### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

Because of CRUD I have used direct input from source code on the ones that needed it.


- https://validator.w3.org/nu/?doc=https%3A%2F%2FJonathan97-web.github.io%2FMyPortfolio%2Findex.html


| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmyportfoliopp4.herokuapp.com%2F) | ![screenshot](documentation/images/validation-home.png) | Pass: No Errors / info trailing slashes |
| Sign up | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmyportfoliopp4.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/images/validation-signup.png) | Pass: No Errors  |
| Sign in | [W3C](https://myportfoliopp4.herokuapp.com/accounts/login/) | ![screenshot](documentation/images/validation-signin.png) | Pass: No Errors |
| Sign out | n/a | ![screenshot](documentation/images/validation-signout.png) | Warning because double h1's from base.html |
| Profile Detail | n/a | ![screenshot](documentation/images/validation-profile.png) | Pass: No Errors |
| My Profile | n/a | ![screenshot](documentation/images/validation-myprofile.png) | Pass: No Errors |
| Project Edit |n/a| ![screenshot](documentation/images/validation-project-edit.png) | Warning because double h1's from base.html |
| Project Create |n/a| ![screenshot](documentation/images/validation-project-create.png) | Warning because double h1's from base.html |
| Project Detail |n/a| ![screenshot](documentation/images/validation-project-detail.png) | Warning because double h1's from base.html |
| Edit comment |n/a| ![screenshot](documentation/images/validation-edit-comment.png) | Pass: No Errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

Since I am using bootstrap I only validated the style.css file that is in the static/css folder since otherwise I get a lot of errors.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | n/a | ![screenshot](documentation//images/validation-css.png) | Pass: No Errors |


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| main/views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jonathan97-web/MyPortfolio/main/main/views.py) | ![screenshot](documentation/images/validation-python-main-views.png) | All clear, no errors found |
| main/settings.py | n/a | ![screenshot](documentation/images/validation-python-settings.py.png) | All clear, no errors found |
|  profiles/views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jonathan97-web/MyPortfolio/main/profiles/views.py) | ![screenshot](documentation/images/validation-python-profiles-views.png) | All clear, no errors found |
| profiles/models.py | n/a | ![screenshot](documentation/images/validation-python-profiles.models.png) | All clear, no errors found |
| projects/views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jonathan97-web/MyPortfolio/main/projects/views.py) | ![screenshot](documentation/images/validation-python-projects-views.png) | All clear, no errors found |
| projects/models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jonathan97-web/MyPortfolio/main/projects/models.py) | ![screenshot](documentation/images/validation-python-projects-models.png) | All clear, no errors found |
| main/urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jonathan97-web/MyPortfolio/main/main/urls.py) | ![screenshot](documentation/images/validation-python-main-urls.png) | All clear, no errors found |
| projects/urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jonathan97-web/MyPortfolio/main/projects/urls.py) | ![screenshot](documentation/images/validation-python-projects-urls.png) | All clear, no errors found |
| profiles/urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jonathan97-web/MyPortfolio/main/profiles/urls.py) | ![screenshot](documentation/images/validation-python-profiles-urls.png) | All clear, no errors found |


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/images/compability-chrome.png) | Works as expected |
| Firefox Developer edition | ![screenshot](documentation/images/compability-mozilla-firefox-de.png) | Minor differences |
| Edge | ![screenshot](documentation/images/compability-edge.png) | Works as expected |
| Opera GX | ![screenshot](documentation/images/compability-opera-gx.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/images/responsive-mobile.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/images/responsive-tablet.png) | Works as expected |
| Desktop | ![screenshot](documentation/images/responsive-desktop.png) | Works as expected |
| XL Monitor | ![screenshot](documentation/images/responsive-xl-monitor.png) | Works as expected |
| 4K Monitor | ![screenshot](documentation/images/responsive-4k-monitor.png) | Minor scaling issues |
| iPhone 14 Pro | ![screenshot](documentation/images/responsive-iphone-14.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

Mostly SEO warnings due to not having a meta description since it's in the base template.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Mobile | ![screenshot](documentation/images/lighthouse-mobile-home.png) | Some minor warnings |
| Home | Desktop | ![screenshot](documentation/images/lighthouse-desktop-home.png) | Some minor warnings |
| My Profile | Mobile | ![screenshot](documentation/images/lighthouse-mobile-my-profile.png) | Some minor warnings |
| My Profile | Desktop | ![screenshot](documentation/images/lighthouse-desktop-my-profile.png) | Few warnings |
| Sign in | Mobile | ![screenshot](documentation/images/lighthouse-mobile-login.png) | Slow response time due to large images |
| Sign in | Desktop | ![screenshot](documentation/images/lighthouse-desktop-login.png) | Slow response time due to large images |
| Sign up | Mobile | ![screenshot](documentation/images/lighthouse-mobile-signup.png) | Slow response time due to large images |
| Sign up | Desktop | ![screenshot](documentation/images/lighthouse-desktop-signup.png) | Slow response time due to large images |
| Edit comment | Mobile | ![screenshot](documentation/images/lighthouse-mobile-edit-comment.png) | Slow response time due to large images |
| Edit comment | Desktop | ![screenshot](documentation/images/lighthouse-desktop-edit-comment.png) | Slow response time due to large images |
| Edit project | Mobile | ![screenshot](documentation/images/lighthouse-mobile-edit-project.png) | Slow response time due to large images |
| Edit project | Desktop | ![screenshot](documentation/images/lighthouse-desktop-edit-project.png) | Slow response time due to large images |
| Create project | Mobile | ![screenshot](documentation/images/lighthouse-mobile-create-project.png) | Slow response time due to large images |
| Create project | Desktop | ![screenshot](documentation/images/lighthouse-desktop-create-project.png) | Slow response time due to large images |


## Defensive Programming

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

Flask/Django:
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home Page | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Profile Page | | | | |
| | Click on My Profile link in navbar | Redirection to My Profile page | Pass | |
| | User can click on submit when finished editing profile | User will be redirected to the profile page with a success message | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter intro in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Redirection to home page | Pass | |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first | |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Other Users Profiles | | | | |
| | Click on Profile button | User will be redirected to the other users Profile page | Pass | |
| | User cannot edit another users profile | Invalid link results in error or redirection to own profile | Pass | |


## User Story Testing


Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to register, so that I can use the functions of the website. | ![screenshot](documentation/images/user-story-sign-up1.png)![screenshot](documentation/images/user-story-sign-up2.png) |
| As a new site user, I would like to create a profile, so that I can so that I can interact with other people. | ![screenshot](documentation/images/feature-view-myprofile.png) |
| As a new site user, I would like to create a project post, so that I can so that I can share my portfolio to other people. | ![screenshot](documentation/images/feature-create-project-post.png) |
| As a returning site user, I would like to I would like to view other users posts, so that I can see updates on the website. | ![screenshot](documentation/images/feature-view-project-detail.png) |
| As a returning site user, I would like to I would like to see others profiles, so that I can check on updates they made. | ![screenshot](documentation/images/feature-view-profile.png) |
| As a returning site user, I would like to be able to like posts, so that I can show endorsement to other peoples work. | ![screenshot](documentation/images/feature-liked.png) |
| As a site administrator, I should be able to access the administration panel, so that I can overview the website. | ![screenshot](documentation/images/user-story-admin.png) |
| - As a site administrator, I should be able to delete projects and comments, so that I can moderate the website.  | ![screenshot](documentation/images/user-story-admin-comment-edit.png) ![screenshot](documentation/images/user-story-admin-comment-edit1.png) ![screenshot](documentation/images/user-story-admin-project-edit.png) ![screenshot](documentation/images/user-story-admin-project-edit1.png) |
| - As a site administrator, I should be able to see profiles, so that I can moderate the profiles. | ![screenshot](documentation/images/user-story-admin-profile-edit.png) ![screenshot](documentation/images/user-story-admin-profile-edit1.png) |
|

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## Bugs

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

For JavaScript and Python applications, it's best to screenshot the errors to include them as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**


**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/Jonathan97-web/MyPortfolio/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/Jonathan97-web/MyPortfolio/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/Jonathan97-web/MyPortfolio/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/Jonathan97-web/MyPortfolio/issues/3) | Closed |

**Open Issues**

Any remaining open issues can be tracked [here](https://github.com/Jonathan97-web/MyPortfolio/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/Jonathan97-web/MyPortfolio/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/Jonathan97-web/MyPortfolio/issues/5) | Open |

## Unfixed Bugs

As of writing this there are no more bugs that I am aware off.