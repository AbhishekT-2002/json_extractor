"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""
import subprocess

subprocess.run(["pip", "install", "google-generativeai"])
import google.generativeai as genai
import gradio as gr
article = """ ## How to Use

1. **Input:** Enter the job information in plain text in the input section.
2. **Submit:** Click the "Submit" button.
3. **Output:** View the generated JSON output in the result section.\n
**NOTE:** You can and should provide id: 0 or any other number that you want in the first message to the bot. Which avoids it to generate random numbers as id:\n
That's it! Explore the structured JSON output for the provided job information.

"""
genai.configure(api_key="AIzaSyA1tw6ss1qxwGjJomexhqtLjBEI7rhAutg")

# Set up the model
generation_config = {
  "temperature": 0.05,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["#Repost\n\nSDET Intern - Frontend At Cred - Bengaluru\n\nBatch: 2023, 2024, 2025\nNote : Apply ASAP ! \n\nKnow More: https://internfreak.co/jobs-and-internship-opportunities/sdet-intern-frontend-at-cred-bengaluru"]
  },
  {
    "role": "model",
    "parts": ["{\n    \"id\": 1,\n    \"title\": \"SDET Intern - Frontend\",\n    \"company\": \"Cred \",\n    \"location\": \"Bengaluru\",\n    \"pay\": \"NA\",\n    \"applyLink\": \"https://internfreak.co/jobs-and-internship-opportunities/sdet-intern-frontend-at-cred-bengaluru\",\n    \"logo\": \"NA\",\n    \"skills\": [],\n    \"description\": \"NA\",\n    \"postedDate\": \"NA\"\n}"]
  },
  {
    "role": "user",
    "parts": ["Backend Engineering Intern Hiring (New) At Fampay\n\nBatch: 2024, 2025\nExpected Salary : 1 Lakhs per month \n\nKnow More: https://internfreak.co/jobs-and-internship-opportunities/backend-engineering-intern-hiring-new-at-fampay"]
  },
  {
    "role": "model",
    "parts": ["{\n    \"id\": 2,\n    \"title\": \"Backend Engineering Intern\",\n    \"company\": \"Fampay\",\n    \"location\": \"NA\",\n    \"pay\": \"1 Lakhs per month\",\n    \"applyLink\": \"https://internfreak.co/jobs-and-internship-opportunities/backend-engineering-intern-hiring-new-at-fampay\",\n    \"logo\": \"NA\",\n    \"skills\": [],\n    \"description\": \"Batch: 2024, 2025\",\n    \"postedDate\": \"NA\"\n}"]
  },
  {
    "role": "user",
    "parts": ["GeeksforGeeks is hiring for SDE role\n\nBatch: 2022, 2023\nExpected Salary : 50,000 / month (as per Glassdoor) \n\nKnow More: https://internfreak.co/jobs-and-internship-opportunities/geeksforgeeks-is-hiring-for-sde-role"]
  },
  {
    "role": "model",
    "parts": ["{\n    \"id\": 11,\n    \"title\": \"SDE\",\n    \"company\": \"GeeksforGeeks\",\n    \"location\": \"NA\",\n    \"pay\": \"50,000 / month (as per Glassdoor)\",\n    \"applyLink\": \"https://internfreak.co/jobs-and-internship-opportunities/geeksforgeeks-is-hiring-for-sde-role\",\n    \"logo\": \"NA\",\n    \"skills\": [],\n    \"description\": \"Batch: 2022, 2023\",\n    \"postedDate\": \"NA\"\n}"]
  },
  {
    "role": "user",
    "parts": ["Walmart Global Tech India is hiring 2023 pass-outs!\n\nBatch: 2023\nNote : Please fill this form only if you meet all the criteria. \n\nKnow More: https://internfreak.co/jobs-and-internship-opportunities/walmart-global-tech-india-is-hiring-2023-pass-outs"]
  },
  {
    "role": "model",
    "parts": ["{\n    \"id\": 11,\n    \"title\": \"Hiring 2023 Pass-outs!\",\n    \"company\": \"Walmart Global Tech India\",\n    \"location\": \"NA\",\n    \"pay\": \"NA\",\n    \"applyLink\": \"https://internfreak.co/jobs-and-internship-opportunities/walmart-global-tech-india-is-hiring-2023-pass-outs\",\n    \"logo\": \"NA\",\n    \"skills\": [],\n    \"description\": \"Batch: 2023\",\n    \"postedDate\": \"NA\"\n}"]
  },
  {
    "role": "user",
    "parts": ["- Last day to go !\n\nSoftware Student Training in Engineering Program (STEP) Intern, 2024 At Google\n\nBatch: 2026, 2027\nStipend : 1.25 L per month \n\nKnow More: https://internfreak.co/jobs-and-internship-opportunities/software-student-training-in-engineering-program-step-intern-2024-at-google"]
  },
  {
    "role": "model",
    "parts": ["{\n    \"id\": 13,\n    \"title\": \"Software Student Training in Engineering Program (STEP) Intern, 2024\",\n    \"company\": \"Google\",\n    \"location\": \"NA\",\n    \"pay\": \"1.25 L per month\",\n    \"applyLink\": \"https://internfreak.co/jobs-and-internship-opportunities/software-student-training-in-engineering-program-step-intern-2024-at-google\",\n    \"logo\": \"NA\",\n    \"skills\": [],\n    \"description\": \"Batch: 2026, 2027\",\n    \"postedDate\": \"NA\"\n}"]
  },
  {
    "role": "user",
    "parts": ["#Expired\n\nFrontend Engineering Intern At Zuddl\n\nBatch: 2024, 2025, 2026\nExpected Stipend : 30-50k / Month \n\nKnow More: https://internfreak.co/jobs-and-internship-opportunities/frontend-engineering-intern-at-zuddl"]
  },
  {
    "role": "model",
    "parts": ["{\n    \"id\": 11,\n    \"title\": \"Frontend Engineering Intern\",\n    \"company\": \"Zuddl\",\n    \"location\": \"NA\",\n    \"pay\": \"30-50k / Month\",\n    \"applyLink\": \"https://internfreak.co/jobs-and-internship-opportunities/frontend-engineering-intern-at-zuddl\",\n    \"logo\": \"NA\",\n    \"skills\": [],\n    \"description\": \"Batch: 2024, 2025, 2026\",\n    \"postedDate\": \"NA\"\n}"]
  },
  {
    "role": "user",
    "parts": ["CERN openlab Summer Student Programme 2024\n\nBatch: 2024\nExpected Stipend : 3 Lakhs / Month \n\nKnow More: https://internfreak.co/jobs-and-internship-opportunities/cern-openlab-summer-student-programme-2024"]
  },
  {
    "role": "model",
    "parts": ["{\n    \"id\": 15,\n    \"title\": \"Summer Student Programme 2024\",\n    \"company\": \"CERN openlab\",\n    \"location\": \"NA\",\n    \"pay\": \"3 Lakhs / Month\",\n    \"applyLink\": \"https://internfreak.co/jobs-and-internship-opportunities/cern-openlab-summer-student-programme-2024\",\n    \"logo\": \"NA\",\n    \"skills\": [],\n    \"description\": \"Batch: 2024\",\n    \"postedDate\": \"NA\"\n}"]
  },
  {
    "role": "user",
    "parts": ["𝙅𝙋𝙈𝙊𝙍𝙂𝘼𝙉 𝘾𝙃𝘼𝙎𝙀 & 𝘾𝙊  𝐈𝐬 𝐇𝐢𝐫𝐢𝐧𝐠 𝐅𝐨𝐫 𝐅𝐫𝐞𝐬𝐡𝐞𝐫𝐬 \n𝐑𝐨𝐥𝐞  : Software Engineer - I\n𝐋𝐨𝐜𝐚𝐭𝐢𝐨𝐧  PAN INDIA: \n𝐄𝐱𝐩𝐞𝐜𝐭𝐞𝐝 𝐂𝐭𝐜: 14 LPA - 28 LPA\n𝐀𝐩𝐩𝐥𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐋𝐢𝐧𝐤 🖇️:\n https://cuvette.tech/app/other-jobs/65ae43b33c88479c35c11b7d?referralCode=8T994D\n\n𝐋𝐚𝐬𝐭 𝐃𝐚𝐭𝐞 : ASAP\n\nTech Community & Referrals Network\n-> https://t.me/addlist/KBNT2WWRIEs0NzIx\n\nAll the best 👍👍"]
  },
  {
    "role": "model",
    "parts": ["{\n    \"id\": 0,\n    \"title\": \"Software Engineer - I\",\n    \"company\": \"JP MORGAN CHASE & CO\",\n    \"location\": \"PAN INDIA\",\n    \"pay\": \"14 LPA - 28 LPA\",\n    \"applyLink\": \"https://cuvette.tech/app/other-jobs/65ae43b33c88479c35c11b7d?referralCode=8T994D\",\n    \"logo\": \"NA\",\n    \"skills\": [],\n    \"description\": \"Last Date : ASAP\",\n    \"postedDate\": \"NA\"\n}"]
  },
  {
    "role": "user",
    "parts": ["Role: Python Developer \nExpected CTC: 25 to 30 LPA \n🔗Apply here: https://www.quadeye.com/careers/?gh_jid=5795180002&gh_src=4eab9f2d2\nOOPs concept and flask and django is required\n\nTech Community & Referrals Network\n-> https://t.me/addlist/KBNT2WWRIEs0NzIx\nPosted on: 24/01/24\nLast Date: 1/02/2024\nAll the best 👍👍"]
  },
  {
    "role": "model",
    "parts": ["{\n    \"id\": 1,\n    \"title\": \"Python Developer\",\n    \"company\": \"Quadeye\",\n    \"location\": \"NA\",\n    \"pay\": \"25 to 30 LPA\",\n    \"applyLink\": \"https://www.quadeye.com/careers/?gh_jid=5795180002&gh_src=4eab9f2d2\",\n    \"logo\": \"NA\",\n    \"skills\": [\"OOPs concept\", \"flask\", \"django\"],\n    \"description\": \"OOPs concept and flask and django is required\",\n    \"postedDate\": \"24/01/24\",\n    \"lastDate\": \"1/02/2024\"\n}"]
  },
  {
    "role": "user",
    "parts": ["id: 1Harman is hiring!\nPosition: Associate Software Engineer\nQualifications: Bachelor’s/ Master’s Degree\nSalary: 5.8 LPA (Expected)\nExperience: Freshers\nLocation: Pune/ Bangalore\nskills like Fullstack, teamwork, communication, management is a must\n📌Apply Link: https://jobs.harman.com/en_US/careers/JobDetail?jobId=18328\n\nTech Community & Referrals Network\n-> https://t.me/addlist/KBNT2WWRIEs0NzIx\n\nAll the best 👍👍"]
  },
  {
    "role": "model",
    "parts": ["{\n    \"id\": 1,\n    \"title\": \"Associate Software Engineer\",\n    \"company\": \"Harman\",\n    \"location\": \"Pune/ Bangalore\",\n    \"pay\": \"5.8 LPA (Expected)\",\n    \"applyLink\": \"https://jobs.harman.com/en_US/careers/JobDetail?jobId=18328\",\n    \"logo\": \"NA\",\n    \"skills\": [\"Fullstack\", \"teamwork\", \"communication\", \"management\"],\n    \"description\": \"Bachelor’s/ Master’s Degree\",\n    \"postedDate\": \"NA\",\n    \"lastDate\": \"NA\"\n}"]
  },
  {
    "role": "user",
    "parts": ["id: 0Company Name : Fractal\n\nRole : Summer Internship\n\nBatch : 2025 passouts\nskills: excellent communication and AI/ML \nLink : https://fractal.wd1.myworkdayjobs.com/en-US/Careers/job/Mumbai/Summer-Project-Intern_SR-21908?q=Intern\nPosted ON: 30/12/2023\nLast Date: 15/01/2024"]
  },
  {
    "role": "model",
    "parts": ["{\n    \"id\": 0,\n    \"title\": \"Summer Internship\",\n    \"company\": \"Fractal\",\n    \"location\": \"NA\",\n    \"pay\": \"NA\",\n    \"applyLink\": \"https://fractal.wd1.myworkdayjobs.com/en-US/Careers/job/Mumbai/Summer-Project-Intern_SR-21908?q=Intern\",\n    \"logo\": \"NA\",\n    \"skills\": [\"excellent communication\", \"AI/ML\"],\n    \"description\": \"Batch : 2025 passouts\",\n    \"postedDate\": \"30/12/2023\",\n    \"lastDate\": \"15/01/2024\"\n}"]
  },
])

convo.send_message("""Company Name: Headout
Role: Software Engineer Internship
Batch eligible: 2024 and 2025 passouts
Location: Bangalore, Karnataka

Join my Telegram & Whatsapp Groups for Quick instant Jobs and Internships Updates

FOR LATEST JOB, JOIN- https://whatsapp.com/channel/0029VaBHo3d7YSd6Kf29B12v

FOR NOTES And PDFs, JOIN- 
https://telegram.me/codewithimanshu

https://t.me/codewithimanshu_notes

Share with your College Whatsapp Groups & Friends too

Apply Link : https://boards.greenhouse.io/headoutreferrals/jobs/4318904006""")


# print(convo.last.text)


def json_chat(user_input):
    convo.send_message(user_input)
    return convo.last.text

#Gradio Interface
demo = gr.Interface(json_chat, 
                    inputs="textbox", outputs="textbox", title="JSON Job Extractor", article= article)
demo.launch(share=True)