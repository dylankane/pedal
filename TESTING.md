# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpedal-forum-80408630e3b0.herokuapp.com%2F) | ![screenshot](documentation/tests/html-validation-home.png) | No errors or warnings to show |
| About | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpedal-forum-80408630e3b0.herokuapp.com%2Fabout%2F) | ![screenshot](documentation/tests/html-validation-about.png) | No errors or warnings to show |
| Sign-Up | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpedal-forum-80408630e3b0.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/tests/html-validation-sign-up.png) | No errors or warnings to show |
| Log-in | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpedal-forum-80408630e3b0.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/tests/html-validation-log-in.png) | No errrors or warnings to show |
| Categories | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpedal-forum-80408630e3b0.herokuapp.com%2Fcategories%2FRoad%2F) | ![screenshot](documentation/tests/html-validation-categories.png) | No errors or warnings to show |
| Profile | n/a | ![screenshot](documentation/tests/html-validation-profile.png) | No errors or warnings to show |
| Liked | n/a | ![screenshot](documentation/tests/html-validation-liked.png) | No errors or warnings to show |
| Create Post | n/a | ![screenshot](documentation/tests/html-validation-create-post.png) | No errors or warnings to show |
| Edit Post | n/a | ![screenshot](documentation/tests/html-validation-edit-post.png) | No errors or warnings to show |
| Delete Post | n/a | ![screenshot](documentation/tests/html-validation-delete-post.png) | No errors or warnings to show |
| Edit Comment | n/a | ![screenshot](documentation/tests/html-validation-edit-comment.png) | No errors or warnings to show |
| Delete Comment | n/a | ![screenshot](documentation/tests/html-validation-delete-comment.png) | No errors or warnings to show |
| Contact Message | n/a | ![screenshot](documentation/tests/html-validation-message.png) | No errors or warnings to show |
| Delete User | n/a | ![screenshot](documentation/tests/html-validation-delete-user.png) | No errors or warnings to show |
| Log Out | n/a | ![screenshot](documentation/tests/html-validation-log-out.png) | No errors or warnings to show |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | n/a | ![screenshot](documentation/tests/css-validation.png) | Pass: No Errors |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JavaScript.
As I only have a small bit of custom JS I dont have a file .js but rather have it at the bottom of the base.html.

| File | Screenshot | Notes |
| --- | --- | --- |
| base.html | ![screenshot](documentation/tests/jshint-validation.png) | One undefined variable
4	bootstrap |


### Python


I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/dylankane/pedal/main/pedal/settings.py) | ![screenshot](documentation/tests/py-validation-settings.png) | Pass: No Errors |
| views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/dylankane/pedal/main/forum/views.py) | ![screenshot](documentation/tests/py-validation-views.png) | Pass: No Errors |
| urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/dylankane/pedal/main/pedal/urls.py) | ![screenshot](documentation/tests/py-validation-urls.png) | Pass: No Errors |
| wsgi.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/dylankane/pedal/main/pedal/wsgi.py) | ![screenshot](documentation/tests/py-validation-wsgi.png) | Pass: No Errors |
| asgi.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/dylankane/pedal/main/pedal/asgi.py) | ![screenshot](documentation/tests/py-validation-asgi.png) | Pass: No Errors |
| admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/dylankane/pedal/main/forum/admin.py) | ![screenshot](documentation/tests//py-validation-admin.png) | Pass: No Errors |
| apps.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/dylankane/pedal/main/forum/apps.py) | ![screenshot](documentation/tests/py-validation-app.png) | Pass: No Errors |
| forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/dylankane/pedal/main/forum/forms.py) | ![screenshot](documentation/tests/py-validation-forms.png) | Pass: No Errors |
| models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/dylankane/pedal/main/forum/models.py) | ![screenshot](documentation/tests/py-validation-models.png) | Pass: No Errors |
| urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/dylankane/pedal/main/forum/urls.py) | ![screenshot](documentation/tests/py-validation-url.png) | Pass: No Errors |
| manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/dylankane/pedal/main/manage.py) | ![screenshot](documentation/tests/py-validation-manage.png) | Pass: No Errors |


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/chrome-browser.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/firefox-browser.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/microsoft-browser.png) | Works as expected |


## Responsiveness


I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Google Pixel 6 a | ![screenshot](documentation/responsiveness/mobile-responsive.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/tablet-responsive.png) | Works as expected |
| Pixel Chromebook | ![screenshot](documentation/responsiveness/laptop-responsive.png) | Works as expected |
| XL Monitor | ![screenshot](documentation/responsiveness/monitor-responsive.png) | Works as expected |


## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Screenshot | Notes |
| --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home.png) | Acceptable results |
| About | ![screenshot](documentation/lighthouse/lighthouse-about.png) | Acceptable results |
| Profile | ![screenshot](documentation/lighthouse/lighthouse-proflie.png) | Acceptable results |
| Liked | ![screenshot](documentation/lighthouse/lighthouse-liked.png) | Acceptable results |
| Categories | ![screenshot](documentation/lighthouse/lighthouse-categories.png) | Acceptable results |
| Post Detail | ![screenshot](documentation/lighthouse/lighthouse-post-detail.png) | Acceptable results |

- Some warnings that came back on some of the lighthouse audits are image sizes slowing down performances and some accesibility issues with links and buttons, while the results are acceptable these are issues that have to be looked at in teh next stage of development.

## Defensive Programming

