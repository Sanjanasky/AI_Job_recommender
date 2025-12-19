from apify_client import ApifyClient
from apify_client.errors import ApifyApiError
import os
from dotenv import load_dotenv

load_dotenv()

apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# ---------------- INDEED ----------------
def fetch_indeed_jobs(search_query, location="India", rows=50):
    try:
        run_input = {
            "position": search_query,
            "country": "IN",
            "location": location,
            "maxItems": rows,
            "parseCompanyDetails": False,
            "saveOnlyUniqueItems": True,
            "followApplyRedirects": False
        }

        run = apify_client.actor("hMvNSpz3JnHgl5jkh").call(run_input=run_input)
        return list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())

    except ApifyApiError:
        return []


# ---------------- NAUKRI ----------------
def fetch_naukri_jobs(search_query, rows=50):
    try:
        run_input = {
            "keyword": search_query,
            "maxJobs": rows,
            "freshness": "all",
            "sortBy": "relevance",
            "experience": "all"
        }

        run = apify_client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)
        return list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())

    except ApifyApiError:
        return []
