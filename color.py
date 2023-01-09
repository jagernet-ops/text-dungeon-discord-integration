# \033[1;32m

regular = "\033[0m"

bad = "\033[1;31m"
notification = "\033[1;33m"
good = "\033[1;92m"

cool = "\033[1;36m"

# effect colors has effect as an argument because python tries to input self into them
def effect_good(effect, text):
    return good + text + regular

def effect_neutral(effect, text):
    return notification + text + regular

def effect_bad(effect, text):
    return bad + text + regular


def compare(actual, base):
    if actual < base:
        return bad + str(actual) + regular
    elif actual > base:
        return good + str(actual) + regular
    else:
        return str(actual)


def threat(text):
    return bad + text + regular

def loot(text):
    return notification + text + regular


def damage(text):
    return bad + str(text) + regular

def effect(eff):
    return eff.color(eff, eff.name.upper())

def harm(text):
    return bad + text + regular


def critical_health(text):
    return bad + text + regular

def low_health(text):
    return notification + text + regular

def full_health(text):
    return good + text + regular

def health_status(health, maxHealth):
# returns green, yellow, or red depending on health
    text = f"{health}/{maxHealth}"
    if health / maxHealth < 0.4:
        return critical_health(text)
    elif health / maxHealth < 0.8:
        return low_health(text)
    else:
        return full_health(text)

def player(text):
    return good + text + regular

def special(text):
    return notification + text + regular


def blessed(text):
    return good + text + regular

def cursed(text):
    return bad + text + regular

def desc(text): # description
    return cool + text + regular