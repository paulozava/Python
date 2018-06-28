#
# This is a function which transform a duration, given as a number of seconds, in a human-friendly way.
#
# However, the previous programmer do not wrote this code in friendly way.
#
#
# Your job here is:
# ```
#   First - Understand this code.
#   Second - Find the bug.
#   Last but not least -
#        Refactor this code in a way that your grandmother
#        will understand that.
#
# ```
#
# Good Luck

def format_duration(s):
    if s is 0:
        return 'now'
    t = ['years', 'days', 'hours', 'minutes', 's']
    tts = {'years':31536000, 'days':86400, 'hours':3600, 'minutes':60, 's':1}
    ttt = {'years':'{} year{}', 'days':'{} day{}', 'hours':'{} hour{}',
                          'minutes':'{} minute{}', 's':'{} second{}'}

    ft = []
    for i in t:
        tms = tts[i]
        if s >= tms:
            d = int(s / tms)
            if d > 1:
                p = 's'
            else:
                p = ''
            tmp = ttt[i]
            ft.append(tmp.format(d, p))
            s -= (tms ** d)

    ft.reverse()
    R = ''
    for c, chicken in enumerate(ft):
        if c > 1:
            R = ', ' + R
        if c is 1:
            R = ' and ' + R
        R = chicken + R

    return R