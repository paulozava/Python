#a function which formats a duration, given as a number of seconds, in a human-friendly way.

def format_duration(seconds):
    if seconds is 0:
        return 'now'
    times = ['years', 'days', 'hours', 'minutes', 'seconds']
    times_to_seconds = {'years':31536000, 'days':86400, 'hours':3600, 'minutes':60, 'seconds':1}
    times_to_templates = {'years':'{} year{}', 'days':'{} day{}', 'hours':'{} hour{}',
                          'minutes':'{} minute{}', 'seconds':'{} second{}'}

    formatted_templates = []
    for time in times:
        time_minimal_second = times_to_seconds[time]
        if seconds >= time_minimal_second:
            data = int(seconds / time_minimal_second)
            if data > 1:
                plural = 's'
            else:
                plural = ''
            template = times_to_templates[time]
            formatted_templates.append(template.format(data, plural))
            seconds -= (time_minimal_second * data)

    formatted_templates.reverse()
    response = ''
    for counter, formatted_template in enumerate(formatted_templates):
        if counter > 1:
            response = ', ' + response
        if counter is 1:
            response = ' and ' + response
        response = formatted_template + response

    return response