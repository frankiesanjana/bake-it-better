# Bake It Better Testing

Testing was carried out from a number of different perspectives:

- Continuous manual testing during development by running the server and checking that the functionality I was adding worked as intended
- User testing of the concept in order to develop personas
- User testing of the site within the development environment, in particular with regard to the look and feel of the site
- User testing of the deployed site (open feedback)
- User story testing of the deployed site
- Automated Django testing
- Manual testing of the deployed site
- Testing of the deployed site across a range of screen sizes and devices
- Colour contrast testing in order to ensure accessibility
- Validator testing
- Resolved Bugs
- Unresolved Bugs

## Manual Testing During Development

The program was tested continuously by running the local server during its development. Each time a new piece of functionality was created, I ran the server in order to test whether it functioned as intended. This allowed debugging to take place as problems arose, helping me to isolate the cause of bugs relatively quickly rather than attempting to debug once the code was more complex. A detailed description of the bugs encountered during development is given in the Bugs section below.

Once the program had been successfully deployed to Heroku, I followed the logic flow through all the user actions that can be taken on the website to check that it responded appropriately; full details of this are provided in the "Manual Testing of the Deployed Site" section below.

## User Testing: Concept

The concept of the site was tested by interviewing actual and potential users of baking recipes and websites, as well as discussion with my mentor. Based on these conversations, user personas were developed; these are described in more detail in the general Readme.

In particular, the "Best For" concept was based on user comments, for example:
- "Cookbooks often group recipes by type (e.g. for a baking book, bread, cakes, biscuits etc.). However, I would find it useful to have the option to sort recipes by occasion - for example if my grandkids are coming over, I'd like to have a collection of recipes that are easy and fun for them to make."
- "Sometimes I would love to see options that are great for taking to a party: bakes that are easy to make but look impressive and are easily divided into portions to share while still looking good"
- "What about a section of bakes that are a bit more complicated but could be really rewarding to make at the weekend or on a bank holiday when you have the whole day free?"

The ability to star bakes both as a bookmark-style function and to show appreciation of other users' recipes was also identified as a desired capability in the user interviews; for this reason it serves to fulfil both these functions in Bake It Better.

## User Testing During Development

One of the limiters of this project in terms of my own skillset is that I find it hard to intuitively understand the aesthetics of what is pleasing and easy to work with from an end user perspective. In a real-life situation I would be likely to work with a graphic designer and / or have client feedback or colleagues around me, but for this project this was not the case. 
For this reason I interviewed users where possible to obtain feedback on the look and feel of the site from an end user perspective. Some quotes from users are below:
- “I really like what you’ve done with the logo” (no prompt)
- “It’s readable and looks great!” (when asked about the font choice for the bake and page titles) … “but I would change the sub-header font to something simpler [instead of the font used for the bake and page titles] since here it is a bit harder to read”
- “No, keep it – I would like to see the date a bake was posted so that I can see what’s been added recently or since I was last on the site” (when asked if the date and time added unnecessary clutter to the bake list)
- “Get rid of that grey colour [the original background colour for cards and buttons], use a lighter shade that is similar to the background colour of the main page” (no prompt)

## User Testing of the Deployed Site

I sought user feedback on the deployed site once it was tested as working correctly and obtained a number of feedback items that have been implemented:

Add text to My Starred Bakes page if no bakes have been starred yet - initially this was displaying as a blank page if no bakes had been starred, which was confusing for the user. I added a message to be shown in the eventuality that no bakes had yet been starred, linking users to the homepage so they can browse and star bakes:

<img src="readme-images/my-starred-bakes-message.png" alt="View of new My Starred Bakes page with message displayed">

Add cancel button on signout form - I had originally set up the Sign Out form without a Cancel button, reasoning that this was purely a confirmation screen and users could use the navigation links in the navbar if they decided to remain signed in after all:

<img src="readme-images/old-signout-page.png" alt="View of original signout page with no Cancel button">

However, it was deemed a better user experience to have the option to click the Cancel button to cancel signout as well, so this was added:

<img src="readme-images/new-signout-page.png" alt="View of new signout page with Cancel button">

