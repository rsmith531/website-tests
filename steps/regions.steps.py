from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from behave import *

use_step_matcher("re")


@given('we have navigated to the "(?P<state>.+)" webpage from the route directory')
def step_impl(context, state):
    context.browser = webdriver.Chrome(executable_path=
                                       "C:\\browser_drivers\\chromedriver.exe")
    context.site = "https://www.mountainproject.com/route-guide"
    context.browser.get(context.site)
    time.sleep(2)
    context.state = state
    state_page = context.browser.find_element(
        By.PARTIAL_LINK_TEXT, context.state)
    state_page.click()
    time.sleep(2)
    print(f'Navigated to {context.browser.title}.')


@when('we look for the "(?P<region>.+)" on the webpage')
def step_impl(context, region):
    context.page = context.browser.page_source
    context.region_length = len(region)
    context.region_index = context.page.find(region)
    if context.region_index != -1:
        print(f'Found {region}.')


@then('we find that the region has at least one route')
def step_impl(context):
    i = context.page.find("text-warm", context.region_index)
    routes = ""
    # print(context.page.encode("utf-8"))
    while context.page[i] != '<':
        if context.page[i].isdigit():
            routes += context.page[i]
        i += 1
    assert int(routes) != 0
    print(f'This region has {routes} routes.')


@given('we are at the "Route Guide" webpage')
def step_impl(context):
    context.browser = webdriver.Chrome(executable_path=
                                       "C:\\browser_drivers\\chromedriver.exe")
    context.site = "https://www.mountainproject.com/route-guide"
    context.browser.get(context.site)
    time.sleep(2)
    context.page = context.browser.page_source


@when("we check to see how many routes are on the Top 10 list")
def step_impl(context):
    start_index = context.page.find('The Top 10 Classic Rock Climbing Routes')
    end_index = context.page.find('</tbody>', start_index)
    context.routes = context.page.count('text-truncate', start_index, end_index)


@then("the list should contain exactly 10 routes")
def step_impl(context):
    assert context.routes == 10
    print(f'There are {context.routes} routes in the Top 10 list.')
