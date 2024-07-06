# job_scraper.py

import requests
from bs4 import BeautifulSoup

def fetch_job_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def scrape_brightermonday():
    url = "https://www.brightermonday.co.ke/jobs"
    soup = fetch_job_data(url)
    jobs = []

    for job_card in soup.find_all('div', class_='search-result__job'):
        title = job_card.find('h3', class_='search-result__job-title').text.strip()
        company = job_card.find('a', class_='search-result__job-company-name').text.strip()
        location = job_card.find('span', class_='search-result__location').text.strip()
        date_posted = job_card.find('span', class_='search-result__posted-date').text.strip()
        job_link = job_card.find('a', class_='search-result__job-title')['href']

        jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'date_posted': date_posted,
            'job_link': f"https://www.brightermonday.co.ke{job_link}"
        })

    return jobs

def scrape_myjobmag():
    url = "https://www.myjobmag.co.ke"
    soup = fetch_job_data(url)
    jobs = []

    for job_card in soup.find_all('li', class_='jobs-list-item'):
        title = job_card.find('h2').text.strip()
        company = job_card.find('div', class_='company-name').text.strip()
        location = job_card.find('span', class_='job-location').text.strip()
        date_posted = job_card.find('span', class_='job-date').text.strip()
        job_link = job_card.find('a')['href']

        jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'date_posted': date_posted,
            'job_link': f"https://www.myjobmag.co.ke{job_link}"
        })

    return jobs


# save_data.py

import csv

def save_to_csv(jobs, filename='kenyan_jobs.csv'):
    keys = jobs[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(jobs)

# # main.py



# from job_scraper import scrape_brightermonday, scrape_myjobmag # type: ignore
# from save_data import save_to_csv # type: ignore

# def main():
#     jobs = []
#     print("Scraping jobs from BrighterMonday...")
#     try:
#         jobs.extend(scrape_brightermonday())
#         print(f"Found {len(jobs)} jobs on BrighterMonday.")
#     except Exception as e:
#         print(f"Error scraping BrighterMonday: {e}")

#     print("Scraping jobs from MyJobMag...")
#     try:
#         myjobmag_jobs = scrape_myjobmag()
#         print(f"Found {len(myjobmag_jobs)} jobs on MyJobMag.")
#         jobs.extend(myjobmag_jobs)
#     except Exception as e:
#         print(f"Error scraping MyJobMag: {e}")

#     if jobs:
#         save_to_csv(jobs)
#         print(f"Scraped {len(jobs)} job postings and saved to kenyan_jobs.csv")
#     else:
#         print("No jobs found")

# if __name__ == "__main__":
#     main()

