:- dynamic fact/1.
:- dynamic nonfact/1.


is_true(Question):-
(
      fact(Question) ->
      true;
      nonfact(Question) -> false;
      (
      format('~w~n', [Question]), Answer = read(yes),
       Answer -> assert(fact(Question)); assert(nonfact(Question)), false
      )
).


food(bacon_and_eggs) :- is_true('is breakfast'), is_true('has eggs'), is_true('has meat').
food(omelette) :- is_true('is breakfast'), is_true('has eggs'), is_true('has meat'), is_true('is folded').
food(waffle) :- is_true('is breakfast'), is_true('is baked').
food(bagel) :- is_true('is breakfast'), is_true('is baked'), is_true('is held').
food(pancakes) :- is_true('is breakfast'), is_true('is fried').

food(pizza) :- is_true('is lunch'), is_true('has cheese').
food(hamburger) :- is_true('is lunch'), is_true('has meat').
food(burrito) :- is_true('is lunch'), is_true('has cheese'), is_true('has meat').
food(buffalo_wings) :- is_true('is lunch'), is_true('has meat'), is_true('has buffalo sauce').
food(salad) :- is_true('is lunch'), is_true('has leaves').

food(steak) :- is_true('is dinner'), is_true('has meat').
food(roasted_turkey) :- is_true('is dinner'), is_true('has meat'), is_true('is poultry').
food(fried_chicken) :- is_true('is dinner'), is_true('has meat'), is_true('is poultry'), is_true('is fried') .
food(pho) :- is_true('is dinner'), is_true('has noodles'), is_true('is soup').
food(spaghetti) :- is_true('is dinner'), is_true('has noodles').


begin :- write('Welcome to the ES about animals!
I am going to ask questions about animal features.
Please answer yes. or no.
Ready?  '),
      read(Answer),
      nl,
      ((Answer == yes ; Answer == y) -> assertz(yes(Answer)) , process;
       (Answer == no ; Answer ==n) -> assertz(no(Answer)), halt ;
        write('\nInvalid Input.\n'),fail).

process :-
    food(A),
    write(A),
    nl,
    retractall(fact(_)),
    retractall(nonfact(_)),
    write('Did I do good on my guess?'),
    nl,
    read(Answer),
    ((Answer == yes ; Answer == y) -> assertz(yes(Answer)) , write('Yay!');
       (Answer == no ; Answer ==n) -> assertz(no(Answer)), write("I'm sorry UwU") ;
        write('\nInvalid Input.\n'),fail).


