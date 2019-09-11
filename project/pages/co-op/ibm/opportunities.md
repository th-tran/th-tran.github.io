title: IBM - Opportunities
url: co-op-ibm-opportunities

<h1 class="u-lead center">Opportunities</h1>

<img class="left-aligned" src="{{ url_for('static', filename='images/ibm/personalization.png') }}" alt="">

The main opportunity that highlighted my work term was writing the backend to a personalization system using React, Node.js and Express. This system was only in its infant stages of development when I joined the team. Similar to recommendation systems used in popular services like Netflix and Amazon, our goal was to personalize a user’s experience in the IBM Cloud platform by providing useful and relevant recommendations. The idea for our first iteration differed from typical recommendation systems though; we planned to incorporate an ‘intent’ system, allowing the user to directly inform us what they want (via dropdown option) so we can provide quality suggestions. No one was against the idea and the implementation was straightforward. I used an open source library, “JSON Rules Engine”, to implement both the recommendations and the logic to determine the best recommendations for specific users. I worked on the server-side to call the API that provides recommendations, cache them and handle different languages. The target launch date for our MVP was start of July and it was only the start of June; things were looking very good time wise.

However, things took a turn for the unexpected. We decided to present our current product to the Offering Manager before we followed through with release. Although the design had been approved already, they made the call that – in its current state – this product was not to standard. Specifically, they reasoned that there was no reason why the recommendation system should not be automated with the abundance of user data in our hands. And they were right; we were only using a tiny fragment of user data for dynamic recommendations and we leaned too much on our intent system (which mostly acted like a static dropdown list anyways). Though it wasn’t appreciated by many at the time, the change proved to transform it into an organic, self-learning system that I’m proud to have worked on.

<img class="left-aligned" src="{{ url_for('static', filename='images/ibm/this_is_fine.png') }}" alt="">

Our team got together over the next few weeks to discuss how design would change (I won’t go into too much detail for confidentiality reasons). The work that I did became much harder after this point, but it was for the best. We decided to scrap the intent system entirely and instead provide recommendations without any necessary input from the user (like Amazon or Netflix). The new system was much smarter as well; we would incorporate algorithms to mimic the same core model used in renowned recommendation systems such as Google. We also planned to set up a database to store the user data and statistics, and use it to drive the system with information. The entire launch date was pushed back to start of September – nearly twice as long as the original date. The learning curve was steep, but it was manageable. I spent the week ramping up on the new design requirements and researching Cloudant (a NoSQL database). The following month, I focused on refactoring the recommendation engine, removing the old intent system and implementing the new algorithms. I also took charge of the database setup and wrote Cloudant classes to read/write data and resolve conflicts. The most difficult part of this was scaling the database to production-level; we needed to deploy it in several regions, each with multiple instances to ensure uptime. By working together with the lead architect, I implemented a robust system that reads in and updates data on a regular basis and handles read/write conflicts gracefully. I finished off by writing unit tests to ensure that each part was reliable and worked as expected.

When everything came together, it was a sight to see. It performed as expected and beyond – the recommendations were accurate and dynamic, and were all based on the user’s context and recent activity. I can say that this is the culmination of my work at IBM, and I am very thankful for this opportunity and for the trust my supervisor put in me. I learned an incredible amount in a short period of time and I got to apply my skills to a real-world problem. I am much more capable as a web developer now.

You can take a look at the personalization system
<a href="https://imgur.com/a/BbKRIu7" target="\_blank" rel="noopener">here</a>.

<br>
<hr>

<h2 class="u-sublead">More About This Work Term</h2>

[About the Employer]({{site_url}}/co-op/ibm/about-the-employer)

[Job Description]({{site_url}}/co-op/ibm/job-description)

[Work Term Goals]({{site_url}}/co-op/ibm/work-term-goals)

[Skills and Application]({{site_url}}/co-op/ibm/skills-and-application)

<span class='active'>
  [Opportunities]({{site_url}}/co-op/ibm/opportunities)
</span>

[Conclusion]({{site_url}}/co-op/ibm/conclusion)

[Acknowledgements]({{site_url}}/co-op/ibm/acknowledgements)

<div class="left-aligned no-margin">
  Previous: <a href="{{ site_url }}/co-op/ibm/skills-and-application">Skills and Application</a>
</div>

<div class="right-aligned no-margin">
  Next: <a href="{{ site_url }}/co-op/ibm/conclusion">Conclusion</a>
</div>
