title: NCR - Opportunities
url: co-op-NCR-opportunities

<h1 class="u-lead center">Opportunities</h1>

<img src="{{ url_for('static', filename='images/ncr/authentic.png') }}" alt="">

There were two opportunities that highlighted my work term at NCR. The first was the chance to learn about different processes and technologies by working on their transaction-processing platform, “Authentic”. This platform is at the core of their products; it is a very complex Java application consisting of a web service API, database, many microservices, and various open source applications to provide important features like high availability and security. I spent my first month setting up and becoming familiarized with my development environment. This was a long-winded and manual process, but I learned a great deal as a result. I had worked with Kubernetes and Docker in my previous work term, but only at a high level. By setting up a local cluster and experimenting though, it cleared up my misconceptions about images and pods. I observed how containers act as modular virtual machines and how images produce snapshots of those containers. I observed how Kubernetes uses pods to wrap these containers and group them into clusters, where each cluster is a separate copy of Authentic. Having the opportunity to bounce between clusters and work at a low level (manually mounting images, managing dependent containers, etc.) made these concepts so much clearer.

During the next two months, I worked on different components of Authentic. The component that was most involved was ActiveMQ (AMQ), an open source message broker. This was used to process requests between the web service API and “core”, which facilitated microservices. It needed to be up at all times for Authentic to function properly. I made changes so that in the case of AMQ failure, a replica would take its place and continue processing requests. It’s a simple task that became very complex; in addition to cross-service dependencies, every microservice had an implicit dependency on AMQ. While working on this task, I visualized dependencies via diagrams and considered the side effects of changing AMQ. Through manual and end-to-end testing, I made certain that both compatibility with dependent components and functionality were not compromised as a result. Lastly, I documented the changes made and instructed the other development teams how to update their copy of Authentic. I am very thankful for the trust my supervisor put in me to complete these tasks. By working on the same tasks as my team members,  I learned through mistakes and now fully understand the importance of following the software development process.

<img src="{{ url_for('static', filename='images/ncr/team.png') }}" alt="">

The second was the chance to add new functionality to their web-based sample teller application with a team of other co-ops. Shortly after my work term started in September, the development teams collectively decided to deprecate Authentic’s current API and redesign it as RESTful in Swagger. This change allowed new features to be developed, including bulk transactions and currency transaction report (CTR) filing. At the start of December, an executive decision was made by team leads to assemble 6 co-op students into a team, including myself. It was our last month at NCR, and our task was to update the sample teller app by adding the new features and fixing any modules that used the now-deprecated API.

It was a sudden change, but it led to a very rewarding experience. The co-op team, the management, the timing of the project – all of these factors had a noticeable effect. The most notable effect was collaboration. Though many of us had little experience with web development, we helped each other through the learning curve by pair programming. We held our own meetings, and we’d often come together as a team to solve difficult problems. Late into development, we realized that it was not feasible to implement and test everything, especially with the full-time workers on vacation. As a group, we decided to prioritize our tasks based on importance, determine who is most qualified for each task, and then split our resources accordingly. At the end, we recorded a demo of the application and documented what was left to be done for the next co-ops. This was a great way to sum up our work at NCR, and I am thankful for the opportunity to be able to work with other co-ops. I feel much more confident working in teams now.

<br>
<hr>

<h2 class="u-sublead">More About This Work Term</h2>

[About the Employer]({{site_url}}/co-op/ncr/about-the-employer)

[Job Description]({{site_url}}/co-op/ncr/job-description)

[Work Term Goals]({{site_url}}/co-op/ncr/work-term-goals)

[Skills and Application]({{site_url}}/co-op/ncr/skills-and-application)

<span class='active'>
  [Opportunities]({{site_url}}/co-op/ncr/opportunities)
</span>

[Conclusion]({{site_url}}/co-op/ncr/conclusion)

[Acknowledgements]({{site_url}}/co-op/ncr/acknowledgements)

<div class="left-aligned no-margin">
  Previous: <a href="{{ site_url }}/co-op/ncr/skills-and-application">Skills and Application</a>
</div>

<div class="right-aligned no-margin">
  Next: <a href="{{ site_url }}/co-op/ncr/conclusion">Conclusion</a>
</div>
