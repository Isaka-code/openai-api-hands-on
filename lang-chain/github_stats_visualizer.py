import requests


def make_api_request(url):
    """APIリクエストを行い、JSONレスポンスを返す"""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"GitHub API Error: {response.status_code}")

def get_repo_stats(repo):
    """GitHubリポジトリの基本統計情報を取得する"""
    url = f'https://api.github.com/repos/{repo}'
    data = make_api_request(url)
    return {
        'Stars': data['stargazers_count'],
        'Forks': data['forks_count'],
        'Watchers': data['watchers_count'],
        'Open Issues': data['open_issues_count'],
        'Created At': data['created_at']
    }

def get_additional_stats(repo):
    """追加のリポジトリ統計情報を取得する"""
    commits_data = make_api_request(f'https://api.github.com/repos/{repo}/stats/commit_activity')
    code_freq_data = make_api_request(f'https://api.github.com/repos/{repo}/stats/code_frequency')
    return {
        'Total Commits': sum(week['total'] for week in commits_data),
        'Code Additions': sum(week[1] for week in code_freq_data),
        'Code Deletions': sum(week[2] for week in code_freq_data)
    }

def get_latest_release(repo):
    """リポジトリの最新リリース情報を取得する"""
    releases = make_api_request(f'https://api.github.com/repos/{repo}/releases')
    return releases[0] if releases else None

def display_repo_info(repo):
    """リポジトリの情報を表示する"""
    stats = get_repo_stats(repo)
    stats.update(get_additional_stats(repo))

    print("\nRepository Statistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")

    latest_release = get_latest_release(repo)
    if latest_release:
        print("\nLatest Release:")
        print(f"- {latest_release['name']} (Tag: {latest_release['tag_name']})")

    contributors = make_api_request(f'https://api.github.com/repos/{repo}/contributors')[:5]
    print("\nTop 5 Contributors:")
    for contributor in contributors:
        print(f"- {contributor['login']} (Contributions: {contributor['contributions']})")

if __name__ == "__main__":
    repo = 'langchain-ai/langchain'  # リポジトリ名を設定
    display_repo_info(repo)
