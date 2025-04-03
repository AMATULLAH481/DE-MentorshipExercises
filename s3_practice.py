import requests
import boto3
import awswrangler as wr
import pandas as pd
from dotenv import load_dotenv
import os 

load_dotenv(dotenv_path=r"C:\Users\HP\.vscode\Jupyter Notebook files\.env")


API_KEY= os.getenv("API_key")
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

#API_1
url = "http://api.football-data.org/v4/competitions/"
response = requests.get(url)
football_data = response.json()
football_data = football_data["competitions"]
df = pd.DataFrame(football_data)

# upload the football data file to S3 in parquet format
wr.s3.to_parquet(
    df=df,
    path= "s3://amatullah-mahmud-bucket/football-API-data-folder/football_api_data.parquet"
)


# API_2
url = "https://randomuser.me/api/?results=500"
response = requests.get(url)
response.status_code
user_details_data = response.json()
#list collecting our data
female_details = []
male_details = []
date_of_birth = []
first_name = []
last_name = []
full_names = []
user_details_data

for user_details in user_details_data["results"]:
    if user_details["gender"] == "female":
        female_details.append(user_details)
    elif user_details["gender"] == "male":
        male_details.append(user_details)

#convert the female_data list to dataframe
df = pd.DataFrame(female_details)
df = df[["gender", "name", "email"]] #get specific data to be uploaded to the folder

#upload to s3
wr.s3.to_parquet(
    df= df,
    path= "s3://amatullah-mahmud-bucket/random-user-details-folder/female_details.parquet"
)

#convert the male_data list to dataframe
df = pd.DataFrame(male_details)
df = df[['gender', 'name', 'email']]
df

#upload to s3
wr.s3.to_parquet(
    df=df,
    path= "s3://amatullah-mahmud-bucket/random-user-details-folder/male_details.parquet"
)

for user_details in user_details_data["results"]:
    date_of_birth.append(user_details["dob"]["date"])

df_birthdate= pd.DataFrame(date_of_birth)
df_birthdate.rename(columns={0: 'date_of_birth'}, inplace=True) 

wr.s3.to_parquet(
    df = df_birthdate,
    path = "s3://amatullah-mahmud-bucket/random-user-details-folder/birthdate_details.parquet"
)

for user_details in user_details_data["results"]:
    first_name.append(user_details["name"]["first"])
    last_name.append(user_details["name"]["last"])

df_firstname = pd.DataFrame(first_name)
df_firstname.rename(columns={0: 'firstname'}, inplace=True)

wr.s3.to_parquet(
    df= df_firstname,
    path = "s3://amatullah-mahmud-bucket/random-user-details-folder/first_name.parquet"
)

df_lastname = pd.DataFrame(last_name)
df_lastname.rename(columns={0: 'lastname'}, inplace=True)


wr.s3.to_parquet(
    df = df_lastname,
    path = "s3://amatullah-mahmud-bucket/random-user-details-folder/last_names.parquet"
)

for user_details in user_details_data["results"]:
    full_name = f"{user_details['name']['first']} {user_details['name']['last']}"
    full_names.append(full_name)

df_fullnames = pd.DataFrame(full_names, columns=["full_names"])
df_fullnames

wr.s3.to_parquet(
    df = df_fullnames,
    path = "s3://amatullah-mahmud-bucket/random-user-details-folder/fullnames.parquet"
)

