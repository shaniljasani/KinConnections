# KinConnections WebApp

## Data Structures

### **All Users**


- `uid` - unique user ID generated at signup
- `first_name`
- `last_name`
- `email`
- `password` - encrypted
- `dob` - date of birth (everyone 18+)
- `country_origin` - 126+ options
- `region_current` - enumerated below
- `location_current` - string
- `gender` - male/female/non-binary/other/prefer to not share
- `languages` - Languages you are comfortable with
- `acknowledgement` - boolean for agreement with code of conduct
- `user_type` - Connectee or Connector or *Admin*

### **Connectee**
- `ge_status` - select which camp(s) you attended
- `is_ismaili`

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
- *Communication Channel*s
  - *probably an email from our service?*
- `images`
  - upload image(s) 
  - profile picture + action shots @ work
- `approved` - confirms harrassment training & waiver system

*Filter Connectors with:* Language, Country of Origin, Professional Category, and School


**Languages** 
# TODO Alphebatize
- English
- French
- Spanish
- Portuguese
- Russian
- Tajiki language
- Farsi
- Dari
- Urdu / Hindi
- Gujarati
- Kutchi
- Arabic
- Other

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
- Mosambique
- Pakistan
- Portugal
- Syria
- Tajikistan
- Tanzania
- Uganda
- United Arab Emirates
- United Kingdom
- United States of America