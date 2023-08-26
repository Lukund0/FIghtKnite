import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

kivy.require('1.9.0')
Config.set('graphics', 'Height','250' )
Config.set('graphics', 'width','610' )
x1 = 40
x2 = 100
y1 = 0
throw = 1
retract = 10
hit = 1
back = 10
punched = False

class Gameroot(FloatLayout):
    def __int__(self):
        super(Gameroot).__int__()

    def punch(self, event):
        global throw, retract, punched
        if throw <= 10:
            if throw == 10:
                if retract >= 1:
                    if x2 - x1 <= 28 and punched is False:
                        self.reaction('none')
                        punched = True
                    self.frame.source = f'punch/{retract}.png'
                    retract -= 1
                else:
                    throw += 1
            else:
                self.frame.source = f'punch/{throw}.png'
                throw += 1
                Clock.schedule_interval(self.punch,  0.06)
        else:
            throw = 1
            retract = 10
            self.frame.source = f'punch/{throw}.png'
            punched = False
            Clock.unschedule(self.punch)

    def reaction(self, event):
        global hit, back
        if hit <= 10:
            if hit == 10:
                if back >= 1:
                    self.react.source = f'react/{back}.png'
                    back -= 1
                else:
                    hit += 1
            else:
                self.react.source = f'react/{hit}.png'
                hit += 1
                Clock.schedule_interval(self.reaction,  0.04)
        else:
            hit = 1
            back = 10
            self.react.source = f'react/{hit}.png'
            Clock.unschedule(self.reaction)

    def button_func(self, event):
        global x1, y1
        if event == 'right':
            if x1 <= 250 and x2 - x1 >= 25:
                self.frame.x += 5
                x1 += 5
        elif event == 'left':
            if x1 >= -250:
                self.frame.x -= 5
                x1 -= 5
        elif event == 'up':
            if y1 < 100:
                pass
        elif event == 'down':
            pass
        elif event == 'kick':
            pass
        elif event == 'punch':
            self.punch('punch')
        elif event == 'block':
            pass


class Fightknite(App):
    def build(self):
        return Gameroot()

app = Fightknite()
app.run()
