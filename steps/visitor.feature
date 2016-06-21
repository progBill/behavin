

Feature: Demoing a typical visitor experience

    Scenario: Matt comes over
        Given I greet the guest
        When Matt shows up
        Then I say hi

    Scenario: Matt eats some stuff
        Given Matt gets hungry
        When Matt wants to eat a biscuit
        Then Matt eats a biscuit

    Scenario Outline: Matt is very hungry
        Given Matt raids the fridge
        When I have bought <something>
        Then Matt eats <it>

        Examples:
        | something |    it    |
        | biscuits  | biscuits |
        | apples    | apples   |
        | beer      | beer     |


    Scenario: Matt goes home
       Given Matt has shit to do
        When Matt leaves
        Then I say bye

