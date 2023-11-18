# Medisecuremask
# Docs Link
[https://medisecuremask.readthedocs.io/en/latest/](https://medisecuremask.readthedocs.io/en/latest/)
# Project description
Currently, the medical field is utilizing medical big data for various research and artificial intelligence development. However, in order to utilize these data, it is necessary to de-identify personal information, which is sensitive information. Therefore, in this project, we created a site where medical data can be de-identified and searched.

# Applied technologies
- **OCR**: Recognize text embedded in images.
- **De-identification model**: Categorize what's private and what's not, and blur it if it's private
- **Web**: De-identify the original data in storage (AWS S3) and make the results available on your website

# Development Language and Framework
- Python
- Spark
- Flask
- Mysql
- AWS S3, Lambda , EC2 
#  Architecture
![Project Architecture](https://i.ibb.co/RgszdpN/2023-09-20-8-45-05.png)

