from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
spacy.load('en_core_web_sm')
# from spacy.lang.en import English
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chat = ChatBot('MRCET BOT')

#nlp = spacy.load("en_core_web_sm")

chat = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Hi there, Welcome to MRCET! 👋 If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br><br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'   
) 
trainer = ListTrainer(chat)

# python app.py
# Training with Personal Ques & Ans 
conversation = [
"Hi",
"Helloo!",
"Hey",

"How are you?",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Parents Section Enquiry. </br>3.&emsp;Visitor's Section Enquiry.</br>",

"Great",
"Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Parent's Section Enquiry. </br>3.&emsp;Visitor's Section Enquiry.</br>",

"good",
"Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Parent's Section Enquiry. </br>3.&emsp;Visitors Section Enquiry.</br>",

"fine",
"Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Parent's Section Enquiry. </br>3.&emsp;Visitors Section Enquiry.</br>",

"Thank You",
"Your Welcome 😄",

"Thanks",
"Your Welcome 😄",

"Bye",
"Thank You for visiting!..",

"What do you do?",
"I am made to give Information about MRCET college.",

"What else can you do?",
"I can help you know more about MRCET",
    
    "1",
    "<b>STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below : <br> <br> 1.1 Curriculars <br>1.3  Administrative<br>1.4 Examination <br>1.4 Placements </b>",

   
    "1.1",
    "<b>  CURRICULAR <br>  These are the top results:  <br> 1.1.2 Academic Calendar <br> 1.1.3 Syllabus </b>",
    "1.1.1",
    "<b > 1.1.1 Academic Calender<br>The link to Academic Calender👉<a href=" 'https://mrcet.com/AcademicCalendar.html' ">Click Here</a> </b>",
    "1.1.2",
    "<b> 1.1.2 Syllabus<br>The link to Syllabus 👉 <a href=" 'https://mrcet.com/Syllabus.html' ">Click Here</a> </b>",

    "1.2",
    "<b>EXTRA-CURRICULARS<br>These are the top results: <br>  1.2.1 Events<br> </b>",
    "1.2.1",
    "<b > 1.2.1 Events<br>The link to Events👉 <a href=" 'https://mrcet.com/ME_Events.html' ">Click Here</a></b>",

    "1.3",
    "<b>1.3 ADMINISTRATIVE<br>These are the top results: <br>  1.3.1 Students Portal<br> 1.3.2 Notices </b>",
    "1.3.1",
    "<b> 1.3.1 Students Portal<br>The link to Students Portal👉 <a href=" 'https://mrcet.com/studentpage.html' ">Click Here</a> </b>",
    "1.3.2",
    "<b> 1.3.2 Notices<br>The link to Notices👉 <a href=" '' ">Click Here</a> </b>",

     "1.4",
    "<b > PLACEMENTS These are the top results:<br> 1.5.1 Placements<br> 1.5.2 Our Recruiters <br> 1.5.3 Placement Statistics </b>",
    "1.4.1",
    "<b> 1.5.1 Placements<br>The link to Placements👉 <a href=" 'https://mrcet.com/Placements.html' ">Click Here</a> </b>",
    "1.4.2",
    "<b> 1.5.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'https://mrcet.com/Placements.html' ">Click Here</a> </b>",
    "1.4.3",
    "<b > 1.5.3 Placement Statistics<br>The link to Placement Statistics👉 <a href=" 'https://mrcet.com/Placements.html' ">Click Here</a> </b>",

    "2",
    "<b> PARENTS <br>The following are frequently searched terms related to Parents. Please select one from the options below :<pre>2.1 About Us <br>2.2  Notices <br> 2.3  Fee Payment </br> 2.4  Placements </b> " ,

    "2.1",
    "<b > ABOUT US<br>These are the top results:<br> 2.1.1 About MRCET<br> 2.1.2 Director's Address <br> 2.1.3 Principal's Address </b>",
    "2.1.1",
    "<b > .2.1.1 About MRCET👉<br>The link to About MRCET👉 <a href=" 'https://mrcet.com/Campus.html' ">Click Here</a> </b>",
    "2.1.2",
    "<b > 2.1.2 Director's Address <br>The link to Director's Address👉<a href=" 'https://mrcet.com/Governance.html' ">Click Here</a> </b>",
    "2.1.3",
    "<b > 2.1.3 Principal's Address <br>The link to Principal's Address👉 <a href=" 'https://mrcet.com/Principal.html' ">Click Here</a> </b>",

    "2.2",
    "<b > NOTICES<br>These are the top results:<br> 2.1.1 All Notices  </b>",
    "2.2.1",
    "<b > .2.2.1 All Notices <br>The link to All Notices👉 <a href=" 'https://mrcet.com/notices_circulars.html' ">Click Here</a> </b>",

    "2.3",
    "<b > ABOUT US<br>These are the top results:<br> 3.3.1 Payment Details <br> 3.3.2 Online Payment Portal </b>",
    "2.3.1",
    "<b > .2.3.1 Payment Details<br>The link to Payment Details 👉 <a href=" 'https://mrcet.com/timetableOnline%20Exam%20Fee%20Payment%20Procedure.pdf' ">Click Here</a> </b>",
    "2.3.2",
    "<b > 2.3.2 Payment Portal <br>The link to Payment Portal👉<a href=" 'https://mrcet.com/ExamBranch.html' ">Click Here</a> </b>",

    "2.4",
    "<b > PLACEMENTS These are the top results:<br> 3.4.1 Placements<br> 3.4.2 Our Recruiters <br> 3.4.3 Placement Statistics </b>",
    "2.4.1",
    "<b> 2.4.1 Placements<br>The link to Placements👉 <a href=" 'https://mrcet.com/Placements.html' ">Click Here</a> </b>",
    "2.4.2",
    "<b> 2.4.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'https://mrcet.com/Placements.html' ">Click Here</a> </b>",
    "2.4.3",
    "<b > 2.4.3 Placement Statistics<br>The link to Placement Statistics👉 <a href=" 'https://mrcet.com/Placements.html' ">Click Here</a> </b>",

    "3",
    "<b VISITORS <br>The following are frequently searched terms related to faculty. Please select one from the options below :<pre>3.1About Us </b>",
    
    "3.1",
    "<b > ABOUT US<br>These are the top results:<br> 3.1.1 About MRCET<br> 3.1.2 Director's Address <br> 3.1.3 Principal's Address </b>",
    "3.1.1",
    "<b > .3.1.1 About MRCET<br>The link to About MRCET👉 <a href=" 'https://mrcet.com/Campus.html' ">Click Here</a> </b>",
    "3.1.2",
    "<b > 3.1.2 Director's Address <br>The link to Director's Address👉<a href=" 'https://mrcet.com/Governance.html' ">Click Here</a> </b>",
    "3.1.3",
    "<b > 3.1.3 Principal's Address <br>The link to Principal's Address👉 <a href=" 'https://mrcet.com/Principal.html' ">Click Here</a> </b>",
  
]

trainer.train(conversation)
