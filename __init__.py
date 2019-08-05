from mycroft import MycroftSkill, intent_file_handler


class SwitchToAltLink(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('link.alt.to.switch.intent')
    def handle_link_alt_to_switch(self, message):
        self.speak_dialog('link.alt.to.switch')


def create_skill():
    return SwitchToAltLink()

