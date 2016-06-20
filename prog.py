

class Visitor(object):

    def __init__(self,*args, **kwargs):
        self.food = list(args)

    def say_hi(self, name):
        return 'Hi {}'.format(name)

    def say_bye(self, name):
        return  'See ya, {}'.format(name)

    def eat_my_food(self, name, kibble):
        if self.has_food(kibble):
            self.food.remove(kibble)
            return "Have some {}, {}".format(kibble, name)
        else:
            return "Sorry, {}, I don't have any {}".format(name, kibble)

    def go_shopping(self, new_food):
        self.food.append(new_food)

    def has_food(self, kibble):
        return kibble in self.food

if __name__ == '__main__':
    v = Visitor('grapes','biscuits','cheese')

    print v.say_hi('Matt')
    print v.eat_my_food('Matt', 'biscuits')
    print v.say_bye('Matt')


