name: Daily Commit

on:
  schedule:
    - cron: '*/5 * * * *' # Run every 5 minutes

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

    - name: Install GitHub CLI
      run: |
        sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key C99B11DEB97541F0
        sudo apt-add-repository https://cli.github.com/packages
        sudo apt update
        sudo apt install gh
      
    - name: Run script
      run: python script.py
