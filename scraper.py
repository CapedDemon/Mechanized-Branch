from selenium import webdriver
import subprocess
import sys

path = 'D:\Chrome Driver\chromedriver.exe' # The path of chromedriver.exe(You can give your own path)

# Class
class GitScraper():
    driverPath = ''
    url = "https://github.com/login"
    username = ''
    password = ''
    driver = ''
    button = ''
    NEW = ''
    Repository = ''
    Description = ''
    Public = ''
    Private = ''
    add_command = "git add -A"
    commit_command = 'git commit -m "'
    push_command = 'git push'

    # init function ehich takes the chromedriver.exe path
    def __init__(self, driverPath):
        self.driverPath = driverPath

    # This funtion initialises the chrome driver and opens it with the url
    def driver_init(self):
        self.driver = webdriver.Chrome(self.driverPath)
        self.driver.get(self.url)

    # This function logins inito the github profile
    def login(self, username_val, password_val):
        self.username = self.driver.find_element_by_id("login_field")
        self.password = self.driver.find_element_by_id("password")
        self.button = self.driver.find_element_by_name("commit")

        self.username.send_keys(username_val)
        self.password.send_keys(password_val)
        self.button.click()

    # This function creates a new repository
    def new_repo(self, repoName, desc_val, type):
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
    def add_commit_push(self, commit_msg):
        completed1 = subprocess.Popen(["powershell.exe", self.add_command], stdout = sys.stdout)
        completed2 = subprocess.Popen(["powershell.exe", self.commit_command + commit_msg + '"'], stdout = sys.stdout)
        completed3 = subprocess.Popen(["powershell.exe", self.push_command], stdout=sys.stdout)
        
        
# Object
bot = GitScraper(path)

# Fucntion with their specifications
#bot.driver_init()
#bot.login("<Your github username>", "<Your github passord>")
#bot.new_repo("<Your Repo Name>",  "<Your Repo Description>", "<Type of project- Public or Private>")
bot.add_commit_push("Added a function which can add and commit and push to repository.")