response = {'apiVersion': '2.0',
 'documentationUrl': 'https://jobi.cy/apidocs',
 'friendlyNotice': "We appreciate your use of Jobicy API in your projects! Please note that our API access is designed primarily to facilitate broader distribution of our content. We kindly request that you refrain from distributing Jobicy's job listings to any external job platforms, such as Jooble, Google Jobs, and LinkedIn, among others. To ensure that Jobicy is credited as the original source across various platforms, content in the feeds is published with a slight delay. As our data doesn't change frequently, accessing the Feed a few times daily is sufficient and recommended. Be advised that excessive querying may lead to restricted access. Thank you for understanding and cooperating!",
 'jobCount': 6,
 'xRayHash': 'ac90d4ab958aa0925987872dc4abcd52',
 'clientKey': 'a379b5aa59c89858cc4ca2e05041d6ad1ab5d118619785bd3dae12c15ca056f6',
 'lastUpdate': '2025-03-19 05:28:46',
 'jobs': [{'id': 111598,
   'url': 'https://jobicy.com/jobs/111598-growth-manager-3',
   'jobSlug': '111598-growth-manager-3',
   'jobTitle': 'Growth Manager',
   'companyName': 'Awesome Motive',
   'companyLogo': 'https://jobicy.com/data/server-nyc0409/galaxy/mercury/2022/01/b8e354b088bd65fd9f299af4f4bc1706.jpeg',
   'jobIndustry': ['Marketing &amp; Sales'],
   'jobType': ['full-time'],
   'jobGeo': 'Anywhere',
   'jobLevel': 'Any',
   'jobExcerpt': 'We are Awesome Motive, the company behind popular web apps and business tools like All in One SEO (AIOSEO), OptinMonster, MonsterInsights, WPForms, and many others. Over 25 million websites use our tools to get more traffic, subscribers, and sales. We&amp;#8217;re passionate about helping Small Businesses Grow &amp;amp; Compete with the Big Guys, and we believe&amp;#8230;',
   'jobDescription': '<p>We are Awesome Motive, the company behind popular web apps and business tools like All in One SEO (AIOSEO), OptinMonster, MonsterInsights, WPForms, and many others. Over 25 million websites use our tools to get more traffic, subscribers, and sales. We&#8217;re passionate about helping Small Businesses Grow &amp; Compete with the Big Guys, and we believe marketing plays a crucial role in delivering on that promise.</p>\n<p>This is your chance to join a dynamic team and lead strategic initiatives across marketing channels to acquire, engage, and retain users. You&#8217;ll wear many hats – strategist, analyst, campaign champion – all aimed at one goal: accelerating our growth to reach more small businesses.</p>\n<h2>To love this role, here’s the type of person you are</h2>\n<ul>\n<li>You can leverage imperfect data to create and execute winning digital marketing campaigns and funnels.</li>\n<li>You’re extremely self-driven and curious to find creative answers to complex questions.</li>\n<li>You’re comfortable seeing the big picture and how the small details get you there.</li>\n<li>You love to create systems, tools, and processes for others where they don’t already exist.</li>\n<li>You have a passion for digital marketing and customer acquisition.</li>\n</ul>\n<h2>Common responsibilities include (but are not limited to)</h2>\n<ul>\n<li>Utilize Content Marketing, Email and SMS Marketing, Pay Per Click, Sponsorships, Affiliates and Partnerships, Social Media, and Freemium Software to grow new sales.</li>\n<li>Strategize, plan, and implement both long and short-term processes to meet targets, emphasizing priorities in process development and documentation.</li>\n<li>Facilitate data-driven decision-making by collecting, analyzing, interpreting, and visualizing data, providing actionable insights, and promoting data literacy within the organization.</li>\n<li>Directly manage a team of growth professionals, including independently making decisions to ensure team performance &amp; cohesion.</li>\n<li>Design and implement website A/B tests to improve conversion rates and funnel performance.</li>\n<li>Conceptualize and build new targeted landing pages for various channels and users.</li>\n<li>Provide conversion-focused copywriting feedback and suggestions for newsletters, customer-facing websites, our apps and plugins, and ad copy.</li>\n<li>Strategize and execute high-visibility promotions across all digital marketing channels.</li>\n<li>Research competitor&#8217;s UI/UX trends and work with the team to articulate new features/ideas to help us remain competitive.</li>\n<li>Control qualified traffic to our website by designing and executing strategies to improve our search engine rankings.</li>\n<li>Develop and execute an outbound marketing strategy to complement our existing inbound strengths.</li>\n<li>Maintain in-depth familiarity with growth-related procedures and workflows.</li>\n<li>Respond promptly to growth team members&#8217; queries and escalations.</li>\n<li>Uphold and promote the core values of Awesome Motive.</li>\n<li>Conduct research before escalating issues and proactively identify trends and process improvements.</li>\n<li>Provide oversight for PPC campaigns, PPC keyword research, and program ROAS.</li>\n<li>Provide oversight for Affiliate Marketing and Partnerships.</li>\n<li>Directly supervise the work of content marketing team members.</li>\n<li>Assist in crafting better internal processes and systems by documenting the work of the Growth team.</li>\n</ul>\n<h2>Requirements</h2>\n<ul>\n<li>Relevant experience:\xa0 With over 4 years of experience in growth marketing for product-led/ freemium SaaS, ideally in the B2B/SMB space, you have achieved direct business growth impact through successful growth initiatives.</li>\n<li>SEO &amp; Content Marketing: You are well-versed in best practices for SEO in marketing site content, including blog posts. You are fluent in other commonly used tools such as Semrush, Clearscope, and Ahrefs.</li>\n<li>Copywriting: You have strong personal experience with copywriting, as well as leading and reviewing the work of copywriters. Your expertise in hiring and managing copywriters will be invaluable.</li>\n<li>Email Marketing: You can demonstrate and teach best practices within email marketing, from crafting individual emails to creating complete targeted campaigns and evaluating effectiveness to drive improvement over time. You must have personally written and iterated upon multiple email campaigns for SaaS products.</li>\n<li>CRO / Funnels / Testing &amp; Optimization: You must have expertise in best practices for SaaS products. Knowledge and experience in pricing page tests, countdown timers, popups, etc, is required.</li>\n<li>PPC / Paid Advertising: You have experience in Google Ads, Facebook Ads, and Google Search Console for PPC</li>\n<li>Affiliates &amp; Partnerships: You know how to build and maintain partnership relationships. You have managed an affiliate program.</li>\n<li>Data &amp; Analytics: You are experienced in using GA (preferably GA4), and digital marketing channels.</li>\n</ul>\n<p><strong>Bonus points if you also have:</strong></p>\n<ul>\n<li>You have experience working in the admin area of self-hosted WordPress sites as a site owner/developer/etc.</li>\n<li>You have experience with support specifically for WordPress.</li>\n<li>You have trained managers and had managers as direct reports.</li>\n</ul>\n<h2>Benefits</h2>\n<p>Working for a fast-growing bootstrapped company is a rare opportunity, one we consider a lifestyle choice rather than a job choice. Our positions are challenging, but also come with amazing advantages and fulfillment to those who earn them. Here’s what we offer.</p>\n<ul>\n<li>Competitive Salary.</li>\n<li>Term Life Insurance and Accidental Death &amp; Dismemberment for all full-time team members during their employment.</li>\n<li>Health, Dental, and Vision Insurance benefits for full-time U.S. employees.</li>\n<li>Health Insurance benefits for all employees in India, Pakistan, Brazil, Philippines, Ukraine, Poland, Romania, Nepal, Kenya, Mexico, Nigeria, Spain &amp; Jamaica.</li>\n<li>Work from your home. We’re spread out all over the world – United States, Canada, Ukraine, India, Pakistan, Singapore, and more.</li>\n<li>Flexible PTO after 90 days of employment. We encourage employees to take the time they need for a vacation, stay healthy, and spend time with friends and family.</li>\n<li>Holidays (based on your location).</li>\n<li>Paid maternity and paternity leave.</li>\n<li>We happily provide or reimburse software you’ll need as well as books or courses that promote continued learning.</li>\n<li>We cover all costs of company travel (including our annual all-company retreat and mini-team meetups).</li>\n<li>Additional Perks include AM Welcome Box for new team members, Yearly Anniversary Gifts, and Technology Stipend each work anniversary.</li>\n<li>We give you the opportunity to solve challenging and meaningful problems that make a difference.</li>\n<li>Ability to work with some of the best people in the business through frequent, if not daily, interactions.</li>\n<li>And in case you were wondering: no politics, no b.s., and no jerks.</li>\n</ul>\n<p><strong>Location\xa0</strong>This is a remote position &#8211; our team is spread around the globe! Our home base is in Florida, USA, so company operating hours are 9am &#8211; 5pm ET (UTC -5). While full coverage is not a requirement, you must be available for a portion of the day.</p>\n<p><strong>Inclusion Statement\xa0</strong>At Awesome Motive, we strive to have the broadest possible view of diversity, going beyond visible differences to include the background, experiences, skills, and perspectives that make each person unique. Awesome Motive is proud to be an equal opportunity workplace and is committed to equal employment opportunity regardless of race, color, ancestry, religion, sex, national origin, sexual orientation, age, citizenship, marital status, disability, gender identity, veteran status, or any other basis protected by federal, state, or local law.</p>\n<p><strong>How to apply?\xa0</strong>If all of this sounds interesting, then please submit your application!</p>\n<p><strong>Please clearly include the following in your cover letter:</strong></p>\n<ul>\n<li>Do you have experience in creating revenue impact through marketing?</li>\n<li>Do you have experience in directly managing teams?</li>\n<li>Do you have a minimum of 3 years of experience in SaaS marketing?</li>\n<li>What is your proficiency level (from 1 to 5, 5 highest) in programmatic SEO? Share an example of the impact created.</li>\n<li>What is your proficiency in GA4?</li>\n</ul>',
   'pubDate': '2025-03-19 05:15:32'},
  {'id': 116374,
   'url': 'https://jobicy.com/jobs/116374-senior-content-marketing-manager-2',
   'jobSlug': '116374-senior-content-marketing-manager-2',
   'jobTitle': 'Senior Content Marketing Manager',
   'companyName': 'Postman',
   'companyLogo': 'https://jobicy.com/data/server-nyc0409/galaxy/mercury/2022/01/6f061e1cad5e2783cea0b2976ed2f4c3.png',
   'jobIndustry': ['Content &amp; Editorial', 'Marketing &amp; Sales'],
   'jobType': ['full-time'],
   'jobGeo': 'USA',
   'jobLevel': 'Senior',
   'jobExcerpt': 'We’re seeking a creative strategist who’s versed in every aspect of a content marketing ecosystem and obsessed with driving growth through data-driven storytelling. As the Sr. Content Marketing Manager at Postman, you’ll sit at the heart of our customer journey, ensuring our content finds and resonates with developers worldwide. The ideal candidate is no stranger&amp;#8230;',
   'jobDescription': '<p>We’re seeking a creative strategist who’s versed in every aspect of a content marketing ecosystem and obsessed with driving growth through data-driven storytelling. As the Sr. Content Marketing Manager at Postman, you’ll sit at the heart of our customer journey, ensuring our content finds and resonates with developers worldwide. The ideal candidate is no stranger to building quickly in ambiguous environments, has scaled content marketing programs at companies of various stages and has a proven track record of both leading and executing against ambitious strategies.</p>\n<p>The Sr. Content Marketing Manager is a key cross-functional player, leading and executing various content initiatives in line with business and GTM goals. You should feel at ease driving projects that range from SEO, to email marketing, blog and long form editorial, thought leadership, influencer marketing and more. You’ll help lead innovative thinking for how to find, engage and move audiences across all of our channels, making sure that we’re maximizing business impact across the funnel. This is an opportunity to help shape and improve the customer journey and the ideal candidate has a comprehensive and strategic view on how content can help achieve that.</p>\n<h2><strong>What You&#8217;ll Do</strong></h2>\n<ul>\n<li>Work in tandem with the Head of Content and cross-functional teams to prioritize and service a pipeline of content initiatives that fuel business and GTM goals</li>\n<li>Lead the charge on shaping and implementing multi-channel content strategies that touch everything from\xa0SEO to email, blog, thought leadership, social, influencer, web, community and more</li>\n<li>Manage the entire content lifecycle, from ideation and creation to approvals and distribution across various channels</li>\n<li>Work with channel owners across the entire ecosystem to shape and iterate creative strategy to drive results for owned initiatives</li>\n<li>Continuously analyze and optimize content performance metrics, leveraging data-driven insights to refine and evolve the content strategy for maximum impact</li>\n<li>Stay deeply immersed in industry trends, emerging technologies, and best practices in the developer and API universe to ensure that Postman’s content remains relevant and valuable to our target audience</li>\n</ul>\n<h2><strong>About You</strong></h2>\n<ul>\n<li>5+ years of experience building and servicing content strategies across a variety of channels: SEO, email, social, web, webinars, case studies, etc.</li>\n<li>A hyper strategic and analytical mindset for content creation and distribution</li>\n<li>Solid creative chops: you don’t need to be an expert in everything, but you need to have a demonstrated record of creative excellence as an IC</li>\n<li>An ability to move quickly but remain focused and prioritize ruthlessly</li>\n<li>Expert-level cross-functional collaboration</li>\n</ul>\n<p>This is a remote role based in the United States &amp; the reasonably estimated salary for this role ranges from $150,000 to $190,000, plus a competitive equity package. Actual compensation is based on the candidate&#8217;s skills, qualifications, and experience.</p>\n<h2><strong>What Else?</strong></h2>\n<p>In addition to Postman&#8217;s pay-on-performance philosophy, and a flexible schedule working with a fun, collaborative team, Postman offers a comprehensive set of benefits, including full medical coverage, flexible PTO, wellness reimbursement, and a monthly lunch stipend. Along with that, our wellness programs will help you stay in the best of your physical and mental health. If you have little ones in your family, the creche allowance can help in supporting your work-life balance. Our frequent and fascinating team-building events will keep you connected, while our donation-matching program can support the causes you care about. We’re building a long-term company with an inclusive culture where everyone can be the best version of themselves.</p>\n<p>At Postman, we embrace a hybrid work model. For all roles based out of San Francisco Bay Area, Boston, Bangalore, Noida, Hyderabad, and New York, employees are expected to come into the office 3-days a week. We were thoughtful in our approach which is based on balancing flexibility and collaboration and grounded in feedback from our workforce, leadership team, and peers. The benefits of our hybrid office model will be shared knowledge, brainstorming sessions, communication, and building trust in-person that cannot be replicated via zoom.</p>\n<h2><strong>Our Values</strong></h2>\n<p>At Postman, we create with the same curiosity that we see in our users. We value transparency and honest communication about not only successes, but also failures. In our work, we focus on specific goals that add up to a larger vision. Our inclusive work culture ensures that everyone is valued equally as important pieces of our final product. We are dedicated to delivering the best products we can.</p>\n<h2><strong>Equal opportunity</strong></h2>\n<p>Postman is an Equal Employment Opportunity and Affirmative Action Employer. Qualified applicants will receive consideration for employment without regard to race, color, religion, sex, sexual orientation, gender perception or identity, national origin, age, marital status, protected veteran status, or disability status. Headhunters and recruitment agencies may not submit resumes/CVs through this website or directly to managers. Postman does not accept unsolicited headhunter and agency resumes. Postman will not pay fees to any third-party agency or company that does not have a signed agreement with Postman.</p>',
   'pubDate': '2025-03-18 16:13:07'},
  {'id': 116301,
   'url': 'https://jobicy.com/jobs/116301-senior-digital-acquisition-strategist',
   'jobSlug': '116301-senior-digital-acquisition-strategist',
   'jobTitle': 'Senior Digital Acquisition Strategist',
   'companyName': 'ServiceNow',
   'companyLogo': 'https://jobicy.com/data/server-nyc0409/galaxy/mercury/2021/11/3f9f6951a15d7f9fff1e42f86a01430e.png',
   'jobIndustry': ['Marketing &amp; Sales'],
   'jobType': ['full-time'],
   'jobGeo': 'Canada,  USA',
   'jobLevel': 'Senior',
   'jobExcerpt': 'We are seeking a dynamic Senior Digital Acquisition Strategist to join our global digital marketing team.\xa0 This pivotal person will drive the global end-to-end digital marketing strategy and execution for our highest priority programs, creating effective persona-based user journeys and an exceptional digital experience. As a Senior Digital Acquisition Strategist, you will play a critical&amp;#8230;',
   'jobDescription': '<p>We are seeking a dynamic Senior Digital Acquisition Strategist to join our global digital marketing team.\xa0 This pivotal person will drive the global end-to-end digital marketing strategy and execution for our highest priority programs, creating effective persona-based user journeys and an exceptional digital experience.</p>\n<p>As a Senior Digital Acquisition Strategist, you will play a critical role in connecting the dots across teams, synthesizing global perspectives, and leading execution for key B2B persona programs. This role is instrumental in managing the strategic planning, execution, and reporting across all digital marketing channels and ensuring a unified site and content experience. The digital marketing strategist will act in a product manager capacity for their dedicated program focus – responsible for the plan that spans across all owned and paid digital channels and connects to the overall integrated marketing program and content strategy. They will also focus on identifying our strengths and weaknesses, evaluating operational effectiveness, and uncovering opportunities for improvement.</p>\n<p>The ideal candidate possesses extensive experience in digital planning and strategy, adept stakeholder management skills, and proficiency in media execution.\xa0 We are seeking a passionate individual who embodies the qualities of a strategic thinker and a hands-on implementer. A proven track record of pushing the boundaries to drive innovation that generates positive business impact is highly desirable. Additionally, candidates should be well-versed in media and digital experience, with familiarity in at least two or more areas within the digital advertising landscape (display programmatic, SEM, SEO, paid social, analytics and attribution).</p>\n<h2>Key Responsibilities:</h2>\n<ul>\n<li>Strategic Planning &amp; Execution</li>\n<li>Partner with the Integrated Marketing Program Director and Content Strategy lead to translate into a highly-effective digital strategy that interlinks with regional digital planning and execution teams to drive marketing outcomes</li>\n<li>Leverage experience with persona development, buying groups, customer journeys, and the CXO audience to tailor strategies that resonate with key target audiences.</li>\n<li>Define and champion a unified digital experience vision, ensuring all program and campaign touchpoints are engaging, consistent, and customer centric.</li>\n<li>Leverage data and user journey mapping to refine digital ecosystems, ensuring continuous improvement in engagement and conversion.</li>\n<li>Adeptly manage adjustments in program scopes and schedules and spearhead the evaluation of their impacts on broader strategic initiatives.</li>\n<li>Provide thought leadership on platform selection, media mix optimization, and creative approaches to boost campaign performance.</li>\n<li>End-to-End Digital Campaign Management</li>\n<li>Drive the strategy for integrated full funnel digital user journeys for the best-in-class execution from campaigns to website experience in service of the overall program’s strategy and objectives.</li>\n<li>Consult with respective channel leads, events partners, and regional liaisons on the paid, owned and earned channel strategy.</li>\n<li>Own the end-to-end paid and organic digital marketing strategy outcomes across Paid Social, Content Syndication, Programmatic, Video, Email, SEO, SEM etc.</li>\n<li>Oversee campaign planning, execution, optimization, and reporting, ensuring alignment between digital strategy and business objectives.</li>\n<li>Partner with regional planners and Ad Ops to implement best practices, drive continuous optimization, and ensure unified tracking across regions.</li>\n<li>Reporting &amp; Stakeholder Management</li>\n<li>Maintain continuous alignment with key stakeholders, including integrated marketing, digital marketing teams, product marketing, field marketing, brand marketing, and operations, through proactive and effective communication.</li>\n<li>Oversee the integration and connectivity of various digital marketing campaigns, ensuring data consistency and accuracy across platforms. Develop and maintain robust reporting frameworks to track campaign performance and provide actionable insights.</li>\n<li>Assess organizational performance and implement processes to enhance effectiveness. Develop plans to improve overall operational efficiency and optimization.</li>\n<li>Develop and deliver regular health check-ins, monthly summaries, and QBRs for marketing stakeholders.</li>\n</ul>\n<h2>Qualifications</h2>\n<p>Core Requirements</p>\n<ul>\n<li>Experience in leveraging or critically thinking about how to integrate AI into work processes, decision-making, or problem-solving. This may include using AI-powered tools, automating workflows, analyzing AI-driven insights, or exploring AI’s potential impact on the function or industry.</li>\n<li>8+ years in strategic B2B digital marketing campaign management and program management</li>\n<li>Experience with digital media platforms across Paid Social, Content Syndication, Programmatic, Video, Email, SEM etc.</li>\n<li>Track record running large scale, full funnel integrated digital advertising campaigns.</li>\n<li>Experience with landing page optimizations for paid campaigns as part of the overall end to end digital user journey, with basic understanding of UX elements and experience that impacts users from different channels.</li>\n<li>Previous management of complex client/stakeholder relationships.</li>\n<li>Experience in analyzing multi-platform data insights across web analytics suites such as Google Analytics or Adobe Analytics</li>\n<li>Strong critical thinking and analytical skills, self-starter, curious</li>\n<li>Outstanding interpersonal skills and relationship builder, as this role requires ability to connect with other partners across the organization to ensure omnichannel planning</li>\n<li>Detail-oriented with strong organizational and project management skills</li>\n</ul>\n<p>Preferred Qualifications</p>\n<ul>\n<li>A/B Testing experience</li>\n<li>Preferred experience with web experience, website journeys and SEO.</li>\n<li>Familiarity with Google Campaign Manager, DV360, SA360, LinkedIn Campaign Manager, The Trade Desk, Adobe Analytics, Tableau or similar ad tech and BI tools is a plus.</li>\n<li>Curiosity for AI &amp; Innovation: We’re looking for candidates who are excited about AI and love experimenting with new ideas and tools. A passion for learning and innovation is a must!</li>\n</ul>\n<p><em>Not sure if you meet every qualification? We still encourage you to apply! We value inclusivity, welcoming candidates from diverse backgrounds, including non-traditional paths. Unique experiences enrich our team, and the willingness to dream big makes you an exceptional candidate!</em></p>\n<h2>Additional Information</h2>\n<p><strong>Work Personas</strong></p>\n<p>We approach our distributed world of work with flexibility and trust. Work personas (flexible, remote, or required in office) are categories that are assigned to ServiceNow employees depending on the nature of their work.</p>\n<p><strong>Equal Opportunity Employer</strong></p>\n<p>ServiceNow is an equal opportunity employer. All qualified applicants will receive consideration for employment without regard to race, color, creed, religion, sex, sexual orientation, national origin or nationality, ancestry, age, disability, gender identity or expression, marital status, veteran status, or any other category protected by law. In addition, all qualified applicants with arrest or conviction records will be considered for employment in accordance with legal requirements.</p>',
   'pubDate': '2025-03-15 02:39:37'},
  {'id': 116055,
   'url': 'https://jobicy.com/jobs/116055-marketing-assistant',
   'jobSlug': '116055-marketing-assistant',
   'jobTitle': 'Marketing Assistant',
   'companyName': 'Scorpion',
   'companyLogo': 'https://jobicy.com/data/server-nyc0409/galaxy/mercury/2021/11/5d0f5219d1a5557d70758202f92e0076.png',
   'jobIndustry': ['Marketing &amp; Sales'],
   'jobType': ['full-time'],
   'jobGeo': 'USA',
   'jobLevel': 'Any',
   'jobExcerpt': 'Scorpion is the leading provider of technology and services helping local businesses thrive. We do this by helping customers understand local market dynamics, make the most of their marketing, and deliver experiences their customers will love. We offer tools to know what’s going on with marketing, competitors, and customers. We offer a unique blend of&amp;#8230;',
   'jobDescription': '<p>Scorpion is the leading provider of technology and services helping local businesses thrive. We do this by helping customers understand local market dynamics, make the most of their marketing, and deliver experiences their customers will love. We offer tools to know what’s going on with marketing, competitors, and customers. We offer a unique blend of AI support and teams of real human people with local expertise committed to customer success. At Scorpion, we are ready to do whatever it takes to help our clients reach their goals. Our technology and personalized tools bring everything together to help local businesses easily understand their unique business, market, and customer needs. We put SEO, Reviews, Advertising, Email Marketing, Chat and Messaging, Social Media, Website, Lead Management, Appointment Scheduling, and more to work for local businesses. We’re a technology-led service with a human touch.</p>\n<h2>About the Role</h2>\n<p>We’re looking for a detail-oriented and motivated individual to join our team as a Marketing Assistant. No prior experience in digital marketing is required—just a strong willingness to learn and an interest in marketing.</p>\n<p>In this role, you’ll receive structured training and hands-on experience in digital advertising. You’ll work closely with account managers to support client digital campaign execution and ensuring seamless coordination across teams.</p>\n<h2>What your success will look like</h2>\n<ul>\n<li>Manage and track all campaign requests and project updates for internal teams, clients, and agency partners.</li>\n<li>Organize and oversee creative assets, ensuring they are properly stored and accessible.</li>\n<li>Communicate updates on upcoming campaigns, assets, and landing pages across teams, clarifying outstanding questions or issues.</li>\n<li>Monitor and track new landing page requests, ensuring quality and timely delivery.</li>\n<li>Support project coordination and tracking, helping the team stay organized and on schedule.</li>\n<li>Participate in weekly client calls, providing clear and concise campaign launch updates.</li>\n<li>Join status meetings with agency partners to align on project progress and priorities.</li>\n</ul>\n<h2>Who you are and what you bring</h2>\n<ul>\n<li>Education: Bachelor&#8217;s degree in Marketing, Advertising, Business, Communications, or a related field—or equivalent practical experience.</li>\n<li>Experience: 0-1 year, including internships. Great for recent graduates or early-career professionals.</li>\n<li>Skills:\n<ul>\n<li>Exposure to digital marketing through coursework or experience in SEO, SEM, or social media.</li>\n<li>Familiarity with content management systems (CMS) and customer support platforms (CS).</li>\n<li>Strong communication skills, with the ability to engage professionally with internal teams and external partners.</li>\n<li>Highly organized and detail-oriented, with a proactive approach to tracking projects and meeting deadlines.</li>\n</ul>\n</li>\n</ul>\n<h2>Our Scorpion Values</h2>\n<p><strong>Winning Mindset:</strong> \xa0When our clients win, we win.<br />\n<strong>Genuine Care: </strong>\xa0We only succeed when we are truly invested in our clients and each other.<br />\n<strong>Unmatched Results:</strong> \xa0We deliver more than expected–and then some–driving the best results and impacting lives.<br />\n<strong>Constant Improvement: </strong>\xa0We believe there is always a better way. We learn we ask “What if?” we build and then do it again.<br />\n<strong>Unbeatable Teamwork:</strong> \xa0We come from different backgrounds but have the same vision. We only get there by doing it together, as a team.</p>\n<h2>Our Benefits</h2>\n<p>We invest in our employees by offering them diverse benefits from best-in-class carriers. These benefits provide enough choice and flexibility to keep our employees and their families healthy and happy—today and tomorrow.</p>\n<ul>\n<li>100% employer-paid medical, dental, and vision insurance</li>\n<li>Flexible paid time off, so you can rest, relax, and recharge away from work</li>\n<li>Employee equity program</li>\n<li>Paid parental leave</li>\n<li>Paid cell phone and service</li>\n<li>Remote office allowance</li>\n<li>Professional development and development courses</li>\n<li>Regular manager check-ins to drive performance and career growth through Lattice</li>\n</ul>\n<h2>Compensation</h2>\n<p>We acknowledge that states have passed legislation promoting pay transparency. As a national employer, Scorpion has made the decision to post our expected pay rate or pay range (as applicable) in all our job postings, regardless of geographic location.</p>\n<ul>\n<li>The base salary range is $52,000 (entry-level) &#8211; $60,000 (highly experienced), exclusive of fringe benefits. If you are hired at Scorpion, your final base salary compensation will be determined based on factors such as geographic location, skills, education, and/or experience. Additionally, we believe in the importance of pay equity and consider the internal equity of our current team members as a part of any final offer. Please keep in mind that the range mentioned above is the total salary range for the role. Hiring at the maximum of the range would not be typical in order to allow for future &amp; continued salary growth. The compensation package may also include incentive compensation opportunities in the form of discretionary bonuses or commissions.</li>\n<li>The compensation package may also include incentive compensation opportunities in the form of discretionary bonuses or commissions.</li>\n</ul>\n<p>Scorpion is an equal opportunity employer and considers applicants for all positions without regard to race, color, religion or belief, sex, age, national origin, citizenship status, marital status, military/veteran status, genetic information, sexual orientation, gender identity, or physical or mental disability. We believe in creating a dynamic work environment that values diversity and inclusion.</p>\n<p>Scorpion\u202fparticipates\u202fin the E-Verify program to confirm employment authorization of all newly hired employees.\xa0The\xa0E-Verify process is completed during new hire onboarding and completion of the Form I-9, Employment Eligibility Verification, at the start of employment.\xa0E-Verify is not used as a tool to pre-screen candidates.\u202fFor more information on E-Verify, please visit\xa0www.uscis.gov.</p>',
   'pubDate': '2025-03-05 19:21:30',
   'annualSalaryMin': 52000,
   'annualSalaryMax': 60000,
   'salaryCurrency': 'USD'},
  {'id': 111984,
   'url': 'https://jobicy.com/jobs/111984-manager-digital-marketing',
   'jobSlug': '111984-manager-digital-marketing',
   'jobTitle': 'Manager, Digital Marketing',
   'companyName': 'CrossFit',
   'companyLogo': 'https://jobicy.com/data/server-nyc0409/galaxy/mercury/2021/12/6966c9ea04a0e651f69f113113a45e27.png',
   'jobIndustry': ['Marketing &amp; Sales'],
   'jobType': ['full-time'],
   'jobGeo': 'Anywhere',
   'jobLevel': 'Any',
   'jobExcerpt': 'CrossFit is looking to hire a Manager, Digital Marketing to join our Marketing team. You will play a pivotal role in shaping and executing CrossFit’s digital initiatives. This position requires a blend of strategic thinking, technical expertise, and hands-on execution to drive impactful outcomes. The ideal candidate will be a visionary leader who can develop&amp;#8230;',
   'jobDescription': '<p>CrossFit is looking to hire a Manager, Digital Marketing to join our Marketing team. You will play a pivotal role in shaping and executing CrossFit’s digital initiatives. This position requires a blend of strategic thinking, technical expertise, and hands-on execution to drive impactful outcomes. The ideal candidate will be a visionary leader who can develop and implement digital strategies that align with our business objectives while also rolling up their sleeves to actively participate in execution. This role requires a seasoned digital marketer with a proven track record in planning and implementing successful omnichannel campaigns.</p>\n<h2><b>RESPONSIBILITIES:</b></h2>\n<p><strong>Email Marketing:</strong></p>\n<ul>\n<li>Designing and executing email campaigns that nurture leads, engage customers, and drive conversions. Responsibilities include general setup, QA, managing email lists, segmenting audiences, a/b testing, analyzing results, and optimizing performance.</li>\n<li>Collaborate cross-functionally to continuously improve lifecycle marketing strategies and the customer journey.</li>\n<li>Generate reports to track business KPIs and inform strategic decisions.</li>\n</ul>\n<p><strong>Digital Strategy Development:</strong></p>\n<ul>\n<li>Formulate and execute comprehensive digital marketing strategies aligned with business objectives.</li>\n<li>Stay informed about industry trends, emerging technologies, and digital marketing best practices.</li>\n<li>Develop and maintain a deep understanding of consumer behaviors and the CrossFit brand and ensure the digital experience meets customer needs</li>\n</ul>\n<p><strong>Campaign Planning and Execution:</strong></p>\n<ul>\n<li>Plan and execute digital campaigns across various channels, including but not limited to the website, email, SMS, SEO, social media, paid media, and the CrossFit app.</li>\n<li>Collaborate with cross-functional teams to ensure seamless execution of campaigns.</li>\n</ul>\n<p><strong>Content Strategy and Creation:</strong></p>\n<ul>\n<li>Develop and oversee the content strategy for digital channels (email &amp; app), ensuring alignment with brand messaging and campaign goals.</li>\n<li>Collaborate with content creators to produce high-quality and engaging digital content.</li>\n</ul>\n<p><strong>Website Operations &amp; CRO:</strong></p>\n<ul>\n<li>Work in collaboration with Director of Growth Marketing to optimize website content and structure for search engines (SEO)</li>\n<li>Utilize the content management system (CMS) to execute regular content updates for the websites, including building new landing pages.</li>\n<li>Use data to apply insights on customer journey and inform site updates</li>\n<li>Continuously look for ways to optimize conversion and customer experience.</li>\n</ul>\n<p><strong>Paid Media:</strong></p>\n<ul>\n<li>Collaborate with Director of Growth Marketing on optimizing paid marketing campaigns for maximum ROI.</li>\n</ul>\n<p><strong>Collaboration with Stakeholders:</strong></p>\n<ul>\n<li>Collaborate with internal teams, including sales, product, social, and customer service, to align digital marketing efforts with overall business goals.</li>\n<li>Foster strong cross-functional collaboration for successful campaign execution.</li>\n</ul>\n<h2><b>KNOWLEDGE AND SKILL:</b></h2>\n<ul>\n<li>Proficient in email marketing platforms (e.g., Braze, Klaviyo, Mailchimp, Constant Contact, etc.) and marketing automation tools.</li>\n<li>Proven leadership, ability to establish and maintain a positive work culture among a team, and ability to communicate effectively to both large and small workgroups.</li>\n<li>Strong understanding of email marketing principles, automation, segmentation, and testing methodologies.</li>\n<li>Excellent copywriting skills with the ability to craft compelling and persuasive email content.</li>\n<li>Analytical mindset with the ability to interpret data and generate actionable insights.</li>\n<li>Familiarity with regulations and best practices related to email marketing compliance.</li>\n<li>The discipline, flexibility, and self-starter mentality required to work as part of a high-performing, distributed team.</li>\n</ul>\n<h2><b>EDUCATION/EXPERIENCE:</b></h2>\n<ul>\n<li>Bachelor’s degree in Marketing, Communications, Business, or a related field.</li>\n<li>Previous experience (3+ years) in email marketing, preferably within the health and fitness industry.</li>\n</ul>\n<h2>\xa0<b>WHAT WE OFFER:</b></h2>\n<ul>\n<li>Rich Medical, Dental, and Vision plans</li>\n<li>Unlimited Paid Time Off––empowering you to unplug whenever and however you need to</li>\n<li>Flexible spending account and 401(k) with employer matching at 5%</li>\n<li>CrossFit Gym Membership Reimbursement</li>\n<li>CrossFit Courses Benefit</li>\n<li>Partnership Perks</li>\n</ul>',
   'pubDate': '2025-03-04 03:56:21'},
  {'id': 114143,
   'url': 'https://jobicy.com/jobs/114143-director-of-product-marketing',
   'jobSlug': '114143-director-of-product-marketing',
   'jobTitle': 'Senior Content Marketing Manager',
   'companyName': 'ActiveCampaign',
   'companyLogo': 'https://jobicy.com/data/server-nyc0409/galaxy/mercury/2021/09/af4e42567a6faa8e315a3991ae7f24a0.jpeg',
   'jobIndustry': ['Marketing &amp; Sales'],
   'jobType': ['full-time'],
   'jobGeo': 'USA',
   'jobLevel': 'Senior',
   'jobExcerpt': 'As a Senior Content Marketing Manager, you’ll create content that drives business across the entire customer lifecycle. You’ll touch all types of content, from original research to white papers to webinars to landing pages, and support customer acquisition, customer retention, and acquisition of customers for new product lines. This is not your typical content marketing&amp;#8230;',
   'jobDescription': '<p>As a Senior Content Marketing Manager, you’ll create content that drives business across the entire customer lifecycle. You’ll touch all types of content, from original research to white papers to webinars to landing pages, and support customer acquisition, customer retention, and acquisition of customers for new product lines.</p>\n<p>This is not your typical content marketing role, and we’re not following the typical SEO-to-gated content playbook. Instead, content at ActiveCampaign will focus on market-leading insights, original research, and using the power of content across every stage of a customer’s relationship with ActiveCampaign.</p>\n<h2>What your day could consist of:</h2>\n<ul>\n<li>Write original content of various types (e.g., original research, thought leadership articles, blog posts, long-form assets, videos, website copy, email messaging, etc.)</li>\n<li>Work with agencies and freelancers to scale execution, improve organic traffic, and level up multimedia content</li>\n<li>Craft content that appeals to targeted audience segments and funnel stages, as well as to broader audiences</li>\n<li>Edit, proofread, and improve content written by others</li>\n<li>Collaborate with key stakeholders across Marketing, Sales, Customer Success, and Product teams and other team members to produce high-quality content to achieve growth objectives</li>\n<li>Contribute to organic growth and SEO initiatives to improve top-line and category-relevant traffic</li>\n<li>Brainstorm new ideas and help plan an editorial calendar with the rest of the Content Marketing team</li>\n</ul>\n<h2>What is needed:</h2>\n<ul>\n<li>8+ years of marketing experience, 5+ of which is content marketing experience, preferably in a high-growth environment. Familiarity with SEO is preferred.</li>\n<li>Sharp writing and editing skills, with the ability to turn ideas into compelling stories and clean, clear, vibrant copy</li>\n<li>Love for storytelling and matching content to specific stages of a customer’s purchase process</li>\n<li>Able to bridge the gap between data and storytelling, to help turn quantitative insights into compelling content</li>\n<li>Can articulate visual needs and brainstorm ideas with photo editors, graphic designers, and video producers to create content with a strong visual impact</li>\n<li>Applying and refining our voice and tone guidelines to maintain consistency and quality (and encouraging others to do so, as well)</li>\n<li>Self-starter with excellent organizational and time management skills who can drive projects from start to finish</li>\n<li>Experience with Craft CMS, Adobe Analytics, Asana, and other content marketing-related systems is a plus</li>\n</ul>\n<p>$132,000 &#8211; $181,500 a year</p>\n<p>Compensation details listed in this posting reflect the base rate only and do not include bonus, equity, sales incentives or other role specific compensation that the role may be eligible for. ActiveCampaign believes in and is committed to equitable compensation practices. The salary range provided above is a good faith estimate of the pay range determined by the location associated with the job posting. The actual salary depends on a candidate’s skills, experience, and work location.</p>\n<h2><b>About ActiveCampaign:</b></h2>\n<p>ActiveCampaign helps small teams power big businesses with the must-have platform for intelligent marketing automation. Customers from over 170 countries depend on ActiveCampaign’s mix of pre-built automations and integrations (including Facebook, Google, WordPress, Salesforce, Shopify, and Square) to power personalized marketing, transactional emails, and one-to-one CRM interactions throughout the customer lifecycle.</p>\n<p>As a global multicultural company, we are proud of our inclusive culture which embraces diverse voices, backgrounds, and perspectives. We don’t just celebrate our differences, we believe our diversity is what empowers our innovation and success. You can find out more about our DEI initiatives here.</p>\n<p>ActiveCampaign holds the highest customer satisfaction rating among Marketing Automation, E-Commerce Personalization, Landing Page Builders, and CRM solutions on G2.com and is one of only a handful of software solutions with over 10,000 positive reviews. ActiveCampaign has also been named the Top Rated Email Marketing Software on TrustRadius. Learn more and start your free trial at ActiveCampaign.com.</p>\n<h2><b>Perks and benefits:</b></h2>\n<p>ActiveCampaign is an employee-first culture. We take care of our employees at work and outside of work. You can see more of the details here, but some of our most popular benefits include:</p>\n<ul>\n<li>Comprehensive health and wellness benefits that includes a High Deductible Health Plan (HDHP) fully covered by ActiveCampaign, complimentary access to telehealth and tele-mental health resources, and a complimentary membership to Calm</li>\n<li>Open paid time off</li>\n<li>Generous 401(k) matching program with immediate vesting</li>\n<li>Quarterly Path Perks with options for commuter and lunch benefits (for those reporting to a Hub), or a remote home office stipend</li>\n<li>Access to professional development resources through LinkedIn Learning</li>\n<li>After five years of service, you’ll be eligible for a four-week paid sabbatical leave and a sabbatical leave bonus</li>\n</ul>\n<p>ActiveCampaign is an equal opportunity employer. We recruit, hire, pay, grow and promote no matter of gender, race, color, sexual orientation, religion, age, protected veteran status, physical and mental abilities, or any other identities protected by law.</p>\n<p>Our Employee Resource Groups (ERGs) strive to foster a diverse inclusive environment by supporting each other, building a strong sense of belonging, and creating opportunities for mentorship and professional growth for their members.</p>',
   'pubDate': '2025-02-20 04:04:56',
   'annualSalaryMin': 132000,
   'annualSalaryMax': 181500,
   'salaryCurrency': 'USD'}]}

