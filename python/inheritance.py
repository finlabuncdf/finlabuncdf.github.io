import csv

title_t = ""
about_t = ""

with open('uncdf.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    name = []
    about = []
    for row in readCSV:
        name_n = row[1]
        about_n = row[2]

        name.append(name_n)
        about.append(about_n)
    
for index in range(1, len(name)):
    title_t = name[index]
#        print(dates[index])
    f = open("helloworld"+str(index)+".html",'w')
    
    
    message = """<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	
	<meta http-equiv="x-ua-compatible" content="ie=edge">
	
	<title>Tool Page</title>
	
	<meta name="description" content="">
	
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	
	<!--<script src="p5/p5.min.js" type="text/javascript"></script>
	<script src="p5/p5.dom.js" type="text/javascript"></script>-->
	<!--<script src="header.js" type="text/javascript"></script>-->


	  <link rel="stylesheet" href="project.css">
</head>
<body>
	<div class="header-section">
		<div class="header-container">
			<div class="header-text">
				<h1>"""+title_t+"""</h1>
				<div class="header-links"><a href="#">About</a>
					<a href="#">"""+about_t+"""</a></div>
			</div>
		</div>
	</div>
    <div class="tool-section">
		<div class="tool-grid">
			<div class="tool-name">
				<h2>Problem Tree + 5 Whys</h2>
				
				<p>90-135 Mins</p>
				
				<p>Template, Chart Paper, Post-its, Pens/Sketch Pens</p>
			</div>
			
			<div class="tool-example-image">
				<img src="tool-s.png" alt="" />
			</div>
			
			<div class="tool-about">
				<h2>About Tool</h2>
				<p>Problem Tree is a tool used to identify effects and causes of a given challenge. The aim is to repeatedly unpack each symptom until one reaches a 'root cause' or unexpected angle from which to think of the problem. While traditionally the tool is looked only through a problem lens, it can also use it to appreciate opportunities. 5 Whys are an activity that can be run during  the Problem Tree to help participants get to the root cause of the topic.</p>
			</div>
			
			<div class="tool-use-case">
				<h2>Use cases</h2>
				
				<ul>
					<li>Reframing a problem or topic to make sure the way the problem is understood by the group is the best way to look at it.</li>
					<li>Uncovering unexpected opportunities in the space a team or organisation is working in.</li>
				</ul>
			</div>
			
			<div class="tool-understand">
				<h2>Understand</h2>
				
				<ul><li>The 'Problem/Opportunity' section should be something specific that has been chosen to be investigated. This could be the problem faced by the user, or an opportunity area defined by the startup (this can be taken from the problems listed in the Startup Canvas) or organisation.</li><li>The 'Effects' are what happens as a result of the problem. These symptoms should be written in the branches of the tree. For example, if the problem is defined as 'Poor Public Transport', then an effect would probably be, 'Commuter getting late to work', or 'Expensive private transport options'.</li>
					<li>The 'Causes' are the reasons why the problem causes the effects. The aim is to write down as many clear and concise reasons in the roots of the tree. Following up on the same example, the root cause of 'Poor Public Transport' could probably be, 'Inadequate public funding' or 'Poor route planning'.</li>
					<li>The levels to which the 'Effects' and the 'Causes' can be unpacked will vary depending on the understanding the team has of the topic at hand. There is no pressure to be exhaustive - it is meant to start the planning process - not to complete the analysis.</li>
					<li>The Problem Tree provides a visual breakdown of problems into their symptoms as well as their causes, and furthermore create a visual output that can be understood by anyone.</li>
				</ul>
			</div>
			
			<div class="tool-card-image"></div>
			
			<img src="toolcard.png" alt="" />
			
			<div class="tool-limitations">
				<h2>Limitations</h2>
				
				<p>The Problem Tree does not give any indication of the magnitude or the importance of the causes of the problem or opportunity area. It may also be difficult to understand the effects and causes right from the beginning and may require a few iterations of this activity.</p>
			</div>
			
			<div class="f-how-to">
				<h2>How to for facilitators</h2>
				
				<ol>
					<li>At the start: Explain the activity to the participants, preferably using examples. Make sure they first write down the effects and then the causes.</li>
					<li>During the exercise: Ensure that the participants don't get stuck or fixate on a single train of thought.</li>
					<li>When summarising: Have participants share their root causes and talk through their process of getting to the root cause.</li>
				</ol>
			</div>
			
			<div class="f-question-bank">
				<h2>Facilitators Question Bank</h2>
				
				<ul>
					<li>What are the most immediate causes and effects you can think of as a group?</li>
					<li>Have we gone deep enough? Can we unpack this effect / cause further?</li>
					<li>Why does [cause] happen? Can we list those reasons as well as sub causes?</li>
					<li>What root causes have we identified? Are any of those surprising or unexpected?</li>
					<li>Since we have to use this as an input for planning research in the next phase, what are some themes (to be taken from effects or causes) that you feel we need to focus on understanding better during research?</li>
					<li>How should we prioritise between causes? Which ones do you think are the most important? Is there a cause that we are all excited about trying to solve?</li>
				</ul>
			</div>
		</div>
	</div>
</body>
</html>"""
    f.write(message)
    f.close()
