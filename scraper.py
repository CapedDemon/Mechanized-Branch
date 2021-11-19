from selenium import webdriver
import os
import subprocess
import sys
import json
import requests

path = 'D:\Chrome Driver\chromedriver.exe' # The path of chromedriver.exe(You can give your own path)

# Class
class GitScraper():
    driverPath = ''
    url = "https://github.com/login"
    add_command = "git add -A"
    commit_command = 'git commit -m "'
    push_command = 'git push -u origin '
    api_url = "https://api.github.com/users/"

    # init function ehich takes the chromedriver.exe path
    def __init__(self, driverPath):
        self.driverPath = driverPath

    # This funtion initialises the chrome driver and opens it with the url
    def driver_init(self):
        self.driver = webdriver.Chrome(self.driverPath)
        self.driver.get(self.url)

    # This function logins inito the github profile and gives you your information
    def login(self):
        username_val = input("Enter your username: ")
        password_val = input("Enter your password: ")
        self.username = self.driver.find_element_by_id("login_field")
        self.password = self.driver.find_element_by_id("password")
        self.button = self.driver.find_element_by_name("commit")

        self.username.send_keys(username_val)
        self.password.send_keys(password_val)
        self.button.click()

    # This function creates a new repository
    def github_profile(self):
        username_val = input("Enter your ussername: ")
        self.response = requests.get(self.api_url + username_val)

        self.data = json.loads(self.response.text)
        print("\nUsername : " + self.data['login'])
        print("\nName: " + self.data['name'])
        print("\nLocation: " + self.data['location'])
        print("\nBio : " + self.data['bio'])
        print("\nPublic Repos : " + str(self.data['public_repos']))
        print("\nFollowers : " + str(self.data['followers']))
        print("\nFollowing : " + str(self.data['following']))

    def new_repo(self):
        repoName = input("Enter your new repository name: ")
        desc_val = input("Enter the description of your new repo.(You can keep it blank)\n:")
        type = input("Your repository should be Public or Private: ")
        self.driver.implicitly_wait(3)
        self.NEW = self.driver.find_element_by_xpath(
            '/html/body/div[6]/div/aside/div[2]/div[1]/div/h2/a')
        self.NEW.click()

        self.Repository = self.driver.find_element_by_id("repository_name")
        self.Repository.send_keys(repoName)

        self.Description = self.driver.find_element_by_id(
            "repository_description")
        self.Description.send_keys(desc_val)

        if type == "Public" or type == "public":
            self.Public = self.driver.find_element_by_id("repository_visibility_public")
            self.Public.click()
        else:
            self.Private = self.driver.find_element_by_id(
                "repository_visibility_private")
            self.Private.click()
    
    # This function can git add and git commit and git push make sure git is install and the configuration is global
    def add_commit_push(self):
        commit_msg = input("Enter your commit message: ")
        branch_name = input("Enter your branch name: ")
        decision = input("Do you want ti change directory: Yes(y) or No(n): ")
        if decision == 'y':
            directory = input("Enter the directory path where your repo is located: ")
            os.chdir(directory)

        completed1 = subprocess.Popen(["powershell.exe", self.add_command], stdout = sys.stdout)
        completed2 = subprocess.Popen(["powershell.exe", self.commit_command + commit_msg + '"'], stdout = sys.stdout)
        completed3 = subprocess.Popen(["powershell.exe", self.push_command + branch_name], stdout = sys.stdout)
        completed4 = subprocess.Popen(["powershell.exe", "cls"], stdout=sys.stdout)
        
        
# Object
bot = GitScraper(path)

# Fucntion with their specifications
#bot.driver_init()
#bot.login()
#bot.new_repo()
#bot.add_commit_push()
bot.github_profile()