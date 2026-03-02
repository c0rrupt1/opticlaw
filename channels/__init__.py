import core

def get_all():
    import channels
    return core.module.load(channels, core.channel.Channel)
