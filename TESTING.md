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
| Sign in | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmyportfoliopp4.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/images/validation-signin.png) | Pass: No Errors |
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
| main/settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jonathan97-web/MyPortfolio/main/main/settings.py) | ![screenshot](documentation/images/validation-python-settings.py.png) | All clear, no errors found |
|  profiles/views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jonathan97-web/MyPortfolio/main/profiles/views.py) | ![screenshot](documentation/images/validation-python-profiles-views.png) | All clear, no errors found |
| profiles/models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Jonathan97-web/MyPortfolio/main/profiles/models.py) | ![screenshot](documentation/images/validation-python-profiles.models.png) | All clear, no errors found |
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
| Sign in | Mobile | ![screenshot](documentation/images/lighthouse-mobile-login.png) | Some minor warnings |
| Sign in | Desktop | ![screenshot](documentation/images/lighthouse-desktop-login.png) | Some minor warnings |
| Sign up | Mobile | ![screenshot](documentation/images/lighthouse-mobile-signup.png) | Some minor warnings |
| Sign up | Desktop | ![screenshot](documentation/images/lighthouse-desktop-signup.png) | Some minor warnings |
| Edit comment | Mobile | ![screenshot](documentation/images/lighthouse-mobile-edit-comment.png) | Some minor warnings |
| Edit comment | Desktop | ![screenshot](documentation/images/lighthouse-desktop-edit-comment.png) | Some minor warnings |
| Edit project | Mobile | ![screenshot](documentation/images/lighthouse-mobile-edit-project.png) | Some minor warnings |
| Edit project | Desktop | ![screenshot](documentation/images/lighthouse-desktop-edit-project.png) | Some minor warnings |
| Create project | Mobile | ![screenshot](documentation/images/lighthouse-mobile-create-project.png) | Some minor warnings |
| Create project | Desktop | ![screenshot](documentation/images/lighthouse-desktop-create-project.png) | Some minor warnings |


## Defensive Programming

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

## Bugs

- Python `E501 line too long` (93 > 79 characters)

    - On several locations I have had this bug,

```python
path(
    'project_delete/<int:id>',
    views.delete_project, name='project_delete'),
```

- To fix this, I pressed enter to cut the line into 3 pieces if necessary, if you have brackets you can do this at the start of the opening brackets to format the code like the above example.

- Django `NoReverseMatch at /`

![screenshot](documentation/images/bugs-1.png)

- The problem is if you are looking for example for the url/id/slug but don't declare that in the views or accidently forget to write it in the html template it will give you this error. It's trying to match the specific id/slug to the post but it cannot and give you this error.
- To fix this I made sure to go over my code again and include the id/slug both in my HTML and views.

## Unfixed Bugs

As of writing this, there are no more bugs that I am aware of.

## GitHub Issues

### **Open Issues**

Any remaining open issues can be tracked [here](https://github.com/Jonathan97-web/MyPortfolio/issues).

| User Story | Status |
| --- | --- |
| [#18 Share profiles](https://github.com/Jonathan97-web/MyPortfolio/issues/18) | Open |
| [#14 Share post](https://github.com/Jonathan97-web/MyPortfolio/issues/14) | Open |
| [#3 Approve comments](https://github.com/Jonathan97-web/MyPortfolio/issues/3) | Open |

![screenshot](documentation/images/project-open-issues.png)

### **Closed Issues**

All finalised issues are closed and can be tracked [here](https://github.com/Jonathan97-web/MyPortfolio/issues?q=is%3Aissue+is%3Aclosed)

![screenshot](documentation/images/project-closed-issues.png)