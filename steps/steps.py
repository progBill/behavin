import behave
from prog import Visitor



@given('I greet the guest')
def step_impl(context):
   context.visitor = Visitor('bread','cheese') 

@when('{someone} shows up')
def step_impl(context, someone):
    assert context.visitor.say_hi('Matt') == 'Hi Matt'

@then('I say hi')
def step_impl(context):
    assert not context.failed

@given('{someone} has shit to do')
def step_impl(context, someone):
    context.visitor = Visitor('wine','grapes')

@when('{someone} leaves')
def step_impl(context, someone):
    assert context.visitor.say_bye(someone)== 'See ya, {}'.format(someone)

@then('I say bye')
def step_impl(context):
    assert not context.failed

@given('{someone} gets hungry')
def step_impl(context, someone):
    context.someone = someone
    context.visitor = Visitor('a biscuit')

@when('{someone} wants to eat {something}')
def step_impl(context, someone, something):
    #something = ' '.join([x for x in something if x not in ['a','an','the']])
    assert something in context.visitor.food
    
@then('{someone} eats {something}')
def step_impl(context, someone, something):
    assert not context.failed

@given('{someone} raids the fridge')
def step_impl(context, someone):
    context.someone = someone
    context.visitor = Visitor('ham')

@when('I have bought {something}')
def step_impl(context, something):
    context.visitor.food.append(something)
    assert something in context.visitor.food


