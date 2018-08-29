title: Auvik - Opportunities
url: co-op-auvik-opportunities

<h1 class="u-lead center">Opportunities</h1>

<img class="left-aligned" src="{{ url_for('static', filename='images/auvik/kubernetes.png') }}" alt="">

There were many great opportunities afforded to me at Auvik, but two in particular highlighted my work term. The first was the chance to learn by taking an active role in revamping the current application deployment system. The timing of my hire as a co-op student was not a coincidence; my manager was under pressure to rewrite his legacy code fast. This code drove many important scripts he had written years ago. These scripts generated customer reports for the marketing team and system health checks for the engineering team, and needed to run on a regular basis. At the time, my manager developed his own method to automate the scripts (Bash scripts running on a jump server), but it was showing its age. Some scripts were failing at runtime, others had wrong output, and some didn’t run at all. With the engineering team now using Kubernetes to automate deployment, there was no choice but to port over the scripts – an impossible task in their current state.

This was the situation I was thrown into! The learning curve was immense; in only a few days of training, I needed to learn Python, the APIs of Salesforce and other SaaS tools, and the tools used in agile development. It was difficult, but not impossible. I coordinated with my manager, starting with small objectives and defining ways to achieve them; to refactor, learn how the scripts work; to debug, use small test cases; to write pythonic code, research best Python practices. In two short weeks, I not only learned how to rewrite his code to improve efficiency and fix bugs but also learned effective Python by mirroring his functional programming practices. I moved on to write proper test modules via PyTest, factoring in all the edge cases that could break the scripts. Finally, to enable the scripts to be deployed as recurring pods via Kubernetes, I refactored the scripts to write results to MongoDB and Amazon S3 instead of the local file system. This entire process took a month with many pitfalls along the way, but surely things came together in the end. Not only are the scripts much more robust but also self-contained; they are much easier to diagnose through built-in logging and monitoring. I am highly thankful for the trust my manager placed in me. This allowed me to learn at an accelerated pace and apply my skills to a real-world problem.

<img class="left-aligned" src="{{ url_for('static', filename='images/auvik/python_web.png') }}" alt="">

The second was the chance to have full design control over their engineering tools web application. Before the revamp, the script results would be displayed hourly on the jump server as HTML. With the jump server now being taken down, my manager entrusted me the task of creating an entirely new web application on their web server to replace it. I could choose any frameworks I wanted, design the UI, and write its functionality from scratch. The only requirement was to retain the original functionality of the jump server and improve upon it. Considering I’ve never created a web application in Python, I could not let this opportunity pass.

I chose Flask to build the application, Jinja2 to template HTML, and Bootstrap and CSS to create the UI. Though I was educated on the fundamentals of web development in lectures, I realized that there is so much more to consider when developing a web application. I learned about core operations including the ability to template output, store sessions and route URLs, and how powerful these features are when put together. I discovered the pros and cons of caching, its effect on my own application and how I can fully utilize it. Over time I weaved these ideas into the web application, rewriting and refining my code several times. As a result, I created a web application that is easily extendable and updates in real-time. This truly feels like the culmination of my work at Auvik, and I am highly thankful for this opportunity from my manager. I feel much more capable as a web developer now.

You can find screenshots of the web application
<a href="https://imgur.com/a/veUQ0sc/" target="\_blank" rel="noopener">here</a>.

<br>
<hr>

<h2 class="u-sublead">More About This Work Term</h2>

[About the Employer]({{site_url}}/co-op/auvik/about-the-employer)

[Job Description]({{site_url}}/co-op/auvik/job-description)

[Work Term Goals]({{site_url}}/co-op/auvik/work-term-goals)

[Skiils and Application]({{site_url}}/co-op/auvik/skills-and-application)

<span class='active'>
  [Opportunities]({{site_url}}/co-op/auvik/opportunities)
</span>

[Conclusion]({{site_url}}/co-op/auvik/conclusion)

[Acknowledgements]({{site_url}}/co-op/auvik/acknowledgements)

<div style="float: left;">
  Previous: <a href="{{ site_url }}/co-op/auvik/skills-and-application">Skills and Application</a>
</div>

<div style="float: right;">
  Next: <a href="{{ site_url }}/co-op/auvik/conclusion">Conclusion</a>
</div>