job_dict = response['jobs']
print (job_dict)
jobs_list = []
senior_roles = []
manager_roles = []

for job_details in job_dict:
    if "Senior" in job_details['jobTitle']:
        senior_roles.append(job_details['jobTitle'])
    elif "Manager" in job_details['jobTitle']:
        manager_roles.append(job_details['jobTitle'])
    else:
        # print(f" Odd one : {job_details['jobTitle']}")
        continue

df_senior_roles = pd.DataFrame(senior_roles)
df_senior_roles.rename(columns={0: 'senior_roles'}, inplace=True)

wr.s3.to_parquet(
    df = df_senior_roles,
    path = "s3://amatullah-mahmud-bucket/random-user-details-folder/senior_roles.parquet"
)

df_manager_roles = pd.DataFrame(manager_roles)
df_manager_roles.rename(columns={0: 'manager_roles'}, inplace=True)

wr.s3.to_parquet(
    df = df_manager_roles,
    path = "s3://amatullah-mahmud-bucket/random-user-details-folder/manager_roles.parquet"
)


# API_3
# url = f"https://content.guardianapis.com/search?q=Nigeria&from-date=2025-01-01&to-date=2025-12-31&api-key={API_KEY}"
# response = requests.get(url)
nigerian_data = response.json()
nigerian_data

all_articles = []

for page in range(1, 11):  # Since 'pages': 10 in the response
    url = f"https://content.guardianapis.com/search?q=Nigeria&from-date=2025-01-01&to-date=2025-12-31&api-key={API_KEY}"

    articles = nigerian_data["response"]["results"]

    if not articles:
        break  

    all_articles.extend(articles)
all_articles

df_articles = pd.DataFrame(all_articles)
df_articles = df_articles[["id", "webPublicationDate", "webTitle", "webUrl"]]

wr.s3.to_parquet(
    df = df_articles,
    path = "s3://amatullah-mahmud-bucket/guardian-nigerian-articles/the_articles.parquet"
)

