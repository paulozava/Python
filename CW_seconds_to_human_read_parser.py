#a function which formats a duration, given as a number of seconds, in a human-friendly way.

def format_duration(seconds):
    if seconds is 0:
        return 'now'
    resp = []
    checker = [[31536000, '{} year{}'], [86400, '{} day{}'], [3600, '{} hour{}'], [60, '{} minute{}'], [1, '{} second{}']]
    for seconds_checker, template in checker:
        if seconds >= seconds_checker:
            data = int(seconds / seconds_checker)
            if data > 1:
                plural = 's'
            else:
                plural = ''
            resp.append(template.format(data, plural))
            seconds -= (seconds_checker * data)

    resp.reverse()
    cont, response = 0, ''
    for item in resp:
        if cont is 1:
            response = ' and ' + response
        if cont > 1:
            response = ', ' + response
        response = item + response
        cont += 1

    return response