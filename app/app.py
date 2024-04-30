import streamlit as st
from streamlit_lottie import st_lottie
from langchain_helper import BabyNameGenerator
#from dotenv import load_dotenv

# Configuration of page
#load_dotenv()

st.set_page_config(page_icon=None, layout="centered", initial_sidebar_state="expanded",
                   menu_items={'Report a bug': 'mailto:muni.dimitra@gmail.com'})

st.title('Jeeves Replies')

text="""
## Introducing **Jeeves Replies** - Your Trusted Companion in Naming Your Bundle of Joy!

In the whimsical world of P.G. Wodehouse, there exists a character named Jeeves, a paragon of wit and wisdom, who never failed to assist those in a pickle with his unrivaled problem-solving skills and innate ability to untangle even the most convoluted situations. Inspired by Jeeves's remarkable talent for providing solutions to all manner of dilemmas, we proudly present *Jeeves Replies*, a Streamlit-based app powered by **OpenAI** using *Langchain* 🦜🔗 dedicated to helping new parents navigate one of life's most delightful conundrums - choosing the perfect name for their precious little one.

Parenthood is a grand adventure filled with countless decisions, and perhaps none is more momentous than selecting the name that will define your child's identity. Just as Jeeves was the ever-reliable confidant and advisor in Wodehouse's tales, **Jeeves Replies** is your steadfast companion on the delightful journey of naming your baby.

But before we dive into the world of baby names, it's worth a brief nod to the historic predecessor, Ask Jeeves. Ask Jeeves, a search engine launched in 1996, was designed to assist users in finding answers to their queries by employing a personified butler, Jeeves, to guide them through the search process. This innovative approach to online search was a precursor to the modern-day search engines we use today, and it too shared a connection with the spirit of Jeeves, the problem solver.

Now, *Jeeves Replies* takes this concept to a whole new level by applying the wisdom and charm of Jeeves to the delightful task of baby naming. Our app offers a delightful and efficient platform for exploring a vast array of baby names and their meanings, sorting through them based on your preferences, and ultimately, helping you make the perfect choice for your little one. Whether you're seeking a classic, trendy, or unique name, Jeeves is here to provide a curated list of options that suit your preferences, ensuring your baby's name is a reflection of your dreams and aspirations.

"""
st.markdown(text)
# Sidebar
number_of_names = st.sidebar.selectbox('Insert a number ', (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
country = st.sidebar.selectbox('Name of Country', ('Albania', 'Algeria', 'American Samoa', 'Andorra', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', 'Cote d\'Ivoire', 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czech Republic', 'DR Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'North Macedonia', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Barthelemy', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe'
))

gender = st.sidebar.selectbox('Gender of the baby', ('Male', 'Female', 'Gender Fluid'))
open_ai_api_key=st.sidebar.text_input('Plug in OpenAI api key')

# Button to start analysis
if st.sidebar.button("Fetch Names"):
    st_lottie('https://lottie.host/9d1bf3d4-651e-447f-b93b-e24f9efd7e5a/lO2JMi8PhD.json',height=300)
    if country and number_of_names and gender and open_ai_api_key:
        baby_name_generator = BabyNameGenerator(open_ai_api_key)

        response = baby_name_generator.generate_baby_names(number_of_names, country, gender)

        st.subheader('Baby Names with meaning:\n')
        baby_name_meaning = response['baby_name_meanings'].strip('')
        st.write(baby_name_meaning)
