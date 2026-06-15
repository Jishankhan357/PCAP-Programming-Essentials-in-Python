import urllib.request
import json
import urllib.error
from datetime import datetime

def format_date(date_string):
    """Converts GitHub's ISO date format into a readable string."""
    date_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
    return date_obj.strftime("%d %b %Y")

def fetch_github_profile():
    print("\n" + "="*55)
    print("           🚀 GITHUB PROFILE ANALYZER")
    print("="*55)
    
    username = input("Enter GitHub Username: ")
    
    # 2 URLs: Ek basic profile ke liye, ek repos ke liye (per_page=100 ensures we get maximum repos in one go)
    api_url = f"https://api.github.com/users/{username}"
    repo_url = f"https://api.github.com/users/{username}/repos?per_page=100"
    
    print(f"\n🔍 Fetching live data for '{username}'...\n")
    
    try:
        # --- 1. FETCH BASIC PROFILE ---
        req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            user_data = json.loads(response.read().decode('utf-8'))
            
        name = user_data.get('name', 'Name not provided')
        location = user_data.get('location', 'Location not provided')
        bio = user_data.get('bio', 'No bio available')
        followers = user_data.get('followers', 0)
        following = user_data.get('following', 0)
        repos_count = user_data.get('public_repos', 0)
        
        raw_date = user_data.get('created_at', '')
        joined_date = format_date(raw_date) if raw_date else "Unknown"

        # --- 2. FETCH AND SORT REPOSITORIES ---
        top_repos = []
        if repos_count > 0:
            repo_req = urllib.request.Request(repo_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(repo_req) as repo_response:
                repos_data = json.loads(repo_response.read().decode('utf-8'))
                
                # Sorting magic: Sort by 'stargazers_count' in descending order
                sorted_repos = sorted(repos_data, key=lambda x: x.get('stargazers_count', 0), reverse=True)
                
                # Slicing: Sirf shuru ki 3 repositories uthao
                top_repos = sorted_repos[:3]

        # --- BEAUTIFUL CLI DASHBOARD OUTPUT ---
        print("="*55)
        print(f"👤 Name      : {name}")
        print(f"📍 Location  : {location}")
        print(f"📝 Bio       : {bio}")
        print(f"👥 Network   : {followers} Followers | {following} Following")
        print(f"📦 Repos     : {repos_count} Public Repositories")
        print(f"📅 Joined    : {joined_date}")
        print("-" * 55)
        
        # Printing Top 3 Repositories
        if top_repos:
            print("🌟 TOP 3 REPOSITORIES:")
            for i, repo in enumerate(top_repos, 1):
                repo_name = repo.get('name', 'Unknown')
                stars = repo.get('stargazers_count', 0)
                language = repo.get('language', 'N/A')
                # Printing each repo beautifully
                print(f"  {i}. {repo_name}")
                print(f"     └─ ⭐ {stars} Stars | 🛠️ {language}")
        else:
            print("🌟 No public repositories found.")
            
        print("="*55)
        
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("❌ Error: Yeh user GitHub par exist nahi karta (404 Not Found).")
        elif e.code == 403: # GitHub allows only 60 unauthenticated requests per hour
            print("❌ Error: API Rate Limit Exceeded. Aapne bohot zyada requests bhej di hain, thodi der baad try karein.")
        else:
            print(f"❌ Error: HTTP Error {e.code}")
    except Exception as e:
        print(f"❌ Network Error: Please check your internet connection. Details: {e}")

if __name__ == "__main__":
    fetch_github_profile()