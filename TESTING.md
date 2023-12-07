# Splash Swim School - Testing

![App Preview](media/amiresponsive.png)


## Table of Contents

- [Test Record](#testrecord)
- [CSS3 Validator](#css)
- [HTML5 Validator](#html)
- [JavaScript Validator](#js)
- [Python Validator](#python)
- [Accessibility](#access)
- [Compatibility](#compatibility)
- [Performance](#performance)
- [User Story](#user)
- [Known Bugs](#bugs)



<a name="#testrecord"></a>
## Test Record :
**TEST** | **ACTION** | **EXPECTATION** | **RESULT** 
----------|----------|----------|----------
 Home page | Size to 320px using Chrome Dev Tools	| Elements look good @ 320px | Works as expected
Home page | Size to 1920px using Chrome Dev Tools | Elements look good 1920px | Works as expected
Home page | Size to 990px using Chrome Dev Tools | Navbar to toggle | Works as expected
Home page | Scroll action | NavBar Scrolls with user | Works as expected
Home page | Header Nav links clicked |  User taken to respective correct pages | Works as expected
Home page | Size to 990px & Toggle Nav links clicked |  User taken to respective correct pages | Works as expected
Home page |Header Logo Text clicked | User taken to Home page | Works as expected
Home page | Book Now Button clicked | Take user to levels and book section | Worked as expected
Home page | All three links clicked on who we are section | Take user to correct sections of the site respectively | Worked as expected
Home page | Book Now buttons clicked in the Swim Levels section | Take user to relevant level page all 4 tried | Worked as expected
Home page | Haeding links clicked in the Swim Levels section | Take user to relevant level page all 4 tried | Worked as expected
Home page | About link clicked in Nav | Take user to About section | Worked as expected
Home page | Contact link clicked in Nav | Take user to Contact section | Worked as expected
Level page1 | Size to 320px using Chrome Dev Tools	| Elements look good @ 320px | Works as expected
Level page1| Size to 1920px using Chrome Dev Tools | Elements look good 1920px | Works as expected
Level page1 | Book Now button clicked  | Take user to the course selection section | Worked as expected
Level page1 | Size to 990px using Chrome Dev Tools and toggle links clicked | NavBar to toggle and links take user to respective correct pages | Works as expected
Level page1 | FAQ's Section  | Accordions collapse and revert correctly| Works as expected
Level page1 | Scroll action | NavBar Scrolls with user | Works as expected
Level page1 | Header Nav links & Logo Text clicked |  User taken to respective correct pages | Works as expected
Level page1 | Course selection Radio selects and Book Now button clicked |  correct course added to bag | Works as expected
Level page1 | Course selection Book Now button clicked without Radio selection |  book now button disabled | Works as expected
Level page2 | Size to 320px using Chrome Dev Tools	| Elements look good @ 320px | Works as expected
Level page2| Size to 1920px using Chrome Dev Tools | Elements look good 1920px | Works as expected
Level page2 | Book Now button clicked  | Take user to the course selection section | Worked as expected
Level page2 | Size to 990px using Chrome Dev Tools and toggle links clicked | NavBar to toggle and links take user to respective correct pages | Works as expected
Level page2 | FAQ's Section  | Accordions collapse and revert correctly| Works as expected
Level page2 | Scroll action | NavBar Scrolls with user | Works as expected
Level page2 | Header Nav links & Logo Text clicked |  User taken to respective correct pages | Works as expected
Level page2 | Course selection Radio selects and Book Now button clicked |  correct course added to bag | Works as expected
Level page2 | Course selection Book Now button clicked without Radio selection |  book now button disabled | Works as expected
Level page3 | Size to 320px using Chrome Dev Tools	| Elements look good @ 320px | Works as expected
Level page3| Size to 1920px using Chrome Dev Tools | Elements look good 1920px | Works as expected
Level page3 | Book Now button clicked  | Take user to the course selection section | Worked as expected
Level page3 | Size to 990px using Chrome Dev Tools and toggle links clicked | NavBar to toggle and links take user to respective correct pages | Works as expected
Level page3 | FAQ's Section  | Accordions collapse and revert correctly| Works as expected
Level page3 | Scroll action | NavBar Scrolls with user | Works as expected
Level page3 | Header Nav links & Logo Text clicked |  User taken to respective correct pages | Works as expected
Level page3 | Course selection Radio selects and Book Now button clicked |  correct course added to bag | Works as expected
Level page3 | Course selection Book Now button clicked without Radio selection |  book now button disabled | Works as expected
Level page4 | Size to 320px using Chrome Dev Tools	| Elements look good @ 320px | Works as expected
Level page4 | Size to 1920px using Chrome Dev Tools | Elements look good 1920px | Works as expected
Level page4 | Book Now button clicked  | Take user to the course selection section | Worked as expected
Level page4 | Size to 990px using Chrome Dev Tools and toggle links clicked | NavBar to toggle and links take user to respective correct pages | Works as expected
Level page4 | FAQ's Section  | Accordions collapse and revert correctly| Works as expected
Level page4 | Scroll action | NavBar Scrolls with user | Works as expected
Level page4 | Header Nav links & Logo Text clicked |  User taken to respective correct pages | Works as expected
Level page4 | Course selection Radio selects and Book Now button clicked |  correct course added to bag | Works as expected
Level page4 | Course selection Book Now button clicked without Radio selection |  book now button disabled | Works as expected
Bag |Size to 320px using Chrome Dev Tools	| Elements look good @ 320px | Works as expected
Bag |Size to 1920px using Chrome Dev Tools | Elements look good 1920px | Works as expected
Bag |Size to 990px using Chrome Dev Tools and toggle links clicked | NavBar to toggle and links take user to respective correct pages | Works as expected
Bag  | Header Nav links & Logo Text clicked |  User taken to respective correct pages | Works as expected
Bag | Bag empty Clicks Keep shopping | Takes User to home page | Works as expected
Bag| contents added  | displays course information  | Works as expected
Bag| contents added delete button selected  | Course removed from bag with success message  | Works as expected
Bag| contents added check out button selecetd | User passed to checkout  | Works as expected
Checkout | All sizes checked using Chrome Dev Tools	| Elements look good @ all sizes | Works as expected
Checkout | Form inputs filled out | All forms accept their inputs | Works as expected
Checkout| STRIPE test payment used | Purchase completes |Works as expected
Checkout| Review order information | correct course information displayed |Works as expected
Checkout Success | All sizes checked using Chrome Dev Tools	| Elements look good @ all sizes | Works as expected
Checkout Success | purchase made | information populated correctly on checkout success page | Works as expected
Checkout Success | button sleected to find out more about splash | takes user to home page |Works as expected
Profile | All sizes checked using Chrome Dev Tools	| Elements look good @ all sizes | Works as expected
Profile |User Logged in - clicks to access | user can access profile |Works as expected
Profile |User not Logged in | No profile option available |Works as expected
Profile |User Logged in information fields updated | information updated |Works as expected
Profile |User Logged in | order history correctly shown |Works as expected
Profile |User Logged in information inputed to Guradian Profile| Guardian profile information saved |Works as expected
Profile |User Logged in information edited in field | Guardian profile updated information saved |Works as expected
Profile |User Logged in Guardian profile deleted| modal activated information daleted and all related child profiles deleted |Works as expected
Profile |User Logged in information inputed to Child Profile| Child profile information saved |Works as expected
Profile |User Logged in Child profile update btn clicked | child profile edit view opened and ability to save or cancel |Works as expected
Profile |User Logged in Child profile deleted| modal activated information daleted and all related child profiles deleted |Works as expected
Login page| All sizes checked using Chrome Dev Tools	| Elements look good @ all sizes | Works as expected
Login page| Header Nav links & Logo Text clicked |  User taken to respective correct pages | Works as expected
Login page| User inputs valid username and password | User taken to home page successful login message displayed | Works as expected
Login page| User inputs valid username and password | Navigation bar options for profile and admin management become available | Works as expected
Login page| User inputs in-valid username and password | Flash message appears to highlight they have entered an invalid username or password  | Works as expected
Sign Up page| All sizes checked using Chrome Dev Tools	| Elements look good @ all sizes | Works as expected
Sign Up page| Header Nav links & Logo Text clicked |  User taken to respective correct pages | Works as expected
Sign Up page| User inputs username and password | user redirected to login page saying success and inviting them to use their new credentials to login | Works as expected - Database checked password is successfully hashed
Logout NavBar Button| Logged in user clicks to logout | User logged out and redirected to the the confirmation sign out page | Works as expected
Sign Out Page | Logged in user clicks to sign out | User is signed out and redirected to home and confirmation message appears | Works as expected


<a name="#css"></a>
## CSS3 validator - Pass
Files Tested 
 - base.css
 - profile.css

<img src="media/cssvalidator.png" />

<a name="#html"></a>
## HTML5 validator
- base.html - Passed using HTML from View Page Source to remove Jinja Templating and Statci urls.
- home.html - Passed using HTML from View Page Source to remove Jinja Templating and Statci urls.
- about.html - Passed using HTML from View Page Source to remove Jinja Templating and Statci urls.
- add_note.html - Passed after some form editing - used HTML from View Page Source to remove Jinja Templating and Statci urls.
- edit_note.html - Passed after some form editing - used HTML from View Page Source to remove Jinja Templating and Statci urls.
- login.html - Passed using HTML from View Page Source to remove Jinja Templating and Statci urls.
- signup.html - Passed using HTML from View Page Source to remove Jinja Templating and Statci urls
<img src="documents/htmlvalidator.png" />


<a name="#js"></a>
## Javascript validator
- Reported Metrics - 
There are 7 functions in this file.

Function with the largest signature take 1 arguments, while the median is 1.

Largest function has 8 statements in it, while the median is 1.

The most complex function has a cyclomatic complexity value of 1 while the median is 1.

One undefined variable line 5 bootstrap

<img src="media/jsvalidation.png" />

<a name="#python"></a>
## Python validator
- routes.py - All clear, no errors found

<img src="documents/routes.png" height="200px"/>

- models.py - All clear, no errors found

<img src="documents/models.png" height="200px"/>

- __init__.py - All clear, no errors found

<img src="documents/init.png" height="200px"/>

- run.py - All clear, no errors found

  <img src="documents/run.png" height="200px"/>

- env.py - All clear, no errors found


<a name="#access"></a>
## Accessibility

### Lighthouse testing
- At the time of testing Lighthouse would not complete its warm up on the local server or the Heroku deployed app so wave was utilised instead

### Wave testing
- Wave testing highlighted several contrasting issues with Home page and about page Hero and Recap areas text. Now initially I used the contrast tool to evaluate what Hex colour would pass and applied those colours to the text areas in question. On inspecting these areas after the changes were made they passed the wave contrast checker but I strongly felt that the text was less readable. I have provided screenshots of the before and after of these sections for you in order to demonstrate the change and why I chose to go against the contrast guidance from Wave. I also read within the Wave checker that “WAVE does not detect contrast of background gradients, transparency, etc. For background images, WCAG requires a fallback background color in case the image does not display” I believe that Wave has not been able to read the background accurately enough to assess the correct contrast for the text areas in question. There are currently No erros present only Contrasting errors as detailed below.

    - Changes I have made based on wave testing 
        - aria-label="Scroll to next section" Added to both downward chevrons on home and about
        - Section title from #1f1f1f to #0F0F0F
        - Body text from #444444 to #1C1C1C
    - Changes i trialed and chose to revert to the before images;
        - Hero & Recap text for the home and about page changed from #ADAA99 to #7A7462 
        
        Before 
        
        <img src="documents/herobefore.png" height="200px"/> 
        
        After
        
        <img src="documents/heroafter.png" height="200px"/>


        - Title Anam Cara in the recap section of home and about from #FFD685 to #946800.

        Before

        <img src="documents/recapbefore.png" height="200px"/>
        
        After

        <img src="documents/recapafter.png" height="200px"/>



<a name="#compatibility"></a>
## Compatibility Testing
- Browser Compatibility tested via [Browser Stack](https://live.browserstack.com/) 
- tested on the latest versions of the following
    | Safari    | Firefox   | Chrome  | Opera  | Edge  |
    | --------- |:---------:| -------:| ------:| -----:|
    | Pass      | Pass      | Pass    | Pass   | Pass  | 
    
- Chrome developer tools has been used to check the responsiveness of the site across different screen sizes and devices. 
- The site has mostly been built and tested on a Macbook Air operating on MacOs Catalina.

<a name="#performance"></a>
## Performance Testing
-  The performance of the site was tested on the following site with satisfactory results. [Web Page Test](https://www.webpagetest.org)

<a name="#user"></a>
## Testing User Stories 
>### External testing
- All testers confirmed that they coud sign up, login and logout.
- All testers confirmed that all buttons and navigation links performed the correct function.
- All testers confirmed that the forms submitted and messages displayed correctly.
- All testers confirmed that they could read messages, update and delete their messages.

>### User Stories - Customer
- From user story 1;
    - Community message board created providing a space for likeminded individuals to connected and foster meaningful and supportive interactions.
    - Users able to login and edit or delete messages should they change their mind.
    - Users able to scroll through the message board to read and reflect on their previous messages and personal growth.
    - the implementation of a 100 minimum requirement within the text area means that the user needs to take their time and really express in detail how they are feeling rather than quick messages with no thought behind them. The selection of a Publish Date takes the immediacy out of the posting. Both of these elements work together to create a slower less intrusive way of expressing yourself and connecting.



- From user story 2;
     - The structure of the site has been kept to a traditional interface meaning that the user does not have to think about how they navigate to where they want to go. Nav links at the top and the bottom of the page along with the Discover links funnel the user to the correct pages. All restricted pages invite the user to login and once the user has actioned logging in, out, signing up or submitting, updating or deleting a message they are redirected intuitively to relevant next page for them.
    - The selected Publish date allows users to choose when they publish their message.
    - The Colour palette has been specifically chosen to create a tranquil peaceful experience whilst still retaining the modern Celtic vibe in line with the brand. The use of colours behind the messages and lack of imagery mean that the messages remain the focus of the connect page.
    - There is a free text section where people can choose to input their contact details or choose to leave it blank - this is the only field within the form that is not required in order to fulfil this user request.



- From user story 3;
    - There is a free text section where people can choose to input their contact details or choose to leave it blank - this is the only field within the form that is not required in order to fulfil this user request.
    - The delayed posting/schedule feature of the messages and once a day release of the scheduled posts fosters the slow reading and once a day visits rather than endless scrolling. The newest messages appear at the top to ensure users are not scrolling through countless messages to review the most recent.
    - Comments are not enabled in this version and contact details are optional to share limiting trolls or attacks on certain posts. 
    - The messages and profiles have been kept image free to foster love and friendship at a spiritual level before material judgement


>### User Stories - Business Owner
-  The brand ethos and values have been incorporated into the messaging styling of the site. All users stories have been met to create the requested type of environment where the user would feel safe to freely make meaningful connections.
- All passwords have been hashed for security. There are elements of defensive programming protecting the user from accidentally deleting their own content and we have implemented user authorisation for access to the update and delete functions of the messages. 
- The beta test version of Anam Cara captures its core values and provides the raw facility needed to post messages and start garnering a community. This provides the business with the ability to watch how their community utilises the site and listen to feedback about additional features the community would like. Creating a solid base allows the business to equate what features they can add and use to scale the community in a sustainable way. 



<a name="bugs"></a>
## Known Bugs

- One potential bug known of at the time of submission - Not all notes appear to be listed in a descending order from most recently added first. This was fully tested locally and found to be fine but one blip shown when users posted via heroku app. 


## Bugs & challenges experienced during the build


- The largest challenge faced was the inability to migrate my database changes half way through the build. I built out the basic CRUD function first and foremost and only when i was happy with that did i attempt to add user authentication. The additional table for the user data migrated organically through git push however the additional user_id column added to the original Note table did not migrate. After endless attempts to update and migrate the database to Heroku/ElephantSQL i took the decision to delete the ElephantSQL instance and Heroku App and work through the deployment steps again. This has fixed the bug. Deletion of Heroku & ElephantSQL linked to your app is not recommended due to the data loss implications, however in this instance the data base was blank and so posed not risk to the build. 

- The addition of the Delete Modal in the notes.html allowing the bootstrap modal to pop up when the trash can icon was selected appeared to create a bug within the code. On closer inspection the Delete Modal was not within the for loop and it did not have not_id associated with it. This was picked up by Jason on tutoring support. Once the issue was discovered I moved the Delete modal into the for loop, setting the delete button to call the delete route and pass the note_id value. This rectified the delete bug and restored the Delete function.

- All Flash messages functioned as expected apart from the flash to flag an invalid username or password at login. This was resolved by duplicating the else statement to show the message for both an incorrect username or password without disclosing to the user which field was inputted incorrectly.

- I experienced issues with implementing a Jinja Templating filter to allow the messages to appear in reverse order. After further research i discovered to effect this change i only needed to make a change within the routes.py file, creating a descending query order. 

- Initially the form was not passing the submission date information to the database. On further inspection the name, ID & value had an extra note_ at the start of them. This was removed and the input functioned correctly. 