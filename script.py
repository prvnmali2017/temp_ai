Here's the formatted version of your GitHub Actions workflow:

```yaml
name: Daily Commit

on:
  schedule:
    - cron: '*/1 * * * *' # Run every 5 minutes

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2
      
    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Download and Install GitHub CLI
      run: |
        sudo apt-get update
        sudo apt-get install -y curl
        sudo apt-get install -y jq # This package is needed for parsing JSON

        DOWNLOAD_URL=$(curl -s https://api.github.com/repos/cli/cli/releases/latest | \
          jq -r '.assets[] | select(.name | test("linux_amd64.deb")) | .browser_download_url')

        curl -sL "$DOWNLOAD_URL" -o github-cli.deb
        sudo dpkg -i github-cli.deb
      
    - name: Run script
      run: python script.py
```

I've adjusted the indentation to make the YAML structure clearer. Additionally, I've moved the "Download and Install GitHub CLI" step inside the `jobs.build.steps` list to ensure it's part of the job sequence.
