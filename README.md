# Celebration Scraper

## Automatically Scrapes Daily Greek Name Day Celebrations

This Python script scrapes daily Greek name day celebrations from [eortologio.net](https://www.eortologio.net/) and saves them to a CSV file. The script runs automatically using GitHub Actions.

---

## How to Set Up GitHub PAT (Personal Access Token)

Follow these steps to allow GitHub Actions to push changes (like updates to the CSV file) back to the repository.

### Create Your Personal Access Token (PAT)
1. Go to [https://github.com/settings/personal-access-tokens](https://github.com/settings/personal-access-tokens)
2. Click **"Generate new token"**
3. **Enter a name** for the token
4. Set an **expiration** (e.g., 90 days)
5. **Repository access**: Select **"Only select repositories"** and choose this one
6. **Permissions**:
    - Under **"Repository contents"**, check: **Read and write**
7. Click **"Generate token"**
8. **Copy the token** — you won’t be able to see it again!

### Add PAT as a GitHub Secret
9. Go to your repository → **Settings** → **Secrets and variables** → **Actions**
10. Click **"New repository secret"**
11. Set:
    - **Name**: `PAT_TOKEN`
    - **Value**: (Paste the token you copied)

---

Now your GitHub Action has permission to push CSV updates to your repository!
