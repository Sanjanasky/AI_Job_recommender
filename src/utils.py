def normalize_job(job, source):
    return {
        "title": job.get("title") or job.get("position"),
        "company": job.get("companyName") or job.get("company"),
        "location": job.get("location"),
        "salary": job.get("salary"),
        "url": job.get("url") or job.get("jobUrl"),
        "source": source
    }
