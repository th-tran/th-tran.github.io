title: Resume
url: resume

<h1 class="u-lead center">Resume</h1>

Here you will find my resume. I plan to update it often, so that it paints a picture of my full story. 

<div class="center">
  <object data="{{ url_for('static', filename='images/ThomasTranResume.pdf') }}" type="application/pdf" width="80%" height="720px">
    <p>Looks like your browser doesn't support PDF files... :(</p>
    <p> No biggie... you can 
      <a href="{{ url_for('static', filename='images/ThomasTranResume.pdf') }}">click here</a> 
      to download the PDF file instead.
    </p>
  </object>
</div>