Make the whole Bake card clickable rather than just the title.
- I was initially concerned that this could end up being complex to implement, but it was extremely easy to do by adding `stretched-link` to the link tags since [Bootstrap have built this functionality in](https://getbootstrap.com/docs/4.6/utilities/stretched-link/).

Remove the stars display on the bake-detail page for users who are not signed in, since they need to be signed in to star the bake themselves and this could be too confusing. I had initially thought that this would be fairly self-explanatory (compare Instagram or Facebook for example where it is possible to see the number of likes on a post without being logged in, but users must be logged in to like the post themselves). However, following discussion with users, to ensure a smooth experience for all users it was ultimately decided to remove this view for users who are not signed in.

## User Story Testing of the Deployed Site

## Automated Django Testing

The first step in the automated testing process was to check everything worked via a “test test” by creating a TestCase class in the sheet `bakes/tests.py`. This initially produced an error with the message “permission denied to create database”. This was because I had not realised that when running tests it is necessary to use the local sqlite db and not the postgres one. Conditional formatting has now been applied to the databases so that when Debug is set to True the local database is selected and tests can be performed, but otherwise the postgres database is used so that the site works correctly.

Once I had adjusted this so that the local database was used and the postgres one temporarily disabled, the test ran as intended, giving a fail since I had used `assertEqual(1, 0)`.
I then ran a second test designed to pass, to ensure that a passing test would be evaluated correctly as passing, and obtained the result I was looking for. Since these tests were then deleted, they are also shown here:

<img src="readme-images/automated-testing-concept-tests.png" alt="View of 'test tests' for automated testing">

After this, three testing files were created, to test the forms, the views and the models.

The form testing in `test_forms.py` was relatively straightforward, using the examples laid out in Code Institute's Hello Django testing section. Tests include:

- Testing that the title is required for Bake form submission - pass
- Testing that the equipment needed list is required for Bake form submission - pass
- Testing that the ingredients list is required for Bake form submission - pass
- Testing that the method is required for Bake form submission - pass
- Testing that the description is not required for Bake form submission (since a user might have a favourite recipe but not have the time or creativity needed to write a description) - pass
- Testing that fields are explicit in the form metaclass for the Bake form - pass
- Testing that the message body is required for Comment form submission - pass
- Testing that fields are explicit in the form metaclass for the Comment form - pass
- Testing that the "Best For" field is required for BestFor form submission - pass
- Testing that fields are explicit in the form metaclass for the BestFor form - pass

The view testing in `test_views.py` was, as expected, a little more complicated, and unfortunately in view of time constraints I was not able to test every part of the `views.py` file completely. However, the full CRUD functionality and the ability for a signed-in user to star a bake was tested within the automated tests, and overall I am reasonably satisfied with this approach in combination with thorough manual testing.

First, `setUp` and `tearDown` classes were created, to create and destroy the test objects used to perform the view testing in multiple tests, so that these did not need to be created multiple times. Tests were then written, including:

- Testing that the main page of the site with the bake list loads correctly (response code 200) - pass
- Testing that the bake-detail.html page showing the detailed description of each bake loads correctly (response code 200) - pass
- Testing that the signup page for new users loads correctly (response code 200) - pass
- Testing that the login page loads correctly (response code 200) - pass
- Testing that the Add Bake page loads correctly for a signed-in user (response code 200) - pass
- Testing that the Edit Bake page loads correctly for a signed-in author user (response code 200) - pass
- Testing that the Delete Bake page loads correctly for a signed-in author user (response code 200) - pass
- Testing that the Best For Bakes page loads correctly for a signed-in user (response code 200) - pass
- Testing that the My Starred Bakes page loads correctly for a signed-in user (response code 200) - pass
- Testing that the logout page loads correctly for a signed-in user (response code 200) - pass
- Testing that a signed-in user can successfully add a bake, by creating a new bake and then asserting that this new bake exists - pass
- Testing that a signed-in author user can successfully edit a bake, by editing an existing bake and then asserting that the edited bake exists - pass
- Testing that a signed-in author user can successfully delete a bake, by deleting an existing bake and then asserting that the deleted bake does not exist - pass
- Testing that a signed-in user can successfully star a bake, by creating and starring a new bake and then asserting that the bake is starred - pass

Similarly, for the model testing in `test_models.py`, the automated testing focused around the Bake model, since this is the largest and most complex model, and this is combined with extensive manual testing in order to ensure the site functions as intended.

Again, `setUp` and `tearDown` classes were created, to create and destroy the test objects used to perform the model testing in multiple tests, so that these did not need to be created multiple times. Tests were then written, including:

- Testing that the bake slug is successfully created from the title in the Bake model - pass
- Testing that the string is successfully created in the Bake model - pass
- Testing that a new bake created using the Bake model defaults to not being starred when it is created - pass

To ensure that I had, in fact, tested a reasonable proportion of the site via automated testing, I created a coverage report. The details of this can be seen below:

<img src="readme-images/automated-testing-coverage.png" alt="View of automated testing coverage report">

## Manual Testing of the Deployed Site

Manual testing results are displayed in the images below:

<img src="readme-images/manual-testing-1.png" alt="View of manual testing image 1">
<br>
<img src="readme-images/manual-testing-2.png" alt="View of manual testing image 2">
<br>
<img src="readme-images/manual-testing-3.png" alt="View of manual testing image 3">
<br>
<img src="readme-images/manual-testing-4.png" alt="View of manual testing image 4">
<br>
<img src="readme-images/manual-testing-5.png" alt="View of manual testing image 5">

## Colour contrast testing in order to ensure accessibility

The colour contrast of the website was tested by using the [Coolors colour checker](https://coolors.co/contrast-checker). The results are as follows:

- Text against the main background colour: "good" contrast for smaller text and "great" contrast for larger text or smaller bold text

<img src="readme-images/text-on-main-background.png" alt="View of testing report for text colour on main background">

- Text against the main background colour: "good" contrast for smaller text and "great" contrast for larger text or smaller bold text

<img src="readme-images/text-on-secondary-background.png" alt="View of testing report for text colour on secondary background">

## Lighthouse Testing

Lighthouse testing was undertaken in Chrome's Developer Tools. The Lighthouse reports brought to light several issues, most notably relating to the Performance metric. The initial testing on the homepage was as follows:

<img src="readme-images/lighthouse-testing.png" alt="View of homepage Lighthouse testing">

The images were a potential source of the performance issue. However, testing on the Add Bake page showed an even poorer performance score:

<img src="readme-images/lighthouse-test-add-bake.png" alt="View of Add Bake page Lighthouse testing">

And the Best For Bakes page, which always contains eight images, returned a better score:

<img src="readme-images/lighthouse-test-best-for.png" alt="View of Best For Bakes page Lighthouse testing">

The image size is difficult to control because the images are uploaded by the site users. Ideally a future feature of the website could be to resize them automatically when they are uploaded, although it is not certain how much difference this would make. It is also possible that part of the issue is caused by using free hosting for the site on Heroku, since this is likely to be slower than paid hosting.

Other issues that were brought to light by the testing include some accessibility issues, where not all buttons had `aria-label` attributes (now rectified), and the issue that headings were not used in descending order (beginning at `h1`, then `h2` and so on). This has also now been rectified using a combination of adjusting the headings to appear in the correct order and where appropriate using `p` elements with classes and applying styling to these instead.

## Validator Testing

### PEP8 Testing

The Python code was run through [CI's Python Linter](https://pep8ci.herokuapp.com/). Several files returned no errors, but some examples of those that did are shown below:

<img src="readme-images/python-forms-testing.png" alt="View of Python forms linter testing">
<img src="readme-images/python-views-testing.png" alt="View of Python views linter testing">

Initially I obtained a number of "line too long" errors, trailing whitespace at ends of lines and some line spacing errors, as well as one place in the forms.py file where the indentation had not worked correctly. These issues were fairly simple to rectify, and all files then returned the "All clear, no errors found" message:

<img src="readme-images/python-testing-complete.png" alt="View of Python views linter testing finished">
