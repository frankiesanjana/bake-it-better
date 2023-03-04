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

## Manual Testing During Development

The program was tested continuously by running the local server during its development. As functionality was created, [xxx]

Once the program had been successfully deployed to Heroku, I followed the logic flow through all the user actions that can be taken on the website to check that it responded appropriately:


## User Testing: Concept

## User Testing During Development

One of the limiters of this project in terms of my own skillset is that I find it hard to intuitively understand the aesthetics of what is pleasing and easy to work with from an end user perspective. In a real-life situation I would be likely to work with a graphic designer and / or have client feedback or colleagues around me, but for this project this was not the case. 
For this reason I interviewed users where possible to obtain feedback on the look and feel of the site from an end user perspective. Some quotes from users are below:
- “I really like what you’ve done with the logo” (no prompt)
- “It’s readable and looks great!” (when asked about the font choice for the bake and page titles) … “but I would change the sub-header font to something simpler [instead of the font used for the bake and page titles] since here it is a bit harder to read”
- “No, keep it – I would like to see the date a bake was posted so that I can see what’s been added recently or since I was last on the site” (when asked if the date and time added unnecessary clutter to the bake list)
- “Get rid of that grey colour [the original background colour for cards and buttons], use a lighter shade that is similar to the background colour of the main page” (no prompt)

## Automated Testing

First I ran a “test test” by creating a TestCase class in the sheet `bakes/tests.py`. This initially produced an error with the message “permission denied to create database”. This was because I had not realised that when running tests it is necessary to use the local sqlite db and not the postgres one [add pic of switching commented out database]
Once I had adjusted this so that the local database was used and the postgres one temporarily commented out, the test ran as intended, giving a fail since I had used assertEqual(1, 0).
I then ran a second test designed to pass, to ensure that a passing test would be evaluated correctly as passing, and obtained the result I was looking for. Since these tests were then deleted, they are also shown here:

<img src="readme-images/automated-testing-concept-testing.png" alt="View of 'test tests' for automated testing">

After this, three testing files were created, to test the forms, the views and the models.

The form testing was relatively straightforward, using the examples laid out in Code Institute's Hello Django testing section.

The view testing was, as expected, a little more complicated, and unfortunately in view of time constraints I was not able to test every part of the `views.py` file completely. However, the full CRUD functionality and the ability for a signed-in user to star a bake was tested within the automated tests, and overall I am reasonably satisfied with this approach in combination with thorough manual testing.

Similarly, for the model testing, the automated testing focused around the Bake model, since this is the largest and most complex model, and this is combined with extensive manual testing in order to ensure the models function as intended.

To ensure that I had, in fact, tested a reasonable proportion of the site via automated testing, I created a coverage report. The details of this can be seen below:

<img src="readme-images/automated-testing-coverage.png" alt="View of 'test tests' for automated testing">

## Validator Testing - SECTION TO UPDATE
<!-- ### PEP8 Testing

The Python code was run through [PEP8 online](http://pep8online.com/):

<img src="" alt="View of PEP8 testing, first screen">

Initially I obtained a large number of "line too long" errors, as well as one place where a function did not have two blank lines before it but only one, and one "trailing whitespace" error that was part of the ASCII art:

<img src="assets/images/validator-two.png" alt="View of PEP8 testing, second screen">
<br>
<img src="assets/images/validator-three.png" alt="View of PEP8 testing, third screen">

I spent some time adjusting the code so that the lines were shorter than 80 characters, inserted an extra blank line before the function, and was able to adjust the ASCII art without affecting the way it displayed. The code then passed through the validator successfully:

<img src="assets/images/validator-four.png" alt="View of PEP8 testing, fourth screen"> -->