I have undergone extensive manual deffensive and general testing of all ares of the application.
- Clicking on all the links in the nav bar and collapsable area of the nav barare redirecting to the right pages and forms.
- The categorey tags are redirecting the user to the correct matching list of posts, when clicked from any of the post cards in any page (main list, liked list, profile and the categorey list itself), they are also working correctly from the post detaiil view.
- The "Show Us Your Bike" link to create a post is redireting to the creae a post form from. Working correctly from all its locations, home page and profile page.
- The liked list of posts is beig correctly populated by current users favourite posts, and is loading on the click of the favourites button in the profile page.
- The comment section is working as it was designed. If the user is not logged in the comment form is not visible, with a log-in or sign-up link present instead, both passing manual tests and redirecting to correct forms. When the user is looged in the form is present and working. The text area is accepting text input and the submit button is sending data to the database, reloading page with new comment present, with user name and date. If the textarea is left blank it will not submit and a warning is given. If there is a comment present in the comment section under the current post, made by the current user those comments display an edit and delete link, both redirecting to the correct forms when clicked. Both of these forms also correctly editing and deleting the comments
- In the profile page the three links at the top of the page redirect correctly. The posts present there ar only ones created by the current user. They are also correctly displaying an edit and delete button which do redirect the user to the appropriate forms. The logout and delete user links in the drop down button both redirect to the right forms.
- In the footer all links redirect correctly. The social media links all open in a new tab. The email icon within the social links redirects in a new tab to the users email service with the email address of the site prepopulated.
- All log-in, log-out and sign up forms are working correctly. The sign-up form has email set to optional clearly shown, so can be left empty, but if text has been entered it must conform to an email structure with an @ symbol. All other fields must be populated. If the two password fields dont match, it wont submit. the log-in form all works the same but with out the email input, as its not mandatory so not needed to log in.
- The create a post is working correctly and redirecting to the newly created post on completion, as is the update post form which when redirected to is identical to the create a post form but with prepopulated fields.
- The about page is being directed to from the correct links. When the contact and t&cs links are clicked user is redirected to the about page but to the specific section either contact or t&cs. All links within these section on the about page working correctly.
- In the contact section of the about page if the user is logged in, the send messgae button redirects to a contact form, if user is not logged in then it redirects to the login form. The message form asks for a name email and message the are all accepting text and when submitted the messages database is updated and shown in the admin panel. All these fields are mandatory and form caannot be submitted otherwise
- The delete user form is correctly deleteing the user from the database and all their content, and redirecting to the home page.
- On the successful completion of any form on the site, log in/out, sign up, create update or delete comments or posts, delete user and sending messages a success pop up message apperars at the head of whatever page the user has been redirected, and disappears. A specific message is printed into the pop up depending on the action just completed.
- All areas restricted to logged in users have been tested for brute-force navigation with urls and were unsuccesful acessing with beig logged in.



## Bugs


- TemplateDoesNotExist at/
    ![screenshot](documentation/template-error.png)
    - This bug was a recurring bug/error during the development stages. Where the url paths were wrongly configured, eack url took a bit of trial and error. In particular the post detail url, ended up taking a slug and a pk as its parameters. Each view needed slightly different approaches to get the path waorking. I found help with this from multiple stack overflow conversations.

- Page not found/
    ![screenshot](documentation/page-not-found.png)
    - This bug turned out to be very similar to the prrevious one, however the solution was not exactly a bad url just two very similar pathways using the slug as the parameters, so django was using the first url it cam to that matched, even though the correct one was after it.

- Integritty Error at/
    ![screenshot](documentation/integritty-error.png)
    - In views.py in the post function for comments, I had the wrong request for the author.
    - comment_form.instance.author = request.user  < = correct
    - comment_form.instance.author = request.user.usernane < = inncorrect

- On the deployed heroku site while testing I noticed that if I created a post with out entering a value for the categories i was getting a server error 500
    ![screenshot](documentation/server-error.png)
    - By turning back ob debug on the live site I could see it was a error with the pathway to the catergorey list view, which was looking for a parameter "cat" but because I had updated the model specifically the text choices values for none to N/A to be more frontend friendly than "unknown" however it turns out that the use of the / seems to have affrected the url breaking it, So I had to change the value to "other".

- With a few of my views I had to get a queryset of objects for a list, the main home page list the likes list or the categories list, coming accross many different bugs and issue. 
    - There was no one solution, but with a bit more reading of the django docs and the site ccbv.co.uk explaining the way to update class based view with a function I got there.


- This Error was in the small amount of custom Javascript I have in the project. When the page loadedlocally or deployed I was getting a error in the console
    ![screenshot](documentation/js-error.png)
    - This was due to the browser trying to access an object that was null, again with a lot of trial and error and stackoverflow by adding an if statement to the alert object this would check if its not null,making sure the alert.close(); runs when needed.
    

## Unfixed Bugs


- In the light house audits there are some notes on performance specifically on mobile due to image size
    - To fix this I can specify height and width but at the moment I have cloudinary looking afer keeping the images responsive to screen sizes and I think doing a great job of it. At this mvp stage I feel like the performance levels are still good, but it definitely needs to be addressed in the next stage, I also feel it needs road testing from users to see what kind of images are uploaded, scale and size

- In the local version of the sire I have a favicon image in the staic folder, called in the head of the base html, and working fine, however in the live deployed site on heroku it is not finding or loading the image.
    - I have tried placing the image in other places in the directory to no avail, and tried different colectstatic setting in the heroku config vars. The static is cbeing collect as the css is rendering. I have decided to leave this it was a last minute addition, while it wile have to be addressed but agin at this mvp stage I feel it doesnt affect the testing and over all ux. A bit more investigation into the heroku staic files is needed and am sure it will be sorted at the next stage. I have left the image in the local version and code to see.

- Another issue with the live site is the rendering of the placeholder image on very large screens isnt great, I like the image and coulnt find a better quality version. 
    - A new image is need of better quality
