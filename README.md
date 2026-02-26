<h1>AI Travel Itinerary Generator ✈️🗺️</h1>

<p>
  An <strong>AI-powered travel planning application</strong> that generates personalized travel itineraries
  based on user preferences using the <strong>OpenRouter API</strong>.
  The project focuses on producing <strong>clean, human-readable PDF itineraries</strong> by converting
  AI-generated content into structured and professional documents.
</p>

<p>
  <strong>Repository:</strong>
  <a href="https://github.com/shrishailya1/AICTE-7.git" target="_blank">GitHub</a>
</p>

<hr>

<h2>Features</h2>
<ul>
  <li>AI-based itinerary generation using OpenRouter API</li>
  <li>Dynamic travel plans with day-wise activities</li>
  <li>Automatic cleaning of AI-generated markdown content</li>
  <li>Professional PDF generation with pagination support</li>
  <li>Scalable backend architecture using Python</li>
</ul>

<hr>

<h2>Tech Stack</h2>
<ul>
  <li><strong>Language:</strong> Python</li>
  <li><strong>Backend:</strong> Flask</li>
  <li><strong>AI API:</strong> OpenRouter</li>
  <li><strong>PDF Generation:</strong> ReportLab</li>
  <li><strong>Markdown Processing:</strong> markdown2</li>
</ul>

<hr>

<h2>Project Workflow</h2>
<ul>
  <li><strong>Step 1:</strong> User provides travel details (destination, days, preferences)</li>
  <li><strong>Step 2:</strong> Request sent to OpenRouter AI model</li>
  <li><strong>Step 3:</strong> AI generates itinerary content (Markdown format)</li>
  <li><strong>Step 4:</strong> Markdown is cleaned and converted into readable text</li>
  <li><strong>Step 5:</strong> Final itinerary is exported as a professional PDF</li>
</ul>

<hr>

<h2>Prerequisites</h2>
<ul>
  <li><strong>Python (3.9 or later):</strong> <a href="https://www.python.org/downloads/" target="_blank">Download</a></li>
  <li><strong>pip:</strong> Python package manager</li>
  <li><strong>Git:</strong> <a href="https://git-scm.com/" target="_blank">Download</a></li>
</ul>

<hr>

<h2>Installation</h2>

<h3>1. Clone the Repository</h3>
<pre><code>git clone https://github.com/shrishailya1/AICTE-7.git</code></pre>

<h3>2. Navigate to Project Directory</h3>
<pre><code>cd ai-itinerary-generator</code></pre>

<h3>3. Install Dependencies</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<hr>

<h2>Run the Project</h2>
<pre><code>python app.py</code></pre>

<p>
  Once the server is running, submit travel details and the application will
  generate a clean PDF itinerary.
</p>

<hr>

<h2>Usage</h2>
<ul>
  <li>Enter destination and travel preferences</li>
  <li>Generate AI-based itinerary</li>
  <li>Download clean and readable PDF output</li>
</ul>

<hr>

<h2>Proof of Concept</h2>

<ul>
  <li>
    <strong>Interface</strong><br>
    <img src="./images/ai_output.png" alt="AI Output" width="600">
  </li>

  <li>
    <strong>Map</strong><br>
    <img src="./images/cleaned_text.png" alt="Cleaned Text" width="600">
  </li>

  <li>
    <strong>Final PDF Output</strong><br>
    <img src="./images/final_pdf.png" alt="Final PDF" width="600">
  </li>
</ul>

<hr>

<h2>Project Structure</h2>
<pre><code>ai-itinerary-generator/
├── app.py              # Application entry point
├── planner.py          # OpenRouter API integration
├── pdf_utils.py        # PDF generation & markdown cleaning
├── map_utils.py        # Travel mapping utilities
├── requirements.txt    # Dependencies
├── itinerary.pdf       # Generated output
└── README.md           # Project documentation
</code></pre>

<hr>

<h2>Future Improvements</h2>
<ul>
  <li>Add HTML-based PDF styling for richer layouts</li>
  <li>Integrate hotel and transport APIs</li>
  <li>Deploy application on cloud (AWS / Render)</li>
  <li>Add frontend UI for user interaction</li>
</ul>

<hr>

<h2>Author</h2>
<p>
  <strong>Shrishailya Patil</strong><br>
  📧 Email: shrishailyapatil339@gmail.com<br>
  🔗 GitHub: <a href="https://github.com/shrishailya1/AICTE-7.git" target="_blank">shrishailya1</a><br>
  🔗 LinkedIn: <a href="https://www.linkedin.com/in/shrishailya-patil" target="_blank">Shrishailya Patil</a>
</p>

<hr>
<h2>Contributing</h2>
<p>
  Contributions are welcome! Please fork the repository and submit a pull request.
</p>

<p>
  ⭐️ If you like this project, don’t forget to star the repository!
</p>