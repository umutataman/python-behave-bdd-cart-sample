from selenium import webdriver
import os

def before_all(context):
    print("Executing before all")
    #Get screen size from userdata(paramaters from cmd)
    context.screen_width = int(context.config.userdata.get("width"))
    context.screen_height = int(context.config.userdata.get("height"))

def before_feature(context, feature):
    print("Before feature\n")
    context.browser = webdriver.Chrome()
    context.browser.set_window_size(context.screen_width, context.screen_height)
    

def before_scenario(context,scenario):
    print("Before scenario\n")

def after_scenario(context,scenario):
    print("after scenario")
    print("scenario status" + str(scenario.status))
    if str(scenario.status) == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(str(scenario.name) + "_failed.png")
    context.browser.quit()

def after_feature(context,feature):
    print("After feature\n")

def after_all(context):
     print("Executing after all")

