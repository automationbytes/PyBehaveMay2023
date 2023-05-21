import allure
from selenium import webdriver
# from castro import Castro


def before_all(context):
    print("Before All")


def before_scenario(context, scenario):
    print("Before Scenario")
    # c = Castro()
    # c.start()

def after_scenario(context, scenario):
    print("After Scenario")
    # c = Castro()
    # c.stop()


def before_step(context, step):
    print("Before Step")

def after_step(context,step):
    print("After Step")
    allure.attach(context.driver.get_screenshot_as_png(), name=step.name,
                  attachment_type=allure.attachment_type.PNG)
    if step.status == "failed":

        print("fail")
        context.driver.get_screenshot_as_png()
        context.driver.get_screenshot_as_file(step.name+".png")



def After_all(context):
    print("After All")