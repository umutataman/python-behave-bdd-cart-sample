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
    value_int = 1
    if value_int == 1:
        print("1")

def after_scenario(context,scenario):
    print("after scenario")
    print("scenario status" + str(scenario.status))
    if scenario.status == "failed":
        fail_path = "failed_scenarios_screenshots"
        if not os.path.exists(fail_path):
            os.makedirs(fail_path)
        os.chdir(fail_path)
        context.browser.save_screenshot(scenario.name + "_failed.png")
        os.chdir("..")
    context.browser.quit()

def after_feature(context,feature):
    print("After feature\n")

def after_all(context):
     print("Executing after all")

