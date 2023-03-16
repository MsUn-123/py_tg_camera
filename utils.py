import time

def get_uptime(bootMark):
    uptime = int(time.time() - bootMark)
    seconds = uptime % 60
    minutes = uptime // 60
    hours = uptime // 3400
    text = f"H:{hours} M:{minutes} S:{seconds} "
    return text
