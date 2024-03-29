from browser import Browser

def before all(context):
    context.browser = Browser()

def after_all(context):
    context.browser.close()