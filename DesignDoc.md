# KinConnections WebApp

## Data Structures

### **All Users**

- `id`
- `email`
- `password` - encrypted
- `first_name`
- `last_name`
- `dob` - date of birth (everyone 18+)
- `region_current` - enumerated below
- `location_current` - string
- `gender` - male/female/non-binary/other/prefer to not share
- `languages` - Languages you are comfortable with
<!-- # - `acknowledgement` - boolean for agreement with code of conduct [handled by code] -->
<!-- # - `user_type` - Connectee or Connector or *Admin* [separate bases] -->

### **Connectee**
- `attended_ge` - yes/no
- `ge_camps` - open text
- `is_ismaili` - yes/no (currently not a requirement)

### **Connectors**

- `title`
- `professional_category`
  - enumerated (dynamic?) array
- `education`
  - array of `{School, Degree}`
- `linkedin`
  - URL
- `bio`
  - Paragraph
- `location`
  - short text
<!-- - *Communication Channel*s
  - *probably an email from our service?* -->
- `images`
  - upload image(s) 
  - profile picture + action shots @ work
- `approved` - confirms harrassment training & waiver system

*Filter Connectors with:* Language, Country of Origin, Professional Category, and School


**Languages** 
- Arabic
- Dari
- English
- Farsi
- French
- Gujarati
- Kutchi
- Portuguese
- Russian
- Spanish
- Urdu/Hindi

**Professional Category**
- Arts & Media
- Business
- Engineering
- Architecture
- Health & Medicine
- Human Resources
- International Relations, Law & Policy
- Marketing & Sales
- Non-Profit & Foundation
- Tourism & Hospitality

**Regions**
- Afghanistan
- Australia/New Zealand
- Bangladesh
- Canada
- Democratic Republic of Congo
- Far East
- France
- India
- Kenya
- Madagascar
- Mozambique
- Pakistan
- Portugal
- Syria
- Tajikistan
- Tanzania
- Uganda
- United Arab Emirates
- United Kingdom
- United States of America